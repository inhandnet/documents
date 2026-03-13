# InHand 资源中心实施方案

> 本文档是 `PLATFORM_EXPANSION_PLAN.md` 的升级版。原方案完成了仓库内部的多内容类型扩展（specs/qa/downloads/brochures/configurations），本方案在此基础上，将面向用户的前端从 React SPA（哈希路由，不可索引）升级为 **WordPress + MkDocs Material** 双平台架构。

### 现状事实（关键修正）

1. **用户手册不是 PDF 下载** — 当前用户手册是在线文档的**链接**：国外指向 Zoho Desk，国内指向语雀。这些链接存储在 poweris 数据库中。
2. **poweris 是资源管理核心后端** — 固件、PDF（规格书/宣传册/合规文档）上传到 S3，元数据（文件名、版本、S3 URL、产品关联）存在 poweris 数据库中，前端通过 poweris API 获取下载链接。
3. **poweris API 能力完整** — 除 `series-list`（产品列表）外，还提供：文件上传/下载（S3 代理）、changelogMaps（版本更新日志）、资源分类聚合（按产品获取所有关联资源）。
4. **MkDocs 将逐步替代 Zoho/语雀** — 新产品手册直接在 MkDocs 编写；存量产品手册逐步从 Zoho/语雀迁移到 MkDocs，过渡期两者共存。

---

## 一、整体架构

### 数据流与系统关系

```
┌─ poweris 后端 ────────────────────────────────┐
│  数据库: 产品列表、资源元数据、手册链接、changelog │
│  S3:     固件包、PDF 文件（规格书/宣传册/合规）   │
│  API:    series-list / 资源聚合 / 文件下载       │
│          changelogMaps / 文件上传                │
└───────────────────────┬───────────────────────┘
                        │ API 调用
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌─ WordPress ──┐ ┌─ MkDocs ────┐ ┌─ React SPA ──┐
│ /downloads/  │ │ /docs/      │ │ 现有资源中心  │
│ /library/    │ │ /kb/        │ │ (逐步替换)   │
│ /products/   │ │ /releases/  │ └──────────────┘
│              │ │ /developers/│
└──────────────┘ └─────────────┘
```

**关键**：
- WordPress 下载中心（`/downloads/`）和文档库（`/library/`）直接调用 poweris API 获取文件列表和 S3 下载链接，不需要在 WordPress 数据库中复制一份
- MkDocs 在线文档（`/docs/`）是手册内容的**新归宿**，逐步替代 Zoho Desk / 语雀链接
- 过渡期：产品聚合页的「在线文档」链接优先指向 MkDocs，无 MkDocs 版本的回退到 Zoho/语雀链接（链接从 poweris API 获取）

### 核心思路

- **MkDocs Material** 负责在线技术文档和知识库（工程团队 Git 工作流）
- **WordPress** 负责下载中心、PDF 文档库和产品页（市场团队 CMS）
- **Nginx 反向代理** 将两个平台统一到同一域名 `inhand.com.cn` 下
- **`overrides/main.html`** 通过 Jinja2 模板覆盖，为所有 MkDocs 站注入 WordPress 统一导航头

### 平台分工

| 平台 | URL 路径 | 管理内容 | 技术栈 | 维护团队 |
|------|----------|----------|--------|----------|
| WordPress | `/`, `/downloads/`, `/library/`, `/products/` | 主站、产品页、下载中心（固件/软件）、PDF 文档库（规格书/宣传册/合规） | poweris API (S3) + WordPress | 市场/产品团队 |
| MkDocs 文档站 | `/docs/`, `/docs/en/` | 在线技术文档（用户手册、部署案例） | MkDocs Material | 工程团队 |
| MkDocs 知识库站 | `/kb/`, `/kb/en/` | QA 知识库（FAQ、应用笔记、故障排除） | MkDocs Material | 工程/支持团队 |
| MkDocs Release Notes 站 | `/releases/` | 每产品的固件发版说明 | MkDocs Material | 工程团队 |
| MkDocs 开发者站 | `/developers/` | API 文档、MQTT 规范、集成指南 | MkDocs Material | 工程团队 |

### MkDocs vs Docusaurus 决策依据

| 维度 | MkDocs Material | Docusaurus | 结论 |
|------|:-:|:-:|--------|
| 迁移成本 | 零（已有基础设施） | 高（重建全部） | **MkDocs** |
| 双语支持 | 独立配置文件（已有 4 个） | 单配置 i18n 框架 | 略逊但够用 |
| 文档版本化 | `mike` 工具 | 内置 | 略逊但够用 |
| 中文搜索 | 内置 lunr + jieba | 需 Algolia（付费） | **MkDocs** |
| 构建速度 | 500 页 5-15 秒 | 500 页 60-180 秒 | **MkDocs** |
| 输出体积 | 纯 HTML | HTML + React 运行时 | **MkDocs** |
| 插件生态 | PDF 导出、Git 日期、宏 | React 组件灵活 | **MkDocs**（B2B 场景） |
| 团队学习 | Python（已熟悉） | Node.js/React（需学习） | **MkDocs** |
| WordPress 导航统一 | Jinja2 模板覆盖（简单） | React Swizzle（复杂） | **MkDocs** |

**结论**：保持 MkDocs Material，投资改进而非迁移。

---

## 二、Nginx 反向代理

```nginx
server {
    server_name inhand.com.cn;

    # WordPress 主站（默认）
    location / {
        proxy_pass http://wordpress_upstream;
    }

    # MkDocs 在线文档
    location /docs/ {
        alias /var/www/mkdocs/docs/;
        try_files $uri $uri/ =404;
    }

    # MkDocs 知识库
    location /kb/ {
        alias /var/www/mkdocs/qa/;
        try_files $uri $uri/ =404;
    }

    # MkDocs Release Notes（Phase 3）
    location /releases/ {
        alias /var/www/mkdocs/releases/;
        try_files $uri $uri/ =404;
    }

    # MkDocs 开发者门户（Phase 4）
    location /developers/ {
        alias /var/www/mkdocs/dev/;
        try_files $uri $uri/ =404;
    }
}
```

参考配置文件：`nginx.conf.example`

---

## 三、全局导航

```
┌────────────────────────────────────────────────────────────┐
│  [Logo] InHand    产品  文档  下载  知识库  开发者  支持    │
└────────────────────────────────────────────────────────────┘
                      │     │     │      │       │      │
                      │     │     │      │       │      └─ /support/ (WP)
                      │     │     │      │       └─ /developers/ (MkDocs)
                      │     │     │      └─ /kb/ (MkDocs)
                      │     │     └─ /downloads/ (WP)
                      │     └─ /docs/ (MkDocs)
                      └─ /products/ (WP)
```

通过 `overrides/main.html` 注入所有 MkDocs 站，所有 8 个 mkdocs*.yml 配置文件均已配置 `custom_dir: overrides`。

---

## 四、各站点页面详解

### 4.1 在线技术文档 `/docs/` — MkDocs

**入口**：全局导航「文档」
**布局**：MkDocs Material 标准三栏（左侧导航 + 内容 + 右侧目录）

**内容组织**（每产品）：
```
/docs/{Category}/{Model}/
├── index.html          ← CI 生成的产品聚合索引
├── User_Manual.html    ← 用户手册
├── deployment/         ← 部署案例（从 configurations/ 迁移合并）
│   ├── fleet-management/
│   └── remote-monitoring/
└── images/
```

**配置文件**：`mkdocs.yml`（zh）、`mkdocs.en.yml`（en）
**CI**：`.github/workflows/deploy-manuals.yml`

### 4.2 知识库 `/kb/` — MkDocs

**入口**：全局导航「知识库」
**布局**：同 MkDocs Material 三栏

**内容组织**（Phase 2 扩展后）：
```
qa/zh/
├── getting-started/{Category}/{Model}/    ← 快速入门
├── how-to/{Category}/{Model}/             ← 操作指南
├── troubleshooting/{Category}/{Model}/    ← 故障排除
├── application-notes/{Category}/{Model}/  ← 应用笔记
└── faq/{Category}/{Model}/                ← FAQ（现有内容迁移至此）
```

**配置文件**：`mkdocs.qa.zh.yml`（zh）、`mkdocs.qa.en.yml`（en）
**CI**：`.github/workflows/deploy-qa.yml`

### 4.3 下载中心 `/downloads/` — WordPress

**入口**：全局导航「下载」
**数据来源**：现有 `poweris.inhand.online` API

```
┌─ 筛选栏 ─────────────────────────────────────┐
│ 产品线: [全部▾] 类型: [固件▾] [软件▾] [工具▾] │
│ 搜索: [_______________]  [搜索]               │
└───────────────────────────────────────────────┘
┌─ 下载列表 ───────────────────────────────────┐
│ 文件名          产品    版本   大小    操作   │
│ IR915_FW_3.2.1  IR915  3.2.1  28MB  [下载]   │
└───────────────────────────────────────────────┘
```

### 4.4 技术文档库 `/library/` — WordPress

**入口**：下载中心子导航 / 产品聚合页链接
**数据来源**：poweris API（PDF 存储在 S3，元数据在 poweris 数据库）

```
/library/
├── datasheets/     规格书 PDF ← poweris S3
├── drawings/       结构图 PDF ← poweris S3
├── compliance/     合规认证（FCC/CE/PTCRB）← poweris S3（新增分类）
└── brochures/      产品宣传册 ← poweris S3
```

> **注意**：用户手册不是 PDF，是在线文档链接。原 `/library/manuals/` 分类不再需要，或仅用于少量确实以 PDF 形式存在的遗留手册。用户手册的**新归宿**是 MkDocs `/docs/`，过渡期回退到 Zoho/语雀链接（从 poweris API 获取）。

### 4.5 Release Notes `/releases/` — MkDocs（Phase 3）

**入口**：产品聚合页链接 / 全局导航「文档」下拉

```
/releases/{product}.html

# IR915 Release Notes

## V3.2.1 (2025-12-15)
- 修复 VPN 断线重连问题
- 新增 MQTT 5.0 支持
```

**配置文件**：`mkdocs.releases.zh.yml`（zh）、`mkdocs.releases.en.yml`（en）
**CI**：`.github/workflows/deploy-releases.yml`

### 4.6 开发者门户 `/developers/` — MkDocs（Phase 4）

**入口**：全局导航「开发者」

```
/developers/
├── api/                  InCloud Manager REST API 文档
├── mqtt/                 MQTT 主题与报文格式
└── integration-guides/   Azure IoT / AWS IoT 集成指南
```

**配置文件**：`mkdocs.dev.zh.yml`（zh）、`mkdocs.dev.en.yml`（en）
**CI**：`.github/workflows/deploy-dev.yml`

### 4.7 产品聚合页 `/products/{model}/` — WordPress

**入口**：全局导航「产品」→ 具体型号
**作用**：汇总一个产品的所有资源（对标 Ubiquiti techspecs 页）

```
┌─ IR915 工业路由器 ──────────────────────────────────┐
│                                                      │
│  [产品图片]    关键规格（内联表格）                   │
│                                                      │
│  在线文档      → /docs/.../IR915/                   │
│                  （若 MkDocs 无此产品，回退到 Zoho/语雀链接 from poweris API）
│  固件下载      → /downloads/?product=IR915          │
│  规格书        → poweris S3 下载链接                 │
│  结构图        → poweris S3 下载链接                 │
│  宣传册        → poweris S3 下载链接                 │
│  Release Notes → /releases/IR915.html               │
│  知识库文章    → /kb/?product=IR915                 │
│  合规认证      → poweris S3 下载链接                 │
└────────────────────────────────────────────────────┘
```

> **手册链接过渡策略**：产品聚合页的「在线文档」链接，优先检查 MkDocs `/docs/` 是否有该产品页面，有则链接到 MkDocs；没有则从 poweris API 获取 Zoho/语雀链接。随着迁移推进，Zoho/语雀链接逐步消失。

---

## 五、仓库目录结构

### 完整结构图

```
F:\github\documents/
├── docs/                          # 用户手册 → /docs/
│   ├── zh/{Category}/{Model}/
│   │   ├── User_Manual.md
│   │   ├── deployment/            # [新增] 从 configurations/ 合并
│   │   │   └── {CaseName}/
│   │   │       ├── case-manual.md
│   │   │       └── config/
│   │   └── images/
│   └── en/...
│
├── qa/                            # QA 知识库 → /kb/
│   ├── zh/{Category}/{Model}/     # 现有结构
│   │   └── {Model}_FAQ.md
│   ├── zh/getting-started/{Category}/{Model}/  # [Phase 2 新增分类]
│   ├── zh/how-to/{Category}/{Model}/
│   ├── zh/troubleshooting/{Category}/{Model}/
│   ├── zh/application-notes/{Category}/{Model}/
│   ├── zh/faq/{Category}/{Model}/
│   └── en/...
│
├── releases/                      # [新增] Release Notes → /releases/
│   ├── zh/
│   │   ├── index.md               # 首页
│   │   ├── IR915.md               # 每产品一个文件，按版本倒序
│   │   └── assets/
│   └── en/...
│
├── dev/                           # [新增] 开发者文档 → /developers/
│   ├── zh/
│   │   ├── index.md               # 首页
│   │   ├── api/
│   │   │   └── index.md
│   │   ├── mqtt/
│   │   │   └── index.md
│   │   ├── integration-guides/
│   │   │   └── index.md
│   │   └── assets/
│   └── en/...
│
├── specs/                         # 规格书 PDF → WordPress /library/
├── brochures/                     # 宣传册 PDF → WordPress /library/
│
├── configurations/                # [废弃] 内容迁移到 docs/deployment/
│   └── (保留旧内容，不再新增)
│
├── overrides/                     # [新增] MkDocs 模板覆盖
│   └── main.html                  # 注入 WordPress 统一导航头
│
├── mkdocs.yml                     # 中文文档站 → /docs/
├── mkdocs.en.yml                  # 英文文档站 → /docs/en/
├── mkdocs.qa.zh.yml               # 中文知识库 → /kb/
├── mkdocs.qa.en.yml               # 英文知识库 → /kb/en/
├── mkdocs.releases.zh.yml         # [新增] 中文 Release Notes → /releases/
├── mkdocs.releases.en.yml         # [新增] 英文 Release Notes → /releases/en/
├── mkdocs.dev.zh.yml              # [新增] 中文开发者文档 → /developers/
├── mkdocs.dev.en.yml              # [新增] 英文开发者文档 → /developers/en/
│
├── scripts/
│   ├── generate_product_index.py  # [已修改] 支持 deployment/ 交叉链接
│   ├── scaffold_product.py        # [已修改] scaffold 时创建 deployment/
│   ├── build_specs.py             # 不变
│   ├── discourse_sync.py          # 不变
│   └── wp_sync.py                 # 不变
│
├── .github/workflows/
│   ├── deploy-manuals.yml         # [已修改] 增加 overrides/ 触发
│   ├── deploy-qa.yml              # [已修改] 增加 overrides/ 触发
│   ├── deploy-specs.yml           # 不变
│   ├── deploy-downloads.yml       # 不变
│   ├── deploy-releases.yml        # [新增] Phase 3
│   └── deploy-dev.yml             # [新增] Phase 4
│
├── validate_products.py           # [已修改] 跳过 releases/ 和 dev/ 路径
├── nginx.conf.example             # [新增] Nginx 反向代理参考配置
├── RESOURCE_CENTER_PLAN.md        # [本文档]
├── PLATFORM_EXPANSION_PLAN.md     # 上一阶段方案（已完成）
└── DIRECTORY_STRUCTURE.md         # 目录结构说明（需同步更新）
```

### 关键变更说明

1. **configurations/ → docs/deployment/**
   - 将方案配置合并到产品文档中，每个产品下新增 `deployment/` 子目录
   - 旧 `configurations/` 保留但不再新增内容
   - `generate_product_index.py` 已支持扫描 deployment/ 并生成交叉链接
   - `scaffold_product.py` 已在 scaffold 时创建 deployment/ 目录
   - `SKIP_DIRS` 已添加 `deployment`，避免被误认为产品子目录

2. **qa/ 目录分类扩展（Phase 2）**
   - 现有 qa/ 采用产品镜像路径，Phase 2 将增加内容分类前缀
   - 分类在前、产品路径在后：`qa/zh/how-to/{Category}/{Model}/`

3. **releases/ 新增**
   - 每产品一个 Markdown 文件，按版本号倒序排列
   - 已创建 index.md 首页和 MkDocs 配置

4. **dev/ 新增**
   - 按主题组织（api/mqtt/integration-guides/），不按产品
   - 已创建 index.md 首页和各分类的占位页

5. **overrides/ 新增**
   - MkDocs 模板覆盖目录，所有 8 个 mkdocs*.yml 共享
   - `main.html` 注入 WordPress 统一导航头

6. **URL 映射变更**
   - 文档站 `site_url`: `https://inhandnet.github.io/documents/` → `https://inhand.com.cn/docs/`
   - 知识库 `site_url`: `https://inhandnet.github.io/documents/qa/` → `https://inhand.com.cn/kb/`
   - QA 交叉链接: `/qa/` → `/kb/`

---

## 六、MkDocs 配置文件清单

| 配置文件 | 站点名称 | docs_dir | site_dir | site_url | 语言 |
|----------|----------|----------|----------|----------|------|
| `mkdocs.yml` | Docs | `docs/zh` | `site` | `https://inhand.com.cn/docs/` | zh |
| `mkdocs.en.yml` | Docs | `docs/en` | `site/en` | `https://inhand.com.cn/docs/en/` | en |
| `mkdocs.qa.zh.yml` | QA 知识库 | `qa/zh` | `site-qa` | `https://inhand.com.cn/kb/` | zh |
| `mkdocs.qa.en.yml` | QA Knowledge Base | `qa/en` | `site-qa/en` | `https://inhand.com.cn/kb/en/` | en |
| `mkdocs.releases.zh.yml` | Release Notes | `releases/zh` | `site/releases` | `https://inhand.com.cn/releases/` | zh |
| `mkdocs.releases.en.yml` | Release Notes | `releases/en` | `site/releases/en` | `https://inhand.com.cn/releases/en/` | en |
| `mkdocs.dev.zh.yml` | Developer Portal | `dev/zh` | `site/dev` | `https://inhand.com.cn/developers/` | zh |
| `mkdocs.dev.en.yml` | Developer Portal | `dev/en` | `site/dev/en` | `https://inhand.com.cn/developers/en/` | en |

所有配置文件共享 `custom_dir: overrides`、绿色主题（primary: green）、Material 主题。

---

## 七、CI/CD Workflow 清单

| Workflow | 触发路径 | 构建产出 | 部署目标 |
|----------|----------|----------|----------|
| `deploy-manuals.yml` | `docs/**`, `overrides/**`, `mkdocs.yml`, `mkdocs.en.yml` | `site/` | 海外服务器 + 国内服务器 + GitHub Pages |
| `deploy-qa.yml` | `qa/**`, `overrides/**`, `mkdocs.qa.*.yml` | `site-qa/` | 海外服务器 + 国内服务器 + Discourse |
| `deploy-specs.yml` | `specs/**` | PDF | WordPress 服务器 |
| `deploy-downloads.yml` | `downloads/**` | 原始文件 | WordPress 服务器 |
| `deploy-releases.yml` | `releases/**`, `overrides/**`, `mkdocs.releases.*.yml` | `site-releases/` | 海外服务器 + 国内服务器 |
| `deploy-dev.yml` | `dev/**`, `overrides/**`, `mkdocs.dev.*.yml` | `site-dev/` | 海外服务器 + 国内服务器 |

---

## 八、脚本变更记录

### `scripts/generate_product_index.py`

**新增功能**：
- `collect_deployment_cases(model_path)` — 扫描 `model_path/deployment/` 下的部署案例文件
- `DEPLOYMENT_EXTENSIONS` — 部署案例文件类型白名单
- `SKIP_DIRS` 新增 `deployment` — 避免 deployment 被误当作产品子目录
- `build_index_content()` 新增 `deployment_cases` 参数 — 在产品索引页生成「部署案例」章节
- 完整性报告新增 `Deploy` 列 — 追踪每个产品是否有部署案例

**QA 链接修正**：
- 产品索引中的 QA 链接从 `/qa/` 改为 `/kb/`（匹配新的 site_url）

### `scripts/scaffold_product.py`

**新增功能**：
- scaffold 新产品时自动创建 `docs/{lang}/{product_path}/deployment/.gitkeep`

### `validate_products.py`

**新增功能**：
- `releases/` 和 `dev/` 路径变更不再触发产品名白名单校验（这两类目录不使用 Category/Model 结构）

---

## 九、分阶段实施

### Phase 1：基础完善 — ✅ 已完成

- [x] 创建 `overrides/main.html` 注入 WordPress 统一导航头
- [x] 所有 8 个 mkdocs*.yml 添加 `custom_dir: overrides`
- [x] 4 个现有 mkdocs*.yml 更新 `site_url` 到 inhand.com.cn
- [x] 创建 4 个新 mkdocs 配置文件（releases + dev，zh + en）
- [x] 修改 `generate_product_index.py` 支持 deployment/ 子目录
- [x] 修改 `scaffold_product.py` 在 scaffold 时创建 deployment/
- [x] 修改 `validate_products.py` 支持 releases/ 和 dev/ 路径
- [x] `.github/workflows/deploy-manuals.yml` 增加 `overrides/**` 触发
- [x] `.github/workflows/deploy-qa.yml` 增加 `overrides/**` 触发
- [x] 创建 `deploy-releases.yml` 和 `deploy-dev.yml` CI workflow
- [x] 创建 releases/ 和 dev/ 目录结构与 index.md 首页
- [x] 创建 `nginx.conf.example` 参考配置
- [x] 所有站点本地构建验证通过

**待运维完成**：
- [ ] 配置 Nginx 反向代理（`/docs/` → MkDocs, `/kb/` → MkDocs QA）
- [ ] 将 configurations/ 现有内容迁移到 docs/{product}/deployment/
- [ ] 确认 SSL 证书覆盖所有路径
- [ ] 确认 CI 部署目标路径

### Phase 2：知识库内容扩展

- [ ] qa/ 目录增加分类子目录（getting-started, how-to, troubleshooting, application-notes, faq）
- [ ] 编写首批内容：Top 5 产品各 1 篇 Getting Started + 1 篇 Troubleshooting
- [ ] mkdocs.qa.zh.yml 配置导航分组
- [ ] validate_products.py 适配 qa/ 新的分类路径结构

### Phase 3：Release Notes

- [ ] 从 poweris API changelogMaps 拉取现有 Release Notes 转为 Markdown（写脚本）
- [ ] 填充 `releases/zh/` 和 `releases/en/` 内容
- [ ] Nginx 添加 `/releases/` location
- [ ] 产品聚合页添加 Release Notes 链接

### Phase 4：开发者门户

- [ ] 编写 InCloud Manager API 文档
- [ ] 编写 MQTT 主题规范文档
- [ ] 编写 Azure IoT / AWS IoT 集成指南
- [ ] Nginx 添加 `/developers/` location

### Phase 5：WordPress 侧改进（与 MkDocs 工作并行）

**目标**：WordPress 新站搭建下载中心和文档库，数据全部来自 poweris API

- [ ] 实现 `/downloads/` 页面模板（筛选+搜索，直接调用 poweris API 获取 S3 下载链接）
- [ ] 实现 `/library/` 页面模板（PDF 分类浏览，数据来自 poweris API）
- [ ] poweris 后台添加 compliance（合规认证）资源分类，或在前端筛选现有分类
- [ ] 构建产品聚合页模板 `/products/{model}/`（聚合 poweris 资源 + MkDocs 在线文档链接）
- [ ] 产品聚合页手册链接过渡逻辑：优先 MkDocs，回退 Zoho/语雀（从 poweris 获取）
- [ ] 导航从行业优先改为产品优先
- [ ] 实现 SEO: sitemap.xml、面包屑、meta 标签
- [ ] 旧 SPA 哈希路由 301 重定向到新 URL
- [ ] 评估是否需要 WordPress CPT 缓存 poweris 数据，还是纯前端调用 poweris API

---

## 十、验证方法

### 本地验证

```bash
cd F:\github\documents

# 验证各站点构建
python -m mkdocs build -f mkdocs.yml -d site --clean
python -m mkdocs build -f mkdocs.en.yml -d site/en
python -m mkdocs build -f mkdocs.releases.zh.yml -d site-releases --clean
python -m mkdocs build -f mkdocs.dev.zh.yml -d site-dev --clean

# 验证 generate_product_index.py
python scripts/generate_product_index.py --dry-run --report

# 验证 scaffold_product.py（含 deployment/）
python scripts/scaffold_product.py --model TEST999 --category "Routers" --chipset "Industrial" --dry-run
```

### 部署验证

```bash
# Nginx 反向代理
curl -I https://inhand.com.cn/docs/      # MkDocs 文档首页
curl -I https://inhand.com.cn/kb/        # MkDocs 知识库首页
curl -I https://inhand.com.cn/           # WordPress 主站

# SEO 验证
curl -s https://inhand.com.cn/docs/ | grep '<title>'
```

---

## 十一、待确认事项

### 内容侧（需要产品/支持团队提供）

1. **首批 Release Notes**：从 poweris API changelogMaps 接口导出现有版本记录，转为 Markdown
2. **知识库首批文章**：每个热门产品至少 1 篇 Getting Started + 1 篇常见故障排除
3. **合规认证文档**：确认 poweris 是否已有 compliance 分类，或需新增
4. **部署案例内容**：将现有客户部署经验整理为 Markdown 案例文档
5. **API 文档**：InCloud Manager API endpoint 列表、请求/响应示例
6. **手册迁移优先级列表**：确定哪些产品的 Zoho/语雀手册优先迁移到 MkDocs

### 技术侧（需要开发/运维确认）

1. **WordPress 新站进度**：wp-beta.inhand.online 的开发状态
2. **Nginx 配置权限**：谁负责生产环境 Nginx 配置变更
3. **域名与 SSL**：确认 /docs/ 等路径的 SSL 证书覆盖
4. **CI 部署目标路径**：确认 MkDocs 构建输出部署到服务器的具体路径
5. **poweris API 文档**：需要完整的 poweris API 文档（资源聚合接口、changelogMaps 接口的请求/响应格式），用于实现 WordPress 下载中心和 Release Notes 导入脚本
6. **poweris 手册链接字段**：确认 poweris 数据库中 Zoho/语雀链接的字段名和格式，用于实现产品聚合页的过渡链接逻辑
7. **poweris CORS 策略**：WordPress 前端直接调用 poweris API 是否有跨域限制，是否需要后端代理
