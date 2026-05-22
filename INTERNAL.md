# InHand Documents — 产品手册文档站点

本仓库是 InHand Networks 的**统一文档资产管理主仓库**，集中管理用户手册、QA 知识库、产品规格书、方案配置等内容，支持中英文双语，基于 MkDocs Material 主题构建，通过 GitHub Actions 自动部署。

> **说明**：本仓库是文档资产的主汇总点。QA、规格书、方案配置等内容正逐步从其他仓库合并汇总至此。目前仓库中 `Manuals/` 为主要内容类型，产品目录 `{Model}/` 下可包含 `Specs/`、`Solutions/` 等多种内容类型子目录。

---

## 一、项目结构

```
documents/
│
├── docs/                                # 产品文档（MkDocs 站点源文件）
│   ├── zh/                              #   中文内容
│   │   ├── {Model}/                     #     产品型号目录
│   │   │   ├── Manuals/                 #       用户手册（.md）
│   │   │   │   └── images/              #       手册配图
│   │   │   └── ...                      #       其他内容类型（由外部仓库推送）
│   │   ├── assets/                      #   站点 Logo、Favicon 等静态资源
│   │   ├── javascripts/                 #   自定义 JS
│   │   ├── stylesheets/                 #   自定义 CSS 样式
│   │   └── index.md                     #   站点首页
│   └── en/                              #   英文内容（结构与 zh/ 对称）
│
├── scripts/                             # 构建脚本
│   ├── generate_product_index.py        #   按产品聚合索引页生成（CI 构建时自动运行）
│   ├── scaffold_product.py              #   新产品脚手架：一键创建目录和模板
│   ├── validate_docs.py                 #   校验文档路径到 PLM 系统
│   └── upload_specs_to_cloud.py         #   上传非 Markdown 文件到云存储
│
├── .github/workflows/                   # CI/CD 流水线
│   └── deploy-manuals.yml               #   用户手册：构建 → 部署到服务器
│
├── mkdocs.yml                           # 中文站点配置
├── mkdocs.en.yml                        # 英文站点配置
├── requirements.txt                     # Python 依赖
└── README.md                            # 本文件
```

**目录层级规范：**

- 第一层：语言目录（`zh/` / `en/`）
- 第二层：产品型号目录（如 `CPE02`、`EC300`、`ER805`），命名须与官网产品名称一致
- 第三层：内容类型子目录（如 `Manuals/`、`Specs/`、`Solutions/` 等）

---

## 二、各模块详细说明

### 1. `docs/` — 产品文档

| 项目      | 说明                                                       |
| --------- | ---------------------------------------------------------- |
| 用途      | 产品文档（用户手册、规格书、方案配置等），Markdown/PDF 格式 |
| 站点框架  | MkDocs + Material 主题                                     |
| 配置文件  | `mkdocs.yml`（中文）、`mkdocs.en.yml`（英文）              |
| CI 流水线 | `deploy-manuals.yml`                                       |
| 部署目标  | 海外服务器（英文）+ 国内服务器（中文）                     |
| 触发条件  | `docs/**`、`overrides/**`、`mkdocs.yml`、`mkdocs.en.yml` 变更时自动构建 |

**目录结构示例：**

```
docs/en/
├── CPE02/
│   ├── Manuals/
│   │   ├── CPE02_User_Manual.md
│   │   └── images/
│   # ├── Specs/           ← 规格书
│   # └── Solutions/       ← 方案配置
├── EC300/
│   └── Manuals/
│       ├── EC300_User_Manual.md
│       └── images/
├── assets/
├── javascripts/
├── stylesheets/
└── index.md
```

### 2. 产品索引页

CI 构建时，`scripts/generate_product_index.py` 自动为每个产品型号生成 `index.md` 索引页，汇总该产品目录下的所有手册文档。

MkDocs 的 `navigation.indexes` 特性会将 `index.md` 作为目录的入口页面展示在导航栏中。

**本地预览：**

```bash
# 生成索引页（dry-run 模式，仅打印不写入）
python scripts/generate_product_index.py --dry-run

# 生成索引页并查看覆盖度报告
python scripts/generate_product_index.py --report

# 生成后启动本地预览
python scripts/generate_product_index.py
mkdocs serve -f mkdocs.yml
```

> 生成的 `index.md` 已在 `.gitignore` 中排除，不会被提交到 Git。

**CI Job Summary：**

在 GitHub Actions 中运行时，覆盖度报告会自动写入 [Job Summary](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#adding-a-job-summary)，以 Markdown 表格形式展示在 workflow 运行页面中。

### 3. 新产品脚手架

`scripts/scaffold_product.py` 用于快速创建新产品的目录结构和模板文件：

```bash
# 创建 EC999 产品的完整脚手架（中英文）
python scripts/scaffold_product.py \
  --model EC999 \
  --category "AI Edge Computers" \
  --chipset Rockchip

# 仅创建中文
python scripts/scaffold_product.py \
  --model IR302 \
  --category Routers \
  --chipset "Industrial Routers" \
  --langs zh

# 预览将要创建的内容（不实际写入）
python scripts/scaffold_product.py \
  --model EC999 \
  --category "AI Edge Computers" \
  --chipset Rockchip \
  --dry-run
```

### 4. `scripts/validate_docs.py` — 文档路径校验

对接 PLM 系统 API，校验文档文件路径的合法性：

```bash
# 校验 git 变更的文件（默认）
python scripts/validate_docs.py --diff

# 校验指定文件
python scripts/validate_docs.py --file docs/en/CPE02/Manuals/CPE02_User_Manual.md

# 校验所有文件
python scripts/validate_docs.py --all
```

### 5. `.github/workflows/deploy-manuals.yml` — CI/CD 流水线

| 流水线                 | 触发路径                                          | 构建产物              | 部署目标                     |
| ---------------------- | ------------------------------------------------- | --------------------- | ---------------------------- |
| `deploy-manuals.yml`   | `docs/**`、`overrides/**`、`mkdocs.yml`、`mkdocs.en.yml` | MkDocs 静态站点       | 海外服务器（en）+ 国内服务器（zh） |

流水线步骤（push 到 `master` 时）：
1. `validate_docs.py --diff` — 校验变更文件
2. `validate_docs.py --forbid-deleted` — 禁止删除文档
3. `upload_specs_to_cloud.py --dist-dir docs` — 上传非 Markdown 文件到云存储
4. `generate_product_index.py --report` — 生成产品索引页
5. `mkdocs build`（中文 + 英文）— 构建静态站点
6. SCP 部署 — 中文站点到国内服务器，英文站点到海外服务器

PR 提交时仅执行校验步骤，不触发构建和部署。

---

## 三、文档上传操作指导

### 1. 分支管理规则

- 禁止直接向 master 分支上传文件或提交修改；
- 团队成员需创建个人 / 功能分支用于文档上传与编辑；
- 文档完成后需通过合并请求（Pull Request）提交至 master 分支，经审核通过后合并。

```mermaid
graph LR
    A["团队成员"] -->|"创建"| B["个人/团队分支"]
    B -->|"上传文档"| C["文档完成"]
    C -->|"提交"| D["合并请求（Pull Request）"]
    D -->|"审核"| E["审核人员"]
    E -->|"通过"| F["合并至 master 分支"]
```

### 2. 目录命名规范

- 产品目录命名必须与官网产品名称保持一致；
- 文档放在对应产品目录下的 `Manuals/` 子目录中；
- 图片等资源文件放在 `Manuals/images/` 目录下。

#### 目录结构示例

```
docs/en/
├── CPE02/
│   └── Manuals/
│       ├── CPE02_User_Manual.md
│       └── images/
│           └── screenshot.png
├── EC300/
│   └── Manuals/
│       ├── EC300_User_Manual.md
│       └── images/
└── index.md

docs/zh/
├── CPE02/
│   ├── Manuals/
│   │   ├── CPE02_用户手册.md
│   │   └── images/
│   # ├── Specs/           ← 规格书
│   # └── Solutions/       ← 方案配置
└── index.md
```

### 3. 网页端操作流程

#### （1）创建分支

1. 访问主仓库地址；
2. 点击分支选择框（默认显示 master），输入新分支名称（建议格式：`docs-产品分类或产品系列或团队`，如 `docs-Vehicles-teams`），点击 "Create branch: 分支名" 完成创建。

#### （2）上传文档至目标目录

1. 在仓库页面切换至已创建的个人分支；
2. 导航至对应语言目录（`docs/en` 或 `docs/zh`），按目录结构找到目标产品目录；
   - 若目标目录不存在：进入上级目录后，点击 "Add file" → "Create new file"，在文件名输入框中输入 "目录名/"（末尾加斜杠），即可创建目录；
3. 点击 "Add file" → "Upload files"，拖拽文档至上传区域或选择本地文件；
4. 下拉至 "Commit changes" 区域，填写提交说明，点击 "Commit changes" 完成推送。

#### （3）提交合并请求

1. 文档上传完成后，点击 "Pull requests" → "New pull request"；
2. 左侧选择 base 分支为 master，右侧选择 compare 分支为个人分支；
3. 核对修改内容，填写标题和描述，点击 "Create pull request"。

#### （4）审核与合并

1. 审核人员将对文档的命名、目录路径、内容完整性进行审核；
2. 审核通过后合并至 master，CI 自动触发构建和部署；
3. 若需修改，将在合并请求中备注修改意见，提交人需在个人分支中完善后重新审核。

### 4. 命令行操作

```bash
# 1. 拉取最新 master 并创建分支
git checkout master
git pull
git checkout -b docs-Vehicles-teams

# 2. 添加文档文件（按目录规范放置）
#    例如：docs/en/CPE02/Manuals/CPE02_quick_guide.md
#    图片放 docs/en/CPE02/Manuals/images/

# 3. 提交改动
git add .
git commit -m "docs: add CPE02 quick guide (EN)"

# 4. 推送到远端
git push -u origin docs-Vehicles-teams

# 5. 去 GitHub 页面创建 PR（推送后通常会提示 "Compare & pull request"）
```

---

## 四、注意事项

1. 分支命名需清晰可辨，便于团队识别文档归属；
2. 文档上传前需核对目录路径，确保语言目录、产品目录无错误；
3. 禁止在个人分支中修改 master 分支已合并的其他文档，如需修改需单独创建分支并提交审核；
4. 合并请求提交后，需及时关注审核反馈，避免长时间未处理导致文档过时；
5. CI 会在构建前自动运行文档路径校验，请确保文件路径符合规范。
