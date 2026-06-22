# MO-62A 快速入门指南

## 目录

- [1. 简介](#1-简介)
- [2. 所需物品](#2-所需物品)
- [3. 烧录 SD 卡](#3-烧录-sd-卡)
- [4. 硬件连接](#4-硬件连接)
- [5. 首次启动](#5-首次启动)
- [6. 网络访问](#6-网络访问)
- [7. 摄像头预览（IMX219）](#7-摄像头预览imx219)
- [8. Edge AI 推理](#8-edge-ai-推理)
- [9. 40 Pin 扩展接口](#9-40-pin-扩展接口)
- [10. 常见问题与技巧](#10-常见问题与技巧)

---

## 1. 简介

### 1.1 关于 MO-62A

MO-62A 是一款专为边缘 AI 推理、机器视觉和工业控制应用设计的单板计算机。搭载 **TI AM62A7** 处理器——四核 Arm Cortex-A53 SoC，内置专用 MMA（矩阵乘法加速器），AI 推理性能高达 **2 TOPS**。

### 1.2 主要规格

| 参数         | 规格                                                              |
|--------------|-------------------------------------------------------------------|
| SoC          | TI AM62A74（四核 Cortex-A53 @ 1.4 GHz + Cortex-R5F）             |
| AI 加速器    | MMA，2 TOPS                                                       |
| 内存         | LPDDR4（32-bit）                                                   |
| 存储         | Micro SD（启动 / 存储）                                            |
| 显示         | Micro HDMI（最高 1080p，via SiI9022ACNU）                         |
| 网络         | 1 × 千兆以太网 RJ45                                               |
| 无线         | Wi-Fi + 蓝牙（FG6221A，U.FL 天线接口）                            |
| USB          | 1 × USB Type-C（供电 + USB 2.0），4 × USB 2.0 Type-A             |
| 摄像头       | 22-pin FPC CSI（4-lane MIPI CSI-2）                               |
| 音频         | 3.5 mm 耳机麦克风二合一接口                                       |
| 扩展接口     | 40-pin（GPIO / I2C / SPI / UART / PWM）                           |
| RTC          | PCF85263ATL，带纽扣电池接口                                        |
| 风扇         | PWM 风扇接口（PWM + TACH）                                         |
| 供电         | USB Type-C 5 V（建议 ≥ 3 A）                                      |
| 指示灯       | 红色（电源），绿色（活动）                                         |
| 调试接口     | UART0 串口控制台（3-pin SH1.0 接口）                               |
| 操作系统     | Debian 13（Trixie）+ XFCE 桌面                                    |

### 1.3 板卡布局

![MO-62A 板卡](images/interface.png)

| 接口 / 元件                  | 位置         |
|------------------------------|--------------|
| USB Type-C（供电 + USB 2.0） | 顶边左侧     |
| 4 × USB 2.0 Type-A           | 顶边右侧     |
| Micro HDMI                   | 右边上方     |
| RJ45 以太网                  | 右边下方     |
| Micro SD 卡槽                | 底边         |
| 40-pin 扩展接口              | 左边         |
| CSI 摄像头接口               | 中部 FPC     |
| 3.5 mm 音频接口              | 前边         |
| Wi-Fi / BT 天线接口（U.FL）  | 靠近无线模块 |
| 调试串口（SH1.0 3-pin）      | 靠近 USB-C   |
| 风扇接口                     | 靠近 40-pin  |

---

## 2. 所需物品

以下物品为必备：

| 物品                  | 说明                                  |
|-----------------------|---------------------------------------|
| MO-62A 开发板         |                                       |
| USB Type-C 电源适配器 | 5 V，≥ 3 A                            |
| Micro SD 卡           | ≥ 16 GB，Class 10 / UHS-I (U1) 或更快 |
| Micro HDMI 线         | 连接显示器或电视                      |
| RJ45 网线             | 初始网络配置必需                      |
| 主机电脑              | Windows——用于烧录 SD 卡               |

以下物品为可选但推荐：

| 物品                      | 说明                         |
|---------------------------|------------------------------|
| IMX219 CSI 摄像头模块     |                              |
| USB 键盘和鼠标            | 用于直接操作桌面             |
| 3.5 mm 耳机               | 耳机输出 + 麦克风输入        |
| CR1220 纽扣电池           | RTC 掉电保持                 |
| Wi-Fi 天线（U.FL）        | 显著提升无线信号覆盖范围     |
| PWM 风扇                  | 4-pin，5 V                   |

---

## 3. 烧录 SD 卡

### 3.1 下载镜像

从发布页面下载最新预构建的 SD 卡镜像：

<!-- TODO: 插入发布下载链接 -->

镜像文件格式为 `.img.zip`。

完整 SDK 源码（内核、设备树、文件系统定制）可在以下地址获取：

**GitHub：** [https://github.com/inhandnet/mo-62a](https://github.com/inhandnet/mo-62a)

### 3.2 使用 balenaEtcher 烧录（Windows）

1. 下载并安装 [balenaEtcher](https://etcher.balena.io)。

2. 点击 **Flash from file**。

   ![Flash from file](images/balenaEtcher-flashfromfile.png)

3. 选择下载的 `.img.zip` 文件。

   ![选择镜像文件](images/balenaEtcher-image.png)

4. 点击 **Select target**。

   ![Select target](images/balenaEtcher-selecttarget.png)

5. 从设备列表中选择 Micro SD 卡。

   ![选择 SD 卡](images/balenaEtcher-sdtarget.png)

6. 点击 **Flash!** 开始烧录。

   ![Flash](images/balenaEtcher-flash.png)

7. 等待显示 **Flash Complete!**，然后安全移除 SD 卡。

   ![烧录完成](images/balenaEtcher-flashcompleted.png)

> **警告：** SD 卡上的所有现有数据将被清除。

---

## 4. 硬件连接

1. **插入 SD 卡** — 将烧录好的 Micro SD 卡插入板卡底面的卡槽，直到听到咔哒声。
2. **连接显示器** — 用 Micro HDMI 线连接板卡与显示器。
3. **连接网线** — 将 RJ45 网线插入千兆以太网接口。
4. **连接外设** — 将 USB 键盘和鼠标接入任意 USB 2.0 Type-A 接口（可选）。
5. **连接摄像头** — 如使用 IMX219，将 FPC 排线连接到 22-pin CSI 接口（参见[第 7 节](#7-摄像头预览imx219)）。
6. **接通电源** — 最后连接 USB Type-C 电源适配器，红色电源指示灯将立即亮起。

<!-- TODO: 插入硬件连接示意图 -->

---

## 5. 首次启动

### 5.1 启动过程

接通电源后，板卡从 Micro SD 卡启动，正常启动约需 **30～45 秒**。启动过程中绿色活动指示灯会闪烁。

> **注意——首次启动：** 第一次启动时，系统会自动将根文件系统扩展至 SD 卡的全部可用空间，此过程额外需要 **1～2 分钟**，完成后板卡将自动重启。桌面在第二次启动完成后出现。此后每次启动均为正常速度。

预期启动顺序：

1. U-Boot SPL（R5）→ U-Boot（A53）— 短暂串口输出
2. Linux 内核解压并加载设备树
3. systemd 启动各系统服务——**首次启动**时，文件系统扩容在此阶段进行并触发自动重启
4. HDMI 显示器上出现 XFCE 桌面

### 5.2 桌面登录

XFCE 桌面自动加载，默认凭据如下：

| 字段   | 值        |
|--------|-----------|
| 用户名 | `debian`  |
| 密码   | `123456` |

### 5.3 串口控制台（UART0 调试接口）

如无显示器，可通过 3-pin UART0 调试接口（SH1.0，1.0 mm 间距）访问板卡。

| 引脚 | 信号 |
|------|------|
| 1    | RXD  |
| 2    | TXD  |
| 3    | GND  |

串口参数：**115200 波特，8N1，无流控**

```bash
# Linux 主机示例（将 /dev/ttyUSB0 替换为实际设备节点）
minicom -D /dev/ttyUSB0 -b 115200
```

<!-- TODO: 插入 UART 接口位置照片 -->

---

## 6. 网络访问

### 6.1 有线以太网

板卡启动后通过 DHCP 自动获取 IP 地址。

### 6.2 查找板卡 IP 地址

在 XFCE 桌面终端中执行：

```bash
ip addr show eth0
```

在同一局域网的主机上（如已启用 mDNS）：

```bash
ping mo-62a.local
```

### 6.3 SSH 登录

```bash
ssh debian@<板卡IP>
# 或
ssh debian@mo-62a.local
```

### 6.4 Wi-Fi 配置

使用 `nmcli` 连接 Wi-Fi：

```bash
# 扫描可用网络
nmcli device wifi list

# 连接到指定网络
nmcli device wifi connect "SSID" password "密码"
```

也可使用 XFCE 系统托盘中的网络管理器图形界面。

> **注意：** 板卡提供 U.FL 天线接口，外接天线可显著提升无线覆盖范围。

---

## 7. 摄像头预览（IMX219）

MO-62A 通过 22-pin FPC CSI 接口支持 **IMX219** CSI 摄像头模块（索尼 IMX219）。

### 7.1 连接摄像头

1. 轻轻向上掀开 CSI 接口的 FPC 锁扣。
2. 将排线触点面朝向板卡（金属触点朝下）插入接口。
3. 按下锁扣固定排线。

<!-- TODO: 插入 CSI 接口连接照片 -->

### 7.2 运行预览

`imx219-preview.sh` 脚本已预装于 `/usr/local/bin/imx219-preview.sh`。

```bash
# 默认 15 fps 预览
sudo imx219-preview.sh

# 30 fps 预览
sudo imx219-preview.sh 30

# 低光模式（5 fps，最大增益和曝光）
sudo GAIN=232 imx219-preview.sh 5
```

预览画面显示在 HDMI 输出上，按 **Ctrl+C** 退出。

> **注意：** 脚本需要 root 权限（`sudo`），因为 `kmssink` 需要获取 DRM 主设备控制权。运行期间会自动停止桌面会话（lightdm），退出后自动恢复。

### 7.3 调节参数

| 变量       | 默认值 | 范围         | 说明                                 |
|------------|--------|--------------|--------------------------------------|
| `FPS`      | `15`   | 5/8/10/15/30 | 帧率（作为第一个参数传入）           |
| `WB_R`     | `0.5`  | 0.0 – 1.0    | 白平衡红色通道参考值                 |
| `WB_B`     | `0.6`  | 0.0 – 1.0    | 白平衡蓝色通道参考值                 |
| `GAIN`     | `150`  | 0 – 232      | 模拟增益（低光环境下适当调高）       |
| `DGAIN`    | `256`  | 256 – 4095   | 数字增益（值越高噪点越多）           |
| `EXPOSURE` | 自动   | 行数         | 曝光行数（默认为当前帧率下的最大值） |

示例——暖色白平衡，10 fps：

```bash
sudo WB_R=0.4 WB_B=0.5 imx219-preview.sh 10
```

---

## 8. Edge AI 推理

MO-62A 搭载 TI C7x DSP，可对边缘 AI 推理进行硬件加速（TIDL）。系统已预装模型库、推理运行时和完整的 C/C++ 开发 SDK——开箱即可运行 demo，也可直接在板上编译、调试自己的推理程序。

### 8.1 运行推理 Demo（edgeai-demo）

`edgeai-demo` 是统一入口，同时支持 **Python** 与 **C/C++** 两个后端、**CSI** 与 **USB** 两种摄像头，配置通用。

交互模式（依次选择 摄像头 → 模型 → 后端）：

```bash
edgeai-demo
```

命令行模式：

```bash
edgeai-demo list                                   # 列出可用模型
edgeai-demo run 2 --backend cpp    --camera csi    # C/C++ 后端 + CSI 摄像头
edgeai-demo run 2 --backend python --camera usb    # Python 后端 + USB 摄像头
edgeai-demo status                                 # 查看当前摄像头
```

推理画面（含检测框与性能曲线）显示在 HDMI 输出上，按 **Ctrl+C** 退出。

> **注意：** 使用 CSI 摄像头前先运行 `sudo init-imx219` 初始化。`edgeai-demo` 会自动处理 root 权限、环境变量、C7x 复位、停止/恢复桌面（lightdm），无需手动操作。

### 8.2 在板上开发 C/C++ AI 程序

系统预装了完整的 C/C++ AI SDK，可直接在板上编译自己的推理程序，**无需交叉编译环境**：

| 内容 | 位置 |
|---|---|
| 头文件 | `/usr/include/edgeai/` |
| 库 + CMake 包 | `/usr/lib/edgeai/`、`/usr/lib/cmake/EdgeAI/` |
| 示例工程 | `/usr/share/edgeai-cpp-examples/` |
| 模型库 | `/opt/model_zoo/` |
| 开发指南 | `/usr/share/edgeai-cpp-examples/DEV_GUIDE.md` |

一个 `CMakeLists.txt` 即可链接整套 SDK（无需手动指定头文件/库路径）：

```cmake
find_package(EdgeAI REQUIRED)
add_executable(my_infer main.cpp)
target_link_libraries(my_infer PRIVATE EdgeAI::edgeai)
```

编译并运行最小示例（加载模型 + 跑一次推理，无需摄像头）：

```bash
cp -r /usr/share/edgeai-cpp-examples/hello_inference ~/hello_inference
cd ~/hello_inference && mkdir build && cd build
cmake .. && make
sudo LD_LIBRARY_PATH=/opt/ti/edgeai/lib ./hello_inference \
     -m /opt/model_zoo/ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416
```

输出 `Inference OK.` 即表示模型已在 C7x DSP 上完成推理。完整的"摄像头 → 推理 → HDMI"流水线示例见 `/usr/share/edgeai-cpp-examples/app_edgeai/`，API 用法与更多说明见 `DEV_GUIDE.md`。

---

## 9. 40 Pin 扩展接口

40-pin 扩展接口的所有信号引脚默认工作在 **GPIO 模式**，逻辑电平为 **3.3 V**。I2C、SPI、UART、PWM 等可选外设功能可通过设备树叠加层（overlay）启用。

> **注意：** 引脚 27/28（I2C2）固定用于摄像头模块内部 I2C 总线，不能用作通用 GPIO。

### 9.1 引脚定义

![40-pin 接口](images/40pin.png)

完整 40 针列表见下方 [8.2 节](#82-linux-gpio-对照表)。

### 9.2 Linux GPIO 对照表

以下为全部 40 针的完整对照表，GPIO 引脚可通过 `gpioset` / `gpioget`（软件包 `gpiod`）控制。

| 引脚 | 名称        | 默认功能                  | gpiochip  | Line | 可选功能             |
|------|-------------|---------------------------|-----------|------|----------------------|
|  1   | 3V3         | 3.3 V 电源                | —         | —    | —                    |
|  2   | 5V          | 5 V 电源                  | —         | —    | —                    |
|  3   | GPIO2       | GPIO（MCU\_GPIO0\_20）    | gpiochip0 | 20   | WKUP\_I2C0\_SDA      |
|  4   | 5V          | 5 V 电源                  | —         | —    | —                    |
|  5   | GPIO3       | GPIO（MCU\_GPIO0\_19）    | gpiochip0 | 19   | WKUP\_I2C0\_SCL      |
|  6   | GND         | 地                        | —         | —    | —                    |
|  7   | GPIO4       | GPIO（GPIO0\_39）         | gpiochip1 | 39   | —                    |
|  8   | GPIO14      | GPIO（GPIO1\_25）         | gpiochip2 | 25   | UART5\_TXD           |
|  9   | GND         | 地                        | —         | —    | —                    |
| 10   | GPIO15      | GPIO（GPIO1\_24）         | gpiochip2 | 24   | UART5\_RXD           |
| 11   | GPIO23      | GPIO（GPIO1\_23）         | gpiochip2 | 23   | —                    |
| 12   | GPIO18      | GPIO（GPIO1\_0）          | gpiochip2 |  0   | MCASP2\_ACLKX        |
| 13   | GPIO27      | GPIO（GPIO0\_42）         | gpiochip1 | 42   | —                    |
| 14   | GND         | 地                        | —         | —    | —                    |
| 15   | GPIO22      | GPIO（GPIO1\_22）         | gpiochip2 | 22   | —                    |
| 16   | GPIO17      | GPIO（GPIO0\_38）         | gpiochip1 | 38   | —                    |
| 17   | 3V3         | 3.3 V 电源                | —         | —    | —                    |
| 18   | GPIO24      | GPIO（GPIO0\_40）         | gpiochip1 | 40   | —                    |
| 19   | GPIO10      | GPIO（GPIO1\_18）         | gpiochip2 | 18   | SPI0\_D0（MOSI）     |
| 20   | GND         | 地                        | —         | —    | —                    |
| 21   | GPIO9       | GPIO（GPIO1\_19）         | gpiochip2 | 19   | SPI0\_D1（MISO）     |
| 22   | GPIO25      | GPIO（GPIO0\_14）         | gpiochip1 | 14   | —                    |
| 23   | GPIO11      | GPIO（GPIO1\_17）         | gpiochip2 | 17   | SPI0\_CLK            |
| 24   | GPIO8       | GPIO（GPIO1\_15）         | gpiochip2 | 15   | SPI0\_CS0            |
| 25   | GND         | 地                        | —         | —    | —                    |
| 26   | GPIO7       | GPIO（GPIO1\_16）         | gpiochip2 | 16   | SPI0\_CS1            |
| 27   | I2C2\_SDA   | I2C2 SDA（`i2c-2`）      | —         | —    | （摄像头总线，固定）  |
| 28   | I2C2\_SCL   | I2C2 SCL（`i2c-2`）      | —         | —    | （摄像头总线，固定）  |
| 29   | GPIO5       | GPIO（GPIO0\_36）         | gpiochip1 | 36   | —                    |
| 30   | GND         | 地                        | —         | —    | —                    |
| 31   | GPIO6       | GPIO（GPIO0\_33）         | gpiochip1 | 33   | —                    |
| 32   | GPIO12      | GPIO（GPIO1\_14）         | gpiochip2 | 14   | EHRPWM0\_B           |
| 33   | GPIO13      | GPIO（GPIO1\_13）         | gpiochip2 | 13   | EHRPWM0\_A           |
| 34   | GND         | 地                        | —         | —    | —                    |
| 35   | GPIO19      | GPIO（GPIO0\_91）         | gpiochip1 | 91   | MCASP2\_AFSX         |
| 36   | GPIO16      | GPIO（GPIO1\_9）          | gpiochip2 |  9   | EHRPWM1\_A           |
| 37   | GPIO26      | GPIO（GPIO0\_41）         | gpiochip1 | 41   | —                    |
| 38   | GPIO20      | GPIO（GPIO1\_5）          | gpiochip2 |  5   | MCASP2\_AXR0         |
| 39   | GND         | 地                        | —         | —    | —                    |
| 40   | GPIO21      | GPIO（GPIO1\_2）          | gpiochip2 |  2   | MCASP2\_AXR1         |

> `gpiochip0` = `mcu_gpio0`（MCU 域）；`gpiochip1` = `main_gpio0`（GPIO0\_x）；`gpiochip2` = `main_gpio1`（GPIO1\_x）。

### 9.3 电平说明

扩展接口所有 I/O 引脚均工作在 **3.3 V** 逻辑电平，**请勿将 5 V 信号直接连接到 GPIO 引脚**。

### 9.4 快速示例

系统预装 `libgpiod` v2.x，操作芯片时需使用 `-c` 参数指定芯片名称。

**列出所有 GPIO 芯片：**

```bash
gpiodetect
```

**读取 GPIO 输入（示例：引脚 11 / BCM GPIO23 → gpiochip2 line 23）：**

```bash
gpioget -c gpiochip2 23
# 输出："23"=active  （active = 高电平，inactive = 低电平）
```

**同时读取多个引脚：**

```bash
gpioget -c gpiochip1 39 38 42
# 输出："39"=active "38"=active "42"=active
```

**持续输出高电平（示例：引脚 7 / BCM GPIO4 → gpiochip1 line 39）：**

```bash
# 后台运行，进程存续期间引脚保持驱动状态
gpioset -c gpiochip1 39=1 &

# 释放引脚（恢复为输入模式）
pkill gpioset
```

**定时驱动引脚，到时自动释放：**

```bash
# 高电平保持 2 秒后自动退出
gpioset --hold-period=2s -c gpiochip1 39=1
```

**周期翻转（示例：高 500 ms → 低 500 ms → 退出）：**

```bash
gpioset -t 500ms,500ms,0 -c gpiochip1 39=1
```

**监听引脚边沿（示例：引脚 11 → gpiochip2 line 23）：**

```bash
gpiomon -c gpiochip2 23               # 双边沿
gpiomon --edges=rising -c gpiochip2 23  # 仅上升沿
```

**扫描摄像头 I2C 总线（引脚 27/28，`/dev/i2c-2`）：**

```bash
i2cdetect -y 2
```

**PWM 输出（引脚 32 / BCM GPIO12 → `pwmchip0` 通道 0），1 kHz，50% 占空比：**

```bash
# 导出通道 0
echo 0 | sudo tee /sys/class/pwm/pwmchip0/export

# 设置周期 1 ms = 1000000 ns
echo 1000000 | sudo tee /sys/class/pwm/pwmchip0/pwm0/period

# 设置占空比 500 µs = 500000 ns
echo 500000 | sudo tee /sys/class/pwm/pwmchip0/pwm0/duty_cycle

# 使能
echo 1 | sudo tee /sys/class/pwm/pwmchip0/pwm0/enable
```

**SPI 回环测试（引脚 19 MOSI ↔ 引脚 21 MISO 短接，CS0 = 引脚 24）：**

> 前提条件：
> 1. extlinux.conf 使用 `microSD-periph` 条目（已启用 40-pin 外设模式 overlay）
> 2. 安装 `python3-spidev`：`sudo apt-get install -y python3-spidev`

```bash
sudo python3 - <<'EOF'
import spidev, sys

spi = spidev.SpiDev()
spi.open(0, 0)           # spi0, CS0
spi.max_speed_hz = 1_000_000
spi.mode = 0

tx = [0xAA, 0x55, 0x12, 0x34, 0xDE, 0xAD, 0xBE, 0xEF]
rx = spi.xfer2(tx)
spi.close()

print(f"TX: {[hex(b) for b in tx]}")
print(f"RX: {[hex(b) for b in rx]}")
if tx == rx:
    print("PASS: loopback 数据一致")
else:
    print("FAIL: 数据不一致")
    sys.exit(1)
EOF
```

验证设备节点是否已创建（外设模式启动后）：

```bash
ls /dev/spidev*          # 期望：/dev/spidev0.0
ls /sys/bus/spi/devices/ # 期望：spi0.0
```

---

## 10. 常见问题与技巧

### 启动后屏幕无显示

镜像默认关闭了 DPMS（显示器电源管理）。若屏幕黑屏，可按任意键或移动鼠标检查桌面管理器是否仍在运行。若问题持续，请检查：

```bash
cat /etc/X11/xorg.conf.d/10-no-dpms.conf
grep xserver-command /etc/lightdm/lightdm.conf
```

### 摄像头未被识别

```bash
# 检查 CSI 采集设备是否存在
v4l2-ctl --list-devices

# 查看媒体管道拓扑
media-ctl -d /dev/media0 --print-topology
```

若摄像头未列出，请确认 FPC 排线已完全插入接口且锁扣已锁紧。

### 启动时找不到 SD 卡

- 确认 SD 卡已完全插入（应听到咔哒声）。
- 更换其他 SD 卡，容量小于 16 GB 或速度低于 Class 10 的卡可能无法稳定工作。
- 重新烧录镜像并确认写入过程无错误。

### Wi-Fi 天线

板卡上的 U.FL 接口需外接天线才能获得可靠的 Wi-Fi 性能，不接天线时信号覆盖范围将非常有限。

