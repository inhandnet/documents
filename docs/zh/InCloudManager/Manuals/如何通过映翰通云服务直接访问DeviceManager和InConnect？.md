# 如何通过映翰通云服务直接访问Device Manager 和 InConnect？

[映翰通云服务](https://portal.inhandcloud.cn/)（包含[小星云管家](https://star.inhandcloud.cn/)、[DeviceLive](https://device.inhandcloud.cn/)、白鹰能源管家、ISCada、[InLink](https://link.inhandcloud.cn/)）采用统一账号体系，用户可使用同一组账号密码自由切换各平台，无需重复登录。

此外，映翰通还提供独立的[Device Manager](https://iot.inhand.com.cn/)及[InConnect](https://ics.inhandiot.com/ )设备管理平台。通过简单配置，您可将现有映翰通云服务账号与这两个平台进行关联，实现：

• 一键快速登录

• 平台间无缝切换，免除重复输入账号密码的繁琐操作

详细的配置方式，请参考下文。

## 前置条件

- 已有映翰通云服务系统账号；
- 已有Device Manager或InConnect账号。

## 配置步骤

1. 登录到Device Manager或者InConnect平台；
2. 进入 **设置 >> 映翰通云服务**页面；
3. 开启 **允许通过映翰通云服务登入**。

![图1 Device Manager配置](./img/HrWb1n8lh9lss2Lc/1748332536404-afc350c3-ade9-4f6c-8fa5-e6a1b74381e7-667631.png)

![图2 InConnect配置](./img/HrWb1n8lh9lss2Lc/1762484663788-75ad1a5c-886c-43c1-9a6d-965c4e19e754-673013.png)

## 验证结果

### 方式一：通过映翰通云服务直接访问Device Manager或InConnect

**使用场景：** 当您已经登录到了映翰通云服务，并且需要访问Device Manager或InConnect时。

1. 登录到 [映翰通云服务](https://portal.inhandcloud.cn/)；
2. 进入 **控制台**；
3. 点击 **访问** Device Manager或InConnect。

### 方式二：在Device Manager或InConnect登录页面使用映翰通云服务账号登录

**使用场景：** 当您期望这几个平台使用同一套账号密码管理时，可使用这种方式进行登录。

1. 进入Device Manager或InConnect的登录页面；
2. 点击 **使用映翰通云服务登录**；
3. 输入您在映翰通云服务的登录账号及密码，点击 **登录** 即可。

![1762485780938-18e829c0-5767-4d4e-a190-b294350d5b47.png](./img/HrWb1n8lh9lss2Lc/1762485780938-18e829c0-5767-4d4e-a190-b294350d5b47-839282.png)

## 常见问题

### 在映翰通云服务访问Device Manager或InConnect失败

请检查：

- 您在映翰通云服务的邮箱账号是否在Device Manager或InConnect注册过。如未注册，请先到Device Manager或InConnect注册。
- Device Manager或InConnect 平台是否已开启 “**允许通过映翰通云服务登入**”。

![1762486544690-96a074de-8d60-463d-80a0-8ae2e177b45e.png](./img/HrWb1n8lh9lss2Lc/1762486544690-96a074de-8d60-463d-80a0-8ae2e177b45e-862855.png)

### 管理员已经开启“**允许通过映翰通云服务登入**”，我的账号能直接通过映翰通云服务登录Device Manager或InConnect吗？

不可以。开启“**允许通过映翰通云服务登入**”属于个人账号维度的设置，需要每个账号单独配置。

### Device Manager或InConnect的设备数据会同步到映翰通云服务吗？

不会。Device Manager、InConnect与映翰通云服务的设备数据是互相隔离的。

### **映翰通云服务的用户账号会同步到其他两个平台吗？**

Device Manager、InConnect与映翰通云服务的用户账号是互相隔离的。

当您在映翰通云服务创建了一个账号后，这个账号不会同步在Device Manager或者InConnect平台创建。如果您需要这个账号能访问Device Manager或InConnect，你可以到Device Manager或InConnect的用户列表进行添加。

如果您需要经常同时在这几个平台上添加用户，您可以反馈给我们：<incloud@inhand.com.cn>。
