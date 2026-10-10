# EC系列Linux软件用户手册V1.0

**边缘计算机EC系列**

**Linux软件用户手册**

**（适用于Debian11 V1.1.0及以上版本）**

Version 1.0，2023年12月

[www.inhand.com.cn](http://www.inhand.com.cn)

![1749108342106-9b4b640e-2c60-4156-9466-f7a02456011d.png](./img/R2_F4K-zBA-w0XXw/1749108342106-9b4b640e-2c60-4156-9466-f7a02456011d-083897.png)

本手册中描述的软件是根据许可协议提供的，只能按照该协议的条款使用。

**版权声明**

© 2023 映翰通网络 保留所有权利。

**商标**

InHand标志是映翰通网络的注册商标。

本手册中的所有其他商标或注册商标属于其各自的制造商。

**免责声明**

本公司保留对此手册更改的权利，产品后续相关变更时，恕不另行通知。对于任何因安装、使用不当而导致的直接、间接、有意或无意的损坏及隐患概不负责。

## 1.简介

本用户手册适用于以下列出的Inhand基于Arm架构的边缘计算机，涵盖了适用于所有受支持型号的说明。有关配置高级设置的详细说明在手册的第3章和第4章中有介绍。在参考这些章节之前，确认您的计算机型号的硬件规格支持所涵盖的功能和配置。

**Inhand Arm架构边缘计算机**

● EC312系列

**Inhand Arm架构边缘计算机Linux系统**

Inhand Arm架构边缘计算机Linux系统是为工业应用程序和用户优化的Linux发行版，由Inhand发布和维护，系统以Debian为基础集成了几个功能集，目的在于增强和加快用户应用程序开发，确保系统部署的可靠性。

## 2.快速引导

### 2.1.设备连接

您需要另一台计算机才能连接到基于Arm的计算机，登录到命令行界面方式为通过以太网连接至Arm计算机。

默认的用户名密码如下。

| Username | edge |
| :--- | :--- |
| Password | security@edge |

### 2.1.1.SSH连接

Inhand linux计算机支持基于以太网的SSH连接，使用下述默认IP地址可以连接到Inhand linux计算机。

| Port | Default IP |
| :--- | :--- |
| ETH1 | 192.168.3.100 |
| ETH2 | 192.168.4.100 |

<u>NOTE                                                        `</u>`

在运行ssh命令之前，请确保配置您的笔记本电脑/台式电脑以太网接口的IP地址，范围为ETH1 192.168.3.0/24，ETH2 192.168.4.0/24。

<u>                                                                 `</u>`

**通过ETH1使用SSH命令行连接到Inhand linux计算机。**

![1749108342297-db7dbd9e-2dda-4483-9c73-2ebb89c1962f.png](./img/R2_F4K-zBA-w0XXw/1749108342297-db7dbd9e-2dda-4483-9c73-2ebb89c1962f-572523.png)

**输入yes完成连接。**

![1749108342531-0fb3bcd0-4530-4783-80b6-40050af19657.png](./img/R2_F4K-zBA-w0XXw/1749108342531-0fb3bcd0-4530-4783-80b6-40050af19657-034169.png)

**输入默认密码security@edge进行登录。**

![1749108342730-27046909-fcb5-4f98-be93-97fe7c006917.png](./img/R2_F4K-zBA-w0XXw/1749108342730-27046909-fcb5-4f98-be93-97fe7c006917-968101.png)

**登录成功。**

![1749108342945-397cabf7-732b-4020-9a99-af147b951c47.png](./img/R2_F4K-zBA-w0XXw/1749108342945-397cabf7-732b-4020-9a99-af147b951c47-605012.png)

<u>NOTE                                                        `</u>`

更多SSH信息可以访问[https://wiki.debian.org/SSH](https://wiki.debian.org/SSH)

<u>                                                                 `</u>`

### 2.2.用户管理

### 2.2.1.切换至Root用户

您可以使用sudo -i（或sudo su）命令切换到root用户。出于安全原因，不要使用root用户操作所有命令。

**sudo -i输入默认密码security@edge进行root用户切换。**

![1749108343139-59a42fa4-7caa-4907-abea-ab1e4c6c48f8.png](./img/R2_F4K-zBA-w0XXw/1749108343139-59a42fa4-7caa-4907-abea-ab1e4c6c48f8-450868.png)

<u>NOTE                                                        `</u>`

当执行命令后Arm计算机返回permission denied消息时需要使用sudo来提升权限

您必须使用“sudo su–c”来运行该命令，而不是使用>、`<、>`>、`<<等，命令需要包含在’’内部

更多sudo信息可以访问[https://wiki.debian.org/sudo](https://wiki.debian.org/sudo)

<u>`                                                                 `</u>`

### 2.2.2.创建和删除用户

您可以使用useradd和userdel命令创建和删除用户，请参阅这些命令的Linux man page来使用。以下示例显示了如何在sudo组中创建一个test1用户，该用户的默认登录shell是bash，并且具有home/test1的主目录。

**要创建test1用户，请使用useradd命令。**

![1749108343769-42d2efb0-8e8b-4f7b-a36f-cd308436f314.png](./img/R2_F4K-zBA-w0XXw/1749108343769-42d2efb0-8e8b-4f7b-a36f-cd308436f314-237761.png)

**要更改test1的密码，请使用passwd命令输入并确认密码。**

![1749108344001-b515f72b-11bc-4a7f-905a-0a70985d5621.png](./img/R2_F4K-zBA-w0XXw/1749108344001-b515f72b-11bc-4a7f-905a-0a70985d5621-005658.png)

**要删除用户test1，请使用userdel命令。**

![1749108344215-f5e78632-5a48-4cbb-a8ee-e60a125c9afd.png](./img/R2_F4K-zBA-w0XXw/1749108344215-f5e78632-5a48-4cbb-a8ee-e60a125c9afd-402895.png)

### 2.2.3.禁用默认用户

**使用passwd -l命令锁定默认用户，以便edge用户无法登录。**

![1749108344407-6406796f-0865-41d8-bdb8-ced49f22f153.png](./img/R2_F4K-zBA-w0XXw/1749108344407-6406796f-0865-41d8-bdb8-ced49f22f153-517704.png)

**使用passwd -u命令解锁默认用户，以便edge用户可以登录。**

![1749108344611-f6ae32cc-8cb4-4717-9fb8-486676da6c22.png](./img/R2_F4K-zBA-w0XXw/1749108344611-f6ae32cc-8cb4-4717-9fb8-486676da6c22-648631.png)

<u>NOTE                                                        `</u>`

在禁用默认用户前请创建其他用户并保证其他用户可以SSH访问Arm计算机  

<u>                                                                 `</u>`

### 2.3.网络设置

### 2.3.1.以太网设置

第一次登录后，您可以配置基于Arm的计算机网络设置以适应您的应用程序。

<u>NOTE                                                        `</u>`

在更新网络配置后，以太网IP地址变化将引起SSH连接中断，需要重新创建SSH连接

<u>                                                                 `</u>`

**以太网配置文件路径。**

![1749108344841-10dd2cea-d562-4f5e-a8cc-13bd0bcb560b.png](./img/R2_F4K-zBA-w0XXw/1749108344841-10dd2cea-d562-4f5e-a8cc-13bd0bcb560b-838998.png)

**以太网ETH1和ETH2配置文件。**

![1749108345094-b46f9c0c-09be-440d-b706-73e6b7ebd54a.png](./img/R2_F4K-zBA-w0XXw/1749108345094-b46f9c0c-09be-440d-b706-73e6b7ebd54a-126879.png)

**配置以太网ETH1为静态IP**

要为基于Arm的计算机设置静态IP地址，请使用iface命令修改以太网接口的网关地址、IP地址、网络地址、网络掩码和广播参数。

![1749108345339-0c3eed04-7051-437d-b756-07eafe53e9db.png](./img/R2_F4K-zBA-w0XXw/1749108345339-0c3eed04-7051-437d-b756-07eafe53e9db-382113.png)

![1749108345551-de5c832b-1669-4838-9c38-4e5ea5628904.png](./img/R2_F4K-zBA-w0XXw/1749108345551-de5c832b-1669-4838-9c38-4e5ea5628904-559276.png)

**配置以太网ETH1为动态IP地址**

要配置一个或两个以太网端口以动态请求IP地址，请使用dhcp选项代替iface命令中的static，如下所示。

| Default Setting for ETH1 | Dynamic Setting using DHCP |
| :--- | :--- |
| auto eth1`<br/>`iface eth1 inet static`<br/>`    address 192.168.3.100/24 | auto eth1`<br/>`iface eth1 inet dhcp |

![1749108345724-a2433995-e804-49ee-b44f-25f3c909640d.png](./img/R2_F4K-zBA-w0XXw/1749108345724-a2433995-e804-49ee-b44f-25f3c909640d-147320.png)

**使以太网配置生效**

更新以太网配置文件后，使用ifdown和ifup命令使配置生效。

![1749108345935-3109cbdb-0c4b-4ddf-8820-65481846759a.png](./img/R2_F4K-zBA-w0XXw/1749108345935-3109cbdb-0c4b-4ddf-8820-65481846759a-341909.png)

<u>NOTE                                                        `</u>`

更多vim使用可以参考[https://manpages.org/vim](https://manpages.org/vim)

更多以太网配置可以参考[https://www.baeldung.com/linux/network-interface-configure](https://www.baeldung.com/linux/network-interface-configure)

<u>                                                                 `</u>`

### 2.4.系统管理

### 2.4.1.系统版本

使用ecversion命令检查基于Arm的计算机的系统映像版本。

**要检查基于Arm的计算机的固件版本，请输入ecversion**

![1749108346126-91fbdf4f-f497-4a4c-833d-6f3e9f9a7e5f.png](./img/R2_F4K-zBA-w0XXw/1749108346126-91fbdf4f-f497-4a4c-833d-6f3e9f9a7e5f-005310.png)

**添加–a选项可以输出完整的版本信息**

![1749108346772-089c21c3-fcba-4e4f-ba9b-d9bccc95e1c9.png](./img/R2_F4K-zBA-w0XXw/1749108346772-089c21c3-fcba-4e4f-ba9b-d9bccc95e1c9-364788.png)

### 2.4.2.调整时间

基于Arm的计算机有两种时间设置。一个是系统时间，另一个是RTC（Real time clock）基于Arm的计算机硬件保持的时间。使用date命令查询当前系统时间或设置新的系统时间。使用hwclock命令查询当前RTC时间或者设置新的RTC时间。

使用date MMDDhhmmYYYY命令设置系统时间：

| MM | 月 |
| :--- | :--- |
| DD | 日期 |
| hh | 小时 |
| mm | 分钟 |
| YYYY | 年 |

**获取系统时间**

![1749108347125-4389d15b-1881-4d74-9c39-0100b2452ff8.png](./img/R2_F4K-zBA-w0XXw/1749108347125-4389d15b-1881-4d74-9c39-0100b2452ff8-426651.png)

**设置系统时间**

![1749108347281-c0a33485-dd94-40f7-853d-aa73a5f4567a.png](./img/R2_F4K-zBA-w0XXw/1749108347281-c0a33485-dd94-40f7-853d-aa73a5f4567a-766660.png)

**获取RTC时间**

![1749108347453-a2fade52-912c-4b25-9039-4f960c07f962.png](./img/R2_F4K-zBA-w0XXw/1749108347453-a2fade52-912c-4b25-9039-4f960c07f962-838542.png)

**将系统时间写入RTC**

![1749108347631-facb2df0-e254-4600-a292-626710b90bfa.png](./img/R2_F4K-zBA-w0XXw/1749108347631-facb2df0-e254-4600-a292-626710b90bfa-136023.png)

<u>NOTE                                                        `</u>`

更多日期和时间信息可以参考

[https://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html](https://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html)

[https://wiki.debian.org/DateTime](https://wiki.debian.org/DateTime)

<u>                                                                 `</u>`

### 2.4.3.调整时区

有两种方法可以配置Arm的计算机时区。一种是使用TZ变量，另一种是使用/etc/localtime文件。

**使用TZ变量**

TZ环境变量的格式如下所示：

TZ=`<值>`HH[：MM[：SS]][夏[HH[：MM[：SS]][，开始日期[/starttime]，结束日期[/endtime]]

以下是北美东部时区的一些可能设置：

(1)TZ=EST5EDT

(2)TZ=EST0EDT

(3)TZ=EST0

在第一种情况下，参考时间是GMT，存储的时间值在全球范围内都是正确的。一个简单的更改TZ变量可以在任何时区正确打印本地时间。

在第二种情况下，参考时间是东部标准时间，执行的唯一转换是夏令时。因此，不需要每年调整两次夏令时的硬件时钟。

在第三种情况下，参考时间总是报告过的时间。如果机器上的硬件时钟自动调整为夏令时，或者您希望每年手动调整两次硬件时间，则可以使用此选项。

![1749108347784-d2f82dfc-4a16-4d37-85f2-8cc56afb1db3.png](./img/R2_F4K-zBA-w0XXw/1749108347784-d2f82dfc-4a16-4d37-85f2-8cc56afb1db3-658102.png)

您必须在/etc/rc.local文件中包含TZ设置。当您重新启动计算机时，时区设置将被激活。

下表列出了TZ环境变量的其他可能值：

| Hours From Greenwich Mean Time (GMT) | Value | Description |
| :--- | :--- | :--- |
| 0 | GMT | Greenwich Mean Time |
| +1 | ECT | European Central Time |
| +2 | EET | European Eastern Time |
| +2 | ART | |
| +3 | EAT | Saudi Arabia |
| +3.5 | MET | Iran |
| +4 | NET | |
| +5 | PLT | West Asia |
| +5.5 | IST | India |
| +6 | BST | Central Asia |
| +7 | VST | Bangkok |
| +8 | CTT | China |
| +9 | JST | Japan |
| +9.5 | ACT | Central Australia |
| +10 | AET | Eastern Australia |
| +11 | SST | Central Pacific |
| +12 | NST | New Zealand |
| -11 | MIT | Samoa |
| -10 | HST | Hawaii |
| -9 | AST | Alaska |
| -8 | PST | Pacific Standard Time |
| -7 | PNT | Arizona |
| -7 | MST | Mountain Standard Time |
| -6 | CST | Central Standard Time |
| -5 | EST | Eastern Standard Time |
| -5 | IET | Indiana East |
| -4 | PRT | Atlantic Standard Time |
| -3.5 | CNT | Newfoundland |
| -3 | AGT | Eastern South America |
| -3 | BET | Eastern South America |
| -1 | CAT | Azores |

**使用/etc/localtime文件**

本地时区存储在/etc/localtime中，如果没有为TZ环境变量设置值，则由GNU Library for C（glibc）使用。此文件要么是/usr/share/zoneinfo/文件的副本，要么是指向该文件的符号链接。基于Arm的计算机不提供/usr/share/zoneinfo/文件。您应该找到一个合适的时区信息文件，并在基于Arm的计算机中重写原始本地时间文件。

<u>NOTE                                                        `</u>`

通过localtime变更时区可以参考

[https://linuxize.com/post/how-to-set-or-change-timezone-in-linux/](https://linuxize.com/post/how-to-set-or-change-timezone-in-linux/)

<u>                                                                 `</u>`

### 2.5.确定磁盘空间

要确定可用磁盘空间的大小，请使用带有–h选项的df命令。系统将返回按文件系统划分的磁盘空间量。以下是一个示例：

![1749108347980-e7859bfa-acc8-41ab-b5cf-e9f071c4447b.png](./img/R2_F4K-zBA-w0XXw/1749108347980-e7859bfa-acc8-41ab-b5cf-e9f071c4447b-641867.png)

### 2.6.安装系统镜像

2.6.1.准备可引导的SD卡

(1)准备一张容量至少16GB的Micro SD卡和USB读卡器

(2)将SD卡插入Windows系统上相应的USB插槽

(3)从链接地址下载win32diskimager

[http://sourceforge.net/projects/win32diskimager/](http://sourceforge.net/projects/win32diskimager/)

(4)将附件linux-PE.img另存到本地Windows计算机

(5)确认Device设备是SD卡盘符，Image File选择linux-PE.img

![1749108348270-d0af0f92-f3ce-4eb9-944d-d3f31ea140e5.png](./img/R2_F4K-zBA-w0XXw/1749108348270-d0af0f92-f3ce-4eb9-944d-d3f31ea140e5-265945.png)

(6)点击Write按钮并选择Yes

![1749108348517-0d413834-3705-4433-9264-5ea25703be7d.png](./img/R2_F4K-zBA-w0XXw/1749108348517-0d413834-3705-4433-9264-5ea25703be7d-551940.png)

(7)等待制作完成

![1749108348697-620a19d1-0f01-47da-b21a-c7436ee83ca3.png](./img/R2_F4K-zBA-w0XXw/1749108348697-620a19d1-0f01-47da-b21a-c7436ee83ca3-901279.png)

(8)格式化SD卡，文件系统选择FAT32

![1749108348946-dd84b014-58b5-4c8a-b6b1-dab55d5c57bf.png](./img/R2_F4K-zBA-w0XXw/1749108348946-dd84b014-58b5-4c8a-b6b1-dab55d5c57bf-464168.png)

### 2.6.2.将系统镜像拷贝到SD卡

(1)在SD卡根目录创建flash-image文件夹

![1749108349173-a356d8db-1144-4b79-8e2e-cc5e99e0c678.png](./img/R2_F4K-zBA-w0XXw/1749108349173-a356d8db-1144-4b79-8e2e-cc5e99e0c678-435567.png)

(2)将系统镜像和镜像MD5文件拷贝到flash-image文件夹下

![1749108349354-70e8d81b-197a-4793-939d-6e92f999c665.png](./img/R2_F4K-zBA-w0XXw/1749108349354-70e8d81b-197a-4793-939d-6e92f999c665-853081.png)

(3)从链接地址下载Dos2Unix工具

[https://dos2unix.sourceforge.io/](https://dos2unix.sourceforge.io/)

(4)使用dos2nuix程序将MD5文件中Windows格式换行符转换为Unix格式

![1749108349555-d479d70b-6cba-44ed-93a9-04025b8779dc.png](./img/R2_F4K-zBA-w0XXw/1749108349555-d479d70b-6cba-44ed-93a9-04025b8779dc-138274.png)

![1749108349721-de6cfbf3-4642-418e-98f7-d2a03df6a13d.png](./img/R2_F4K-zBA-w0XXw/1749108349721-de6cfbf3-4642-418e-98f7-d2a03df6a13d-571410.png)

(5)移除SD卡

### 2.6.3.Arm计算机配置为镜像安装模式

(1)设备断电并移除上盖板4颗固定螺丝

![1749108350010-c434eade-9cda-4466-84b8-0e253749278e.png](./img/R2_F4K-zBA-w0XXw/1749108350010-c434eade-9cda-4466-84b8-0e253749278e-596421.png)

(2)将带有系统镜像的可引导SD卡插入SD插槽

![1749108350383-6a4f608e-1c5e-44aa-88d1-a5d3062b593a.png](./img/R2_F4K-zBA-w0XXw/1749108350383-6a4f608e-1c5e-44aa-88d1-a5d3062b593a-972919.png)

(3)短接J16端子

![1749108350776-0f5e6bc3-1bdf-411a-a4fa-3e4d7dcbeeeb.png](./img/R2_F4K-zBA-w0XXw/1749108350776-0f5e6bc3-1bdf-411a-a4fa-3e4d7dcbeeeb-445322.png)

(4)设备上电等待status灯闪烁

(5)通过ETH1连接设备使用telnet连接192.168.3.100，用户名root无密码

![1749108351058-f47e6b60-2945-4ee9-84c5-eea30d02f3f1.png](./img/R2_F4K-zBA-w0XXw/1749108351058-f47e6b60-2945-4ee9-84c5-eea30d02f3f1-819047.png)

![1749108351223-322d2aa7-e024-40ff-bcba-def8a199e4e3.png](./img/R2_F4K-zBA-w0XXw/1749108351223-322d2aa7-e024-40ff-bcba-def8a199e4e3-852800.png)

(6)使用flash命令安装系统

![1749108351444-501f6238-bd89-4b4c-906a-5082373c7f48.png](./img/R2_F4K-zBA-w0XXw/1749108351444-501f6238-bd89-4b4c-906a-5082373c7f48-992725.png)

(7)输入显示出来可用于安装的系统名称

![1749108351620-ad26ce58-94c8-4cde-a243-a68f74f72bb5.png](./img/R2_F4K-zBA-w0XXw/1749108351620-ad26ce58-94c8-4cde-a243-a68f74f72bb5-320019.png)

(8)等待flash complete

![1749108351853-c557d063-7ccc-4cfd-9cce-6950e0cb08bb.png](./img/R2_F4K-zBA-w0XXw/1749108351853-c557d063-7ccc-4cfd-9cce-6950e0cb08bb-784383.png)

(9)断开电源，移除J16短接端子和SD卡，复原上盖板并重新上电

<u>NOTE                                                        `</u>`

通过flash命令更新系统不会清除用户数据和设备厂商固化信息（比如设备型号 / SN号 / 以太网MAC地址等）

如果要清除用户数据和设备厂商固化信息请谨慎使用flash -f命令

<u>                                                                 `</u>`

## 3.外设配置

### 3.1.串口

Arm计算机的串行端口支持RS-232和RS-485，具有灵活的波特率设置。每路端口相互独立，请参考产品手册中硬件说明部分进行相应连接和使用。

stty命令用于查看和修改串行终端设置，详情如下。

**显示设置详情**

![1749108352088-45c26fd0-1500-4fde-8219-0e9905d69357.png](./img/R2_F4K-zBA-w0XXw/1749108352088-45c26fd0-1500-4fde-8219-0e9905d69357-292193.png)

**设置串口波特率115200**

![1749108352263-c4cb2fdc-014a-4082-8b39-21ccceee8514.png](./img/R2_F4K-zBA-w0XXw/1749108352263-c4cb2fdc-014a-4082-8b39-21ccceee8514-058967.png)

**校验设置结果**

![1749108352687-4835a476-5ac2-4237-a346-f80380ccd12c.png](./img/R2_F4K-zBA-w0XXw/1749108352687-4835a476-5ac2-4237-a346-f80380ccd12c-349817.png)

<u>NOTE                                                        `</u>`

更多stty使用方式可以参考

[http://www.gnu.org/software/coreutils/manual/coreutils.html](http://www.gnu.org/software/coreutils/manual/coreutils.html)

<u>                                                                 `</u>`

### 3.2.USB和SD卡

基于Arm的计算机提供了一个USB端口，用于存储扩展。可以使用mkdir命令创建储存器挂载点，使用mount命令挂载存储分区，使用mkfs命令对分区进行格式化。

**查看USB存储器**

![1749108352890-dc2417a6-232d-448d-9840-4594de7b7f34.png](./img/R2_F4K-zBA-w0XXw/1749108352890-dc2417a6-232d-448d-9840-4594de7b7f34-080528.png)

**创建USB存储器挂载点**

![1749108353054-3d473cd9-0890-4975-91fa-d983f5bf799d.png](./img/R2_F4K-zBA-w0XXw/1749108353054-3d473cd9-0890-4975-91fa-d983f5bf799d-726832.png)

**挂载USB存储器分区1到挂载点**

![1749108353258-8045aa42-a48c-4609-8ddc-f09e91f90c30.png](./img/R2_F4K-zBA-w0XXw/1749108353258-8045aa42-a48c-4609-8ddc-f09e91f90c30-685217.png)

**查看挂载情况**

![1749108353495-04c0d444-cf88-43c4-a04e-06011a8fea8b.png](./img/R2_F4K-zBA-w0XXw/1749108353495-04c0d444-cf88-43c4-a04e-06011a8fea8b-846644.png)

**查看SD卡存储器**

![1749108353886-e1c652d7-00be-456b-82f6-f3e64bfbbc15.png](./img/R2_F4K-zBA-w0XXw/1749108353886-e1c652d7-00be-456b-82f6-f3e64bfbbc15-336080.png)

**创建SD卡存储器挂载点**

![1749108354056-17a1d484-1464-4c93-8329-ea028c6564e8.png](./img/R2_F4K-zBA-w0XXw/1749108354056-17a1d484-1464-4c93-8329-ea028c6564e8-857430.png)

**挂载SD卡存储器分区1到挂载点**

![1749108354465-0895ea3c-0b49-4e9c-be94-7b5c5e8de382.png](./img/R2_F4K-zBA-w0XXw/1749108354465-0895ea3c-0b49-4e9c-be94-7b5c5e8de382-921015.png)

**查看挂载情况**

![1749108354665-d98b0559-8de8-4252-8a1a-c4324cdee6c1.png](./img/R2_F4K-zBA-w0XXw/1749108354665-d98b0559-8de8-4252-8a1a-c4324cdee6c1-403601.png)

**卸载并格式化USB分区1为ext4文件系统**

![1749108354898-7157b088-08fa-432d-a58e-b5ab9fd207a3.png](./img/R2_F4K-zBA-w0XXw/1749108354898-7157b088-08fa-432d-a58e-b5ab9fd207a3-044158.png)

<u>NOTE                                                        `</u>`

在格式化存储器前请确保存储器没有挂载到设备

更多mkdir命令使用方式请参考

[https://linuxize.com/post/how-to-create-directories-in-linux-with-the-mkdir-command/](https://linuxize.com/post/how-to-create-directories-in-linux-with-the-mkdir-command/)

更多mount命令使用方式请参考

[https://www.man7.org/linux/man-pages/man8/mount.8.html](https://www.man7.org/linux/man-pages/man8/mount.8.html)

更多mkfs命令使用方式请参考

[https://linuxsimply.com/mkfs-command-in-linux/](https://linuxsimply.com/mkfs-command-in-linux/)

<u>                                                                 `</u>`

### 3.3.CAN总线

Arm计算机上的CAN端口支持CAN 2.0A/B和CAN FD标准，最高数据波特率可以达到5Mbps。

### 3.3.1.配置Socket CAN

默认情况下，CAN端口是未进行初始化的down状态。如果需要配置CAN端口，请使用ip link命令。

**配置CAN端口**

![1749108355154-7cc4b5a7-5e91-408c-9cdf-b2719f83af3f.png](./img/R2_F4K-zBA-w0XXw/1749108355154-7cc4b5a7-5e91-408c-9cdf-b2719f83af3f-006116.png)

**使能CAN端口**

![1749108355360-e42da9c6-d0d3-49f0-b8a8-89a31b408f72.png](./img/R2_F4K-zBA-w0XXw/1749108355360-e42da9c6-d0d3-49f0-b8a8-89a31b408f72-648017.png)

以下代码是SocketCAN API的示例，它使用原始接口接收和发送数据包。

**发送示例**

```cpp
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <net/if.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <sys/ioctl.h> 
#include <linux/can.h> 
#include <linux/can/raw.h> 
int main(void) 
{ 
    int s; 
    int nbytes; 
    struct sockaddr_can addr; 
    struct can_frame frame; 
    struct ifreq ifr; 
    char *ifname = "can1"; 
    if((s = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) { 
        perror("Error while opening socket");
        return -1; 
    } 
    strcpy(ifr.ifr_name, ifname); 
    ioctl(s, SIOCGIFINDEX, &ifr); 
    addr.can_family = AF_CAN; 
    addr.can_ifindex = ifr.ifr_ifindex; 
    printf("%s at index %d\n", ifname, ifr.ifr_ifindex); 
    if(bind(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) { 
        perror("Error in socket bind"); 
        return -2; 
    } 
    frame.can_id = 0x123; 
    frame.can_dlc = 2; 
    frame.data[0] = 0x11; 
    frame.data[1] = 0x22; 
    nbytes = write(s, &frame, sizeof(struct can_frame)); 
    printf("Wrote %d bytes\n", nbytes); 
    return 0; 
}
```

**接收示例**

```cpp
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <net/if.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <sys/ioctl.h> 
#include <linux/can.h> 
#include <linux/can/raw.h> 
int main(void) 
{ 
    int i; 
    int s; 
    int nbytes; 
    struct sockaddr_can addr; 
    struct can_frame frame; 
    struct ifreq ifr; 
    char *ifname = "can0"; 
    if((s = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) { 
        perror("Error while opening socket"); 
        return -1; 
    } 
    strcpy(ifr.ifr_name, ifname); 
    ioctl(s, SIOCGIFINDEX, &ifr); 
    addr.can_family = AF_CAN; 
    addr.can_ifindex = ifr.ifr_ifindex; 
    printf("%s at index %d\n", ifname, ifr.ifr_ifindex); 
    if(bind(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) { 
        perror("Error in socket bind"); 
        return -2; 
    } 
    nbytes = read(s, &frame, sizeof(struct can_frame)); 
    if (nbytes < 0) { 
        perror("Error in can raw socket read"); 
        return 1; 
    } 
    if (nbytes < sizeof(struct can_frame)) { 
        fprintf(stderr, "read: incomplete CAN frame\n");
        return 1; 
    } 
    printf(" %5s %03x [%d] ", ifname, frame.can_id, frame.can_dlc); 
    for (i = 0; i < frame.can_dlc; i++) 
        printf(" %02x", frame.data[i]); 
    printf("\n"); 
    return 0; 
}
```

SocketCAN信息将写入路径/proc/sys/net/ipv4/conf/can*和/proc/sys/net/ipv4/neigh/can*

<u>NOTE                                                        `</u>`

在配置CAN接口前，请保证CAN接口处于down状态

更多CAN总线使用方式可以参考

[https://www.kernel.org/doc/html/latest/networking/can.html](https://www.kernel.org/doc/html/latest/networking/can.html)

<u>                                                                 `</u>`

### 3.4.模拟量输入检测

Arm计算机上的模拟量输入端口支持4-20mA电流信号检测，可以使用cat命令读取电流值。

![1749108355526-7b561ebf-56f5-40cb-aeec-4178e49680c3.png](./img/R2_F4K-zBA-w0XXw/1749108355526-7b561ebf-56f5-40cb-aeec-4178e49680c3-925796.png)

<u>NOTE                                                        `</u>`

模拟量输入检测获取的电流值单位是微安

<u>                                                                 `</u>`

### 3.5.数字量输入输出

Arm计算机上有多路数字量输入检测和数字量输出控制，可以用过cat命令查询数字量接口对应的GPIO信息。

**通过cat命令查询数字量输入输出**

![1749108355705-9fc7c94b-06e3-4405-9589-094e85ab35e0.png](./img/R2_F4K-zBA-w0XXw/1749108355705-9fc7c94b-06e3-4405-9589-094e85ab35e0-986469.png)

| 数字量输入输出通道 | 设备节点 |
| :--- | :--- |
| DI0 | /sys/class/gpio/gpio454 |
| DI1 | /sys/class/gpio/gpio455 |
| DI2 | /sys/class/gpio/gpio456 |
| DI3 | /sys/class/gpio/gpio457 |
| DO0 | /sys/class/gpio/gpio323 |
| DO1 | /sys/class/gpio/gpio453 |
| DO2 | /sys/class/gpio/gpio465 |
| DO3 | /sys/class/gpio/gpio461 |

**通过cat命令读取数字量输入状态**

![1749108355917-b79d9ba1-0f0f-449b-a0f3-9cbd571842bc.png](./img/R2_F4K-zBA-w0XXw/1749108355917-b79d9ba1-0f0f-449b-a0f3-9cbd571842bc-148908.png)

**通过echo命令控制数字量输出状态**

![1749108356123-c3798ba6-9278-4bf8-8742-52bbf7a56032.png](./img/R2_F4K-zBA-w0XXw/1749108356123-c3798ba6-9278-4bf8-8742-52bbf7a56032-364642.png)

<u>NOTE                                                        `</u>`

避免’sudo echo x >’ 时’Permission denied’，这是因为重定向符号 “>” 也是 bash 的命令。sudo 只是让 echo 命令具有了 root 权限，但是没有让 “>” 命令也具有root 权限，所以 bash 会认为这个命令没有写入信息的权限。此时需要使用sudo su -c ‘命令’来处理。

<u>                                                                 `</u>`

### 3.6.用户可编程按键

Arm计算机提供按键可编程按键，使用event事件方式提供给用户开发和使用，按键对应的event是/dev/input/event0。

**参考示例**

```cpp
#include <stdio.h>
#include <linux/input.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define DEV_PATH "/dev/input/event0"

int main()
{
    int keys_fd;
    char ret[2];
    struct input_event t;
    keys_fd = open(DEV_PATH, O_RDONLY);
    if(keys_fd <= 0)
    {
        printf("open /dev/input/event0 device error!\n");
        return -1;
    }
    while(1)
        {
            if(read(keys_fd, &t, sizeof(t)) == sizeof(t))
            {
                if(t.type == EV_KEY)
                    if(t.value==0 || t.value==1)
                    {
                        printf("key %d %s\n", t.code, (t.value) ? "Pressed" : "Released");
                        if(t.code == KEY_ESC)
                            break;
                    }
            }
        }
    close(keys_fd);
    return 0;
}
```

<u>NOTE                                                        `</u>`

更多event使用方式可以参考

[https://askubuntu.com/questions/826719/decoding-key-values-from-dev-input-eventx-in-c](https://askubuntu.com/questions/826719/decoding-key-values-from-dev-input-eventx-in-c)

<u>                                                                 `</u>`

### 3.7.LED

Arm计算机上有多个用户可编程LED，可以使用ls命令查看LED节点，使用echo命令控制LED。

![1749108356526-f8c44b70-29a4-4d17-90e9-ecdadc586cf1.png](./img/R2_F4K-zBA-w0XXw/1749108356526-f8c44b70-29a4-4d17-90e9-ecdadc586cf1-152333.png)

**点亮USER LED**

![1749108356754-3a37f539-6b1f-48fa-87f6-ccc4695f468e.png](./img/R2_F4K-zBA-w0XXw/1749108356754-3a37f539-6b1f-48fa-87f6-ccc4695f468e-369946.png)

**使USER LED闪烁**

![1749108356959-066fec20-db30-48fa-8a0c-8f79946b2db5.png](./img/R2_F4K-zBA-w0XXw/1749108356959-066fec20-db30-48fa-8a0c-8f79946b2db5-231406.png)

<u>NOTE                                                        `</u>`

更多LED使用方式可以参考

[https://www.kernel.org/doc/html/latest/leds/leds-class.html](https://www.kernel.org/doc/html/latest/leds/leds-class.html)

[https://raspberrypi.stackexchange.com/questions/697/how-do-i-control-the-system-leds-using-my-software](https://raspberrypi.stackexchange.com/questions/697/how-do-i-control-the-system-leds-using-my-software)

<u>                                                                 `</u>`

### 3.8.TPM

Arm计算机提供TPM2.0硬件支持，并预装了tpm2-tools工具，可以使用tpm2-tools工具测试和验证TPM2.0。

**生成随机数**

![1749108357197-1366ad59-c83d-4b38-8969-c0ad618bd710.png](./img/R2_F4K-zBA-w0XXw/1749108357197-1366ad59-c83d-4b38-8969-c0ad618bd710-249554.png)

<u>NOTE                                                        `</u>`

更多tpm2-tools使用方式可以参考

[https://tpm2-tools.readthedocs.io/en/latest/](https://tpm2-tools.readthedocs.io/en/latest/)

<u>                                                                 `</u>`

## 4.无线连接

本章中的说明涵盖了Inhand基于Arm的计算机支持的所有无线功能。在参考本章中的章节之前，请确保这些章节适用于Arm计算机平台的硬件规范。

### 4.1.蜂窝设置

基于Arm计算机的蜂窝控制中，需要控制蜂窝电源开关和双卡切换开关，这两个开关均是通过GPIO形式控制切换和使能的。

| | device node | value | state | default |
| --- | :--- | :--- | :--- | :--- |
| cellular power control | /sys/class/gpio/gpio401/value | 1 | enable | |
| | | 0 | disable | ✔ |
| SIM card switch | /sys/class/gpio/gpio405/value | 1 | SIM card 2 | |
| | | 0 | SIM card 1 | ✔ |

<u>NOTE                                                        `</u>`

使用蜂窝时需要确认当前SIM卡位于哪个卡槽或者期望使用哪一个卡槽的SIM卡拨号，在使能蜂窝电源前需要切换至所需的SIM卡否则会导致蜂窝模组检卡失败。

<u>                                                                 `</u>`

**切换SIM至SIM卡1**

![1749108357411-d1affdb7-ab38-4dbf-990c-a9af49d55174.png](./img/R2_F4K-zBA-w0XXw/1749108357411-d1affdb7-ab38-4dbf-990c-a9af49d55174-414615.png)

**使能蜂窝模组**

![1749108357607-49e217ac-1f34-4a10-b0ac-3bb808e7fd4b.png](./img/R2_F4K-zBA-w0XXw/1749108357607-49e217ac-1f34-4a10-b0ac-3bb808e7fd4b-505298.png)

**查询模组型号**

![1749108357842-c7b633cf-d17d-4c9c-9eff-f281246e69c5.png](./img/R2_F4K-zBA-w0XXw/1749108357842-c7b633cf-d17d-4c9c-9eff-f281246e69c5-043933.png)

可以通过envtools命令查询当前硬件设备使用的蜂窝模组，其中cell-*即表示模组型号（当前设备使用FQ53模组）

**使用PPPD拨号**

基于Arm的计算机支持PPPD拨号功能，对于不同种类的蜂窝模组PPPD拨号脚本不同，详细拨号脚本和模组对应关系如下。

| cellular module | PPPD chat script |
| :--- | :--- |
| LQA3 | quectel-ppp-ttyUSB2 |
| MOD1 | quectel-ppp-ttyUSB4 |
| FQ73 | quectel-ppp-ttyUSB5 |
| FQ53 | quectel-ppp-ttyUSB5 |
| FQ33 | quectel-ppp-ttyUSB3 |

![1749108358039-a971eaa6-df8c-4efd-b85a-dcd9d5517270.png](./img/R2_F4K-zBA-w0XXw/1749108358039-a971eaa6-df8c-4efd-b85a-dcd9d5517270-345936.png)

![1749108358197-b3db632b-c9a1-4db8-886b-6c92ac7dc73b.png](./img/R2_F4K-zBA-w0XXw/1749108358197-b3db632b-c9a1-4db8-886b-6c92ac7dc73b-620425.png)

![1749108358472-8391dcfb-2019-41db-acd6-05b3f37e7131.png](./img/R2_F4K-zBA-w0XXw/1749108358472-8391dcfb-2019-41db-acd6-05b3f37e7131-613701.png)

<u>NOTE                                                        `</u>`

设备默认配置的PPPD拨号脚本为最基础的拨号实现方式，并没有配置APN等信息，如果需要配置APN或使用更加丰富的模组功能，需要更改/etc/ppp/peers/quectel-ppp-ttyUSB*脚本

<u>                                                                 `</u>`

### 4.2.Wi-Fi设置

Arm计算机支持Wi-Fi配置，您可以使用wpa_supplicant工具配置和使用Wi-Fi。

**使能Wi-Fi**

![1749108358688-fe9c6eb6-34bb-4813-ad88-961095f8fc24.png](./img/R2_F4K-zBA-w0XXw/1749108358688-fe9c6eb6-34bb-4813-ad88-961095f8fc24-206776.png)

**添加wpa_supplicant.conf配置文件**

![1749108358889-d5cf7dac-6249-44a2-b3bb-8096110fa80f.png](./img/R2_F4K-zBA-w0XXw/1749108358889-d5cf7dac-6249-44a2-b3bb-8096110fa80f-824906.png)

![1749108359108-d09f3e02-87a2-4487-a05e-178aed7464c8.png](./img/R2_F4K-zBA-w0XXw/1749108359108-d09f3e02-87a2-4487-a05e-178aed7464c8-625149.png)

![1749108359280-999c4b34-2b93-4844-979a-09efaa0631d7.png](./img/R2_F4K-zBA-w0XXw/1749108359280-999c4b34-2b93-4844-979a-09efaa0631d7-690125.png)

**启动wpa_supplicant服务**

![1749108359450-3429144f-8773-495b-913a-40a74a8eb928.png](./img/R2_F4K-zBA-w0XXw/1749108359450-3429144f-8773-495b-913a-40a74a8eb928-094742.png)

**扫描热点**

![1749108359662-a0f73a23-796c-4086-9629-5b4704de2af4.png](./img/R2_F4K-zBA-w0XXw/1749108359662-a0f73a23-796c-4086-9629-5b4704de2af4-770854.png)

**查询扫描结果**

![1749108359838-c5843e54-0efe-4b43-aeb3-2ee948a004e3.png](./img/R2_F4K-zBA-w0XXw/1749108359838-c5843e54-0efe-4b43-aeb3-2ee948a004e3-228230.png)

**添加新的连接**

![1749108360089-cea41001-af54-4cf2-8415-d7db919f13e2.png](./img/R2_F4K-zBA-w0XXw/1749108360089-cea41001-af54-4cf2-8415-d7db919f13e2-297054.png)

**保存连接**

![1749108360252-ce64eb6c-692f-4699-8965-076d97b003b0.png](./img/R2_F4K-zBA-w0XXw/1749108360252-ce64eb6c-692f-4699-8965-076d97b003b0-847687.png)

**使能连接**![1749108360453-c4cbeb46-7499-492f-b931-d45e70e57a24.png](./img/R2_F4K-zBA-w0XXw/1749108360453-c4cbeb46-7499-492f-b931-d45e70e57a24-552361.png)

**使能DHCP**

![1749108360657-d822bf3c-2e62-4099-bb89-1c36926c21d7.png](./img/R2_F4K-zBA-w0XXw/1749108360657-d822bf3c-2e62-4099-bb89-1c36926c21d7-450193.png)

**断开连接**

![1749108360826-32c632e7-9d2d-4551-b48a-0a655992c547.png](./img/R2_F4K-zBA-w0XXw/1749108360826-32c632e7-9d2d-4551-b48a-0a655992c547-108227.png)

**列举保存过的连接**

![1749108361005-9bdd736e-27cf-4cc0-85e7-00295234e41c.png](./img/R2_F4K-zBA-w0XXw/1749108361005-9bdd736e-27cf-4cc0-85e7-00295234e41c-075743.png)

<u>NOTE                                                        `</u>`

更多wpa_supplicant使用方式请参考

[https://wiki.archlinux.org/title/Wpa_supplicant](https://wiki.archlinux.org/title/Wpa_supplicant)

<u>                                                                 `</u>`

## 5.安全

在基于Arm的计算机中，为了提高安全性，根帐户的SSH连接被禁用。sudo是一个程序旨在让系统管理员允许的用户以root用户执行程序。目的是尽可能少地给予特权，但仍然允许用户获得相应root权限。使用sudo比以root身份打开会话更好（更安全），原因有很多，包括：

(1)没有人需要知道root密码（sudo提示输入当前用户的密码）。额外的特权可以临时授予单个用户，然后在不需要密码更改。

(2)通过sudo只运行需要特殊权限的命令很容易；剩下的命令，作为一个没有特权的用户执行，减少了错误造成的损害。

(3)如示例所示，某些系统级命令不能直接用于用户edge

**输出如下：**

![1749108361176-411b9f78-f97f-4fca-b813-6ca682af70a9.png](./img/R2_F4K-zBA-w0XXw/1749108361176-411b9f78-f97f-4fca-b813-6ca682af70a9-328751.png)

## 6.启动、恢复和更新

### 6.1.恢复

Arm计算机提供两种系统重置机制，一种是基于update命令方式，一种是基于reset按键机制。

**基于update命令方式**

输入sudo update reset后根据提示输入yes，Arm计算机将自动重启并进行系统重置。

![1749108361384-36b747b7-fe17-46fe-9b50-b69f2edf8da3.png](./img/R2_F4K-zBA-w0XXw/1749108361384-36b747b7-fe17-46fe-9b50-b69f2edf8da3-185412.png)

**基于reset按键机制**

reset按键机制依赖于reset_monitor.service服务，此服务默认未加入到开机自启动列表，也未使能。

**添加至开机自启动列表请使用sudo systemctl enable reset_monitor**

![1749108361572-2767c9b3-90cd-4354-9880-63e3e00863c1.png](./img/R2_F4K-zBA-w0XXw/1749108361572-2767c9b3-90cd-4354-9880-63e3e00863c1-298744.png)

**从开机自启动列表删除请使用sudo systemctl disable reset_monitor**

![1749108362449-7065c4f6-535c-43d0-a1b4-72eb9114acb4.png](./img/R2_F4K-zBA-w0XXw/1749108362449-7065c4f6-535c-43d0-a1b4-72eb9114acb4-127557.png)

**启动reset_monitor服务请使用sudu systemctl start reset_monitor**

![1749108362626-3409f17c-5049-4c97-8727-4dcfedc036f5.png](./img/R2_F4K-zBA-w0XXw/1749108362626-3409f17c-5049-4c97-8727-4dcfedc036f5-599373.png)

**查询reset_monitor服务状态请使用sudu systemctl status reset_monitor**

![1749108362836-40584a2c-6c84-4291-8b42-61cc3063a55b.png](./img/R2_F4K-zBA-w0XXw/1749108362836-40584a2c-6c84-4291-8b42-61cc3063a55b-853257.png)

**使用reset按键重置系统**

在reset_monitor.service服务启动后，可以通过按reset按键方式实现系统重置，当持续按下超过10秒后，warn LED将亮起；按下超过20秒后warn LED将熄灭。在warn LED亮起阶段松开reset按键，Arm计算机将自动重启并进行系统重置。

<u>NOTE                                                        `</u>`

系统重置对Arm计算机而言是重要的功能，系统重置后Arm计算机将恢复到默认状态，此时用户数据和配置将全部丢失

在对Arm计算机进行系统重置前请确保关键数据进行有效备份，转移到可移动磁盘等外部存储介质中

系统重置后reset_monitor服务会从开机自启动列表删除，如果希望再次通过reset按键进行系统重置，请按照上述基于reset按键机制重新配置

### 6.2.更新

### 6.2.1.应用更新、安装和下载

Arm计算机基于发行版Linux系统（Debian 11）提供完善的应用更新策略，可以使用apt命令在线更新和安装应用，使用dpkg命令安装离线应用软件包。

**使用apt命令在线更新和安装应用**

第一步也是最重要的一步是同步Arm计算机中的包索引文件，此文件将从/etc/apt/sources.list中指定的源存储库进行同步更新。当执行同步时，与包相关的信息，包括版本和依赖项也将从存储库中下载。要执行同步，请确保您的网络环境可以连接到apt存储库，然后使用root权限运行apt-get update命令。

![1749108363102-29d1968d-f596-40be-86f5-b43dae4e352b.png](./img/R2_F4K-zBA-w0XXw/1749108363102-29d1968d-f596-40be-86f5-b43dae4e352b-458183.png)

接下来可以使用 sudo apt-get install packages_name 下载和安装新的应用，使用 sudo apt-get upgrade packages_name 更新已安装的应用，例如安装 cron 应用。

![1749108363333-99d38e58-6e6d-4e1c-acf5-7fba0345e165.png](./img/R2_F4K-zBA-w0XXw/1749108363333-99d38e58-6e6d-4e1c-acf5-7fba0345e165-224262.png)

**使用dpkg -l显示已经安装的应用列表**

![1749108363593-83329fbe-6d3b-434d-82b9-941562400ef8.png](./img/R2_F4K-zBA-w0XXw/1749108363593-83329fbe-6d3b-434d-82b9-941562400ef8-111235.png)

**使用dpkg -i `<packages-name.deb>`离线安装**

![1749108363760-cb69b2d8-e452-461e-bd98-75182d762480.png](./img/R2_F4K-zBA-w0XXw/1749108363760-cb69b2d8-e452-461e-bd98-75182d762480-918035.png)

<u>NOTE                                                        `</u>`

更多apt命令使用方式请参考

[https://linuxize.com/post/how-to-use-apt-command/](https://linuxize.com/post/how-to-use-apt-command/)

更多dpkg命令使用方式请参考

[https://linuxize.com/post/how-to-use-apt-command/](https://linuxize.com/post/how-to-use-apt-command/)

在使用dpkg安装离线软件时可能出现依赖问题

dpkg: error processing package bcron (--install):

 dependency problems - leaving unconfigured

此时需要根据提示安装依赖软件后尝试

<u>                                                                 `</u>`

### 6.2.2.Arm计算机版本更新

**准备用于版本更新的可移动USB存储器或SD卡**

(1)将可移动USB存储器或SD卡格式化为FAT32文件系统

![1749108363936-37e25271-dce6-4450-83ed-8fe3c562a25e.png](./img/R2_F4K-zBA-w0XXw/1749108363936-37e25271-dce6-4450-83ed-8fe3c562a25e-379572.png)

(2)在文件系统根目录创建ec300_img文件夹

![1749108364130-3b2522a4-a673-454e-a903-a3e0a27d7315.png](./img/R2_F4K-zBA-w0XXw/1749108364130-3b2522a4-a673-454e-a903-a3e0a27d7315-899882.png)

(3)将Arm计算机需要更新的镜像和镜像MD5文件拷贝至ec300_img目录

![1749108364314-55597275-6daa-40f2-9ce8-e4f7c684dc07.png](./img/R2_F4K-zBA-w0XXw/1749108364314-55597275-6daa-40f2-9ce8-e4f7c684dc07-637460.png)

(4)使用dos2nuix程序将MD5文件中Windows格式换行符转换为Unix格式

![1749108364493-c045df3e-d288-4615-90d2-6b1de96846de.png](./img/R2_F4K-zBA-w0XXw/1749108364493-c045df3e-d288-4615-90d2-6b1de96846de-916340.png)

(5)将可移动USB存储器或SD卡插入Arm计算机，并输入sudo update，根据提示输入yes

![1749108364707-b7368a7c-4eb2-43c4-8c96-4c1cb574e57a.png](./img/R2_F4K-zBA-w0XXw/1749108364707-b7368a7c-4eb2-43c4-8c96-4c1cb574e57a-512280.png)

(6)系统将自动重启并更新系统，在系统更新过程中warn LED进行闪烁提示，更新完成后Arm计算机将自动重启

(7)更新完成后，可以使用sudo ecversion命令检查当前Arm计算机版本

<u>NOTE                                                        `</u>`

当同时接入可移动USB存储器和SD卡时，Arm计算机会判断两个存储器中是否有可更新镜像，如果都存在可更新镜像时，默认启动可移动USB存储器中的镜像进行更新

<u>                                                                 `</u>`

## 7.编程说明

Arm的计算机支持应用本机编译和交叉编译。本机编译更简单明了，因为所有的编码和编译都可以直接在设备上完成。然而，Arm体系结构功能较弱，因此编译速度较慢。为了克服这一点，你可以使用工具链在Linux机器上编译代码，编译速度要快得多。

### 7.1.本机编译环境

按照以下步骤更新程序：

(1)确保网络连接可用

(2)使用apt-get update命令更新Debian包列表

![1749108364879-7134589b-450a-4d37-8c80-367b985e6d2b.png](./img/R2_F4K-zBA-w0XXw/1749108364879-7134589b-450a-4d37-8c80-367b985e6d2b-943903.png)

(3)安装本地编译工具链

![1749108365099-4957ef2e-c67d-41be-b96d-cb1dcb33976a.png](./img/R2_F4K-zBA-w0XXw/1749108365099-4957ef2e-c67d-41be-b96d-cb1dcb33976a-285727.png)

### 7.2.交叉编译环境

交叉编译是使用交叉编译工具链在x86平台计算机上编译出Arm计算机可以识别和执行程序的一种方法，交叉编译Arm计算机可执行程序前，需准备一台Ubuntu操作系统版本在18.04及以上的x86_64平台计算机。

**在本地计算机下载交叉编译工具链**

wget

[**https://developer.arm.com/-/media/Files/downloads/gnu-a/9.2-2019.12/binrel/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz**](https://developer.arm.com/-/media/Files/downloads/gnu-a/9.2-2019.12/binrel/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz)

![1749108365271-650addf1-dd93-4829-a57b-81a9f4630579.png](./img/R2_F4K-zBA-w0XXw/1749108365271-650addf1-dd93-4829-a57b-81a9f4630579-127630.png)

### 7.3.示例程序

使用vim在本机编译hello.c文件并使用gcc编译为hello可执行程序。

**示例代码**

![1749108365447-5f07dc63-8121-4eff-ae8b-26e7ed1eae28.png](./img/R2_F4K-zBA-w0XXw/1749108365447-5f07dc63-8121-4eff-ae8b-26e7ed1eae28-210922.png)

**使用gcc编译**

![1749108365614-f4a441d1-e258-4837-a053-df2b5f993532.png](./img/R2_F4K-zBA-w0XXw/1749108365614-f4a441d1-e258-4837-a053-df2b5f993532-420449.png)

**赋予hello可执行权限**

![1749108365811-97b12253-7cbd-4f18-ba6d-2bc370d68943.png](./img/R2_F4K-zBA-w0XXw/1749108365811-97b12253-7cbd-4f18-ba6d-2bc370d68943-035772.png)

**执行hello程序**

![1749108366004-34453494-0c9e-4dc2-885b-da2c07bd8562.png](./img/R2_F4K-zBA-w0XXw/1749108366004-34453494-0c9e-4dc2-885b-da2c07bd8562-540752.png)

<u>NOTE                                                        `</u>`

基于make和makefile的编译方式请参考

[https://linuxhandbook.com/using-make/](https://linuxhandbook.com/using-make/)

基于C语言的Linux开发请参考

[https://linuxconfig.org/c-development-on-linux-introduction-i](https://linuxconfig.org/c-development-on-linux-introduction-i)
