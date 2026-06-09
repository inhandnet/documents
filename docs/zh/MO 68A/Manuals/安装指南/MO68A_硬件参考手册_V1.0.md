# MO68A 硬件参考手册

**版本 1.0 · 北京映翰通网络技术股份有限公司**

---

本文档从硬件角度归纳 MO68A 的系统构成、电源与启动关系、板载外设接口及扩展连接器定义，并给出关键器件索引（角色等同于面向开发的「硬件接口说明」）。行文以客观说明为主；在涉及选型与接线时补充面向使用者的注意点。

MO68A 是一款基于 TDA4VE / AM68A SoC（TI J721S2 系列）的单板计算机，具有双 Cortex-A72 CPU、最多六个 Cortex-R5F 实时核以及 8 TOPS AI 加速器。

**来源权威性。** 本文档中所有连接器引脚定义和信号分配均来源于 SysConfig 引脚复用文件（`Mo68A-V4.0.syscfg`）。部分外设分配可能尚未反映在 SysConfig 中；BSP 源代码是当前软件状态的最终参考。

---

## 本页导航

| 章节 | 内容摘要 |
| --- | --- |
| [接口一览（快速对照）](#接口一览快速对照) | 按使用目的查找应连接的物理接口 |
| [板卡布局](#板卡布局) | 连接器与元件在 PCB 上的位置 |
| [系统框图](#系统框图) | 整板功能模块关系 |
| [SoC 概述](#soc-概述) | SoC 功能框图与主要参数 |
| [I2C 总线树](#i2c-总线树) | I2C 拓扑示意 |
| [电源供应](#电源供应) | USB-C 供电与上电时序 |
| [启动配置](#启动配置) | SD 与以太网启动行为 |
| [存储](#存储) | LPDDR4、eMMC 占位、Micro SD |
| [板载接口](#板载接口) | 各连接器电气与引脚说明 |
| [扩展接口（40-pin）](#扩展接口40-pin) | GPIO 排针功能表 |
| [指示灯、复位与串口调试](#指示灯复位与串口调试) | LED、SW1、UART 调试座 |
| [板载集成电路与外设摘要](#板载集成电路与外设摘要) | Hub、PHY、RTC、EEPROM |
| [关键器件参考](#关键器件参考) | 主要芯片型号索引 |
| [机械尺寸](#机械尺寸) | PCB 与 HAT 封装参照 |
| [相关文档与资源](#相关文档与资源) | 与快速入门、用户指南的交叉引用 |

---

## 接口一览（快速对照）

若需先建立「该接哪里」的整体印象，可按下表从使用场景定位接口；细述见后文对应小节。

| 使用意图 | 建议连接的接口 | 补充说明 |
| --- | --- | --- |
| 上电运行 | USB Type-C（J5） | **5 V**，适配器建议具备 **≥ 5 A** 持续输出能力（≈27 W） |
| 本地显示 | Mini DisplayPort（J9） | 需 **DisplayPort** 显示器；不直接支持 HDMI |
| 有线网络 | RJ45（J1） | **10/100/1000 Mbps** 自协商 |
| USB 外设 | USB 3.0 Type-A（J2、J3） | 各组 2 口，经板载 **USB 3.0 Hub** |
| MIPI 摄像头或 DSI 显示 | MIPI0（J24）、MIPI1（J25） | **22-pin FPC**；CSI-2 与 DSI 由硬件配置选择 |
| PCIe / NVMe 扩展 | PCIe Gen3 FPC（J10） | **PCIe Gen3 ×1**；详见板载接口小节 |
| 树莓派 HAT / GPIO | 40-pin（J11） | **3.3 V** 逻辑，**不兼容 5 V** |
| 主动散热 | 风扇连接器（J7） | **5 V**、**4-pin PWM**；热管理必要条件 |
| RTC 掉电保持 | RTC 电池连接器（J8） | **CR2032** 等，连接器规格见下文 |
| PoE 受电 | PoE HAT 连接器（J4） | 需 **单独 PoE 扩展板**；RJ45 本体不提供 PoE |
| 串口控制台 / 无显示器排障 | UART 调试（J6） | **115200 8N1**，**3.3 V** |
| 系统存储与启动 | Micro SD（J23） | **MMC1**，主要启动介质 |

---

## 板卡布局

![MO68A 板卡布局](images/MO68A_label.png)

| 连接器 / 组件 | 标识符 | 位置 |
| --- | --- | --- |
| 40-pin HAT 连接器 | J11 | 顶部边缘，左侧 |
| 风扇连接器 | J7 | 顶部边缘，右侧 |
| TDA4VE / AM68A SoC | — | 板卡中央 |
| LPDDR4 8 GB | — | 左侧区域 |
| PCIe Gen3 FPC | J10 | 左侧边缘，上方 |
| Micro SD 插槽 | J23 | 左侧边缘，中部 |
| 复位按钮 | SW1 | 左侧区域，中部 |
| LED | D1 | 左侧区域，下方 |
| USB-C 电源 | J5 | 底部边缘，最左侧 |
| RTC 电池连接器 | J8 | 底部边缘，左侧 |
| Mini DisplayPort | J9 | 底部边缘，左中 |
| UART 调试接口 | J6 | 底部边缘，中央 |
| MIPI0 22-pin FPC | J24 | 底部边缘，中右 |
| MIPI1 22-pin FPC | J25 | 底部边缘，右侧 |
| PoE HAT 连接器 | J4 | 底部区域，最右侧 |
| USB 3.0 × 2 | J3 | 右侧边缘，上组 |
| USB 3.0 × 2 | J2 | 右侧边缘，下组 |
| 千兆以太网 | J1 | 右侧边缘，下方 |

---

## 系统框图

![MO68A 系统框图](images/MO68A_Block_Diagram.png)

主要子系统及其互联关系：

| 子系统 | 与 SoC 的接口 |
| --- | --- |
| LPDDR4 8 GB | DQ×32（DDRSS0） |
| Micro SD 卡 | MMC1 |
| Mini DisplayPort | SERDES0 DP 通道（2 通道 DP0） |
| USB 3.0 Hub（TUSB8041） | USB2.0 + SERDES0 USB3.0 SS |
| 千兆以太网（DP83867） | MCU RGMII1 |
| MIPI FPC × 2 | DSI0/CSI0、DSI1/CSI1（可切换） |
| PCIe Gen3 FPC | SERDES0 PCIe x1（PCIE1） |
| 40-pin GPIO 扩展口 | SOC I2C0、WKUP I2C0、UART5、SPI5、I2S、GPIO |
| RTC（PCF85263ATL） | SOC I2C1（0x51） |
| 板载 EEPROM（BL24C02F） | SOC I2C1（0x50） |
| USB-C（电源） | USB0 |
| 调试 UART（J6） | UART8 |
| 风扇 | PWM + TACH |

---

## SoC 概述

### 功能框图

![AM68A 功能框图](images/AM68A_Block_Diagram.png)

### 主要参数

| 参数 | 值 |
| --- | --- |
| SoC | TDA4VE / AM68A（J721S2 系列） |
| 应用 CPU | 2× ARM Cortex-A72，最高 2.0 GHz |
| AI 加速器 | MMA（矩阵乘法加速器），8 TOPS |
| MCU 子系统 | 最多 6× ARM Cortex-R5F，最高 1.0 GHz |
| 内存接口 | LPDDR4，32 位总线 |
| 连接性 | 1× USB 3.0（SERDES）、1× PCIe Gen3 x1（SERDES）、2× MIPI CSI-2/DSI、1× DisplayPort（SERDES）、RGMII |
| 封装 | FCBGA |

如需完整的 SoC 文档，请参阅 TI J721S2 技术参考手册（SPRUJ28）。

---

## I2C 总线树

![MO68A I2C 总线树](images/MO68A_I2C_Tree.png)

---

## 电源供应

### USB-C 供电端口

电源仅通过 **USB-C** 接口（**J5**）输入。

| 参数 | 值 |
| --- | --- |
| 输入电压 | 5 V |
| 额定功率 | 27 W |
| 所需适配器电流 | 最低 **5 A** |
| 连接器 | USB Type-C（J5） |

USB-C 接口承载板卡电源。若在 **5 V、电流不足** 的条件下长期使用，可能出现复位、存储写入失败或过热等风险。USB-C 电源适配器建议在**其余外设连接完毕后再接通**。

### 上电时序

上电时序由 PMIC（TPS6594）管理。复位 IC（TPS380833）提供干净的 PMIC_ENABLE 信号。

---

## 启动配置

| 参数 | 值 |
| --- | --- |
| 主启动设备 | Micro SD 卡（MMC1） |
| 备用启动设备 | RGMII（以太网） |
| 启动模式引脚 | 出厂时通过电阻跳线固定设置 |

启动模式电阻在出厂时焊接，现场无法更改。主要启动路径为 SD 卡；如未检测到有效 SD 卡，SoC ROM 将尝试通过 RGMII 进行网络启动。

---

## 存储

### LPDDR4

| 参数 | 值 |
| --- | --- |
| 容量 | 8 GB |
| 器件 | Micron MT53E2G32D4DE-046 |
| 总线宽度 | 32 位（×32） |
| 接口 | SoC 上的 DDRSS0 |
| 电压 | DDR_1V1 |

### eMMC

未焊接 eMMC。SoC 上的 MMC0 接口未连接。

### Micro SD 卡

Micro SD 插槽（**J23**）连接至 SoC 上的 **MMC1**。它是主要启动介质，也是板卡上主要的可更换非易失性用户存储。连接器电气规格见 [Micro SD 卡槽（J23）](#micro-sd-卡槽j23)。

---

## 板载接口

### 电源输入 — USB-C（J5）

| 参数 | 值 |
| --- | --- |
| 连接器 | USB Type-C，16-pin |
| 电压 | 5 V |
| 电流 | 5 A（需 27 W 适配器） |

---

### Micro SD 卡槽（J23）

| 参数 | 值 |
| --- | --- |
| 连接器 | MUF-M614 推推式 Micro SD |
| SoC 接口 | MMC1（4 位） |
| 电压 | 3V3_SD（负载切换） |

SD 插槽是板卡上唯一可用户频繁更换的大容量存储接口，也是主要启动介质。

---

### Mini DisplayPort（J9）

| 参数 | 值 |
| --- | --- |
| 连接器 | Mini DisplayPort（20-pin），沉板/凹入式 |
| SoC 接口 | 经 SERDES0 的 DP0（2 通道） |
| HPD | DP0_HPD（MCASP1_ACLKX，焊球 AA24） |
| 电源 | 3V3_DP（负载切换，500 mA） |

显示输出需要 **DisplayPort** 显示器。不直接支持 HDMI 显示器。

| J9 信号 | SoC 信号 | 焊球 |
| --- | --- | --- |
| DP_TX0_P | SERDES0_TX2_P → DP0_TXP0 | AG6 |
| DP_TX0_N | SERDES0_TX2_N → DP0_TXN0 | AG5 |
| DP_TX1_P | SERDES0_TX3_P → DP0_TXP1 | AD8 |
| DP_TX1_N | SERDES0_TX3_N → DP0_TXN1 | AD7 |
| DP_AUX_P | DP0_AUX_P | — |
| DP_AUX_N | DP0_AUX_N | — |
| DP_HPD | DP0_HPD（MCASP1_ACLKX） | AA24 |

---

### USB 3.0 Type-A × 4（J2、J3）

| 参数 | 值 |
| --- | --- |
| 连接器 | J2（下组）、J3（上组），各 2 口 |
| USB Hub | TUSB8041（1× 上行，4× 下行） |
| SuperSpeed 通道 | SERDES0_TX1/RX1 → USB3.0 SS 至 Hub 上行 |
| Hi-Speed | USB0（USB2.0）至 Hub 上行 |
| 口电源 | 5V_TypeA 经 TPS2561，4 口总计最高 3.6 A |
| 过流保护 | 每口独立（PWRCTL、OVERCUR 信号） |

TUSB8041 提供：

- 4× USB 3.0 Gen1（5 Gbps）下行口
- 每口独立电源切换及过流检测

---

### 千兆以太网（J1）

| 参数 | 值 |
| --- | --- |
| 连接器 | 带集成磁性元件的 RJ45 |
| PHY | DP83867 |
| SoC 接口 | MCU RGMII1 |
| 速率 | 10/100/1000 Mbps，自动协商 |
| PHY MDIO 地址 | 0x00 |
| LED0 | 链路指示灯 |
| LED1 | 活动指示灯 |
| PoE | 可用抽头点（J4，参见 [PoE HAT 连接器（J4）](#poe-hat-连接器j4)） |

---

### MIPI 摄像头 / 显示 FPC — MIPI0（J24）与 MIPI1（J25）

两个 MIPI FPC 连接器均为 **22-pin、0.5 mm 间距**。每个连接器可通过 GPIO（OE/SEL）控制的零欧电阻跳线配置为 MIPI CSI-2 摄像头输入或 MIPI DSI 显示输出。

| 参数 | J24（MIPI0） | J25（MIPI1） |
| --- | --- | --- |
| 连接器 | 22-pin FPC，0.5 mm | 22-pin FPC，0.5 mm |
| CSI-2 来源 | CSI0（4 通道，2.5 Gbps/通道） | CSI1（4 通道，2.5 Gbps/通道） |
| DSI 来源 | DSI0（4 通道） | DSI1（4 通道） |
| I2C 总线 | SOC_I2C5（Y24/SCL，W23/SDA） | SOC_I2C5（Y24/SCL，W23/SDA） |
| 电源 | 3V3_EXP | 3V3_EXP |
| SEL GPIO | WKUP_GPIO0_36（OE），WKUP_GPIO0_37（SEL） | WKUP_GPIO0_33（OE），WKUP_GPIO0_32（SEL） |
| PWDN GPIO | GPIO0_47 | GPIO0_48 |

**FPC 引脚定义（22-pin）：**

| 引脚 | 信号 | 方向 |
| --- | --- | --- |
| 1 | GND | — |
| 2 | DSICSI_D0_N | 差分（数据通道 0） |
| 3 | DSICSI_D0_P | 差分（数据通道 0） |
| 4 | GND | — |
| 5 | DSICSI_D1_N | 差分（数据通道 1） |
| 6 | DSICSI_D1_P | 差分（数据通道 1） |
| 7 | GND | — |
| 8 | DSICSI_CLK_N | 差分（时钟） |
| 9 | DSICSI_CLK_P | 差分（时钟） |
| 10 | GND | — |
| 11 | DSICSI_D2_N | 差分（数据通道 2） |
| 12 | DSICSI_D2_P | 差分（数据通道 2） |
| 13 | GND | — |
| 14 | DSICSI_D3_N | 差分（数据通道 3） |
| 15 | DSICSI_D3_P | 差分（数据通道 3） |
| 16 | GND | — |
| 17 | I2C_SCL | 3.3 V 开漏 |
| 18 | I2C_SDA | 3.3 V 开漏 |
| 19 | GPIO（PWDN / REFCLK） | 3.3 V GPIO |
| 20 | GPIO（RESET） | 3.3 V GPIO |
| 21 | GND | — |
| 22 | 3V3_EXP | 电源（3.3 V） |

---

### PCIe Gen3 FPC（J10）

| 参数 | 值 |
| --- | --- |
| 连接器 | 16-pin FPC，1.0 mm 间距 |
| SoC 接口 | PCIe Gen3 × 1 通道（PCIE1，SERDES0 通道 0） |
| 电源 | VCC_IN_5V |
| 参考时钟 | PCIE_REFCLK1_P/N |

**信号摘要：**

| 引脚组 | 信号 | 备注 |
| --- | --- | --- |
| 电源 | VCC_IN_5V | PCIe 设备 5 V 供电 |
| GND | — | 多个地引脚 |
| TX | PCIE1_TXP0，PCIE1_TXN0 | Gen3，8 GT/s |
| RX | PCIE1_RXP0，PCIE1_RXN0 | Gen3，8 GT/s |
| REFCLK | PCIE_REFCLK1_P，PCIE_REFCLK1_N | 250 MHz 差分时钟 |
| PWEN | GPIO0_11（V23） | PCIe 设备电源使能 |
| DET/WAKE | GPIO0_12（T26） | 设备检测 / 唤醒 |
| RST | GPIO0_19（V27） | 复位（低有效） |
| CLKREQ# | PCIE1_CLKREQN | — |

---

### RTC 电池连接器（J8）

| 参数 | 值 |
| --- | --- |
| 连接器 | SH1.0，2-pin（1.0 mm 间距） |
| RTC 芯片 | PCF85263ATL |
| 电池 | CR2032，2-pin JST-SH（1.0 mm 间距） |

**引脚定义：**

| 引脚 | 信号 |
| --- | --- |
| 1 | BAT+（电池正极） |
| 2 | GND |

在板卡断电时，只要连接了电池，RTC 即可保持时间。PCF85263ATL 通过 SOC I2C1（I2C1_SCL：AC25，I2C1_SDA：AD26）与 SoC 通信，I2C 地址 **0x51**。

---

### PoE HAT 连接器（J4）

| 参数 | 值 |
| --- | --- |
| 连接器 | 2 × 2，2.54 mm 间距 |
| 用途 | 以太网变压器中心抽头，用于 PoE 扩展板的被动抽取 |

J4 提供来自 RJ45 变压器的四个中心抽头信号（TR0–TR3）。需要单独的 PoE 扩展板才能从这些抽头提取电源。**RJ45 连接器（J1）本身不提供 PoE 供电。**

---

### 风扇连接器（J7）

| 参数 | 值 |
| --- | --- |
| 连接器 | SH1.0，4-pin（1.0 mm 间距） |
| 风扇电压 | 5 V（VCC_IN_5V） |
| PWM 控制 | PWM1_B（GPIO0_29，R28）经 SN74LVC1T45 电平转换器 |
| 转速计 | TIMER_IO1（AG25）经 MOSFET Q7（NX8008NBKWX） |

**引脚定义：**

| 引脚 | 信号 | 描述 |
| --- | --- | --- |
| 1 | 5V | 风扇电源（5 V） |
| 2 | PWM | 风扇转速控制（PWM） |
| 3 | GND | 地 |
| 4 | TACH | 风扇转速计输入 |

需使用 **5 V 4-pin PWM** 风扇。PWM 频率和占空比由软件控制。连接风扇是**热管理必要条件**；在没有风扇的情况下运行可能导致降频或损坏。

---

## 扩展接口（40-pin）

**连接器（J11）**

| 参数 | 值 |
| --- | --- |
| 连接器 | 2 × 20，2.54 mm 间距，通孔 |
| IO 电压 | 3.3 V（VDDSHV 域），**不兼容 5 V** |
| 电源供应 | 3V3_EXP（负载切换，4 A 总量与 MIPI FPC 共享） |

> **注意：** 此扩展口上的三个 GPIO 信号属于 WKUP 域（MCU 子系统）。相对于主域 GPIO，它们在掉电和睡眠状态下的行为有所不同。

扩展口遵循树莓派 40-pin HAT 机械封装和引脚编号。SoC 信号分配与树莓派不同。

**40-pin 信号图：**

奇数引脚（左列），偶数引脚（右列）。括号内为焊球编号；WKUP 域引脚标注 †。

| 功能（奇数引脚） | 引脚 | | 引脚 | 功能（偶数引脚） |
| ---:|:---:|:---:|:---:|:---|
| 3.3 V | 1 | | 2 | 5.0 V |
| I2C0_SDA（AE24） | 3 | | 4 | 5.0 V |
| I2C0_SCL（AH25） | 5 | | 6 | GND |
| AUDIO_CLK / GPIO0_30（Y25） | 7 | | 8 | UART5_TXD（W25） |
| GND | 9 | | 10 | UART5_RXD（AC24） |
| WKUP_GPIO0_60（E27）† | 11 | | 12 | I2S_CLK（AB28） |
| GPIO0_0（AG24） | 13 | | 14 | GND |
| WKUP_GPIO0_61（E28）† | 15 | | 16 | GPIO0_27（V26） |
| 3.3 V | 17 | | 18 | GPIO0_51（AE27） |
| SPI5_MOSI（R27） | 19 | | 20 | GND |
| SPI5_MISO（AD27） | 21 | | 22 | WKUP_GPIO0_70（B26）† |
| SPI5_CLK（T27） | 23 | | 24 | SPI5_CS0（U28） |
| GND | 25 | | 26 | SPI5_CS1（W28） |
| WKUP_I2C0_SDA（H27）† | 27 | | 28 | WKUP_I2C0_SCL（H24）† |
| GPIO0_18（AB27） | 29 | | 30 | GND |
| GPIO0_33（AA28） | 31 | | 32 | PWM / ECAP0（AB26） |
| PWM5_B / GPIO0_32（U26） | 33 | | 34 | GND |
| I2S_FS（U27） | 35 | | 36 | GPIO0_10（AB24） |
| GPIO0_9（Y28） | 37 | | 38 | I2S_DIN（AC28） |
| GND | 39 | | 40 | I2S_DOUT（Y26） |

**可用接口摘要：**

| 接口 | 引脚 | 备注 |
| --- | --- | --- |
| I2C（SOC） | 3、5 | SOC 域 I2C0 |
| I2C（WKUP） | 27、28 | WKUP 域 I2C0；与 PMIC 共享 |
| UART | 8、10 | UART5，全双工 |
| SPI | 19、21、23、24、26 | SPI5（MOSI、MISO、CLK、CS0、CS1） |
| I2S | 12、35、38、40 | MCASP0（CLK、FS、DIN、DOUT） |
| PWM | 32、33 | 引脚 33（PWM5_B，U26）：经 pwmchip1 ch1 可用；引脚 32（ECAP0，AB26）：已布线但内核设备树中无节点 |
| GPIO（SOC） | 7、13、16、18、29、31、33、36、37 | 主域 GPIO0 |
| GPIO（WKUP） | 11、15、22 | MCU 子系统 GPIO，深度睡眠时仍保持活动 |

---

## 指示灯、复位与串口调试

### LED 指示灯（D1）

D1 为双色 LED（KL-3210URSYGC）。

| 颜色 | 功能 | 控制 GPIO | 焊球 |
| --- | --- | --- | --- |
| 红色 | 电源 / 启动指示 | WKUP_GPIO0_4 | C23 |
| 绿色 | 系统状态 | WKUP_GPIO0_5 | F26 |

正常工作状态：Linux 启动完成、系统运行后 LED 变为**绿色常亮**。启动过程中 LED 为红色。LED 行为详见《MO68A 用户指南》。

### 复位按钮（SW1）

SW1 是一个触觉按钮，用于控制 PMIC_ENABLE。按下 SW1 将启动系统复位。复位 IC（TPS380833）提供经消抖的受控释放复位脉冲。

> SW1 触发完整的系统复位，包括 SoC、DDR 和所有电源轨，相当于重新上电。

### UART 调试控制台（J6）

| 参数 | 值 |
| --- | --- |
| 连接器 | SH1.0，3-pin（1.0 mm 间距） |
| UART | UART8（SOC 域） |
| 波特率 | 115200 |
| 帧格式 | 8N1，无流控 |
| 逻辑电平 | 3.3 V |

**引脚定义：**

| 引脚 | 信号 | 焊球 | 描述 |
| --- | --- | --- | --- |
| 1 | RXD | AF26 | SoC 接收（连接至适配器 TX） |
| 2 | GND | — | 地 |
| 3 | TXD | AH27 | SoC 发送（连接至适配器 RX） |

需使用 **3.3 V** USB 转 UART 适配器。在接通电源**之前**连接串口终端，以捕获完整的早期启动输出。

UART8 用于 Linux 系统控制台输出，提供独立于显示器的登录终端。

---

## 板载集成电路与外设摘要

### USB 3.0 Hub — TUSB8041

TUSB8041 是 USB 3.0 Gen1（5 Gbps）4 口 Hub。它从 SoC 接收 USB2.0（Hi-Speed）和 USB3.0 SuperSpeed，并在 J2 和 J3 上提供四个 USB 3.0 下行口。

- 每口独立电源切换
- 每口过流检测

### 千兆以太网 PHY — DP83867

DP83867 PHY 通过带集成磁性元件的 RJ45 接口将 SoC 的 MCU RGMII1 接口连接到网口。关键配置：

- PHY 地址：0x00
- 已启用自动协商
- LED0：链路，LED1：活动

### RTC — PCF85263ATL

PCF85263ATL 实时时钟使用 32.768 kHz 晶振提供精准计时，连接至 SOC I2C1 总线。

- I2C 总线：SOC_I2C1，地址 **0x51**
- SCL 焊球：AC25，SDA 焊球：AD26
- 通过 J8 电池备份（CR2032，2-pin JST-SH，1.0 mm 间距）

### 板卡 ID EEPROM — BL24C02F

I2C EEPROM 存储板卡标识和制造数据。

| 参数 | 值 |
| --- | --- |
| I2C 总线 | SOC I2C1（SCL：AC25，SDA：AD26），地址 **0x50** |
| 写保护 | 写入前 WP 引脚须拉低 |

---

## 关键器件参考

| 器件 | 型号 | 接口 | 备注 |
| --- | --- | --- | --- |
| SoC | TDA4VE / AM68A（J721S2） | — | 2× A72，8 TOPS |
| LPDDR4 | Micron MT53E2G32D4DE-046 | DDRSS0 ×32 位 | 共 8 GB |
| PMIC | TPS6594 系列 | WKUP I2C0 | 多路电源管理 |
| CPU 电源 | TPS62871（HCPS-A） | — | VDD_CPU_AVS，8 A |
| 核心电源 | TPS62871 × 2（HCPS-B） | — | VDD_CORE_0V8，8 A |
| 3.3V DC-DC | TPS62A06 | — | 6 A，主 3.3 V 轨 |
| USB 电源切换 | TPS2561 | — | 5V_TypeA，3.6 A |
| USB 3.0 Hub | TUSB8041 | USB3.0 SS + USB2.0 HS | 4 口，Gen1 5 Gbps |
| GbE PHY | DP83867 | MCU RGMII1 | 10/100/1000 Mbps |
| RTC | PCF85263ATL | SOC I2C1（0x51） | 电池备份 |
| 板卡 EEPROM | BL24C02F | SOC I2C1（0x50） | 板卡 ID |
| 风扇 PWM 转换器 | SN74LVC1T45 | GPIO/PWM | PWM 电平转换 |
| 风扇 TACH 开关 | NX8008NBKWX（Q7） | TIMER_IO1 | TACH 信号调理 |
| 复位 IC | TPS380833 | — | PMIC_ENABLE 控制 |

---

## 机械尺寸

板卡外形、孔位及器件禁布区请参阅 PCB 布局图 `MO68A_MB_FAB_V1.0.pdf`。

40-pin HAT 连接器（J11）遵循树莓派 40-pin HAT 机械封装。

---

## 相关文档与资源

| 文档 / 资源 | 说明 |
| --- | --- |
| [MO68A 快速入门指南](MO68A_快速入门指南_V1.0.md) | 初始设置、烧录、首次登录 |
| [MO68A 用户指南](MO68A_用户指南_V1.0.md) | 接口使用、外设配置、系统管理 |

---

## 修订历史

| 版本 | 日期 | 描述 |
| --- | --- | --- |
| 1.0 | 2026-04-27 | 初始发布。 |
