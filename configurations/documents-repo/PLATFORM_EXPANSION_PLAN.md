# 文档平台扩展方案：规格书、配置文件、QA 集成

## Context

当前 `inhandnet/documents` 仓库仅管理用户手册（Markdown → MkDocs → HTML），部署到海外/国内服务器 + GitHub Pages。现在需要扩展为一个统一的文档资产管理平台，新增：

- **规格书**：PDF 发布到官网（WordPress）资源中心
- **配置文件/脚本**：原文件发布到官网资源中心
- **QA 问答**：HTML 发布 + 同步到 Discourse 论坛

官网是 WordPress + Elementor 构建，资源中心使用 Hash 路由 SPA，资源由 WP Job Manager 插件管理。

---

## 核心决策

### 1. 单仓库，不分仓

**结论：保持单仓库**，理由：
- `validate_products.py` 的产品名校验逻辑可以复用，只需扩展路径前缀
- 团队只需维护一个 PR 流程
- 用户手册可以直接链接到同产品的规格书/QA
- Git LFS 解决 PDF 二进制文件膨胀问题
- 通过 `paths:` 过滤实现各内容类型独立触发 CI，互不影响

### 2. 按内容类型拆分 CI Workflow

每种内容类型一个独立的 workflow 文件，通过 `paths:` 过滤触发，互相隔离：

| Workflow | 触发路径 | 产出 | 部署目标 |
|---|---|---|---|
| `deploy-manuals.yml` | `docs/**` | HTML | 文档服务器 + GitHub Pages |
| `deploy-specs.yml` | `specs/**` | PDF 文件 | WordPress 服务器 |
| `deploy-downloads.yml` | `downloads/**` | 原始文件 | WordPress 服务器 |
| `deploy-qa.yml` | `qa/**` | HTML + Discourse | 文档服务器 + Discourse API |

### 3. 规格书/下载 → WordPress 集成方式

推荐 **SCP 到 WordPress 服务器静态目录 + WP REST API 创建/更新资源条目**：

```
方案：双管齐下
├── CI 通过 SCP 把文件放到 WordPress 服务器的静态目录
│   例如: /var/www/wordpress/wp-content/uploads/resources/specs/zh/EC954/...
└── CI 通过 WordPress REST API 创建/更新对应的资源帖子（WP Job Manager）
    帖子中的下载链接指向上面的静态文件路径
```

这样资源中心前端无需改动，只需在 WordPress 后台有对应的资源条目即可。

> **备选方案**：如果 WordPress REST API 集成太复杂，可以先只做 SCP 上传文件，资源条目手动在 WP 后台创建。后续再自动化。

---

## 目录结构

```
inhandnet/documents/
├── docs/                          # 【现有】用户手册 (Markdown → HTML)
│   ├── zh/{Category}/{Chipset}/{Model}/
│   └── en/{Category}/{Chipset}/{Model}/
│
├── specs/                         # 【新增】规格书 (PDF)
│   ├── zh/{Category}/{Chipset}/{Model}/
│   │   ├── EC954_Datasheet.pdf       ← 现成 PDF (Git LFS)
│   │   └── EC954_Datasheet.md        ← 需要构建的 (Pandoc → PDF)
│   └── en/{Category}/{Chipset}/{Model}/
│
├── downloads/                     # 【新增】配置文件/脚本
│   ├── zh/{Category}/{Chipset}/{Model}/
│   │   ├── default_config.tar.gz
│   │   └── setup.sh
│   └── en/{Category}/{Chipset}/{Model}/
│
├── qa/                            # 【新增】QA 问答 (Markdown → HTML + Discourse)
│   ├── zh/{Category}/{Chipset}/{Model}/
│   │   └── faq_boot_failure.md
│   ├── en/{Category}/{Chipset}/{Model}/
│   └── discourse_categories.yml      ← 产品 → Discourse 分类 ID 映射
│
├── scripts/                       # 【新增】CI 辅助脚本
│   ├── build_specs.py                ← Markdown → PDF 构建
│   ├── discourse_sync.py             ← QA 同步到 Discourse
│   └── wp_sync.py                    ← 资源条目同步到 WordPress (可选)
│
├── mkdocs.yml                     # 【现有】中文用户手册
├── mkdocs.en.yml                  # 【现有】英文用户手册
├── mkdocs.qa.zh.yml               # 【新增】中文 QA 站
├── mkdocs.qa.en.yml               # 【新增】英文 QA 站
├── .gitattributes                 # 【新增】Git LFS 规则
├── validate_products.py           # 【修改】扩展 --paths 参数
└── .github/workflows/
    ├── deploy-manuals.yml         # 【改名】原 deploy-pages.yml，加 paths 过滤
    ├── deploy-specs.yml           # 【新增】
    ├── deploy-downloads.yml       # 【新增】
    └── deploy-qa.yml              # 【新增】
```

---

## 关键改动详解

### A. Git LFS 配置

`.gitattributes`：
```
specs/**/*.pdf filter=lfs diff=lfs merge=lfs -text
downloads/**/*.tar.gz filter=lfs diff=lfs merge=lfs -text
downloads/**/*.zip filter=lfs diff=lfs merge=lfs -text
downloads/**/*.bin filter=lfs diff=lfs merge=lfs -text
```

### B. validate_products.py 扩展

添加 `--paths` CLI 参数，支持校验任意路径前缀下的产品目录名：
- 默认值保持 `["docs/zh", "docs/en"]`，向后兼容
- 新 workflow 调用时传入 `--paths specs/zh specs/en` 等
- 文件类型过滤放宽：`docs/` 路径仅匹配 `.md`，其他路径接受任意文件

### C. QA 站点构建

- `mkdocs.qa.zh.yml` — `docs_dir: qa/zh`，启用 `tags` 插件
- `mkdocs.qa.en.yml` — `docs_dir: qa/en`，启用 `tags` 插件
- QA 站独立部署到 `/qa/` 路径

### D. Discourse 同步机制

QA Markdown 文件使用 frontmatter 记录 Discourse topic ID：
```yaml
---
title: "EC954 升级后无法启动"
discourse_topic_id: 42  # 首次发布后自动回填
tags: [firmware, boot]
---
```

`scripts/discourse_sync.py` 逻辑：
1. `git diff` 找到本次变更的 QA 文件
2. 有 `discourse_topic_id` → PUT 更新已有帖子
3. 无 `discourse_topic_id` → POST 创建新帖子 → 回填 ID 到文件 → `git commit [skip ci]` + `git push`

### E. 规格书构建 (Markdown → PDF)

`scripts/build_specs.py` 逻辑：
1. 遍历 `specs/` 下所有 `.md` 文件
2. 如果同目录已有同名 `.pdf`，跳过（说明是现成 PDF）
3. 否则用 Pandoc + WeasyPrint 转换为 PDF
4. 输出到 `dist/specs/` 保持目录结构

---

## CI Workflow 概览

### deploy-manuals.yml（改名 + 加 paths 过滤）
```yaml
on:
  push:
    branches: [master]
    paths: ['docs/**', 'mkdocs.yml', 'mkdocs.en.yml']
```

### deploy-specs.yml
```
触发: specs/** 变更
步骤: checkout(lfs) → validate(--paths specs/zh specs/en) → build_specs.py → SCP 到 WordPress 服务器
```

### deploy-downloads.yml
```
触发: downloads/** 变更
步骤: checkout(lfs) → validate(--paths downloads/zh downloads/en) → SCP 到 WordPress 服务器
```

### deploy-qa.yml
```
触发: qa/** 变更
步骤: checkout → validate(--paths qa/zh qa/en) → mkdocs build QA 站 → SCP 到文档服务器 → discourse_sync.py
```

---

## 新增 GitHub Secrets

| Secret | 用途 |
|---|---|
| `WP_HOST` / `WP_USER` / `WP_PASS` | SCP 到 WordPress 服务器 |
| `WP_API_URL` / `WP_API_USER` / `WP_API_TOKEN` | WordPress REST API（可选，Phase 5） |
| `DISCOURSE_BASE_URL` | Discourse 论坛地址 |
| `DISCOURSE_API_KEY` | Discourse API Key |
| `DISCOURSE_API_USERNAME` | Discourse 发帖用户名（如 docs-bot） |
| `GH_BOT_TOKEN` | GitHub PAT，用于 discourse_sync.py 回填 topic ID 后 push |

---

## 实施阶段与状态

### Phase 1: 基础设施 ✅
1. ✅ 初始化 Git LFS，提交 `.gitattributes`
2. ✅ 扩展 `validate_products.py` 支持 `--paths` 参数
3. ✅ 将 `deploy-pages.yml` 改名为 `deploy-manuals.yml`，添加 `paths:` 过滤
4. ✅ 创建目录骨架：`specs/`、`downloads/`、`qa/`、`scripts/`

### Phase 2: 规格书流水线 ✅
5. ✅ 编写 `scripts/build_specs.py`（Pandoc + WeasyPrint）
6. ✅ 创建 `deploy-specs.yml` workflow

### Phase 3: 下载文件流水线 ✅
7. ✅ 创建 `deploy-downloads.yml` workflow

### Phase 4: QA 流水线 ✅
8. ✅ 创建 `mkdocs.qa.zh.yml` 和 `mkdocs.qa.en.yml`
9. ✅ 编写 `scripts/discourse_sync.py`
10. ✅ 创建 `deploy-qa.yml` workflow

### Phase 5: WordPress 自动化 ✅
11. ✅ 编写 `scripts/wp_sync.py`（workflows 中已注释，待启用）

---

## 部署前待办

- [ ] 运行 `git lfs install`
- [ ] 配置所有新增 GitHub Secrets
- [ ] 上传第一批 PDF 测试 LFS + CI 流程
- [ ] 上传第一批配置文件/脚本测试下载流水线
- [ ] 在测试 Discourse 实例验证 QA 同步
- [ ] 全流程验证：同时提交 docs + specs + qa 的改动，确认三个 workflow 各自独立触发
