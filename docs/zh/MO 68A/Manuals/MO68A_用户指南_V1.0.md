# MO68A 用户指南

**版本 1.0 · 北京映翰通网络技术股份有限公司**

## 按任务跳转

| 关注点 | 建议阅读 |
| ------ | -------- |
| 最短上手路径（烧录、接线、首次登录） | [MO68A 快速入门指南](MO68A_快速入门指南_V1.0.md) |
| 连接器引脚、电气与机械规格 | [MO68A 硬件参考手册](MO68A_硬件参考手册_V1.0.md) |
| 向导完成后的主机名、时区、locale、apt | [§3 快速上手](#3-快速上手) |
| 软件安装与升级 | [§4 软件管理](#4-软件管理) |
| SD 分区与空间 | [§5 Micro SD 卡](#5-micro-sd-卡) |
| 串口排障与早期启动日志 | [§6 调试串口控制台](#6-调试串口控制台) |
| 显示器无信号或 DP 兼容性 | [§7 Mini DisplayPort](#7-mini-displayport)、[§19.5 显示器无信号](#195-显示器无信号) |
| 以太网与 SSH | [§8 网络与远程访问](#8-网络与远程访问) |
| 风扇必装与温控 | [§9 风扇与热管理](#9-风扇与热管理) |
| 传感器 / RTC EEPROM 等 I2C | [§10 I2C](#10-i2c)、[§11 RTC](#11-rtc) |
| USB 音频 / 存储 / HID | [§12 USB](#12-usb) |
| NVMe / PCIe 扩展 | [§13 PCIe](#13-pcie) |
| 树莓派 HAT、GPIO / SPI / UART | [§14 40-pin GPIO 扩展口](#14-40-pin-gpio-扩展口) |
| MIPI CSI 摄像头或 DSI 屏 | [§15 MIPI FPC 端口](#15-mipi-fpc-端口)、[§16](#16-mipi-dsi-显示屏)、[§17](#17-摄像头输入) |
| AI 推理 / MMA | [§18 AI 推理加速](#18-ai-推理加速) |
| 启动失败、网络、NVMe、显示 | [§19 故障排查](#19-故障排查) |

---

## 1. 简介

### 1.1 产品概述

MO68A 是一款基于 TDA4VE / AM68A SoC（TI J721S2 系列）的单板计算机，具有双 Cortex-A72 CPU、最多六个 Cortex-R5F 实时核以及 8 TOPS AI 加速器，兼容树莓派 40-pin HAT。

板卡运行 Armbian Linux（Debian 13 Trixie），适用于 AI 边缘推理、机器视觉、嵌入式 Linux 开发及工业计算等应用场景。

### 1.2 主要规格

| 参数     | 值                               |
|:------ |:------------------------------- |
| SoC    | TDA4VE / AM68A（TI J721S2）       |
| CPU    | 2× ARM Cortex-A72，最高 2.0 GHz    |
| AI 加速器 | 8 TOPS（MMA）                     |
| RAM    | 8 GB LPDDR4                     |
| 存储     | Micro SD（主）；PCIe NVMe（扩展）       |
| 操作系统   | Armbian（Debian 13 Trixie）       |
| 网络     | 千兆以太网                           |
| USB    | 4× USB 3.0 Type-A               |
| 显示     | Mini DisplayPort                |
| 摄像头/显示 | 2× MIPI 22-pin FPC（CSI-2 / DSI） |
| 扩展     | 40-pin GPIO 扩展口（兼容树莓派 HAT）      |
| 电源输入   | USB-C，5 V / 5 A（27 W）           |

### 1.3 文档范围

| 文档 | 涵盖内容 |
| --- | --- |
| [MO68A 快速入门指南](MO68A_快速入门指南_V1.0.md) | 最短路径：烧录 SD、接线、上电、首次登录与网络访问 |
| **MO68A 用户指南（本文档）** | 接口使用、外设配置、系统管理与故障排查 |
| [MO68A 硬件参考手册](MO68A_硬件参考手册_V1.0.md) | 电路与连接器电气定义、关键器件与机械参照 |

本文档默认已完成快速入门中的镜像烧录与首次初始化；若尚未完成，请先阅读 [MO68A 快速入门指南](MO68A_快速入门指南_V1.0.md) 中的 [最短上手路径](MO68A_快速入门指南_V1.0.md#最短上手路径)。

---

## 2. 配件与需求

| 配件                  | 规格                       | 备注           |
|:------------------- |:------------------------ |:------------ |
| USB-C 电源适配器         | 5 V / 5 A（最低 25 W）       | 必需           |
| Micro SD 卡          | ≥ 16 GB，Class 10 / UHS-I | 必需           |
| PWM 风扇（4-pin）       | 5 V                      | 热管理必需        |
| RJ45 网线             | —                        | 必需           |
| Mini DisplayPort 线缆 | —                        | 桌面使用         |
| DisplayPort 显示器     | 需支持 DisplayPort 输入       | 桌面使用         |
| USB 键盘和鼠标           | —                        | 桌面使用         |
| USB 转 UART 适配器      | 3.3 V 逻辑电平               | 串口调试控制台      |
| RTC 电池              | CR2032，2-pin JST-SH      | 可选；RTC 使用时需要 |

---

## 3. 快速上手

### 3.1 初始设置

按照 [MO68A 快速入门指南](MO68A_快速入门指南_V1.0.md) 完成以下步骤：

1. 将 Armbian 镜像烧录至 Micro SD 卡
2. 按顺序连接所有外设（风扇、显示器、网线、电源）
3. 完成首次登录初始化向导（语言区域、时区、用户账户）

绿色 LED（D1）常亮时，板卡已就绪。

### 3.2 验证系统状态

登录后，确认系统运行正常：

```bash
# 内核版本
uname -r

# 系统信息
cat /etc/os-release

# 存储布局
lsblk

# 内存
free -h

# 网络
ip addr show eth0
```

预期输出：根文件系统位于 `/dev/mmcblk1p2`，`eth0` 已分配 IP 地址。若安装了 NVMe SSD，`lsblk` 输出中还会出现 `/dev/nvme0n1`。

### 3.3 建议初始配置

**设置主机名：**

```bash
hostnamectl set-hostname mo68a
```

**设置时区**（替换为您当地的时区）：

```bash
timedatectl set-timezone Asia/Shanghai
timedatectl status
```

**更新软件包列表：**

```bash
apt update
```

**设置语言区域：**

```bash
dpkg-reconfigure locales
```

---

## 4. 软件管理

MO68A 运行 Armbian Linux（Debian 13 Trixie），使用 `apt` 进行软件包管理。以下命令需以 root 身份或通过 `sudo` 执行。

**更新软件包索引**（安装或升级前执行）：

```bash
apt update
```

**安装软件包：**

```bash
apt install <软件包名>
```

**删除软件包：**

```bash
# 保留配置文件
apt remove <软件包名>

# 同时删除配置文件
apt purge <软件包名>
```

**删除不再需要的依赖包：**

```bash
apt autoremove
```

**升级所有已安装的软件包：**

```bash
apt upgrade
```

**按关键字搜索软件包：**

```bash
apt search <关键字>
```

**查看软件包详情：**

```bash
apt show <软件包名>
```

---

## 5. Micro SD 卡

Micro SD 卡是主要启动介质和根文件系统存储，包含两个分区：

| 分区          | 大小     | 挂载点     | 用途             |
|:----------- |:------ |:------- |:-------------- |
| `mmcblk1p1` | 256 MB | `/boot` | 内核、设备树、overlay |
| `mmcblk1p2` | 剩余空间   | `/`     | 根文件系统          |

**查看分区布局：**

```bash
lsblk /dev/mmcblk1
```

示例输出：

```
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
mmcblk1     179:0    0 29.7G  0 disk
├─mmcblk1p1 179:1    0  256M  0 part /boot
└─mmcblk1p2 179:2    0 29.2G  0 part /var/log.hdd
                                     /
```

> `mmcblk1p2` 显示两个挂载点：`/`（根文件系统）和 `/var/log.hdd`。Armbian 在运行时将 `/var/log` 挂载为 tmpfs 以减少 SD 卡磨损；`/var/log.hdd` 是 SD 卡上的持久日志目录。

**查看可用空间：**

```bash
df -h /
```

> 首次启动时，Armbian 会自动将根分区扩展至 SD 卡全部容量，此操作会触发一次自动重启，耗时 1–2 分钟。

---

## 6. 调试串口控制台

板卡在连接器 J6（SH1.0 3-pin）上提供硬件串口控制台。该控制台输出完整启动日志，并提供独立于显示器和网络的登录终端——对于无头设置、内核调试和系统恢复至关重要。

### 6.1 硬件连接

将 3.3 V USB 转 UART 适配器连接至 J6：

| 引脚  | 信号  |
|:--- |:--- |
| 1   | RXD |
| 2   | GND |
| 3   | TXD |

> **警告：** 仅使用 **3.3 V 逻辑电平**适配器。5 V 适配器会损坏板卡。

在接通电源**之前**连接适配器，以从头捕获完整启动日志。

### 6.2 终端设置

参数：**115200 波特率，8N1，无流控**

```bash
# Linux
minicom -D /dev/ttyUSB0 -b 115200
```

Windows 系统请使用 PuTTY 或 Tera Term，选择正确的 COM 端口。

板卡上的控制台设备为 `/dev/ttyS2`（UART8）。该端口专用于调试控制台——请勿用于通用 UART 通信。

---

## 7. Mini DisplayPort

将 DisplayPort 显示器连接至 J9（Mini DisplayPort）。桌面环境加载完成后，板卡开始输出视频信号。

> 显示器必须具备原生 DisplayPort 输入。被动式 Mini DP 转 HDMI 适配器无法使用；请使用主动式适配器或支持 DP 原生输入的显示器。

**检查显示器检测状态：**

```bash
cat /sys/class/drm/card*/card*-DP-*/status
```

---

## 8. 网络与远程访问

### 8.1 有线以太网

板卡使用 NetworkManager。以太网接口为 `eth0`，默认使用 DHCP。

**检查连接状态：**

```bash
nmcli device status
```

**查看已分配 IP 地址：**

```bash
ip addr show eth0
```

**配置静态 IP 地址：**

```bash
nmcli con mod "Wired connection 1" \
  ipv4.method manual \
  ipv4.addresses 192.168.1.100/24 \
  ipv4.gateway 192.168.1.1 \
  ipv4.dns "8.8.8.8 8.8.4.4"
nmcli con up "Wired connection 1"
```

**恢复为 DHCP：**

```bash
nmcli con mod "Wired connection 1" ipv4.method auto
nmcli con up "Wired connection 1"
```

### 8.2 SSH 访问

SSH 服务默认已启用。从主机电脑连接：

```bash
ssh <用户名>@<板卡IP>
```

---

## 9. 风扇与热管理

### 9.1 风扇连接器

将 5 V 4-pin PWM 风扇连接至 J7（SH1.0，1.0 mm 间距）：

| 引脚  | 信号   | 方向      |
|:--- |:---- |:------- |
| 1   | 5 V  | 电源输出    |
| 2   | PWM  | 输出至风扇   |
| 3   | GND  | 地       |
| 4   | TACH | 来自风扇的输入 |

### 9.2 自动转速控制

风扇转速由内核热管理模块根据 SoC 温度自动控制。风扇始终保持最低 20% 转速，随温度升高而加速。

| 温度（main0-thermal） | 风扇转速       |
|:----------------- |:---------- |
| 60 °C 以下          | 20 %       |
| 60 – 70 °C        | 40 – 60 %  |
| 70 – 80 °C        | 60 – 80 %  |
| 80 °C 以上          | 80 – 100 % |

PWM 信号频率为 25 kHz。转速过渡由热管理模块每 1 秒轮询一次并逐步调整。

### 9.3 监控

**风扇转速（RPM）：**

```bash
cat /sys/class/hwmon/hwmon0/fan1_input
```

示例输出：

```
5742
```

RPM 从 TACH 信号测量：驱动程序对转速计输入的下降沿计数，每秒采样一次。精度取决于风扇的每转脉冲数规格（默认假设 2 脉冲/转，适用于大多数 4-pin PWM 风扇）。

**PWM 输出状态：**

```bash
cat /sys/kernel/debug/pwm
```

示例输出（空闲，20% 占空比）：

```
0: platform/3010000.pwm, 2 PWM devices
 pwm-0   ((null)   ): period: 0 ns duty: 0 ns polarity: normal
 pwm-1   (pwm-fan  ): requested enabled period: 40000 ns duty: 8000 ns polarity: normal usage_power
```

`duty` 值除以 `period` 即为当前占空比（8000 / 40000 = 20%）。

**当前冷却等级：**

```bash
cat /sys/class/thermal/cooling_device0/cur_state   # 0–4
cat /sys/class/thermal/cooling_device0/max_state   # 4
```

**所有热区温度：**

```bash
for z in /sys/class/thermal/thermal_zone*/; do
  printf '%-20s %d °C\n' "$(cat ${z}type)" "$(($(cat ${z}temp) / 1000))"
done
```

示例输出：

```
wkup0-thermal        50 °C
wkup1-thermal        50 °C
main0-thermal        50 °C
main1-thermal        51 °C
main2-thermal        51 °C
main3-thermal        51 °C
main4-thermal        50 °C
```

风扇由 **main0-thermal**（thermal_zone2）控制。持续监控：

```bash
watch -n 2 cat /sys/class/thermal/thermal_zone2/temp
```

---

## 10. I2C

SoC 提供五条 I2C 总线。使用 `i2cdetect -l` 列出：

```bash
i2cdetect -l
```

示例输出：

```
i2c-0   i2c             OMAP I2C adapter                        I2C adapter
i2c-1   i2c             OMAP I2C adapter                        I2C adapter
i2c-2   i2c             OMAP I2C adapter                        I2C adapter
i2c-3   i2c             OMAP I2C adapter                        I2C adapter
i2c-4   i2c             a000000.dp-bridge                       I2C adapter
```

| 设备节点         | SoC 总线    | 连接设备                      | 40-pin 引脚              |
|:------------ |:--------- |:------------------------- |:---------------------- |
| `/dev/i2c-0` | WKUP I2C0 | PMIC 和电源 IC               | 27、28（与 PMIC 共享——谨慎使用） |
| `/dev/i2c-1` | SOC I2C0  | 40-pin 扩展口（用户）            | 3、5                    |
| `/dev/i2c-2` | SOC I2C1  | 板卡 EEPROM（0x50）、RTC（0x51） | —                      |
| `/dev/i2c-3` | SOC I2C5  | MIPI FPC（内部）              | —                      |
| `/dev/i2c-4` | DP AUX    | Mini DisplayPort（AUX 通道）  | —                      |

> **注意：** `/dev/i2c-0`（引脚 27、28）与 PMIC 共享。该总线上的错误操作可能影响系统电源轨。仅在充分了解后果的情况下扫描或访问。

> **注意：** `/dev/i2c-4` 是 DisplayPort AUX 通道 I2C 适配器，由显示子系统内部使用。请勿扫描或访问此总线。

**扫描 I2C 总线：**

```bash
i2cdetect -y -r <总线号>
```

`-r` 标志使用读模式探测，比默认的 Quick Write 模式更安全。

示例——扫描 40-pin 用户 I2C 总线（SOC I2C0，引脚 3 和 5）：

```bash
i2cdetect -y -r 1
```

**读取寄存器：**

```bash
i2cget -y <总线号> <地址> <寄存器>
```

**转储设备所有寄存器：**

```bash
i2cdump -y <总线号> <地址>
```

**写入寄存器：**

```bash
i2cset -y <总线号> <地址> <寄存器> <值>
```

> **警告：** `i2cset` 直接写入设备寄存器，立即生效。向错误设备写入错误值——尤其是总线 0（PMIC）——可能导致系统不稳定或硬件损坏。仅对已知设备且掌握其寄存器映射时使用 `i2cset`。

---

## 11. RTC

### 11.1 电池安装

RTC（PCF85263ATL）通过 J8（SH1.0，2-pin，1.0 mm 间距）连接 CR2032 电池供电。在设置时间之前先安装电池，以便在掉电后保持时钟运行。

请使用带 2-pin JST-SH（1.0 mm 间距）接头的 CR2032 纽扣电池。请勿将裸纽扣电池直接塞入连接器。

### 11.2 时间配置

Armbian 使用 `systemd-timesyncd` 从 NTP 服务器同步系统时间。有网络时，系统时间会自动保持准确。systemd 还会定期将系统时间写入 RTC，并在关机时执行同步，因此 RTC 无需手动维护。

**确认 RTC 驱动已加载：**

```bash
ls /dev/rtc*
```

**查询当前时间和 RTC 状态：**

```bash
timedatectl status
```

输出中包含 `Local time`（系统时钟）和 `RTC time`（硬件时钟）两项。

如需验证 RTC 功能，可禁用 NTP、手动设置一个已知时间，重启后确认时间是否保持。

**禁用自动时间同步：**

```bash
timedatectl set-ntp false
```

**手动设置系统时间：**

```bash
timedatectl set-time "2026-05-08 12:00:00"
```

systemd 会自动将新时间写入 RTC。确认两个时钟均已更新：

```bash
timedatectl status
```

**重启后确认时间已保持：**

```bash
reboot
# 重启后：
timedatectl status
```

---

## 12. USB

四个 USB 3.0 Type-A 端口提供外设扩展能力。本节涵盖键盘鼠标输入、音频输出和便携存储等常见使用场景。

### 12.1 USB 3.0 Type-A 端口

通过 TUSB8041 Hub 提供四个 USB 3.0 端口：J2 两个，J3 两个。

**列出所有已连接的 USB 设备：**

```bash
lsusb
```

连接鼠标和键盘后的示例输出：

```
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0451:8142 Texas Instruments, Inc. TUSB8041 4-Port Hub
Bus 001 Device 003: ID 046d:c077 Logitech, Inc. Mouse
Bus 001 Device 004: ID 046d:c31d Logitech, Inc. Media Keyboard K200
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```

TUSB8041 Hub 始终出现在 Bus 001。连接到 Type-A 端口的设备作为附加条目显示在 Bus 001 或 Bus 002 下。

### 12.2 键盘和鼠标

USB 键盘和鼠标通过 USB HID 驱动即插即用。连接到任意 Type-A 端口（J2 或 J3）后设备立即可用，无需任何配置。

在桌面环境下，输入由图形环境处理。在无头模式下，USB 键盘可用于本地终端会话。

### 12.3 USB 音频

USB 音频设备（音箱、耳机、USB 声卡）即插即用。内核内置的 USB Audio Class（UAC）驱动无需配置——插入设备后立即作为 ALSA 声卡可用。

**Step 1 — 验证检测：**

```bash
lsusb
```

示例输出（USB 音箱作为新条目出现在 Bus 001 下）：

```
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0451:8142 Texas Instruments, Inc. TUSB8041 4-Port Hub
Bus 001 Device 003: ID 046d:c077 Logitech, Inc. Mouse
Bus 001 Device 004: ID 046d:c31d Logitech, Inc. Media Keyboard K200
Bus 001 Device 008: ID 4c4a:4155 Jieli Technology UACDemoV1.0
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```

确认 ALSA 已将其注册为声卡并查找卡号：

```bash
aplay -l
```

示例输出（同时安装了 I2S 音频 HAT 时，WM8960 占用 card 0，USB 音频分配为 card 1）：

```
card 0: WM8960Audio [WM8960-Audio], device 0: davinci-mcasp.0-wm8960-hifi wm8960-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: UACDemoV10 [UACDemoV1.0], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

> 卡号按探测顺序分配。I2S 设备先于 USB 探测，因此仅在没有 I2S 声卡时，USB 音频设备才会是 card 0。

直接查找 USB 音频的卡号：

```bash
aplay -l | grep -i "USB Audio"
```

示例输出：

```
card 1: UACDemoV10 [UACDemoV1.0], device 0: USB Audio [USB Audio]
```

输出中同时显示卡号和设备号（如 `card 1:`、`device 0:`）。在后续所有命令中使用这两个值（以下用 `<C>` 和 `<D>` 表示）。

**Step 2 — 调整音量：**

查询混音器控制和音量范围（各值因设备而异）：

```bash
amixer -c <C> contents
```

USB 音箱示例输出：

```
numid=2,iface=MIXER,name='PCM Playback Switch'
  ; type=BOOLEAN,access=rw------,values=1
  : values=on

numid=3,iface=MIXER,name='PCM Playback Volume'
  ; type=INTEGER,access=rw---R--,values=2,min=0,max=147,step=0
  : values=44,44
  | dBminmax-min=-28.37dB,max=-0.94dB
```

设置播放音量（控制名称和音量范围因设备而异，请参考 `amixer contents` 输出）：

```bash
amixer -c <C> cset name='PCM Playback Volume' 60,60
```

静音 / 取消静音：

```bash
# 静音
amixer -c <C> cset name='PCM Playback Switch' off

# 取消静音
amixer -c <C> cset name='PCM Playback Switch' on
```

**Step 3 — 测试播放：**

正弦波测试音（任何音箱均可清晰听到）：

```bash
speaker-test -c 2 -t sine -f 1000 -l 3 -D plughw:<C>,<D>
```

播放音频文件（`plughw` 自动处理采样率和声道转换）：

```bash
aplay -D plughw:<C>,<D> audio.wav
```

USB 音频无需修改设备树，即插即用。40-pin I2S 接口（参见第 14.5 节）是需要板载编解码器设计的替代方案。

### 12.4 USB 存储

USB 存储在桌面环境下自动挂载。无头模式下：

```bash
# 列出块设备
lsblk

# 挂载 USB 存储
mkdir -p /mnt/usb
mount /dev/sda1 /mnt/usb

# 拔出前安全卸载
umount /mnt/usb
```

---

## 13. PCIe

PCIe Gen3 FPC 连接器（J10）通过转接板提供高速扩展接口，可连接 NVMe SSD、计算加速器或自定义 PCIe 外设。

已验证兼容设备：**KIOXIA KEG60ZNS1T02**。

**连接并启动后，验证设备检测：**

```bash
lsblk
ls /dev/nvme*
```

**挂载现有分区：**

```bash
mkdir -p /mnt/nvme
mount /dev/nvme0n1p1 /mnt/nvme
```

**开机自动挂载**——添加至 `/etc/fstab`：

```
/dev/nvme0n1p1  /mnt/nvme  ext4  defaults  0  2
```

---

## 14. 40-pin GPIO 扩展口

40-pin 扩展口（J11）遵循树莓派 HAT 机械封装和引脚编号。完整信号分配和焊球编号请参见 **HRM 第 8.8 节**。

> IO 电压为 3.3 V。请勿将 5 V 信号连接到任何 GPIO 引脚。

### 14.1 引脚参考

| 功能（奇数引脚）                  | 引脚  |     | 引脚  | 功能（偶数引脚）            |
| -------------------------:|:---:|:---:|:---:|:------------------- |
| 3.3 V                     | 1   |     | 2   | 5.0 V               |
| I2C0_SDA（AE24）            | 3   |     | 4   | 5.0 V               |
| I2C0_SCL（AH25）            | 5   |     | 6   | GND                 |
| AUDIO_CLK / GPIO0_30（Y25） | 7   |     | 8   | UART5_TXD（W25）      |
| GND                       | 9   |     | 10  | UART5_RXD（AC24）     |
| WKUP_GPIO0_60（E27）†       | 11  |     | 12  | I2S_CLK（AB28）       |
| GPIO0_0（AG24）             | 13  |     | 14  | GND                 |
| WKUP_GPIO0_61（E28）†       | 15  |     | 16  | GPIO0_27（V26）       |
| 3.3 V                     | 17  |     | 18  | GPIO0_51（AE27）      |
| SPI5_MOSI（R27）            | 19  |     | 20  | GND                 |
| SPI5_MISO（AD27）           | 21  |     | 22  | WKUP_GPIO0_70（B26）† |
| SPI5_CLK（T27）             | 23  |     | 24  | SPI5_CS0（U28）       |
| GND                       | 25  |     | 26  | SPI5_CS1（W28）       |
| WKUP_I2C0_SDA（H27）†       | 27  |     | 28  | WKUP_I2C0_SCL（H24）† |
| GPIO0_18（AB27）            | 29  |     | 30  | GND                 |
| GPIO0_33（AA28）            | 31  |     | 32  | PWM / ECAP0（AB26）   |
| PWM5_B / GPIO0_32（U26）    | 33  |     | 34  | GND                 |
| I2S_FS（U27）               | 35  |     | 36  | GPIO0_10（AB24）      |
| GPIO0_9（Y28）              | 37  |     | 38  | I2S_DIN（AC28）       |
| GND                       | 39  |     | 40  | I2S_DOUT（Y26）       |

† WKUP 域 GPIO（gpiochip0）；其余均为主域 GPIO（gpiochip1）。

> I2C 命令和总线分配请参见第 10 节。40-pin 扩展口上的 I2C 引脚：引脚 3 和 5（SOC I2C0，`/dev/i2c-1`），引脚 27 和 28（WKUP I2C0，`/dev/i2c-0`）。

### 14.2 GPIO

40-pin 扩展口上提供多路 GPIO。板卡使用 Linux GPIO 字符设备接口，`gpiod` 软件包中的工具（`gpiodetect`、`gpioinfo`、`gpioget`、`gpioset`）已预装。

**列出 GPIO 芯片：**

```bash
gpiodetect
```

```
gpiochip0 [42110000.gpio] (89 lines)   # WKUP 域 GPIO（WKUP_GPIO0_X）
gpiochip1 [600000.gpio]   (66 lines)   # 主域 GPIO0（GPIO0_X）
gpiochip2 [0-0048]        (11 lines)   # 内部系统控制器（不供用户访问）
gpiochip3 [7inch-touchscreen-p] (2 lines)   # 树莓派 7 寸面板（连接面板时存在）
```

**列出 GPIO 芯片的所有线路**（示例：gpiochip2）：

```bash
gpioinfo -c gpiochip2
```

```
gpiochip2 - 11 lines:
        line   0:       unnamed                 input
        line   1:       unnamed                 input
        line   2:       unnamed                 input
        line   3:       unnamed                 input
        line   4:       unnamed                 output
        line   5:       unnamed                 output
        line   6:       unnamed                 input
        line   7:       unnamed                 input
        line   8:       unnamed                 output
        line   9:       unnamed                 input
        line  10:       unnamed                 output
```

**读取 GPIO 输入**（示例：GPIO0_0，引脚 13）：

```bash
gpioget -c gpiochip1 0
```

输出：`"0"=active`（active = 高，inactive = 低）

**设置 GPIO 输出**（示例：GPIO0_0 高，然后低）：

```bash
gpioset -c gpiochip1 0=1
gpioset -c gpiochip1 0=0
```

> **注意：** `gpioset` 会阻塞直到进程终止——GPIO 线路保持设定状态直到按下 Ctrl+C，之后释放。仅操作 40-pin 扩展口上引出的线路。

> **注意：** 部分引脚的默认引脚复用不是 GPIO（例如引脚 7 默认为 `AUDIO_CLK`）。若 `gpioset` 无效，该引脚需要设备树 overlay 将其引脚复用切换为 GPIO 模式。

**读取 WKUP 域 GPIO**（示例：WKUP_GPIO0_60，引脚 11）：

```bash
gpioget -c gpiochip0 60
```

**40-pin GPIO 线路映射：**

| 扩展口引脚 | 信号            | 芯片        | 线路  |
|:-----:|:------------- |:--------- |:---:|
| 7     | GPIO0_30      | gpiochip1 | 30  |
| 11    | WKUP_GPIO0_60 | gpiochip0 | 60  |
| 13    | GPIO0_0       | gpiochip1 | 0   |
| 15    | WKUP_GPIO0_61 | gpiochip0 | 61  |
| 16    | GPIO0_27      | gpiochip1 | 27  |
| 18    | GPIO0_51      | gpiochip1 | 51  |
| 22    | WKUP_GPIO0_70 | gpiochip0 | 70  |
| 29    | GPIO0_18      | gpiochip1 | 18  |
| 31    | GPIO0_33      | gpiochip1 | 33  |
| 33    | GPIO0_32      | gpiochip1 | 32  |
| 36    | GPIO0_10      | gpiochip1 | 10  |
| 37    | GPIO0_9       | gpiochip1 | 9   |

### 14.3 SPI

SPI5 已在 40-pin 扩展口上引出并默认启用，支持两种使用方式：

- **通过 `spidev` 用户空间访问**：无需 overlay。开机后 `/dev/spidev1.0`（CS0）即可直接使用，传感器、ADC 等外设可通过标准 SPI 库（如 Python `spidev`）从用户空间驱动。
- **需要内核驱动的外设**（如 SPI 显示屏）：需要设备树 overlay，将外设的 `compatible` 字符串、片选号和最大时钟频率注册到设备树，内核才能绑定对应驱动。

| 引脚  | 信号        | SoC Ball |
|:--- |:--------- |:-------- |
| 19  | SPI5_MOSI | R27      |
| 21  | SPI5_MISO | AD27     |
| 23  | SPI5_CLK  | T27      |
| 24  | SPI5_CS0  | U28      |
| 26  | SPI5_CS1  | W28      |

设备节点为 `/dev/spidev1.0`（CS0）。

**验证 SPI 设备节点：**

```bash
ls /dev/spidev*
```

**查看 SPI 配置：**

```bash
spi-config -d /dev/spidev1.0 -q
```

**回环测试**（将引脚 19 与引脚 21 用跳线短接）：

```bash
echo -ne '\x55\xAA\x12\x34' | spi-pipe -d /dev/spidev1.0 -s 1000000 | xxd
```

预期输出：

```
00000000: 55aa 1234                                U..4
```

### 14.4 UART

UART5 已在 40-pin 扩展口上引出，设备节点为 `/dev/ttyS0`，默认启用。

| 引脚  | 信号        | SoC Ball | 方向  |
|:--- |:--------- |:-------- |:--- |
| 8   | UART5_TXD | W25      | 输出  |
| 10  | UART5_RXD | AC24     | 输入  |

> 串口调试控制台（J6，UART8）使用 `/dev/ttyS2`。请勿将 `/dev/ttyS2` 用于通用 UART 通信。

**判断串口号：**

```bash
# 显示每个 ttyS 的 MMIO 地址，对照 SoC 数据手册或 DTS 中的 reg 值确认
cat /proc/tty/driver/serial
```

也可通过文件权限快速区分——调试控制台的所属组为 `tty`，普通串口为 `dialout`：

```
crw------- root tty     ttyS2   ← 调试控制台（J6），用于系统管理
crw-rw---- root dialout ttyS0   ← 通用串口（40-pin 扩展口）
```

**环回测试：**

将 40-pin 扩展口的引脚 8（TXD）与引脚 10（RXD）短接，然后执行：

```bash
# 配置串口：115200 波特率，raw 模式，关闭本地 echo
stty -F /dev/ttyS0 115200 raw -echo

# 后台启动接收
cat /dev/ttyS0 &

# 发送测试字符串，应立即回显
echo "loopback" > /dev/ttyS0

# 停止接收：切换到前台后按 Ctrl+C
fg
```

### 14.5 I2S / 音频

I2S 接口（MCASP0）已在 40-pin 扩展口上引出，音频设备通过 ALSA 管理。

| 引脚  | 信号                 | SoC Ball | 方向       |
|:--- |:------------------ |:-------- |:-------- |
| 12  | BCLK（MCASP0_ACLKX） | AB28     | 输出（时钟主机） |
| 35  | LRCLK（MCASP0_AFSX） | U27      | 输出（时钟主机） |
| 38  | DIN（MCASP0_AXR0）   | AC28     | 输入       |
| 40  | DOUT（MCASP0_AXR1）  | Y26      | 输出       |

使用 I2S 需要将外部 I2S 音频编解码器 IC 连接至 40-pin 扩展口，并加载将编解码器和 MCASP0 注册为 ALSA 声卡的设备树 overlay。若无 overlay，`aplay -l` 将返回"未找到声卡"。

WM8960 Audio HAT 是支持的 I2S 编解码器 HAT，可直接连接至 40-pin 扩展口。以下流程适用于该 HAT。时钟源为内部 MCASP 辅助时钟（196.608 MHz），可精确整除至 48 kHz 系列采样率；44.1 kHz 播放也可工作，但存在约 4860 PPM 的频率偏差。

**Step 1 — 加载 overlay：**

编辑 `/boot/uEnv.txt`，添加或取消注释以下行（同时注释掉其他 `name_overlays` 行）：

```
name_overlays=ti/k3-j721s2-panda-wm8960-audio-hat.dtbo
```

若需同时使用摄像头 overlay，在同一行中以空格分隔列出：

```
name_overlays=ti/k3-j721s2-panda-wm8960-audio-hat.dtbo ti/k3-j721s2-panda-csi2-imx219-mipi0.dtbo
```

编辑完成后重启。

**Step 2 — 验证声卡已注册：**

```bash
aplay -l
```

预期输出：

```
card 0: WM8960Audio [WM8960-Audio], device 0: davinci-mcasp.0-wm8960-hifi wm8960-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

输出中同时显示卡号和设备号（如 `card 0:`、`device 0:`），在后续所有命令中使用这两个值（以下用 `<C>` 和 `<D>` 表示）。

查询可用混音器控制：

```bash
amixer -c <C> scontrols
```

**Step 3 — 初始化混音器控制**（默认状态下可能无声音输出）：

```bash
amixer -c <C> sset 'Left Output Mixer PCM' on
amixer -c <C> sset 'Right Output Mixer PCM' on
amixer -c <C> sset Headphone 80%
amixer -c <C> sset Speaker 80%
amixer -c <C> sset Playback 80%
```

**Step 4 — 测试播放：**

所有播放命令均使用 `plughw:<C>,<D>`，通过 ALSA plug 层自动处理采样率转换、声道映射和格式适配，无论音频文件的原始采样率如何均可正常播放。

正弦波测试（双声道，3 次循环）：

```bash
speaker-test -c 2 -t sine -f 1000 -l 3 -D plughw:<C>,<D>
```

播放音频文件：

```bash
aplay -D plughw:<C>,<D> audio.wav
```

> **注意：** 若同时连接了 USB 音频设备，它将作为独立声卡出现。加载 overlay 后 WM8960 HAT 始终为 card 0；如不确定，请通过 `aplay -l` 确认。

> **提示：** 大多数使用场景下，USB 音频设备（参见第 12.3 节）更为简便——即插即用，无需硬件连线或设备树修改。

**步骤 5 — 测试录音：**

> 以下流程以 WM8960 Audio HAT 为例。控件名称和增益范围与该设备相关，其他 I2S 编解码器可能有所不同。

**步骤 5.1 — 确认录音设备存在：**

列出系统中所有支持录音的硬件设备。若列表为空，说明声卡未注册 capture 接口。

```bash
arecord -l
```

示例输出：

```
**** List of CAPTURE Hardware Devices ****
card 0: WM8960Audio [WM8960-Audio], device 0: davinci-mcasp.0-wm8960-hifi wm8960-hifi-0 [davinci-mcasp.0-wm8960-hifi wm8960-hifi-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

**步骤 5.2 — 查询录音相关配置：**

查询 PGA（可编程增益放大器）当前增益和静音状态。需确认输出中显示 `[on]`（未静音）且增益非 0。

```bash
amixer -c <C> sget 'Capture'
```

示例输出：

```
Simple mixer control 'Capture',0
  Capabilities: cvolume cswitch
  Capture channels: Front Left - Front Right
  Limits: Capture 0 - 63
  Front Left: Capture 46 [73%] [17.25dB] [on]
  Front Right: Capture 46 [73%] [17.25dB] [on]
```

查询 Boost 放大器输出是否已接入 PGA。需确认两者均显示 `[on]`（Boost 通路接通）。

```bash
amixer -c <C> sget 'Left Input Mixer Boost'
amixer -c <C> sget 'Right Input Mixer Boost'
```

示例输出：

```
Simple mixer control 'Left Input Mixer Boost',0
  Capabilities: pswitch pswitch-joined
  Playback channels: Mono
  Mono: Playback [on]
```

查询 Boost 增益当前值及可选范围。记录输出中的 `Limits` 行，供步骤 5.3 参考。

```bash
amixer -c <C> sget 'Left Input Boost Mixer LINPUT1'
amixer -c <C> sget 'Right Input Boost Mixer RINPUT1'
```

示例输出：

```
Simple mixer control 'Left Input Boost Mixer LINPUT1',0
  Capabilities: volume volume-joined
  Playback channels: Mono
  Capture channels: Mono
  Limits: 0 - 3
  Mono: 1 [33%] [13.00dB]
```

**步骤 5.3 — 设置录音相关配置：**

若步骤 5.2 的查询结果与推荐值不符，执行以下命令。

开启 Boost 放大器输出到 PGA 的通路，使麦克风信号能够进入 ADC：

```bash
amixer -c <C> sset 'Left Input Mixer Boost' on
amixer -c <C> sset 'Right Input Mixer Boost' on
```

设置 Boost 增益（来自步骤 5.2：范围 0~3，对应 0 / +13 / +20 / +29 dB）。推荐起始值：`1`（+13 dB）：

```bash
amixer -c <C> sset 'Left Input Boost Mixer LINPUT1' 1
amixer -c <C> sset 'Right Input Boost Mixer RINPUT1' 1
```

设置左右声道 PGA 增益（来自步骤 5.2：范围 0~63，对应 −17 dB ~ +30 dB）。推荐起始值：`46`（+17 dB）：

```bash
amixer -c <C> sset 'Capture' 46,46
```

总录音增益：Boost +13 dB + PGA +17 dB = **+30 dB**。录音出现失真则降低增益，声音过弱则提高增益。

**步骤 5.4 — 查询硬件支持的录音参数：**

查询硬件支持的格式、采样率和声道数，作为步骤 5.5 录音命令参数的选取依据。

```bash
arecord -D hw:<C>,<D> --dump-hw-params -d 1 /dev/null
```

示例输出：

```
FORMAT:   S16_LE S32_LE
CHANNELS: [1 2]
RATE:     [8000 48000]
```

**步骤 5.5 — 录音：**

按步骤 5.4 查询到的参数执行录音：

```bash
arecord -D hw:<C>,<D> -f S16_LE -r 48000 -c 2 -d 10 rec.wav
```

| 参数              | 值            | 来源                                                         |
|:--------------- |:------------ |:---------------------------------------------------------- |
| `-D hw:<C>,<D>` | 直接访问硬件       | 卡号和设备号来自步骤 5.1                                             |
| `-f S16_LE`     | 16-bit 有符号小端 | 步骤 5.4：FORMAT S16_LE S32_LE                                |
| `-r 48000`      | 48 kHz       | 步骤 5.4：RATE [8000 48000]；196.608 MHz MCASP 时钟可精确整除至 48 kHz |
| `-c 2`          | 立体声          | 步骤 5.4：CHANNELS [1 2]                                      |
| `-d 10`         | 10 秒         | 测试时长，按需调整                                                  |

**步骤 5.6 — 播放验证：**

使用 `plughw` 由 ALSA plug 层自动处理格式和采样率转换。若可听到录音内容，则录音功能验证通过。

```bash
aplay -D plughw:<C>,<D> rec.wav
```

### 14.6 PWM

40-pin 扩展口上提供两路 PWM 输出：

| 引脚  | 信号                      | 驱动                      | 设备地址          | 通道  |
|:---:|:----------------------- |:----------------------- |:-------------:|:---:|
| 32  | ECAP0_IN_APWM_OUT（AB26） | `pwm-tiecap`（ECAP0）     | `3100000.pwm` | 0   |
| 33  | PWM5_B / GPIO0_32（U26）  | `pwm-ehrpwm`（EHRPWM5_B） | `3050000.pwm` | 1   |

> `pwmchip` 编号在启动时动态分配，不同板卡可能不同，使用前须通过设备地址查找。`3010000.pwm`（EHRPWM1）保留用于风扇转速控制。

查看所有 pwmchip 与设备的对应关系：

```bash
for c in /sys/class/pwm/pwmchip*; do echo "$c -> $(readlink -f $c/device)"; done
```

查找指定输出的 pwmchip 编号：

```bash
# ECAP0（引脚 32）
grep -rl 3100000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*'

# EHRPWM5（引脚 33）
grep -rl 3050000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*'
```

#### 引脚 32 — ECAP0 APWM 输出

引脚 32 使用 SoC 内置的增强型捕获（ECAP）模块，工作在非对称 PWM（APWM）输出模式，通道 0：

```bash
# 查找芯片编号
CHIP=$(grep -rl 3100000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*')

# 注册通道 0 — 创建 pwm0/ 控制目录
echo 0 > /sys/class/pwm/$CHIP/export

# 设置周期，单位纳秒（1 000 000 ns = 1 kHz）
echo 1000000 > /sys/class/pwm/$CHIP/pwm0/period

# 设置占空比，单位纳秒（500 000 ns = 50%）
echo 500000 > /sys/class/pwm/$CHIP/pwm0/duty_cycle

# 启动输出
echo 1 > /sys/class/pwm/$CHIP/pwm0/enable
```

停止输出：

```bash
CHIP=$(grep -rl 3100000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*')

# 停止输出
echo 0 > /sys/class/pwm/$CHIP/pwm0/enable

# 释放通道 0 — 删除 pwm0/ 目录
echo 0 > /sys/class/pwm/$CHIP/unexport
```

#### 引脚 33 — EHRPWM5_B 输出

引脚 33 使用 EHRPWM5 通道 B，通道 1：

```bash
# 查找芯片编号
CHIP=$(grep -rl 3050000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*')

# 注册通道 1（B）— 创建 pwm1/ 控制目录
echo 1 > /sys/class/pwm/$CHIP/export

# 设置周期，单位纳秒（1 000 000 ns = 1 kHz）
echo 1000000 > /sys/class/pwm/$CHIP/pwm1/period

# 设置占空比，单位纳秒（500 000 ns = 50%）
echo 500000 > /sys/class/pwm/$CHIP/pwm1/duty_cycle

# 启动输出
echo 1 > /sys/class/pwm/$CHIP/pwm1/enable
```

停止输出：

```bash
CHIP=$(grep -rl 3050000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*')

# 停止输出
echo 0 > /sys/class/pwm/$CHIP/pwm1/enable

# 释放通道 1（B）— 删除 pwm1/ 目录
echo 1 > /sys/class/pwm/$CHIP/unexport
```

---

## 15. MIPI FPC 端口

### 15.1 概述

J24（MIPI0）和 J25（MIPI1）是 22-pin FPC 连接器，采用 MIPI D-PHY 接口。每个端口均可通过设备树 overlay 配置为 CSI-2 摄像头输入或 DSI 显示输出——但同一端口不能同时使用两种模式。

已验证兼容设备：

- **摄像头：** Sony IMX219（例如树莓派 Camera Module 2）
- **显示屏：** 树莓派 7 寸 DSI 面板（仅 J24；参见第 16 节）

### 15.2 配置

模式选择通过 `/boot/uEnv.txt` 中的 `name_overlays` 行控制。支持三种使用场景：

| 场景  | J24（MIPI0） | J25（MIPI1） | `name_overlays`                                                                         |
|:--- |:---------- |:---------- |:--------------------------------------------------------------------------------------- |
| A   | CSI 摄像头    | —          | `ti/k3-j721s2-panda-csi2-imx219-mipi0.dtbo`                                             |
| B   | —          | CSI 摄像头    | `ti/k3-j721s2-panda-csi2-imx219-mipi1.dtbo`                                             |
| C   | DSI 显示屏    | CSI 摄像头    | `ti/k3-j721s2-panda-dsi-rpi-7inch-panel.dtbo ti/k3-j721s2-panda-csi2-imx219-mipi1.dtbo` |

`name_overlays` 规则：

- 每个值均为相对于 `/boot/dtb/` 的 `.dtbo` 文件路径

- 仅最后一个未注释的 `name_overlays` 行生效——其余均需注释掉

- 加载多个 overlay 时，在同一 `name_overlays` 行上以空格分隔列出，例如场景 C：
  
  ```
  name_overlays=ti/k3-j721s2-panda-dsi-rpi-7inch-panel.dtbo ti/k3-j721s2-panda-csi2-imx219-mipi1.dtbo
  ```

---

## 16. MIPI DSI 显示屏

J24（MIPI0）支持 DSI 显示输出。overlay 配置参见第 15.2 节；DSI + 摄像头同时使用参见第 17.3 节（场景 C）。

> J25（MIPI1）DSI 支持目前不可用。

> **警告：** DSI 面板必须在启动前物理连接至 J24。若面板缺失，DSS 显示子系统初始化失败，Mini DisplayPort（J9）也将不可用。

---

## 17. 摄像头输入

端口硬件概述和 overlay 配置规则参见第 15 节。

### 17.1 场景 A — J24 摄像头

编辑 `/boot/uEnv.txt`，取消注释以下行（注释掉其他所有 `name_overlays` 行）：

```
name_overlays=ti/k3-j721s2-panda-csi2-imx219-mipi0.dtbo
```

将 IMX219 连接至 J24，验证检测：

```bash
v4l2-ctl --list-devices
```

**配置传感器参数：**

```bash
v4l2-ctl -d /dev/v4l-subdev0 --set-ctrl=analogue_gain=200
v4l2-ctl -d /dev/v4l-subdev0 --set-ctrl=exposure=3000
```

**配置媒体管线：**

```bash
media-ctl -d /dev/media0 -V '"imx219 5-0010":0 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"cdns_csi2rx.4500000.csi-bridge":0 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"cdns_csi2rx.4500000.csi-bridge":1 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"4504000.ticsi2rx":0 [fmt:SRGGB8_1X8/1920x1080]'
```

**抓取一帧 JPEG：**

```bash
gst-launch-1.0 v4l2src device=/dev/video0 num-buffers=1 \
  ! "video/x-bayer,width=1920,height=1080,format=rggb,framerate=30/1" \
  ! bayer2rgb ! videoconvert ! jpegenc ! filesink location=cam.jpg
```

### 17.2 场景 B — J25 摄像头

编辑 `/boot/uEnv.txt`，取消注释以下行（注释掉其他所有 `name_overlays` 行）：

```
name_overlays=ti/k3-j721s2-panda-csi2-imx219-mipi1.dtbo
```

将 IMX219 连接至 J25，验证检测：

```bash
v4l2-ctl --list-devices
```

**配置传感器参数：**

```bash
v4l2-ctl -d /dev/v4l-subdev2 --set-ctrl=analogue_gain=200
v4l2-ctl -d /dev/v4l-subdev2 --set-ctrl=exposure=3000
```

**配置媒体管线：**

```bash
media-ctl -d /dev/media0 -V '"imx219 3-0010":0 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"cdns_csi2rx.4514000.csi-bridge":0 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"cdns_csi2rx.4514000.csi-bridge":1 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"4510000.ticsi2rx":0 [fmt:SRGGB8_1X8/1920x1080]'
```

**抓取一帧 JPEG：**

```bash
gst-launch-1.0 v4l2src device=/dev/video2 num-buffers=1 \
  ! "video/x-bayer,width=1920,height=1080,format=rggb,framerate=30/1" \
  ! bayer2rgb ! videoconvert ! jpegenc ! filesink location=cam.jpg
```

### 17.3 场景 C — J24 DSI 显示屏 + J25 摄像头

编辑 `/boot/uEnv.txt`，取消注释以下行（注释掉其他所有 `name_overlays` 行）：

```
name_overlays=ti/k3-j721s2-panda-dsi-rpi-7inch-panel.dtbo ti/k3-j721s2-panda-csi2-imx219-mipi1.dtbo
```

DSI 显示屏设置参见第 16 节。摄像头抓取命令参见第 17.2 节。

> **警告：** DSI 面板必须在启动前物理连接至 J24。若面板缺失，DSS 显示子系统初始化失败，Mini DisplayPort（J9）也将不可用。

---

## 18. AI 推理加速

TDA4VE / AM68A SoC 包含 8 TOPS 矩阵乘法加速器（MMA）。TI 作为 Edge AI SDK 的一部分提供 TIDL（TI Deep Learning）运行时和模型推理工具。

> **注意：** AI 推理工具链文档和使用示例将在本指南的后续版本中添加。当前信息请参阅 TI Edge AI 文档和 EdgeAI-Studio 资源。

关键组件：

- **MMA（矩阵乘法加速器）**：8 TOPS，支持 INT8 量化推理
- **C7x DSP 核**：用于 TIDL 管线中的前后处理
- **R5F 实时核**：实时控制和传感器管理
- **TIDL 运行时**：模型转换、推理 API、GStreamer 集成

---

## 19. 故障排查

### 19.1 板卡无法启动

- 确认 SD 卡已完全插入 J23（应有咔哒声）。
- 使用 Armbian Imager 重新烧录镜像，弹出前等待出现"写入成功"提示。
- 首次启动时，系统自动扩展文件系统并重启——共需约 3–4 分钟。
- LED 指示：红色 = 已上电，系统未运行；绿色常亮 = 系统运行中。

### 19.2 串口控制台无输出

- 确认适配器连接至 J6，而非 J5（USB-C 电源）。
- 使用 **3.3 V 逻辑电平** USB 转 UART 适配器——5 V 信号会损坏板卡。
- 参数：**115200 波特率，8N1，无流控**。
- 调试控制台位于 `/dev/ttyS2`（UART8）。
- 在接通电源**之前**打开串口终端，以捕获完整启动日志。

### 19.3 无网络连接

- 确认 RJ45 网线已连接至 J1（以太网口）。
- 检查以太网口链路指示灯。
- 验证接口状态：`nmcli device status`
- 检查已分配 IP：`ip addr show eth0`

### 19.4 未检测到 NVMe

- 确认 FPC 线缆已完全插入 J10 和 NVMe 转接板。
- 查看内核消息：`dmesg | grep -i nvme`
- 列出 PCI 设备：`lspci`

### 19.5 显示器无信号

- 请使用具备原生 DisplayPort 输入的显示器。被动式 Mini DP 转 HDMI 适配器无法使用。
- 确认线缆已牢固插入 J9。
- 检查 DRM 状态：`cat /sys/class/drm/card*/card*-DP-*/status`

---

## 附录 A — 快速规格参考

| 项目       | 值                                  |
|:-------- |:---------------------------------- |
| SoC      | TDA4VE / AM68A（J721S2）             |
| CPU      | 2× Cortex-A72，最高 2.0 GHz           |
| AI       | 8 TOPS                             |
| RAM      | 8 GB LPDDR4                        |
| 存储       | Micro SD（启动 + 根文件系统）；PCIe NVMe（扩展） |
| 操作系统     | Armbian（Debian 13 Trixie）          |
| 网络       | 千兆以太网（eth0），默认 DHCP                |
| USB      | 4× USB 3.0（TUSB8041 Hub）           |
| 显示       | Mini DisplayPort（J9）               |
| 摄像头      | 2× MIPI CSI-2 / DSI FPC（J24、J25）   |
| GPIO 扩展口 | 40-pin，兼容树莓派 HAT，3.3 V IO          |
| 调试 UART  | J6，/dev/ttyS2，115200 8N1           |
| 电源       | USB-C（J5），5 V / 5 A                |

## 附录 B — 相关文档与资源

| 文档 / 资源 | 说明 |
| --- | --- |
| [MO68A 快速入门指南](MO68A_快速入门指南_V1.0.md) | 初始设置、烧录、首次登录 |
| [MO68A 硬件参考手册](MO68A_硬件参考手册_V1.0.md) | 连接器引脚定义、信号分配、电气规格 |

---

## 修订历史

| 版本  | 日期         | 描述   |
|:--- |:---------- |:---- |
| 1.0 | 2026-04-28 | 初始发布 |
