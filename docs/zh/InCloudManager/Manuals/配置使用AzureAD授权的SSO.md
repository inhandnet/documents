# 配置使用Azure AD 授权的 SSO

如果您使用 Azure Active Directory (Microsoft Entra ID，本文简称 Azure AD) 管理您的企业账号，可以在 小星云管家 中选择 Azure AD 作为授权服务器配置并开启单点登录（Single Sign-On, SSO）。同时，您还需要在 Azure AD 中进行 OpenID Connect (OIDC) 配置。本文提供了以Azure AD与小星云管家进行用户SSO的示例，帮助您理解企业 Identity Provider (IdP) 与 小星云管家之间进行连接授权 SSO 的端到端配置流程。

## 前置条件

- 已有映翰通云服务系统管理员账号；
- 已有一个Azure租户，并有一个管理员账号（已授予全局管理权限）。您需要使用管理员账号执行本示例中在Azure AD的操作。关于如何在Azure AD中创建用户和为用户授权，请参见[Azure AD文档](https://learn.microsoft.com/zh-cn/entra/fundamentals/)。

您在Azure AD中有一个企业员工用户（test_sso），你希望企业员工用户（test_sso）能通过登录Azure AD，直接SSO访问到映翰通云服务。

## 步骤一：在映翰通云服务获取回调地址

1. 使用系统管理员账号登录到[映翰通云服务](https://portal.inhandcloud.cn/)；
2. 在导航栏中选择 **系统设置 >> Azure AD**；
3. 点击 **添加**；
4. 复制弹窗中的 **重定向URI**。此地址将用于Azure AD中应用的配置。![1740130217534-bcc109d2-5294-44e4-8ede-93c43a8ee89c.png](./img/ix9aM8ZVsrnfNPLG/1740130217534-bcc109d2-5294-44e4-8ede-93c43a8ee89c-950206.png)

## 步骤二：在Azure中创建应用

1. 使用管理员账号登录[Azure 门户](https://portal.azure.com)；
2. 进入主页，并点击 **Microsoft Entra ID**；
3. 在左侧菜单栏，点击 **应用注册**；
4. 点击 **新注册**，并填写以下信息：
    1. 自定义的 **应用名称**，如：InCloud_Beta；
    2. 选择需要使用该应用的**租户类型**；
    3. 填写在映翰通云服务中复制的 **重定向URI**；
    4. 点击 **注册**，即完成新应用的创建。

![1740381731756-829261c1-87ce-44f3-bf54-13d509d7aea0.png](./img/ix9aM8ZVsrnfNPLG/1740381731756-829261c1-87ce-44f3-bf54-13d509d7aea0-931771.png)

## 步骤三：在映翰通云服务中配置SSO信息

1. 在映翰通云服务中配置Azure AD的ID信息：
    1. **应用程序（客户端）ID**：对应Azure AD中应用概述页面的应用程序（客户端）ID；
    2. **目录（租户）ID**：对应Azure AD中应用概述页面的目录（租户）ID。

![1740382491128-1cd706e1-1fdd-4174-88a1-987d5fa31866.png](./img/ix9aM8ZVsrnfNPLG/1740382491128-1cd706e1-1fdd-4174-88a1-987d5fa31866-049748.png)

1. 在Azure门户中，点击左侧菜单栏中的 **证书和密码**；
2. 在 **客户端密码**页面，点击 **新客户端密码**，填写说明和截止期限后，点击 **添加**；然后复制生成的 **值**；
3. 将 **值 **填写到映翰通云服务中的Azure AD信息中，并**提交**。

:::color3
**注意：**Azure AD中生成的客户端密码存在有效期，密码到期后，SSO功能将无法使用，请提前创建新的客户端密码进行替换。

:::

![1740382451283-92a24830-acef-41bf-b7ca-18d824881f4d.png](./img/ix9aM8ZVsrnfNPLG/1740382451283-92a24830-acef-41bf-b7ca-18d824881f4d-216166.png)

## 步骤四：在Azure AD中创建用户并授权应用

1. 在Azure门户的应用概述页面，点击 **转到“企业应用程序”**；![1740382823993-33d08758-d89a-4b1a-9b19-98f1fd7b3098.png](./img/ix9aM8ZVsrnfNPLG/1740382823993-33d08758-d89a-4b1a-9b19-98f1fd7b3098-260561.png)
2. 在左侧菜单栏中，点击 **用户和组** ；
3. 点击 **添加用户/组**，选择需要授权的用户/组，如：<test_sso@inhand.com>；![1740383180087-26c11db6-5ef9-4ea3-a3e8-24d79a479e40.png](./img/ix9aM8ZVsrnfNPLG/1740383180087-26c11db6-5ef9-4ea3-a3e8-24d79a479e40-136472.png)
4. 点击 **分配** ，以完成对用户的应用授权。

## 步骤五：在映翰通云服务中创建子用户

1. 进入映翰通云服务的 **用户管理** 页面；
2. 点击用户列表右上方的 **添加** ；
3. 在弹窗中填写在Azure门户中授权的账号并提交，如<test_sso@inhand.com>。

![1740383593176-36ee4356-f56e-4cdf-b939-9e793efcba6d.png](./img/ix9aM8ZVsrnfNPLG/1740383593176-36ee4356-f56e-4cdf-b939-9e793efcba6d-953927.png)

## 验证结果

1. 进入[映翰通云服务](https://portal.inhandcloud.cn/)登录页面，点击 **Azure 登录** ；![1740383721721-685f3bd5-c4be-40d3-9665-8d8b3652439e.png](./img/ix9aM8ZVsrnfNPLG/1740383721721-685f3bd5-c4be-40d3-9665-8d8b3652439e-681969.png)
2. 输入需要登录的邮箱，如：<test_sso@inhand.com>，点击 **登录** ；![1740383800205-3defb4a5-b5e3-4db9-84dc-e54d7e668dd4.png](./img/ix9aM8ZVsrnfNPLG/1740383800205-3defb4a5-b5e3-4db9-84dc-e54d7e668dd4-932105.png)
3. 选择与上一步输入的账户，如<test_sso@inhand.com>；如果没有，可以点击添加 使用另一个账户 ；![1740383994586-f6f42d64-0a1b-4807-9379-b825068515df.png](./img/ix9aM8ZVsrnfNPLG/1740383994586-f6f42d64-0a1b-4807-9379-b825068515df-449069.png)
4. 输入该账号在Azure门户中的密码，并 **登录**。![1740384460804-d0dbeb18-f493-4cf8-95b6-cd0d45608cc8.png](./img/ix9aM8ZVsrnfNPLG/1740384460804-d0dbeb18-f493-4cf8-95b6-cd0d45608cc8-124491.png)

## 常见问题

### 配置完成后，用户仍无法使用Azure账号登录

请确认以下信息：

- 映翰通云服务中配置的Azure AD信息正确；
- Azure的客户端密码在有效期内；
- Azure与映翰通云服务的账号一致；
- 登录的密码为Azure门户的密码。

### 使用一段时间后，无法使用Azure账号登录了

请确认以下信息：

- Azure的客户端密码在有效期内；
- 在Azure门户中，账号仍有此应用的权限。

### 配置了Azure AD登录后，能否使用账号密码进行登录？

配置了Azure AD后，仍可以使用您在平台配置的密码进行登录。
