# `data/` — 构建期数据

这里放**结构化源数据**：它们不是站点内容，而是构建和同步的输入。

站点内容在 `docs/zh`、`docs/en`（两个 mkdocs 配置的 `docs_dir`）。
`data/` 在站点源之外，**不会被发布**到文档站。

## 当前内容

| 文件 | 用途 |
| --- | --- |
| `eol-products.zh.md` | 中文站 EOL 清单，官网 EOL 页面的数据源 |
| `eol-products.en.md` | 英文站 EOL 清单，同上 |

这两份是**镜像**，由内部仓库 `device-hw-docs` 的 `eol-products/` 自动同步过来，
在本仓库直接改会被下一次同步覆盖。详见文件开头的说明。

本仓库拿它们做两件事：

- `scripts/generate_eol_pages.py` → 生成文档站的 EOL 页面（进 `llms.txt`）
- `scripts/sync_eol_products.py` → 增量同步到官网 WordPress EOL API（由 `sync-eol.yml` 触发）

## 新增数据集时的约定

### 1. 命名：`<数据集>.<语言>.md`，先保持扁平

文件名前缀即分组，两三个文件时不必建子目录。例如：

```
data/eol-products.zh.md
data/product-matrix.zh.md
```

满足下列任一条，再引入 `data/<数据集>/` 子目录：

- 单个数据集超过 3 个文件
- 两个数据集想用同一个文件名
- 某个数据集需要带附件（图片、CSV 等）

分目录时记得同步改动：`scripts/eol_data.py` 的 `DATA_DIR`、各工作流的路径过滤，
以及上游 `device-hw-docs` 里 `eol-sync-to-documents.yml` 的 `--out-dir`。

### 2. 路径过滤必须写到文件名，**不要用 `data/**`**

现有四个工作流都把触发路径写成精确通配：

```yaml
paths:
  - "data/eol-products.*.md"
```

新增数据集就照样**新增一行**，不要图省事改成 `data/**`。

原因：`sync-eol.yml` 会调用官网 API 写数据。一旦改成目录通配，任何一个
数据集的改动都会触发官网 EOL 同步，产生无谓的写入和噪音。

### 3. 读取要指名文件，不要扫目录

现有脚本都通过一个入口取文件，没有 `glob` / `iterdir`：

```python
def data_file(site: str) -> Path:
    return DATA_DIR / f"eol-products.{site}.md"
```

保持这个习惯，新文件才不会被别的脚本误当成 EOL 数据解析。

### 4. 需要从上游同步的数据，两边都要配

如果新数据集也由 `device-hw-docs` 维护并同步过来，除了本仓库的路径过滤，
还要在上游 `eol-sync-to-documents.yml` 里配好渲染和推送。

⚠️ 跨仓库同步对不齐是**静默失效**——校验通过、文件却永远不过来，不会报错。
配完请实际改一次数据、确认文件真的落地，别只看流水线变绿。
