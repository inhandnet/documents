# InHand 产品文档

本仓库包含 InHand Networks 产品文档的源文件，基于 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建，支持自动部署。

## 官方网站

- **英文版**: https://inhand.com
- **中文版**: https://inhand.com.cn

## 仓库结构

```
├── docs/
│   ├── en/              # 英文文档
│   └── zh/              # 中文文档
│
├── data/                # 结构化数据、同步到官网（EOL 产品清单）
├── scripts/             # 构建、校验、同步脚本
├── overrides/           # MkDocs 主题自定义
├── mkdocs.yml           # 中文站点配置
└── mkdocs.en.yml        # 英文站点配置
```

## 产品目录结构

文档按产品型号组织：

```
docs/zh/
├── CPE02/
│   ├── Manuals/
│   │   ├── CPE02_用户手册.md
│   │   └── images/
│   ├── Specs/           # 产品规格书
│   └── Solutions/       # 方案配置
├── EC300/
│   └── Manuals/
│       └── ...
└── index.md
```

### 产品目录（product-catalog.json）自动化

`docs/product-catalog.json` 把文档文件夹映射到一个稳定的产品身份。Documents MCP 检索服务
真正要求登记的，只是**含有至少一个 Markdown 文件**的顶层 `docs/{en,zh}/<文件夹>`——这是它
实际用来切分内容块的文件夹集合。纯 PDF 文件夹（例如多个下市子型号共用的规格书聚合目录）
是按 PDF 文件名单独匹配产品的，完全不需要出现在任何 `source_folders` 里。

当有 push 在 `docs/en/` 或 `docs/zh/` 下新增了**含 Markdown** 的顶层文件夹时，
`sync-product-catalog` GitHub Actions workflow 会运行 `scripts/sync_product_catalog.py`，
自动为新文件夹追加一条目录条目（`kind: model`、`public: true`、无别名）并提交。普通新增
Markdown 产品文件夹**不需要**手工编辑目录。新增的**纯 PDF** 文件夹会被脚本刻意忽略——如果
里面某个 PDF 无法归属到任何产品，MCP 构建本身会明确报错，那才是需要人工介入的信号。

以下情况仍需人工编辑 `docs/product-catalog.json`：

- **别名（aliases）**：产品的其他称呼。
- **调整 `kind`**（例如产品系列用 `family`、非硬件产品用 `software`）或 `public`（内部专用条目）。
- **把多个文件夹合并成一个产品**，例如同一产品在中英文下用了不同名字的文件夹
  （`source_folders: ["Eagle Energy Management", "白鹰能源管家"]`），或者要把一个纯 PDF
  聚合文件夹登记到某个已有产品的 `source_folders` 下。
- **下架产品，或处理改名/删除的文件夹**：脚本不会修改或删除任何已有条目，只会为新的
  Markdown 文件夹追加新条目；它不检查已登记文件夹是否还在磁盘上存在（MCP 构建本来就不是按
  磁盘是否存在来校验的），所以这种情况脚本不会报警，交由 MCP 构建自身的校验来发现。

## 本地开发

### 环境要求

- Python 3.11+
- pip

### 安装依赖

```bash
pip install -r requirements.txt
```

### 本地预览

```bash
# 中文站点
python -m mkdocs serve -f mkdocs.yml

# 英文站点
python -m mkdocs serve -f mkdocs.en.yml
```

### 构建

```bash
python -m mkdocs build -f mkdocs.yml -d site-zh --clean
python -m mkdocs build -f mkdocs.en.yml -d site-en --clean
```

## EOL 产品清单

官网上的 EOL（停产）表格由两张人手编辑的 Markdown 表格驱动——中英文两份
内容本来就不一样，各自独立维护：

| 数据文件 | 对应的官网页面 |
|----------|----------------|
| [`data/eol-products.zh.md`](data/eol-products.zh.md) | https://www.inhand.com.cn/support/eol-products |
| [`data/eol-products.en.md`](data/eol-products.en.md) | https://www.inhand.com/en/support/eol-products |

**这两个文件是镜像，不要在本仓库编辑**：清单在内部仓库 `device-hw-docs` 维护
（市场/产品同事在那边用 Issue 表单提变更申请），合并后自动同步到这里，在本仓库
的修改会被下次同步覆盖。

同步进来后 → CI 会跑一次预演，打印这次改动会让官网**新增/更新/删除**
哪些记录。合并到 `master` 后由 `.github/workflows/sync-eol.yml` 自动同步到
WordPress EOL REST API，双向且幂等：表格里新增/修改/删除的一行，会对应
在官网上新增/更新/删除。**删除是永久、不可恢复的**，删型号前先看 PR 预演，
或本地用 `--no-delete` 演练。

同一份数据也会生成文档站的 EOL 页面（`scripts/generate_eol_pages.py` →
`docs/<lang>/EOL Products/EOL Products.md`），随手册站发布并进 `llms.txt`
（AI 问答 / 爬虫可查）。那个页面是自动生成的，别手改，改 `data/` 下的文件。

如果同步失败，工作流会开（或在已有的上追加评论）一个带 `eol-sync` 标签的
issue，因为失败意味着仓库和官网已经不一致。同步是幂等的：修好原因后重跑
workflow 即可，不会重复创建/删除。

端点按站点用仓库变量 `EOL_API_ZH_URL` / `EOL_API_EN_URL` + 密钥
`EOL_API_ZH_TOKEN` / `EOL_API_EN_TOKEN` 配置，所以从测试站切到正式站只是
改变量，不用改代码。

```bash
# 本地预演
export EOL_API_ZH_URL="https://<host>/wp-json/eol/v1"
export EOL_API_ZH_TOKEN="..."
python scripts/sync_eol_products.py --site zh --dry-run
```

## 贡献

欢迎通过 Pull Request 提交文档改进建议。

- 从 `master` 创建功能分支
- 进行修改
- 提交 Pull Request 等待审核

## 许可证

Copyright (c) InHand Networks. 保留所有权利。
