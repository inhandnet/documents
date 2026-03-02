import os
import requests
import sys

# 1. 明确区分 API 配置
CONFIGS = {
    "zh": {"base": "https://poweris.inhand.online", "key": os.getenv("CN_API_KEY")},
    "en": {"base": "https://poweris.inhandnetworks.com", "key": os.getenv("GLOBAL_API_KEY")}
}


def get_whitelist(lang):
    conf = CONFIGS.get(lang)
    whitelist = set()
    if not conf or not conf["key"]:
        print(f"⚠️ 警告: 未找到 {lang} 版 API 配置，跳过该语言同步。")
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
                break
        except Exception as e:
            print(f"❌ {lang.upper()} 站 API 连接异常: {e}")
            break
    return whitelist


def validate_dir(root_path, whitelist, lang_label):
    invalid_files = []
    found_count = 0

    # 递归扫描目录下所有子文件夹
    for root, dirs, files in os.walk(root_path):
        for f in files:
            if not f.endswith(".md"): continue
            file_name = os.path.splitext(f)[0].lower()
            if file_name == "index": continue

            found_count += 1
            # 校验逻辑：文件名是否包含在白名单中
            is_valid = any(s in file_name for s in whitelist)
            if not is_valid:
                invalid_files.append(os.path.join(root, f))

    return invalid_files, found_count


def run():
    all_invalid = []

    # 分开校验：ZH -> CN API, EN -> Global API
    for lang in ["zh", "en"]:
        path = f"docs/{lang}"
        if not os.path.exists(path):
            print(f"跳过 {lang} 目录，未找到路径。")
            continue

        whitelist = get_whitelist(lang)
        if not whitelist:
            print(f"⚠️ {lang} 站白名单为空，跳过该目录校验。")
            continue

        print(f"🔍 正在校验 {path} 目录下的文件...")
        invalids, count = validate_dir(path, whitelist, lang)
        print(f"✅ 已扫描 {count} 个 {lang.upper()} 文档。")
        all_invalid.extend(invalids)

    if all_invalid:
        print("\n" + "!" * 50)
        print("❌ 校验失败：以下文件命名不合规！")
        for f in all_invalid:
            print(f"  --> {f}")
        print("\n请确保文件名包含 API 返回的系列 ID 或名称。")
        sys.exit(1)

    print("\n🎉 恭喜！所有分区校验均通过。")


if __name__ == "__main__":
    run()