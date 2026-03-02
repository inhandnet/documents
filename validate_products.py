import os
import requests
import sys
import subprocess

# 1. API 配置：国内站与海外站分开
CONFIGS = {
    "zh": {"base": "https://poweris.inhand.online", "key": os.getenv("CN_API_KEY")},
    "en": {"base": "https://poweris.inhandnetworks.com", "key": os.getenv("GLOBAL_API_KEY")}
}


def get_whitelist(lang):
    """从 PLM 系统同步产品 ID 白名单"""
    conf = CONFIGS.get(lang)
    whitelist = set()
    if not conf or not conf["key"]:
        print(f"⚠️ 警告: 未找到 {lang.upper()} 版 API 配置 (Secrets)，跳过该语言同步。")
        return whitelist

    print(f"正在从 {lang.upper()} 站同步产品列表...")
    page = 1
    while True:
        try:
            res = requests.get(
                f"{conf['base']}/api/plm/product/series-list",
                params={"pageNumber": page, "pageSize": 100, "locale": "en"},
                headers={"X-Api-Key": conf["key"].strip()},
                timeout=10
            ).json()

            if res.get("status") == 200:
                items = res.get("result", [])
                if not items: break
                for item in items:
                    if item.get("id"): whitelist.add(item["id"].lower())
                    names = item.get("name", {})
                    if names.get("cn"): whitelist.add(names["cn"].lower())
                    if names.get("en"): whitelist.add(names["en"].lower())
                if page * 100 >= res.get("total", 0): break
                page += 1
            else:
                print(f"❌ {lang.upper()} 站 API 响应错误: {res.get('message')}")
                break
        except Exception as e:
            print(f"❌ {lang.upper()} 站连接异常: {e}")
            break
    return whitelist


def get_changed_folders():
    """通过 git diff 获取本次提交中修改过的产品文件夹"""
    try:
        # 获取当前提交与上一次提交的差异
        cmd = ["git", "diff", "--name-only", "HEAD~1", "HEAD"]
        output = subprocess.check_output(cmd).decode("utf-8")
        files = output.splitlines()

        changed_folders = set()
        for f in files:
            # 只处理 docs/zh 或 docs/en 下的文件，且必须是 .md
            if (f.startswith("docs/zh/") or f.startswith("docs/en/")) and f.endswith(".md"):
                if os.path.basename(f).lower() == "index.md": continue
                # 获取该文件所在的直接父文件夹路径
                changed_folders.add(os.path.dirname(f))
        return changed_folders
    except Exception as e:
        print(f"⚠️ Git 获取差异失败 (可能是首次提交): {e}。将跳过增量校验。")
        return None


def find_similar_names(folder_name, whitelist):
    """当校验失败时，寻找最相关的产品名称作为建议"""
    suggestions = []
    fn_lower = folder_name.lower()
    # 提取前两个字母作为模糊匹配前缀 (例如 ec312 -> ec)
    prefix = "".join([c for c in fn_lower if c.isalpha()])[:2]

    for item in whitelist:
        if fn_lower in item or item in fn_lower or (prefix and item.startswith(prefix)):
            suggestions.append(item)
    return sorted(list(set(suggestions)))[:8]


def run_validation():
    changed_folders = get_changed_folders()
    if changed_folders is None:
        print("✅ 未检测到文件变更或 Git 环境异常，跳过校验。")
        return

    if not changed_folders:
        print("✅ 本次提交未涉及产品文档修改，无需校验。")
        return

    all_invalid = []
    # 分语言进行精准校验
    for lang in ["zh", "en"]:
        path_prefix = f"docs/{lang}"
        # 过滤出属于该语言路径的变更文件夹
        target_folders = [d for d in changed_folders if d.startswith(path_prefix)]

        if not target_folders:
            continue

        whitelist = get_whitelist(lang)
        if not whitelist:
            print(f"⚠️ {lang.upper()} 站白名单为空，跳过该分区校验。")
            continue

        print(f"🔍 正在校验 {lang.upper()} 分区变更的文件夹...")
        for folder_path in target_folders:
            # 获取文件夹名 (例如 docs/en/AI/EC942 -> EC942)
            folder_name = os.path.basename(folder_path).lower()

            # 核心逻辑：校验文件夹名是否在白名单里
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
                print(f"      💡 你是不是想找这些产品？: {', '.join(error['suggestions'])}")
            else:
                print(f"      💡 提示：未在 PLM 库中找到相似产品，请核对 ID。")
        print("\n" + "!" * 60 + "\n")
        sys.exit(1)

    print("\n🎉 增量校验全部通过！")


if __name__ == "__main__":
    run_validation()