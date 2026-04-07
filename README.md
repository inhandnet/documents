# InHand Documents — 统一文档资产管理平台

本仓库是 InHand Networks 的统一文档资产管理平台，集中管理用户手册、QA 知识库、产品规格书、方案配置和产品宣传册，支持中英文双语，基于 MkDocs Material 主题构建，通过 GitHub Actions 自动部署。

---

## 一、项目整体结构

```
documents/
│
├── docs/                                # 用户手册（MkDocs 站点源文件）
│   ├── zh/                              #   中文手册
│   │   ├── {Category}/                  #     第一层：产品大类
│   │   │   └── {Chipset}/               #       第二层：芯片平台/产品子类
│   │   │       └── {Model}/             #         第三层：具体产品型号
│   │   │           ├── index.md         #           [CI 自动生成] 产品索引页（含交叉链接）
│   │   │           ├── User_Manual.md   #           用户手册
│   │   │           └── images/          #           手册配图
│   │   ├── assets/                      #     站点 Logo、Favicon 等静态资源
│   │   ├── javascripts/                 #     自定义 JS（侧边栏搜索、PDF 嵌入等）
│   │   ├── stylesheets/                 #     自定义 CSS 样式
│   │   └── index.md                     #     站点首页
│   └── en/                              #   英文手册（目录结构与 zh/ 对称）
│
├── qa/                                  # QA 知识库（常见问题与解答）
│   ├── zh/                              #   中文 QA
│   │   └── {Category}/{Chipset}/{Model}/
│   │       └── qa_article.md            #     QA 文章（与 docs/ 同路径对应）
│   └── en/                              #   英文 QA
│
├── specs/                               # 产品规格书
│   ├── zh/                              #   中文规格书
│   │   └── {Category}/{Chipset}/{Model}/
│   │       └── datasheet.pdf            #     规格书文件（与 docs/ 同路径对应）
│   └── en/                              #   英文规格书
│
├── configurations/                      # 方案配置（独立案例结构，不与 docs/ 镜像）
│   ├── zh/                              #   中文配置
│   │   └── {Model}/                     #     产品型号
│   │       └── {CaseName}/              #       案例名称
│   │           ├── 案例手册.md           #         案例说明文档
│   │           ├── 配置手册.md           #         配置操作指南
│   │           ├── config/              #         配置文件
│   │           └── assets/              #         资源文件（图片等）
│   └── en/                              #   英文配置（结构与 zh/ 对称）
│
├── brochures/                           # 产品宣传册（Brochure / Single Page）
│   ├── zh/                              #   中文宣传册
│   │   └── {Category}/{Chipset}/{Model}/
│   │       └── brochure.pdf             #     产品宣传册 PDF（与 docs/ 同路径对应）
│   └── en/                              #   英文宣传册
│
├── scripts/                             # 构建与同步脚本
│   ├── generate_product_index.py        #   按产品聚合索引页生成（CI 构建时自动运行）
│   ├── scaffold_product.py              #   新产品脚手架：一键创建四类镜像目录和模板
│   ├── build_specs.py                   #   规格书构建：Markdown → PDF（Pandoc + WeasyPrint）
│   ├── discourse_sync.py                #   QA 文章同步到 Discourse 论坛
│   └── wp_sync.py                       #   规格书/配置/宣传册同步到 WordPress 资源中心
│
├── .github/workflows/                   # CI/CD 流水线
│   ├── deploy-manuals.yml               #   用户手册：构建 → 部署到服务器 + GitHub Pages
│   ├── deploy-qa.yml                    #   QA 知识库：构建 → 部署到服务器 + 同步 Discourse
│   ├── deploy-specs.yml                 #   规格书：Markdown→PDF → 上传到 WordPress 服务器
│   └── deploy-downloads.yml             #   下载资源：上传到 WordPress 服务器
│
├── mkdocs.yml                           # 中文用户手册站点配置
├── mkdocs.en.yml                        # 英文用户手册站点配置
├── mkdocs.qa.zh.yml                     # 中文 QA 知识库站点配置
├── mkdocs.qa.en.yml                     # 英文 QA 知识库站点配置
├── validate_products.py                 # 产品目录名白名单校验（对接官网 API）
├── requirements.txt                     # Python 依赖
└── README.md                            # 本文件
```

**内容类型按产品镜像的目录结构：**

docs、qa、specs、brochures 四种内容类型在 `{lang}/` 下使用**相同的产品目录路径**，`configurations/` 采用独立的案例结构（按产品型号名匹配）：

```
docs/zh/AI Edge Computers/Rockchip/EC942/       ← 用户手册 (.md)
qa/zh/AI Edge Computers/Rockchip/EC942/         ← QA 文章 (.md)
specs/zh/AI Edge Computers/Rockchip/EC942/      ← 规格书 (.pdf)
brochures/zh/AI Edge Computers/Rockchip/EC942/  ← 产品宣传册 (.pdf)
configurations/zh/EC942/                         ← 方案配置（独立结构，按型号匹配）
  ├── 案例A/案例手册.md
  └── 案例B/config/config.json
```

> CI 构建时，`generate_product_index.py` 扫描 `docs/` 下的产品目录，检查 `qa/`、`specs/`、`brochures/` 下是否存在同路径目录，检查 `configurations/` 下是否存在同产品型号目录，自动在产品 `index.md` 中生成交叉链接。

---

## 二、各模块详细说明

### 1. `docs/` — 用户手册

| 项目      | 说明                                                       |
| --------- | ---------------------------------------------------------- |
| 用途      | 产品用户手册，Markdown 格式编写                            |
| 站点框架  | MkDocs + Material 主题                                     |
| 配置文件  | `mkdocs.yml`（中文）、`mkdocs.en.yml`（英文）              |
| CI 流水线 | `deploy-manuals.yml`                                       |
| 部署目标  | 海外服务器 + 国内服务器 + GitHub Pages                     |
| 触发条件  | `docs/**` 或 `mkdocs.yml` / `mkdocs.en.yml` 变更时自动构建 |

**目录层级规范：**

- 第一层：产品大类（如 `AI Edge Computers`、`Routers`）
- 第二层：产品子类或芯片平台（如 `Rockchip`、`Industrial Routers`）
- 第三层：具体产品型号（如 `EC942`、`IR615`）
- 目录命名必须与官网产品名称一致，最多三层

### 2. `qa/` — QA 知识库

| 项目      | 说明                                                          |
| --------- | ------------------------------------------------------------- |
| 用途      | 产品常见问题与解答（FAQ），Markdown 格式                      |
| 站点框架  | MkDocs + Material 主题                                        |
| 配置文件  | `mkdocs.qa.zh.yml`（中文）、`mkdocs.qa.en.yml`（英文）        |
| CI 流水线 | `deploy-qa.yml`                                               |
| 部署目标  | 海外服务器 + 国内服务器                                       |
| 附加功能  | 自动同步到 Discourse 论坛（通过 `scripts/discourse_sync.py`） |
| 触发条件  | `qa/**` 或 QA 配置文件变更时自动构建                          |

**Discourse 同步机制：**

- 新建 QA 文章 → 自动在 Discourse 创建帖子 → 回填 `discourse_topic_id` 到 frontmatter
- 更新 QA 文章 → 自动更新对应 Discourse 帖子内容

### 3. `specs/` — 产品规格书

| 项目      | 说明                                                         |
| --------- | ------------------------------------------------------------ |
| 用途      | 产品规格书（Datasheet），支持 PDF 直传或 Markdown 自动转 PDF |
| 构建脚本  | `scripts/build_specs.py`                                     |
| CI 流水线 | `deploy-specs.yml`                                           |
| 部署目标  | WordPress 服务器（`/wp-content/uploads/resources/specs`）    |
| 触发条件  | `specs/**` 变更时自动构建                                    |

**构建逻辑：**

1. 已有同名 `.pdf` 文件 → 直接复制到输出目录，跳过构建
2. 仅有 `.md` 文件 → 使用 Pandoc + WeasyPrint 转换为 PDF
3. 输出到 `dist/specs/`，保持原始目录结构

### 4. `configurations/` — 方案配置

| 项目      | 说明                                                               |
| --------- | ------------------------------------------------------------------ |
| 用途      | 产品方案配置，按案例组织（案例手册、配置手册、配置文件、资源文件） |
| 目录结构  | `{lang}/{Model}/{CaseName}/`（独立于其余四种内容类型的镜像路径）   |
| CI 流水线 | 待创建（计划 `deploy-configurations.yml`）                         |
| 部署目标  | WordPress 服务器（`/wp-content/uploads/resources/configurations`） |
| 触发条件  | `configurations/**` 变更时自动上传                                 |

**案例目录结构：**

每个产品下按业务场景或客户需求组织案例，每个案例目录包含：

- `案例手册.md` / `case-manual.md` — 案例说明文档（必需）
- `配置手册.md` / `config-manual.md` — 配置操作指南（可选）
- `config/` — 配置文件目录（必需）
- `assets/` — 资源文件目录，如图片（可选）

### 5. `brochures/` — 产品宣传册

| 项目      | 说明                                                          |
| --------- | ------------------------------------------------------------- |
| 用途      | 产品宣传册 / Brochure（单页或多页 PDF，概览性质的产品介绍）   |
| CI 流水线 | 待创建（计划 `deploy-brochures.yml`）                         |
| 部署目标  | WordPress 服务器（`/wp-content/uploads/resources/brochures`） |
| 触发条件  | `brochures/**` 变更时自动上传                                 |

### 6. `scripts/` — 构建与同步脚本

| 脚本                        | 用途                                                                               |
| --------------------------- | ---------------------------------------------------------------------------------- |
| `generate_product_index.py` | 扫描所有产品目录，自动生成按产品聚合的 `index.md` 索引页（含交叉链接与完整度报告） |
| `scaffold_product.py`       | 新产品脚手架，一键在 docs/qa/specs/brochures 创建目录和模板文件                    |
| `build_specs.py`            | 遍历 `specs/` 下的 Markdown 文件，通过 Pandoc 转换为 PDF                           |
| `discourse_sync.py`         | 将 QA 文章变更同步到 Discourse 论坛（创建/更新帖子）                               |
| `wp_sync.py`                | 将规格书/配置/宣传册信息同步到 WordPress 资源中心（可选，REST API）                |

### 7. 产品索引页与交叉链接

CI 构建用户手册时，`scripts/generate_product_index.py` 自动为每个产品型号生成 `index.md` 索引页。

**交叉链接原理：**

脚本以 `docs/{lang}/{Category}/{Chipset}/{Model}/` 为基准，检查 `qa/`、`specs/`、`brochures/` 下是否存在**同路径**目录，检查 `configurations/` 下是否存在**同产品型号**目录，存在则在索引页中生成对应链接。

```
docs/zh/AI Edge Computers/Rockchip/EC942/
  ├── index.md              ← [自动生成] 产品聚合入口
  ├── EC942_User_Manual.md  ← 手册正文
  │
  │   交叉链接指向：
  │   ├── → /qa/AI Edge Computers/Rockchip/EC942/*.md                    （QA 文章，同路径匹配）
  │   ├── → /specs/zh/AI Edge Computers/Rockchip/EC942/*.pdf             （规格书，同路径匹配）
  │   ├── → /configurations/zh/EC942/*/案例手册.md                        （方案配置，按型号匹配）
  │   └── → /brochures/zh/AI Edge Computers/Rockchip/EC942/*.pdf         （产品宣传册，同路径匹配）
```

**生成的 index.md 内容示例：**

```markdown
# EC942

**AI Edge Computers** / **Rockchip** / **EC942**

## User Manual

- [EC942 User Manual](EC942_User_Manual.md)

## QA

- [EC942 FAQ](/qa/AI Edge Computers/Rockchip/EC942/faq.html)

## Specs

- [EC942_Datasheet.pdf](/specs/zh/AI Edge Computers/Rockchip/EC942/EC942_Datasheet.pdf)

## Configurations

- [案例A — 案例手册](/configurations/zh/EC942/案例A/案例手册.html)
- [案例A — config.json](/configurations/zh/EC942/案例A/config/config.json)

## Brochures

- [EC942_Brochure.pdf](/brochures/zh/AI Edge Computers/Rockchip/EC942/EC942_Brochure.pdf)
```

MkDocs 的 `navigation.indexes` 特性会将 `index.md` 作为目录的入口页面展示在导航栏中。

**完整度报告：**

使用 `--report` 参数时，脚本会输出所有产品在五种内容类型下的覆盖情况：

```
Product                        Manual     QA      Specs   Configurations Brochures
------------------------------------------------------------------------------------
[zh] EC942                       Y        Y        Y          -            -
[zh] EC954                       Y        -        Y          -            -
[en] EC942                       Y        Y        -          -            -
------------------------------------------------------------------------------------
Total: 3 products, 0 fully documented (0%)
```

**本地预览：**

```bash
# 生成索引页（dry-run 模式，仅打印不写入）
python scripts/generate_product_index.py --dry-run

# 生成索引页并查看完整度报告
python scripts/generate_product_index.py --report

# 生成后启动本地预览
python scripts/generate_product_index.py
mkdocs serve -f mkdocs.yml
```

> 生成的 `index.md` 已在 `.gitignore` 中排除，不会被提交到 Git。

**CI Job Summary：**

在 GitHub Actions 中运行时，完整度报告会自动写入 [Job Summary](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#adding-a-job-summary)，以 Markdown 表格形式展示在 workflow 运行页面中。

### 8. 新产品脚手架

`scripts/scaffold_product.py` 解决添加新产品时需要在多个内容目录下手动创建文件夹的痛点，一条命令自动创建 docs/qa/specs/brochures 的目录结构和模板文件（`configurations/` 采用独立案例结构，需手动创建）：

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

执行后自动创建：

```
docs/{zh,en}/AI Edge Computers/Rockchip/EC999/
  ├── EC999_User_Manual.md    ← 手册模板（含章节骨架）
  └── images/.gitkeep
qa/{zh,en}/AI Edge Computers/Rockchip/EC999/
  └── EC999_FAQ.md            ← QA 模板（含 frontmatter tags）
specs/{zh,en}/AI Edge Computers/Rockchip/EC999/
  └── .gitkeep                ← 占位，待上传规格书 PDF
brochures/{zh,en}/AI Edge Computers/Rockchip/EC999/
  └── .gitkeep                ← 占位，待上传产品宣传册 PDF
```

### 9. `validate_products.py` — 产品目录校验

在 CI 构建前自动运行，对接官网 API 获取产品名白名单，校验文档目录名是否与官网一致。支持 `--paths` 参数指定校验范围：

```bash
# 校验用户手册目录（默认）
python validate_products.py

# 校验 QA 目录
python validate_products.py --paths qa/zh qa/en

# 校验规格书目录
python validate_products.py --paths specs/zh specs/en
```

### 10. `.github/workflows/` — CI/CD 流水线

| 流水线                 | 触发路径       | 构建产物                                  | 部署目标                               |
| ---------------------- | -------------- | ----------------------------------------- | -------------------------------------- |
| `deploy-manuals.yml`   | `docs/**`      | MkDocs 静态站点（含自动生成的产品索引页） | 海外服务器 + 国内服务器 + GitHub Pages |
| `deploy-qa.yml`        | `qa/**`        | MkDocs 静态站点                           | 海外服务器 + 国内服务器 + Discourse    |
| `deploy-specs.yml`     | `specs/**`     | PDF 文件                                  | WordPress 服务器                       |
| `deploy-downloads.yml` | `downloads/**` | 原始文件                                  | WordPress 服务器                       |

所有流水线仅在 `master` 分支推送时触发，也支持手动触发（`workflow_dispatch`）。

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

- 文件夹命名必须与官网产品名称保持一致，确保产品与文档的对应性；
- 目录层级最多支持三层，无需二级子类时仅保留两层目录，需细分二级子类时扩展为三层目录。

#### 目录结构示例

**示例 1：带三级目录（需二级子类细分）**

    docs/zh/Routers/Industrial Routers/IR615/     ← 用户手册
    docs/zh/Routers/Industrial Routers/IR302/
    docs/en/Routers/Industrial Routers/IR615/     ← 英文对称
    docs/en/Routers/Industrial Routers/IR302/

    层级说明：
    Routers/                  （第一层：产品大类）
      └─ Industrial Routers/  （第二层：带二级子类）
           └─ IR615/          （第三层：产品系列）
                └─ User_Manual.md

**示例 2：仅二级目录（无需二级子类细分）**

    docs/zh/Edge Computers/EC300/                 ← 用户手册
    docs/en/Edge Computers/EC300/

    层级说明：
    Edge Computers/           （第一层：产品大类）
      └─ EC300/               （第二层：产品系列，无三级目录）
           └─ User_Manual.md

**示例 3：多内容类型目录对应**

添加一个产品的完整资源时，docs/qa/specs/brochures 使用**相同路径**，configurations 使用独立的案例结构：

    docs/zh/AI Edge Computers/Rockchip/EC942/EC942_User_Manual.md
    qa/zh/AI Edge Computers/Rockchip/EC942/faq.md
    specs/zh/AI Edge Computers/Rockchip/EC942/EC942_Datasheet.pdf
    configurations/zh/EC942/远程监控方案/案例手册.md         ← 独立结构，按型号匹配
    brochures/zh/AI Edge Computers/Rockchip/EC942/EC942_Brochure.pdf

> docs/qa/specs/brochures 需路径一致（`{Category}/{Chipset}/{Model}`），configurations 通过产品型号名匹配。不要求所有类型同时存在，缺失的类型会被跳过。

### 3. 网页端操作流程

#### （1）创建分支

1. 访问主仓库地址 https://github.com/inhandnet/documents；
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
#    例如：docs/zh/Routers/Industrial Routers/IR302/IR302快速手册.md
#    图片放 docs/zh/.../images/

# 3. 提交改动
git add .
git commit -m "docs: add IR302 quick manual (ZH)"

# 4. 推送到远端
git push -u origin docs-Vehicles-teams

# 5. 去 GitHub 页面创建 PR（推送后通常会提示 "Compare & pull request"）
```

---

## 四、注意事项

1. 分支命名需清晰可辨，便于团队识别文档归属；
2. 文档上传前需核对目录路径，确保语言目录、产品层级无错误；
3. 禁止在个人分支中修改 master 分支已合并的其他文档，如需修改需单独创建分支并提交审核；
4. 合并请求提交后，需及时关注审核反馈，避免长时间未处理导致文档过时；
5. `specs/`、`brochures/` 中的 PDF 大文件已配置 Git LFS 自动管理（见 `.gitattributes`）；
6. 所有目录均支持 `validate_products.py` 产品名校验，CI 会在构建前自动检查。
