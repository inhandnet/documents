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
├── scripts/             # 构建和校验脚本
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

## 贡献

欢迎通过 Pull Request 提交文档改进建议。

- 从 `master` 创建功能分支
- 进行修改
- 提交 Pull Request 等待审核

## 许可证

Copyright (c) InHand Networks. 保留所有权利。
