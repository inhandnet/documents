#!/usr/bin/env python3
"""QA 文档同步到 Discourse 论坛。

逻辑：
1. 通过 git diff 找到本次变更的 QA Markdown 文件
2. 解析 frontmatter 获取 discourse_topic_id
3. 有 topic_id → PUT 更新已有帖子
4. 无 topic_id → POST 创建新帖子 → 回填 ID 到文件 → git commit [skip ci] + git push
"""

import os
import re
import subprocess
import sys

import requests
import yaml

DISCOURSE_BASE_URL = os.getenv("DISCOURSE_BASE_URL", "").rstrip("/")
DISCOURSE_API_KEY = os.getenv("DISCOURSE_API_KEY", "")
DISCOURSE_API_USERNAME = os.getenv("DISCOURSE_API_USERNAME", "docs-bot")

# Discourse 分类映射文件
CATEGORIES_FILE = "qa/discourse_categories.yml"


def get_discourse_headers():
    return {
        "Api-Key": DISCOURSE_API_KEY,
        "Api-Username": DISCOURSE_API_USERNAME,
        "Content-Type": "application/json",
    }


def load_category_mapping():
    """加载产品 → Discourse 分类 ID 映射"""
    if not os.path.exists(CATEGORIES_FILE):
        print(f"⚠️ 分类映射文件 {CATEGORIES_FILE} 不存在，使用默认分类。")
        return {}
    with open(CATEGORIES_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_changed_qa_files():
    """获取本次提交变更的 QA Markdown 文件"""
    try:
        cmd = ["git", "diff", "--name-only", "HEAD~1", "HEAD"]
        output = subprocess.check_output(cmd).decode("utf-8")
        files = output.splitlines()
        return [f for f in files if f.startswith("qa/") and f.endswith(".md") and os.path.exists(f)]
    except Exception as e:
        print(f"⚠️ Git 获取差异失败: {e}")
        return []


def parse_frontmatter(filepath):
    """解析 Markdown 文件的 YAML frontmatter"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\n(.*?)\n---\n?(.*)", content, re.DOTALL)
    if not match:
        return {}, content

    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        meta = {}
    body = match.group(2)
    return meta, body


def write_frontmatter(filepath, meta, body):
    """将更新后的 frontmatter 写回文件"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml.dump(meta, allow_unicode=True, default_flow_style=False))
        f.write("---\n")
        f.write(body)


def create_topic(title, body, category_id=None):
    """在 Discourse 创建新帖子"""
    payload = {
        "title": title,
        "raw": body,
    }
    if category_id:
        payload["category"] = category_id

    resp = requests.post(
        f"{DISCOURSE_BASE_URL}/posts.json",
        json=payload,
        headers=get_discourse_headers(),
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get("topic_id")


def update_topic(topic_id, body):
    """更新 Discourse 已有帖子的内容（更新第一个帖子）"""
    # 先获取帖子 ID
    resp = requests.get(
        f"{DISCOURSE_BASE_URL}/t/{topic_id}.json",
        headers=get_discourse_headers(),
        timeout=30,
    )
    resp.raise_for_status()
    post_id = resp.json()["post_stream"]["posts"][0]["id"]

    # 更新帖子内容
    resp = requests.put(
        f"{DISCOURSE_BASE_URL}/posts/{post_id}.json",
        json={"post": {"raw": body}},
        headers=get_discourse_headers(),
        timeout=30,
    )
    resp.raise_for_status()


def git_commit_and_push(files):
    """提交回填的 topic ID 并推送"""
    if not files:
        return
    try:
        subprocess.run(["git", "config", "user.name", "docs-bot"], check=True)
        subprocess.run(["git", "config", "user.email", "docs-bot@inhandnetworks.com"], check=True)
        for f in files:
            subprocess.run(["git", "add", f], check=True)
        subprocess.run(
            ["git", "commit", "-m", "chore: backfill discourse topic IDs [skip ci]"],
            check=True,
        )
        subprocess.run(["git", "push"], check=True)
        print("✅ Topic ID 回填已提交并推送。")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git 提交/推送失败: {e}")


def main():
    if not DISCOURSE_BASE_URL or not DISCOURSE_API_KEY:
        print("⚠️ Discourse 配置缺失 (DISCOURSE_BASE_URL / DISCOURSE_API_KEY)，跳过同步。")
        return

    qa_files = get_changed_qa_files()
    if not qa_files:
        print("✅ 本次提交未涉及 QA 文件变更，无需同步。")
        return

    category_mapping = load_category_mapping()
    backfill_files = []

    for filepath in qa_files:
        print(f"\n处理: {filepath}")
        meta, body = parse_frontmatter(filepath)
        title = meta.get("title", os.path.splitext(os.path.basename(filepath))[0])
        topic_id = meta.get("discourse_topic_id")

        # 推断分类 ID
        parts = filepath.split("/")
        category_id = None
        if len(parts) >= 4:
            # qa/{lang}/{Category}/{Chipset}/{Model}/file.md → 用 Model 查映射
            model = parts[-2] if len(parts) >= 5 else parts[-1].replace(".md", "")
            category_id = category_mapping.get(model)

        try:
            if topic_id:
                print(f"  更新帖子: topic_id={topic_id}")
                update_topic(topic_id, body)
                print(f"  ✅ 更新成功")
            else:
                print(f"  创建新帖子: {title}")
                new_topic_id = create_topic(title, body, category_id)
                if new_topic_id:
                    meta["discourse_topic_id"] = new_topic_id
                    write_frontmatter(filepath, meta, body)
                    backfill_files.append(filepath)
                    print(f"  ✅ 创建成功: topic_id={new_topic_id}")
                else:
                    print(f"  ❌ 创建失败: 未返回 topic_id")
        except requests.RequestException as e:
            print(f"  ❌ 同步失败: {e}")

    # 回填 topic ID
    if backfill_files:
        print(f"\n回填 {len(backfill_files)} 个文件的 topic ID...")
        git_commit_and_push(backfill_files)

    print("\n🎉 Discourse 同步完成！")


if __name__ == "__main__":
    main()
