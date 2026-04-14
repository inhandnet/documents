# MkDocs 构建错误排查指南

本文档汇总了 MkDocs 构建过程中常见的错误类型及解决方案。

---

## 一、编码错误 (NFKC Normalization)

### 错误表现
```
ValueError: netloc 'xxx' contains invalid characters under NFKC normalization
```

### 导致原因

#### 1. URL 中包含中文标点符号

```markdown
<!-- ❌ 错误：中文冒号 -->
<https://WAN1地址：1024>

<!-- ❌ 错误：中文引号 -->
"<https://example.com"

<!-- ❌ 错误：中文括号 -->
<https://example.com（备用）>

<!-- ✅ 正确 -->
`https://WAN1地址:1024`
```

**危险字符清单**：
| 中文符号 | 英文符号 | 说明 |
|---------|---------|------|
| `：` | `:` | 冒号 |
| `"` `"` | `"` | 引号 |
| `（）` | `()` | 括号 |
| `，` | `,` | 逗号 |
| `。` | `.` | 句号 |
| `、` | `,` | 顿号 |

#### 2. 自动链接 `<...>` 包裹了非 URL 内容

```markdown
<!-- ❌ 错误：URL 后紧跟中文 -->
<https://star.inhandcloud.cn，您将被自动重定向>

<!-- ❌ 错误：URL 包含多余字符 -->
<https://example.com(点击访问)>

<!-- ✅ 正确 -->
访问 https://star.inhandcloud.cn，您将被自动重定向

<!-- ✅ 或用标准 Markdown 链接 -->
[点击访问](https://example.com)
```

#### 3. Markdown 链接语法混乱

```markdown
<!-- ❌ 错误：嵌套混乱 -->
[<https://example.com/](https://example.com/>)

<!-- ❌ 错误：括号不匹配 -->
[链接](https://example.com/路径(带括号))

<!-- ✅ 正确 -->
[链接](https://example.com/%E8%B7%AF%E5%BE%84)
<!-- URL 中的特殊字符需要编码 -->
```

---

## 二、图片引用错误

### 错误表现
```
WARNING -  Doc file 'xxx.md' contains a link './img/xxx.png', 
but the target is not found among documentation files.
```

### 导致原因

#### 1. 图片文件未提交到 Git

```markdown
<!-- Markdown 引用了图片 -->
![描述](./img/xxx.png)

<!-- 但 img/ 目录不存在或未提交 -->
```

**解决方案**：
```bash
# 确保图片目录存在并提交
git add docs/xxx/img/
git commit -m "添加图片"
```

#### 2. 图片路径大小写不匹配（Linux 服务器上）

```markdown
<!-- ❌ 错误：Windows 不区分大小写，但 Linux 区分 -->
![图](./Img/xxx.png)  # 实际目录是 img/

<!-- ✅ 正确：路径完全匹配 -->
![图](./img/xxx.png)
```

---

## 三、锚点链接错误

### 错误表现
```
INFO -  Doc file 'xxx.md' contains a link '#章节标题', 
but there is no such anchor on this page.
```

### 导致原因

#### 1. 标题修改后锚点失效

```markdown
<!-- 链接指向的锚点 -->
[跳转到恢复出厂设置](#15-恢复出厂设置)

<!-- 但实际标题已改为 -->
## 1.6 恢复出厂设置
<!-- 锚点变成了 #16-恢复出厂设置 -->
```

#### 2. 跨文件锚点路径错误

```markdown
<!-- ❌ 错误：跨文件锚点格式不对 -->
[链接](./other.md#章节 1)

<!-- ✅ 正确：空格用连字符代替 -->
[链接](./other.md#章节-1)
```

---

## 四、快速检查命令

### 检查潜在问题
```bash
# 1. 检查中文冒号在 URL 中
grep -rn "https://.*：" docs/ --include="*.md"

# 2. 检查自动链接格式问题
grep -rn "<https://.*[^a-zA-Z0-9/:._-]>" docs/ --include="*.md"

# 3. 检查图片引用是否存在
find docs -name "*.md" -exec grep -l "\.\./img/" {} \;

# 4. 检查重复的锚点格式
grep -rn "](#[0-9]\+-" docs/ --include="*.md"
```

### 本地构建测试
```bash
# 本地构建看是否有错误
python -m mkdocs build -f mkdocs.yml

# 忽略图片警告，只看 ERROR
python -m mkdocs build -f mkdocs.yml 2>&1 | grep -E "(ERROR|Error)"
```

---

## 五、编写规范建议

### 1. URL 示例写法
```markdown
<!-- 作为示例展示，不需要点击 -->
访问 `https://WAN1地址:1024` 即可

<!-- 需要可点击的链接 -->
[访问控制台](https://star.inhandcloud.cn)

<!-- 长链接换行 -->
[查看文档](https://example.com/long/path/
?param=value&other=test)
```

### 2. 图片引用规范
```markdown
<!-- 放在同级 img 目录下 -->
![设备连接图](./img/connection.png)

<!-- 或使用绝对路径 -->
![logo](/assets/images/logo.png)
```

### 3. 标题锚点规范
```markdown
<!-- 使用英文或拼音作为锚点 ID -->
## 1.6 恢复出厂设置 {#factory-reset}

<!-- 引用时 -->
[参考恢复出厂设置](#factory-reset)
```

---

## 六、常见错误速查表

| 错误信息 | 原因 | 解决 |
|---------|------|------|
| `netloc 'xxx' contains invalid characters` | URL 含中文标点 | 用反引号包裹或改为标准链接 |
| `target 'img/xxx.png' is not found` | 图片未提交 | 添加图片到 Git |
| `no such anchor on this page` | 锚点不存在 | 检查标题是否修改 |
| `contains unrecognized character` | 文件编码问题 | 保存为 UTF-8 编码 |
| `expected end of text` | Markdown 语法错误 | 检查括号/引号匹配 |

---

## 七、CI 构建失败排查

### 步骤 1：查看具体错误
```bash
# GitHub Actions 日志中搜索 ERROR
grep -E "(ERROR|Error|Traceback)" build.log
```

### 步骤 2：本地复现
```bash
# 在本地运行相同命令
python -m mkdocs build --clean
```

### 步骤 3：检查最近修改的文件
```bash
# 查看最近修改的 Markdown
git diff HEAD~5 --name-only | grep "\.md$"
```
