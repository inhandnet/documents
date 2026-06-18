<div style="width: 100%;height: 100%;background: url(images/68A.jpg); background-size: 100% 100%;">
  <div style="height:75%;">
    <div style="width:35%; padding: 40px 40px">
      <img src="images/logo.png" alt="logo" />
    </div>
    <div style="font-size: 28px; font-weight: bold; color:#000;text-align: center; margin-bottom: 60px;">
      Embrace Edge AI, Empower Intelligent Vision
    </div>
  </div>
  <div style="padding-left: 40px;">
    <div style="font-size: 40px; font-weight: bold; color:#000;margin-bottom: 30px;">
      MO 68A AI Single Board Computer
    </div>
    <div style="text-align: center;">
      <div style="display: flex; flex-wrap: wrap; gap: 16px; ">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· Open SDK</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· Linux Distribution</div>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 16px;margin-top:16px">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· HAT Expansion</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px; ">· Edge AI</div>
      </div>
    </div>
  </div>
</div>

<div style="page-break-after: always;"></div>

# <span style="color: green;">1. Product Overview</span>

**The MO-68A is an 8 TOPS edge AI single-board computer based on the TI AM68A SoC, designed for AI vision boxes, intelligent cameras, and edge AI inference terminals.**

**Product Features:**
- **Edge AI Acceleration:** 8 TOPS on-device AI inference with TI TIDL runtime supporting TFLite / ONNX
- **Complete Vision Pipeline:** Dual 4-lane MIPI CSI-2, VPAC, DMPAC, 4K@60fps H.265 / H.264 codec
- **Rich Interfaces:** Gigabit Ethernet, PCIe 3.0, 4 × USB 3.0, mini DP, 40-pin HAT connector
- **SBC Ecosystem:** Standard form factor, Debian 13 Trixie, open SDK, Python / C / C++
- **High Security:** Secure Boot, TrustZone, OP-TEE, hardware crypto accelerator

## <span style="color: green;">Core Technical Specification</span>

| Technical Indicator | Specification |
|---|---|
| OS | Debian 13 (Embedded Linux) |
| AI Accelerator | 2 x C7 x DSP + Deep Learning Accelerator, 8 TOPS |
| AI Runtime | TI TIDL, supports TFLite / ONNX |
| Vision | VPAC, DMPAC, 4K@60fps H.265 / H.264 codec |
| Security | Secure Boot, TrustZone, OP-TEE, Hardware AES-256 |
| Development | Python, C/C++, OpenCV, GStreamer |
| CPU | 2 × Cortex-A72 @ 2.0 GHz |
| RAM | LPDDR4 4 GB / 8 GB (default) |
| Interface | 1 × GbE, 4 × USB 3.0, PCIe 3.0, mini DP, MIPI DSI/CSI-2 |
| Power | USB Type-C 5 V / 5 A DC; ≤ 25 W |
| Dimensions (W × D × H) | 85 × 56 mm |
| Operating Temperature | 0 °C ~ +50 °C |

# <span style="color: green;">2. Product Dimensions</span>

<div style="display: flex; align-items: end; flex-wrap: wrap; justify-content: space-between;row-gap: 16px;">
  <div style="width: 45%;">
    <img src="images/prod_1.png" width="100%" alt="Top View" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Top View</div>
  </div>
  <div style="width: 45%;">
    <img src="images/prod_3.png" width="100%" alt="Product View" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Side View</div>
  </div>
  <div style="width: 25%;">
    <img src="images/prod_2.png" width="100%" alt="Front / Back View" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Interface View</div>
  </div>
  
  <div style="width: 45%;">
    <div>Note:</div>
    <div>1. All dimensions are in millimeters (mm).</div>
    <div>2. All dimensions are approximate values for <span style="font-weight: bold;">reference only</span>.</div>
    <div>3. The dimensions shown <span style="font-weight: bold;">shall not be used for production or processing</span>.</div>
    <div>4. Dimensions shall comply with part and manufacturing tolerance requirements.</div>
    <div>5. Dimensions are subject to change without notice.</div>
  </div>
</div>

# <span style="color: green;">3. Hardware Specifications</span>

| Category / Parameter | Specification |
|--------------------------|------|
| <span style="color: green;">**Hardware Platform**</span> | |
| CPU | TI AM68A, 2 × Cortex-A72 @ 2.0 GHz |
| AI Accelerator | 2 x C7 x DSP + Deep Learning Accelerator, 8 TOPS |
| ISP / Vision | On-chip ISP + VPAC (RGB-IR, WDR, LDC) |
| RAM | LPDDR4 4 GB / 8 GB (default) |
| <span style="color: green;">**Interface**</span> | |
| Ethernet | 1 × Gigabit Ethernet |
| USB | 4 × USB 3.0 Type-A |
| PCIe | 1 × PCIe 3.0 |
| Display | 1 × mini DP + up to 2 × 4-lane MIPI DSI |
| Camera | up to 2 × 4-lane MIPI CSI-2 |
| Audio | I²S via 40-pin connector |
| 40-pin Connector | GPIO / I²C / I²S / SPI / UART / PCM, HAT-compatible |
| Fan Connector | 1 × 4-pin fan connector (5 V, PWM, GND, TACH) |
| Button | 1 × Reset button |
| Storage | Micro SD |
| Debug | 1 × TTL UART |
| LED | PWR, STATUS |
| <span style="color: green;">**Power**</span> | |
| Power Input | USB Type-C 5 V / 5 A DC |
| Power Consumption | 25 W (MAX) |
| <span style="color: green;">**Mechanical**</span> | |
| Dimensions (W × D × H) | 85 × 56 mm |
| Weight | 53 g |
| Housing | PCB |
| Cooling | Active fan (optional) |
| RTC | Support (battery backup) |
| <span style="color: green;">**Environmental**</span> | |
| Operating Temperature | 0 °C ~ +50 °C |
| Storage Temperature | -20 °C ~ +70 °C |


# <span style="color: green;">4. Software Specifications</span>

| Category / Parameter | Specification |
|--------------------------|------|
| <span style="color: green;">**Operating System**</span> | |
| OS | Debian 13 Trixie |
| Kernel | Linux Kernel 6.12 |
| <span style="color: green;">**AI & Vision**</span> | |
| AI Runtime | TI TIDL, supports TFLite / ONNX |
| Vision SDK | TI EdgeAI SDK |
| Camera Framework | V4L2 |
| Display Framework | DRM / KMS |
| <span style="color: green;">**Network Features**</span> | |
| IP Application | TCP / UDP, ICMP, DNS, DHCP |
| IP Routing | Static routing |
| <span style="color: green;">**Security**</span> | |
| Secure Boot | Support |
| TrustZone | Support |
| OP-TEE | Support |
| Crypto Accelerator | Hardware AES-256 |
| <span style="color: green;">**Development**</span> | |
| Languages | Python, C/C++ |
| Libraries | OpenCV, GStreamer, NumPy |
| Package Manager | apt (Debian) |
| Open SDK | Supports custom system build by customer |
| <span style="color: green;">**System Management**</span> | |
| Remote Access | SSH |
| Firmware Upgrade | SD card flash |
| Debug | UART console |


<div style="page-break-after: always;"></div>


# <span style="color: green;">5. Ordering Information</span>

## <span style="color: green;">Model Code Rule</span>

**Model code:** MO-68A-\<x\>

\<-x\>: Memory

## <span style="color: green;">Product Models</span>

| Base Model | -x | Memory |
|---------|-------|-----------|
| MO-62A | 4G | 4GB |
| MO-62A | 8G | 8GB |

**Example**<br/>
Model：MO-68A-8G<br/> 
"MO-62A" means Base Model<br/>
"-8G" means 8GB memory

# <span style="color: green;">6. Contact Us</span>

- **Official Website:** [InHand Networks](https://www.inhand.com)
- **Copyright Notice:** © InHand Networks. All rights reserved.
