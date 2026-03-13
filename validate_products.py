import argparse
import os
import requests
import sys
import subprocess

# 1. 配置中心：EN 站保持原样，ZH 站准备好双钥匙
CONFIGS = {
    "zh": {
        "base": "https://poweris.inhand.online",
        "key": os.getenv("CN_API_KEY"),
        "token": os.getenv("CN_XK_TOKEN")
    },
    "en": {
        "base": "https://poweris.inhandnetworks.com",
        "key": os.getenv("GLOBAL_API_KEY"),
        "token": os.getenv("GLOBAL_XK_TOKEN")
    }
}


def get_whitelist(lang):
    """自适应鉴权：ZH 站会尝试大小写及不同 Header 名"""
    conf = CONFIGS.get(lang)
    if not conf: return None

    if not conf["key"] and not conf["token"]:
        print(f"⚠️ 警告: 未找到 {lang.upper()} 版鉴权配置，跳过同步。")
        return None

    print(f"正在从 {lang.upper()} 站同步产品列表...")

    # 构造尝试序列：如果是 ZH 站，我们把大小写都试一遍
    auth_attempts = []
    if conf["key"]:
        auth_attempts.append(("X-Api-Key", conf["key"].strip()))
        auth_attempts.append(("x-api-key", conf["key"].strip()))  # 👈 对应你 JS 里的写法
    if conf["token"]:
        auth_attempts.append(("XK-Token", conf["token"].strip()))
        auth_attempts.append(("xk-token", conf["token"].strip()))  # 👈 对应你 JS 里的写法

    for header_name, auth_val in auth_attempts:
        page = 1
        current_whitelist = set()
        print(f"  🔑 正在尝试使用 {header_name} 进行鉴权...")

        success = True
        while True:
            try:
                res = requests.get(
                    f"{conf['base']}/api/plm/product/series-list",
                    params={
                        "pageNumber": page,
                        "pageSize": 100,
                        "locale": "zh" if lang == "zh" else "en"
                    },
                    headers={header_name: auth_val},
                    timeout=10
                ).json()

                if res.get("status") == 200:
                    items = res.get("result", [])
                    if not items: break
                    for item in items:
                        if item.get("id"): current_whitelist.add(item["id"].lower())
                        names = item.get("name", {})
                        if names.get("cn"): current_whitelist.add(names["cn"].lower())
                        if names.get("en"): current_whitelist.add(names["en"].lower())
                    if page * 100 >= res.get("total", 0): break
                    page += 1
                else:
                    # 如果不是 200，记录错误但不立刻崩溃，换下一个 Header 试试
                    print(f"  ❌ {header_name} 尝试失败: {res.get('message')}")
                    success = False
                    break
            except Exception as e:
                print(f"  ❌ 连接异常 ({header_name}): {e}")
                success = False
                break

        # 只要成功拿到数据（哪怕只有 1 条），就说明这把钥匙是对的
        if success and current_whitelist:
            print(f"  ✅ {header_name} 鉴权成功！已获取 {len(current_whitelist)} 条产品数据。")
            return current_whitelist

    return None


def get_changed_folders(paths=None):
    """获取本次提交中涉及的文件夹路径，并过滤掉已在本地删除的文件

    Args:
        paths: 要校验的路径前缀列表，如 ["docs/zh", "docs/en"]。
               对于 docs/ 路径仅匹配 .md 文件；其他路径（specs/、downloads/ 等）匹配任意文件。
    """
    if paths is None:
        paths = ["docs/zh", "docs/en"]

    # Paths that use flat file structure (product name is filename, not directory)
    flat_prefixes = ("releases/", "dev/")

    try:
        cmd = ["git", "diff", "--name-only", "HEAD~1", "HEAD"]
        output = subprocess.check_output(cmd).decode("utf-8")
        files = output.splitlines()

        changed_folders = set()
        for f in files:
            if not os.path.exists(f):
                continue
            matched_prefix = None
            for prefix in paths:
                if f.startswith(prefix + "/"):
                    matched_prefix = prefix
                    break
            if not matched_prefix:
                continue
            # releases/ and dev/ use different structures — skip product validation
            # for these paths as they don't follow Category/Chipset/Model convention
            if any(matched_prefix.startswith(fp) for fp in flat_prefixes):
                continue
            # docs/ 路径仅关注 .md 文件；其他路径接受任意文件
            if matched_prefix.startswith("docs/"):
                if not f.endswith(".md"):
                    continue
            if os.path.basename(f).lower() == "index.md":
                continue
            changed_folders.add(os.path.dirname(f))
        return changed_folders
    except Exception as e:
        print(f"⚠️ Git 获取差异失败: {e}")
        return None


def find_similar_names(folder_name, whitelist):
    """校验失败时，寻找相关的产品 ID 作为建议"""
    suggestions = []
    fn_lower = folder_name.lower()
    prefix = "".join([c for c in fn_lower if c.isalpha()])[:2]
    for item in whitelist:
        if fn_lower in item or item in fn_lower or (prefix and item.startswith(prefix)):
            suggestions.append(item)
    return sorted(list(set(suggestions)))[:8]


def run_validation(paths=None):
    """校验变更的产品目录名是否在白名单中

    Args:
        paths: 要校验的路径前缀列表，如 ["docs/zh", "docs/en", "specs/zh"]。
               默认值 ["docs/zh", "docs/en"]，向后兼容。
    """
    if paths is None:
        paths = ["docs/zh", "docs/en"]

    changed_folders = get_changed_folders(paths)
    if changed_folders is None:
        print("❌ 错误: 无法获取 Git 变更记录。")
        sys.exit(1)
    if not changed_folders:
        print("✅ 本次提交未涉及产品文档修改，无需校验。")
        return

    all_invalid = []
    for lang in ["zh", "en"]:
        # 收集当前语言下所有匹配的路径前缀
        lang_prefixes = [p for p in paths if p.endswith(f"/{lang}") or p.endswith(f"/{lang}/")]
        if not lang_prefixes:
            continue

        target_folders = []
        for d in changed_folders:
            for prefix in lang_prefixes:
                if d.startswith(prefix):
                    target_folders.append(d)
                    break
        if not target_folders:
            continue

        whitelist = get_whitelist(lang)
        if whitelist is None:
            print(f"\n" + "!" * 60)
            print(f"❌ 严重错误：无法获取 {lang.upper()} 分区白名单！")
            print(f"   请核对该分区的鉴权 Key 是否已配置在 GitHub Secrets 中。")
            print("!" * 60 + "\n")
            sys.exit(1)

        print(f"🔍 正在校验 {lang.upper()} 分区变更的文件夹...")
        for folder_path in target_folders:
            folder_name = os.path.basename(folder_path).lower()
            if not any(s == folder_name or s in folder_name for s in whitelist):
                suggestions = find_similar_names(folder_name, whitelist)
                all_invalid.append({"path": folder_path, "suggestions": suggestions})
            else:
                print(f"  [OK] {folder_path}")

    if all_invalid:
        print("\n" + "!" * 60)
        print("❌ 校验失败：本次提交包含不受支持的产品目录名！")
        for error in all_invalid:
            print(f"\n  --> 错误文件夹: {error['path']}")
            if error['suggestions']:
                print(f"      💡 建议 ID: {', '.join(error['suggestions'])}")
        sys.exit(1)
    print("\n🎉 增量校验全部通过！")


def parse_args():
    parser = argparse.ArgumentParser(description="校验产品目录名是否在白名单中")
    parser.add_argument(
        "--paths",
        nargs="+",
        default=["docs/zh", "docs/en"],
        help="要校验的路径前缀列表（默认: docs/zh docs/en）"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_validation(args.paths)