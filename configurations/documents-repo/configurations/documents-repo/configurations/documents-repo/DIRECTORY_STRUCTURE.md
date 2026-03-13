# InHand Documents — 目录结构说明

本文档说明仓库的内容目录组织方式、产品路径规范和多内容类型的对应关系。

> 资源中心双平台架构的完整方案见 `RESOURCE_CENTER_PLAN.md`。

---

## 一、内容目录总览

仓库按**内容类型**划分为以下顶层目录：

| 目录               | 内容类型     | 目录结构                                        | 文件格式                    | 部署目标               | 说明             |
| ---------------- | ---------- | --------------------------------------------- | ----------------------- | -------------------- | ---------------- |
| `docs/`          | 用户手册     | `{lang}/{Category}/{Chipset}/{Model}/`        | `.md`                   | `/docs/` (MkDocs)    | Markdown 格式产品手册 |
| `qa/`            | QA 知识库   | `{lang}/{Category}/{Chipset}/{Model}/`        | `.md`                   | `/kb/` (MkDocs)      | 常见问题与解答         |
| `releases/`      | Release Notes | `{lang}/{Product}.md`                       | `.md`                   | `/releases/` (MkDocs)| 产品固件发版说明       |
| `dev/`           | 开发者文档   | `{lang}/{topic}/`                             | `.md`                   | `/developers/` (MkDocs)| API/MQTT/集成指南   |
| `specs/`         | 产品规格书   | `{lang}/{Category}/{Chipset}/{Model}/`        | `.pdf` / `.md`（自动转 PDF）| WordPress `/library/` | 产品技术规格          |
| `brochures/`     | 产品宣传册   | `{lang}/{Category}/{Chipset}/{Model}/`        | `.pdf`                  | WordPress `/library/` | 产品概览宣传册       |
| `configurations/`| 方案配置     | `{lang}/{Model}/{CaseName}/`（独立结构）       | `.md` / `.cfg` / `.json` 等 | ~~废弃~~→迁移至 docs/deployment/ | 按案例组织的配置方案  |

> `docs/`、`qa/`、`specs/`、`brochures/` 使用相同的产品镜像路径；`configurations/` 采用独立的案例结构（正在迁移到 docs/deployment/）；`releases/` 和 `dev/` 使用扁平结构。

---

## 二、目录层级规范

### 镜像路径（docs / qa / specs / brochures）

按 **语言 → 产品大类 → 产品子类 → 产品型号** 组织：

```
{content_type}/
├── zh/                                  # 中文
│   ├── {Category}/                      # 第一层：产品大类
│   │   └── {Chipset}/                   # 第二层：芯片平台 / 产品子类
│   │       └── {Model}/                 # 第三层：具体产品型号
│   │           └── ...                  # 该类型的文件
│   └── ...
└── en/                                  # 英文（目录结构与 zh/ 完全对称）
    └── ...
```

**层级说明：**

- **第一层 — 产品大类**：如 `AI Edge Computers`、`Routers`、`Edge Computers`
- **第二层 — 产品子类/芯片平台**：如 `Rockchip`、`Industrial Routers`、`TI`
- **第三层 — 产品型号**：如 `EC942`、`IR615`、`EC300`
- 目录命名必须与官网产品名称一致
- 最多三层；无需二级子类时可省略第二层，直接 `{Category}/{Model}/`

### 案例路径（configurations — 废弃，迁移中）

> **注意**：`configurations/` 目录正在废弃，新增部署案例请直接放在 `docs/{lang}/{Category}/{Chipset}/{Model}/deployment/` 下。

原有结构按 **语言 → 产品型号 → 案例名称** 组织：

```
configurations/
├── zh/
│   └── {Model}/                         # 产品型号（直接在语言目录下）
│       └── {CaseName}/                  # 案例名称
│           ├── 案例手册.md
│           ├── config/
│           └── assets/
└── en/
    └── ...
```

### 扁平路径（releases / dev）

`releases/` 和 `dev/` 不使用 Category/Chipset/Model 层级：

```
releases/
├── zh/
│   ├── index.md                         # 首页
│   └── {Product}.md                     # 每产品一个文件，按版本号倒序
└── en/
    └── ...

dev/
├── zh/
│   ├── index.md                         # 首页
│   ├── api/                             # 按主题组织
│   ├── mqtt/
│   └── integration-guides/
└── en/
    └── ...
```

---

## 三、各目录详细结构

### 1. `docs/` — 用户手册

```
docs/
├── zh/
│   ├── AI Edge Computers/
│   │   └── Rockchip/
│   │       ├── EC942/
│   │       │   ├── index.md               ← [CI 自动生成] 产品索引页（含交叉链接）
│   │       │   ├── EC942_User_Manual.md   ← 用户手册正文
│   │       │   ├── deployment/            ← [新增] 部署案例
│   │       │   │   └── {CaseName}/
│   │       │   │       ├── case-manual.md
│   │       │   │       └── config/
│   │       │   └── images/                ← 手册配图
│   │       │       └── screenshot.png
│   │       └── EC954/
│   │           ├── EC954_User_Manual.md
│   │           ├── deployment/
│   │           └── images/
│   ├── assets/                            ← 站点公共资源（Logo、Favicon）
│   ├── javascripts/                       ← 自定义 JS
│   ├── stylesheets/                       ← 自定义 CSS
│   └── index.md                           ← 站点首页
└── en/                                    ← 英文（结构与 zh/ 对称）
    └── ...
```

### 2. `qa/` — QA 知识库

```
qa/
├── zh/
│   ├── AI Edge Computers/                 # 现有：产品镜像路径
│   │   └── Rockchip/
│   │       └── EC942/
│   │           └── EC942_FAQ.md
│   ├── getting-started/                   # [Phase 2] 按分类前缀组织
│   │   └── {Category}/{Model}/
│   ├── how-to/
│   │   └── {Category}/{Model}/
│   ├── troubleshooting/
│   │   └── {Category}/{Model}/
│   ├── application-notes/
│   │   └── {Category}/{Model}/
│   ├── faq/
│   │   └── {Category}/{Model}/
│   └── assets/
├── en/
│   └── ...
└── discourse_categories.yml               ← Discourse 分类映射
```

### 3. `releases/` — Release Notes

```
releases/
├── zh/
│   ├── index.md                           ← 首页
│   ├── IR915.md                           ← 每产品一个文件
│   ├── ER805.md
│   ├── InCloud_Manager.md
│   └── assets/
└── en/
    └── ...
```

### 4. `dev/` — 开发者文档

```
dev/
├── zh/
│   ├── index.md                           ← 首页
│   ├── api/
│   │   └── index.md                       ← InCloud Manager REST API
│   ├── mqtt/
│   │   └── index.md                       ← MQTT 主题与报文格式
│   ├── integration-guides/
│   │   └── index.md                       ← Azure IoT / AWS IoT
│   └── assets/
└── en/
    └── ...
```

### 5. `specs/` — 产品规格书

```
specs/
├── zh/
│   └── AI Edge Computers/
│       └── Rockchip/
│           └── EC942/
│               └── EC942_Datasheet.pdf
└── en/
    └── ...
```

### 6. `brochures/` — 产品宣传册

```
brochures/
├── zh/
│   └── AI Edge Computers/
│       └── Rockchip/
│           └── EC942/
│               └── EC942_Brochure.pdf
└── en/
    └── ...
```

### 7. `overrides/` — MkDocs 模板覆盖

```
overrides/
└── main.html                              ← 注入 WordPress 统一导航头
```

所有 8 个 mkdocs*.yml 通过 `custom_dir: overrides` 引用此目录。

---

## 四、MkDocs 配置文件清单

| 配置文件 | 源目录 | 部署 URL | 语言 |
|----------|--------|----------|------|
| `mkdocs.yml` | `docs/zh` | `/docs/` | zh |
| `mkdocs.en.yml` | `docs/en` | `/docs/en/` | en |
| `mkdocs.qa.zh.yml` | `qa/zh` | `/kb/` | zh |
| `mkdocs.qa.en.yml` | `qa/en` | `/kb/en/` | en |
| `mkdocs.releases.zh.yml` | `releases/zh` | `/releases/` | zh |
| `mkdocs.releases.en.yml` | `releases/en` | `/releases/en/` | en |
| `mkdocs.dev.zh.yml` | `dev/zh` | `/developers/` | zh |
| `mkdocs.dev.en.yml` | `dev/en` | `/developers/en/` | en |

---

## 五、镜像路径与交叉链接

docs、qa、specs、brochures 四种内容类型在 `{lang}/` 下使用**完全相同的产品目录路径**：

```
docs/zh/AI Edge Computers/Rockchip/EC942/       ← 用户手册
qa/zh/AI Edge Computers/Rockchip/EC942/         ← QA 文章
specs/zh/AI Edge Computers/Rockchip/EC942/      ← 规格书
brochures/zh/AI Edge Computers/Rockchip/EC942/  ← 产品宣传册
```

CI 构建时，`generate_product_index.py` 扫描 `docs/` 下的产品目录，自动在产品 `index.md` 中生成交叉链接，包括：

| 内容类型 | 链接目标 | 匹配方式 |
|----------|----------|----------|
| 用户手册 | 同目录下的 .md 文件 | 直接扫描 |
| 部署案例 | `deployment/` 子目录 | 扫描 model_path/deployment/ |
| QA | `/kb/{path}` | 镜像路径匹配 |
| 规格书 | `/{specs_path}` | 镜像路径匹配 |
| 方案配置 | `/configurations/{path}` | 产品型号匹配 |
| 宣传册 | `/{brochures_path}` | 镜像路径匹配 |

> 不要求所有类型同时存在，缺失的类型会被跳过。

---

## 六、新产品目录创建

使用脚手架脚本一键创建 docs/qa/specs/brochures 的目录结构：

```bash
python scripts/scaffold_product.py \
  --model EC999 \
  --category "AI Edge Computers" \
  --chipset Rockchip
```

自动创建：

```
docs/{zh,en}/AI Edge Computers/Rockchip/EC999/
  ├── EC999_User_Manual.md    ← 手册模板
  ├── images/.gitkeep
  └── deployment/.gitkeep     ← [新增] 部署案例目录
qa/{zh,en}/AI Edge Computers/Rockchip/EC999/
  └── EC999_FAQ.md            ← QA 模板
specs/{zh,en}/AI Edge Computers/Rockchip/EC999/
  └── .gitkeep
brochures/{zh,en}/AI Edge Computers/Rockchip/EC999/
  └── .gitkeep
```

支持 `--langs zh` 仅创建中文、`--dry-run` 预览不写入。

> `configurations/` 已废弃，新增部署案例直接放在 `docs/.../deployment/` 下。
> `releases/` 和 `dev/` 手动创建文件即可，无需 scaffold。
