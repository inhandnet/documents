import os
import requests
import sys

# 1. 这里的配置对应你发给我的 config 数据
ENV_CONFIGS = [
    {"name": "CN", "base": "https://poweris.inhand.online", "key": os.getenv("CN_API_KEY")},
    {"name": "Global", "base": "https://poweris.inhandnetworks.com", "key": os.getenv("GLOBAL_API_KEY")}
]


def get_api_whitelist():
    whitelist = set()
    for env in ENV_CONFIGS:
        if not env["key"]: continue
        print(f"正在从 {env['name']} 站同步产品列表...")
        page = 1
        while True:
            try:
                # 调取你给我的系列列表接口
                res = requests.get(
                    f"{env['base']}/api/plm/product/series-list",
                    params={"pageNumber": page, "pageSize": 100, "locale": "en"},
                    headers={"X-Api-Key": env["key"].strip()},
                    timeout=10
                ).json()

                if res.get("status") == 200:
                    items = res.get("result", [])
                    if not items: break
                    for item in items:
                        # 核心比对项：ID 和 中英文名称
                        if item.get("id"): whitelist.add(item["id"].lower())
                        names = item.get("name", {})
                        if names.get("cn"): whitelist.add(names["cn"].lower())
                        if names.get("en"): whitelist.add(names["en"].lower())

                    if page * 100 >= res.get("total", 0): break
                    page += 1
                else:
                    break
            except Exception as e:
                print(f"警告: {env['name']} 站连接异常: {e}")
                break
    return whitelist


def run_validation():
    # --- 关键：请确保你的产品文档放在这个目录下 ---
    doc_dir = "docs/products"

    if not os.path.exists(doc_dir):
        print(f"跳过校验：未找到目录 {doc_dir}")
        return

    valid_series = get_api_whitelist()
    files = [f for f in os.listdir(doc_dir) if f.endswith(".md")]
    invalid_files = []

    print(f"🔍 开始校验：共 {len(files)} 个文件...")

    for f in files:
        file_name = os.path.splitext(f)[0].lower()
        if file_name == "index": continue  # 忽略 index.md

        # 只要文件名在接口返回的 ID 或名称列表里，就算通过
        if file_name not in valid_series:
            invalid_files.append(f)

    if invalid_files:
        print("\n" + "!" * 50)
        print("❌ 校验失败：发现不合规的文件名！")
        for f in invalid_files:
            print(f"  --> 文件: {f} (在接口产品库中未找到匹配项)")
        print("\n请修正文件名，确保它对应 API 中的系列 ID 或名称。")
        print("!" * 50 + "\n")
        sys.exit(1)  # 强行中断 GitHub Actions

    print("✅ 校验通过！所有文件名均合法。")


if __name__ == "__main__":
    run_validation()