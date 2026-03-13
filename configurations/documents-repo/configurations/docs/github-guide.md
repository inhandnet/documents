# GitHub 使用指南

本文档介绍如何使用 GitHub Desktop 客户端进行日常开发协作，包括安装、拉取代码、分支管理、提交与合并等操作。

## 1. 下载与安装 GitHub Desktop

1. 访问 [GitHub Desktop 官网](https://desktop.github.com/)，点击 **Download for Windows**
2. 运行下载的安装程序，按提示完成安装
3. 打开 GitHub Desktop，点击 **Sign in to GitHub.com**
4. 在浏览器中完成账号授权，返回客户端即可登录成功

> 如果没有 GitHub 账号，需要先在 [github.com](https://github.com/) 注册。

## 2. 拉取代码（Clone）

1. 打开 GitHub Desktop，点击菜单 **File → Clone repository...**
2. 在弹出窗口中选择 **URL** 标签页
3. 输入仓库地址，例如：
   ```
   https://github.com/inhandnet/config-templates.git
   ```
4. 选择本地存储路径（如 `F:\github\config-templates`）
5. 点击 **Clone**，等待下载完成

## 3. 切换与创建分支

### 切换到已有分支

1. 点击顶部工具栏的 **Current branch** 按钮
2. 在分支列表中选择目标分支（如 `main` 或 `draft`）

### 创建新分支

1. 点击 **Current branch** → **New branch**
2. 输入新分支名称（建议使用英文，如 `feature/add-er805-config`）
3. 选择基于哪个分支创建（通常选择 `main`）
4. 点击 **Create branch**

> **分支命名建议**：`feature/功能描述`、`fix/修复描述`、`docs/文档描述`

## 4. 修改文件

在本地文件管理器中，按照仓库的目录结构添加或修改文件。例如：

```
zh/ER805/案例名称/案例手册.md
zh/ER805/案例名称/配置手册.md
zh/ER805/案例名称/config/config.json
```

修改完成后，回到 GitHub Desktop，左侧面板会自动显示所有变更的文件。

## 5. 提交代码（Commit）

1. 在 GitHub Desktop 左侧面板，勾选需要提交的文件
2. 在左下角的 **Summary** 输入框填写提交说明，例如：
   ```
   添加 ER805 XX案例配置模板
   ```
3. 可选在 **Description** 中补充详细说明
4. 点击 **Commit to [分支名]** 按钮

> **提交说明规范**：简要描述本次修改的内容和目的，如"添加"、"修改"、"修复"等开头。

## 6. 推送到远程（Push）

提交完成后，点击顶部工具栏的 **Push origin** 按钮，将本地提交推送到 GitHub 远程仓库。

如果是新创建的分支第一次推送，按钮会显示为 **Publish branch**。

## 7. 创建合并请求（Pull Request）

推送完成后，需要创建 Pull Request（简称 PR）将分支合并到 `main`。

### 方式一：通过 GitHub Desktop

1. 推送后，GitHub Desktop 会提示 **Create Pull Request**
2. 点击后会跳转到浏览器的 GitHub 页面

### 方式二：通过 GitHub 网页

1. 打开仓库页面 https://github.com/inhandnet/config-templates
2. 点击页面顶部的 **Pull requests** 标签
3. 点击 **New pull request**
4. 设置 **base** 为 `main`，**compare** 为你的分支
5. 填写 PR 标题和描述，说明本次变更内容
6. 点击 **Create pull request**

## 8. 代码审查与合并（Merge）

1. PR 创建后，通知相关人员进行审查
2. 审查人在 PR 页面查看变更内容，可以添加评论或提出修改建议
3. 如有修改意见，在本地修改后重新提交并推送，PR 会自动更新
4. 审查通过后，由审查人或管理员点击 **Merge pull request** 完成合并
5. 合并完成后，可以删除已合并的分支

## 9. 同步最新代码（Pull / Fetch）

在开始新的工作之前，建议先同步远程仓库的最新代码：

1. 切换到 `main` 分支
2. 点击顶部工具栏的 **Fetch origin** 获取远程更新
3. 如果有更新，点击 **Pull origin** 拉取到本地

## 常见问题

### 推送失败提示冲突

说明远程分支有其他人的新提交。先点击 **Pull origin** 拉取最新代码，解决冲突后再推送。

### 忘记切换分支就开始修改了

1. 不要提交
2. 点击 **Current branch** → **New branch**，创建新分支
3. GitHub Desktop 会将当前未提交的修改带到新分支上

### 如何撤销未提交的修改

在 GitHub Desktop 左侧面板，右键点击文件，选择 **Discard changes** 即可恢复到上次提交的状态。
