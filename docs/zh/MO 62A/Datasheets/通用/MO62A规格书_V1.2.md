<div style="width: 100%;height: 100%;background: url(images/62A.jpg); background-size: 100% 100%;">
  <div style="height:75%;">
    <div style="width:35%; padding: 40px 40px">
      <img src="images/logo.png" alt="logo" />
    </div>
    <div style="font-size: 28px; font-weight: bold; color:#000;text-align: center; margin-bottom: 60px;">
      拥抱边缘 AI，赋能智能视觉
    </div>
  </div>
  <div style="padding-left: 40px;">
    <div style="font-size: 40px; font-weight: bold; color:#000;margin-bottom: 30px;">
      MO 62A AI 单板计算机
    </div>
    <div style="text-align: center;">
      <div style="display: flex; flex-wrap: wrap; gap: 16px; ">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· 开放 SDK</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· Linux 发行版</div>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 16px;margin-top:16px">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· HAT 扩展接口</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px; ">· 边缘 AI</div>
      </div>
    </div>
  </div>
</div>

<div style="page-break-after: always;"></div>

# <span style="color: green;">1. 产品概述</span>

**MO 62A 是基于 TI AM62A74 SoC 的 2 TOPS 边缘 AI 单板计算机，兼容标准 SBC 外形规格，适用于 AI 视觉及边缘推理终端。**

**产品特点：**
- **AI 加速:** 内置 C7x DSP 与深度学习加速器，2 TOPS 端侧 AI 推理
- **SBC 兼容:** 标准 SBC 外形，兼容 HAT 扩展配件及主流外壳
- **丰富接口:** 千兆以太网、4×USB 2.0、micro HDMI、MIPI CSI-2
- **安全稳定:** 安全启动、TrustZone、OP-TEE、硬件加密加速器
- **开源生态:** Debian 13 Linux，开放 SDK，支持 TFLite/ONNX 模型

## <span style="color: green;">核心技术指标</span>

| 技术指标      | 规格                                       |
|---------------|--------------------------------------------|
| AI 推理       | 2 TOPS（C7x DSP + DLA）                    |
| 操作系统      | Debian 13.2（Linux 6.12）                  |
| Wi-Fi         | Wi-Fi 5 双频（802.11ac）                   |
| 蓝牙          | BLE 4.2                                    |
| AI 框架       | TI TIDL，支持 TFLite / ONNX                |
| 摄像头        | 1 × 4-lane MIPI CSI-2                      |
| 尺寸 (W × D)  | 85 × 56 mm                                 |
| 重量          | 47 g                                       |
| 供电          | USB Type-C 5V/5A DC                        |
| 功耗          | 25W（MAX）                                 |
| 工作温度      | 0 ~ 50 ℃                                   |
| 内存          | LPDDR4 4GB（默认）/ 2GB / 8GB              |

# <span style="color: green;">2. 产品尺寸</span>

<div style="display: flex; align-items: end; flex-wrap: wrap; justify-content: space-between;row-gap: 16px;">
  <div style="width: 45%;">
    <img src="images/prod_1.png" width="100%" alt="正视图" />
    <div style="width: 100%; text-align: center; font-size: 12px;">正视图</div>
  </div>
    <div style="width: 45%;">
    <img src="images/prod_3.png" width="100%" alt="侧视图" />
    <div style="width: 100%; text-align: center; font-size: 12px;">侧视图</div>
  </div>
  <div style="width: 25%;">
    <img src="images/prod_2.png" width="100%" alt="接口图" />
    <div style="width: 100%; text-align: center; font-size: 12px;">接口图</div>
  </div>

  <div style="width: 45%;">
    <div>注意：</div>
    <div>1.所有尺寸单位为毫米（mm）。</div>
    <div>2.所有尺寸均为近似值，<span style="font-weight: bold;">仅供参考</span>。</div>
    <div>3.图示尺寸<span style="font-weight: bold;">不得用于生产加工</span>。</div>
    <div>4.尺寸需符合零件及制造公差要求。</div>
    <div>5.尺寸如有变更，恕不另行通知。</div>
  </div>
</div>

# <span style="color: green;">3. 硬件规格</span>

| 类别/参数 | 规格 |
|--------------------------|------|
| <span style="color: green;">**硬件平台**</span> | |
| CPU | TI AM62A74，4 × Cortex-A53 @ 1.4 GHz |
| AI 加速器 | C7x DSP + Deep Learning Accelerator，2 TOPS |
| ISP / 视觉 | On-chip ISP + VPAC（RGB-IR，WDR，LDC） |
| RAM | LPDDR4 4GB（默认）/ 2GB / 8GB |
| <span style="color: green;">**连接与联网**</span> | |
| 以太网 | 1 × 千兆以太网 |
| USB | 4 × USB 2.0 Type-A |
| 显示 | 1 × micro HDMI |
| 摄像头 | 1 × 4-lane MIPI CSI-2 |
| 音频 | 3.5 mm 接口 + PCM（经 40-pin 连接器引出） |
| 40-pin 连接器 | GPIO / I²C / SPI / UART / PCM，HAT-compatible |
| 存储 | Micro SD |
| 调试串口 | 1 × TTL UART |
| 风扇接口 | 1 × 4-pin 风扇接口 |
| 按键 | 1 × 复位键 |
| LED | PWR，USER |
| <span style="color: green;">**无线**</span> | |
| Wi-Fi | Wi-Fi 5（802.11ac），双频 |
| 蓝牙 | BLE 4.2 |
| 天线接口 | Wi-Fi / BLE：板载扣式天线 |
| <span style="color: green;">**电源与功耗**</span> | |
| 输入电源 | USB Type-C 5V/5A DC |
| 功耗 | 25W（MAX） |
| <span style="color: green;">**机械特性**</span> | |
| 尺寸 (W × D) | 85 × 56 mm |
| 重量 | 47 g |
| 外壳 | PCB |
| 散热 | 主动风扇（可选） |
| RTC | 支持（带电池备份）|
| <span style="color: green;">**环境温度**</span> | |
| 工作温度 | 0 ~ 50 ℃ |
| 存储温度 | -20 ~ 70 ℃ |

# <span style="color: green;">4. 软件规格</span>

| 类别/参数 | 规格 |
|--------------------------|------|
| <span style="color: green;">**操作系统**</span> | |
| 系统 | Debian 13.2 Trixie |
| 内核 | Linux Kernel 6.12 |
| <span style="color: green;">**AI 与视觉**</span> | |
| AI 运行时 | TI TIDL，supports TFLite / ONNX |
| 视觉 SDK | TI EdgeAI SDK |
| 摄像头框架 | V4L2 |
| 显示框架 | DRM / KMS |
| <span style="color: green;">**网络特性**</span> | |
| IP 应用 | TCP/UDP，ICMP，DNS，DHCP |
| IP 路由 | 静态路由 |
| <span style="color: green;">**安全性**</span> | |
| 安全启动 | 支持 |
| TrustZone | 支持 |
| OP-TEE | 支持 |
| 加密加速器 | Hardware AES-256 |
| <span style="color: green;">**开发**</span> | |
| 语言 | Python，C/C++ |
| 库 | OpenCV，GStreamer，NumPy |
| 包管理器 | apt（Debian） |
| 开放 SDK | 支持客户自定义系统构建 |
| <span style="color: green;">**系统管理**</span> | |
| 远程访问 | SSH |
| 固件升级 | SD 卡烧录 |
| 调试 | UART 控制台 |

# <span style="color: green;">5. 订购信息</span>

## <span style="color: green;">型号规则</span>

**Model code:** MO-62A-\<x\>

\<x\>: 内存

## <span style="color: green;">产品型号</span>

| 基础型号 | -x | 内存 |
|---------|-------|-----------|
| MO-62A | 2G | 2GB |
| MO-62A | 4G | 4GB |
| MO-62A | 8G | 8GB |

**示例**<br/>
型号：MO-62A-4G<br/> 
“MO-62A” 为基础型号。<br/>
“–4G”  代表 4GB 内存。

# <span style="color: green;">6. 联系我们</span>

- **官网：** [映翰通官网](https://www.inhand.com.cn)
- **版权声明：** ©映翰通网络 保留所有权利
