# 用户手册文档上传 GitHub 操作指导文档

## 一、核心信息说明

### 1. 目标仓库地址

主仓库：https://github.com/inhandnet/documents

### 2. 语言目录划分

- 英文文档存放目录：/docs/en
- 中文文档存放目录：/docs/zh

### 3. 分支管理规则

- 禁止直接向 master 分支上传文件或提交修改；
- 团队成员需创建个人 / 功能分支用于文档上传与编辑；
- 文档完成后需通过合并请求（Pull Request）提交至 master 分支，经审核通过后合并。

    graph LR
        A["团队成员"] -->|"创建"| B["个人/团队分支"]
        B -->|"上传文档"| C["文档完成"]
        C -->|"提交"| D["合并请求（Pull Request）"]
        D -->|"审核"| E["审核人员"]
        E -->|"通过"| F["合并至 master 分支"]

## 二、目录结构规范

### 1. 核心原则

- 文件夹命名必须与官网产品名称保持一致，确保产品与文档的对应性；
- 目录层级最多支持三层，无需二级子类时仅保留两层目录，需细分二级子类时扩展为三层目录。

### 2. 层级划分细则

#### （1）第一层目录（产品大类）

以产品核心类别命名，示例如下：

- AI Edge Computers
- Edge Computers
- Routers
- （其他产品大类按官网最新分类补充）

#### （2）第二层目录（产品子类 / 产品系列）

根据产品是否需要二级子类细分，分为两种命名场景：

- 场景 1：带二级子类（需进一步区分产品类型）
  
  命名格式：产品细分类型，示例：
  - 父类（第一层）：Routers
  - 子类（第二层）：Industrial Routers（工业路由器）、Enterprise Routers（企业路由器）
  
- 场景 2：不带二级子类（无需细分，直接对应具体产品系列）
  
  命名格式：产品系列名称，示例：
  - 父类（第一层）：Edge Computers
  - 子类（第二层）：EC300（直接以产品系列命名，无额外细分）
  

#### （3）第三层目录（产品系列细分，可选）

仅当第二层目录为 “带二级子类” 时，根据需求补充第三层（以产品系列命名），示例：

- 第一层：Routers
- 第二层：Industrial Routers
- 第三层：IR615、IR302（具体产品系列名称）

### 3. 目录结构示例

#### 示例 1：带三级目录（需二级子类细分）

    docs/
    ├─ en/
    │  ├─ Routers/                  （第一层：产品大类）
    │  │  ├─ Industrial Routers/    （第二层：带二级子类）
    │  │  │  ├─ IR615/              （第三层：产品系列）
    │  │  │  │  └─ User_Manual.md   （英文用户手册）
    │  │  │  └─ IR302/
    │  │  │     └─ User_Manual.md
    ├─ zh/
    │  ├─ Routers/
    │  │  ├─ Industrial Routers/
    │  │  │  ├─ IR615/
    │  │  │  │  └─ 用户手册.md
    │  │  │  └─ IR302/
    │  │  │     └─ 用户手册.md
    

#### 示例 2：仅二级目录（无需二级子类细分）

    docs/
    ├─ en/
    │  ├─ Edge Computers/           （第一层：产品大类）
    │  │  ├─ EC300/                 （第二层：产品系，无三级目录）
    │  │  │  └─ User_Manual.md
    ├─ zh/
    │  ├─ Edge Computers/
    │  │  ├─ EC300/
    │  │  │  └─ 用户手册.md
    

## 三、文档上传与分支操作流程（页面操作）

### 1. 前提准备

- 已获取 GitHub 仓库操作权限（可创建分支、推送代码）；
- 文档已按规范命名（英文文档：建议以 Product_Series_User_Manual.md 命名，如 IR600_User_Manual.md；中文文档：建议以 产品系_用户手册.md 命名，如 IR600_用户手册.md）；
- 使用 Markdown（.md）格式，便于 GitHub 在线预览。

### 2. 分支创建与文档上传（网页端操作）

#### （1）创建分支

1. 访问主仓库地址 https://github.com/inhandnet/documents；
2. 点击分支选择框（默认显示 master），输入新分支名称（建议格式：docs-产品分类或产品系列或团队-，如 docs-Vehicles-teams），点击 “Create branch: 分支名” 完成创建。



#### （2）上传文档至目标目录

1. 在仓库页面切换至已创建的个人分支；
2. 导航至对应语言目录（
       docs/en
    或 
       docs/zh
   ），按目录结构找到目标产品目录（如 
       docs/en/Routers/Industrial Routers
   ）；
   - 若目标目录不存在（如新增产品系目录）：进入上级目录后，点击 “Add file” → “Create new file”，在文件名输入框中输入 “目录名 /”（末尾加斜杠，如 IR600/），即可创建目录；
   
3. 点击 “Add file” → “Upload files”，拖拽文档至上传区域或选择本地文件；
4. 下拉至 “Commit changes” 区域，填写提交说明（示例：“上传 IR600 英文用户手册”），点击 “Commit changes” 完成文档推送。

### 3. 合并请求（Pull Request）提交与审核

#### （1）提交合并请求

1. 文档上传完成后，在仓库页面点击 “Pull requests” 标签 → “New pull request”；
2. 左侧选择 base 分支为 master，右侧选择 compare 分支为已创建的个人分支；
3. 核对修改内容（确保目录、文档无误），填写合并请求标题（示例：“【文档合并】IR600 中英文用户手册上传”）和描述（简要说明文档内容、目录路径），点击 “Create pull request”。

#### （2）审核与合并

1. 相关审核人员收到通知后，将对文档的命名、目录路径、内容完整性进行审核；
2. 若审核通过，将直接合并至 master 分支；若需修改，将在合并请求中备注修改意见；
3. 提交人需根据修改意见在个人分支中完善文档，修改完成后重新提交审核，直至通过合并。

## 四、命令行操作（本地创建分支 → 提交 → 推送 → 开 PR → 审核/合并）

A. 纯 git（PR/审核/合并仍在网页上完成）

### 1. 拉取最新 master分支

    git checkout master
    git pull
    git checkout -b docs-Vehicles-teams

（新 git 也可以）

    git switch main
    git pull
    git switch -c docs-Vehicles-teams

### 2. 添加/修改文档文件

- 把文档放到仓库目录，例如：

- docs/zh/EnRouter/IR302/IR302快速手册.md

- 图片放 docs/zh/.../images/

### 3. 提交改动

    git add .
    git commit -m "docs: add IR302 quick manual (ZH)"

### 4 推送到远端

    git push -u origin docs-Vehicles-teams

### 5 去 GitHub 页面创建 PR

- 推送后 GitHub 通常会提示 “Compare & pull request”

- 或按“页面操作流程”的方式手动 New pull request

## 五、注意事项

1. 分支命名需清晰可辨，便于团队识别文档归属；
2. 文档上传前需核对目录路径，确保语言目录、产品层级无错误；
3. 禁止在个人分支中修改 master 分支已合并的其他文档，如需修改需单独创建分支并提交审核；
4. 合并请求提交后，需及时关注审核反馈，避免长时间未处理导致文档过时；
5. 若遇目录创建、分支操作等技术问题，可联系仓库管理员协助解决。
