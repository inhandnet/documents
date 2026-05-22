# InHand Product Documentation

This repository contains the source files for InHand Networks product documentation, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed automatically.

## Website

- **English**: https://inhand.com
- **Chinese**: https://inhand.com.cn

## Repository Structure

```
├── docs/
│   ├── en/              # English documentation
│   └── zh/              # Chinese documentation
│
├── scripts/             # Build and validation scripts
├── overrides/           # MkDocs theme customizations
├── mkdocs.yml           # Chinese site configuration
└── mkdocs.en.yml        # English site configuration
```

## Product Directory Layout

Documentation is organized by product model:

```
docs/en/
├── CPE02/
│   ├── Manuals/
│   │   ├── CPE02_User_Manual.md
│   │   └── images/
│   ├── Specs/           # Product specifications
│   └── Solutions/       # Solution configurations
├── EC300/
│   └── Manuals/
│       └── ...
└── index.md
```

## Local Development

### Prerequisites

- Python 3.11+
- pip

### Setup

```bash
pip install -r requirements.txt
```

### Preview

```bash
# Chinese site
python -m mkdocs serve -f mkdocs.yml

# English site
python -m mkdocs serve -f mkdocs.en.yml
```

### Build

```bash
python -m mkdocs build -f mkdocs.yml -d site-zh --clean
python -m mkdocs build -f mkdocs.en.yml -d site-en --clean
```

## Contributing

We welcome contributions to improve our documentation. Please submit changes via Pull Requests.

- Create a feature branch from `master`
- Make your changes
- Submit a Pull Request for review

## License

Copyright (c) InHand Networks. All rights reserved.
