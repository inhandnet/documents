<div style="width: 100%;height: 100%;background: url(images/62A.jpg); background-size: 100% 100%;">
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
      Mo 62A AI Single Board Computer
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

**The Mo 62A is a 2 TOPS edge AI single-board computer based on the TI AM62A74 SoC, with a form factor compatible with standard SBCs, designed for AI vision and edge inference terminals.**

**Product Features:**
- **AI Acceleration:** Integrated C7x DSP and deep-learning accelerator, 2 TOPS on-device AI inference
- **SBC Compatibility:** Standard SBC form factor, compatible with HAT accessories and mainstream enclosures
- **Rich Interfaces:** Gigabit Ethernet, 4 × USB 2.0, Micro HDMI, MIPI CSI-2
- **Security and Stability:** Secure Boot, TrustZone, OP-TEE, hardware crypto accelerator
- **Open-source Ecosystem:** Debian 13 Linux, open SDK, support for TFLite / ONNX models

## <span style="color: green;">Core Technical Specifications</span>

| Technical Indicator | Specification |
|---|---|
| AI Inference | 2 TOPS (C7x DSP + DLA) |
| Operating System | Debian 13.2 (Linux 6.12) |
| Wi-Fi | Wi-Fi 5 (802.11ac), dual-band 2.4/5 GHz |
| Bluetooth | BLE 4.2 |
| AI Framework | TI TIDL, supports TFLite / ONNX |
| Camera | 1 × 4-lane MIPI CSI-2 |
| Dimensions | 85 × 56 mm |
| Weight | 47 g |
| Power | USB Type-C 5V/5A DC |
| Power Consumption | 25W (MAX) |
| Operating Temperature | 0 ~ 50 °C |
| Memory | LPDDR4 2GB (default) / 4GB |

# <span style="color: green;">2. Product Dimensions</span>

<div style="display: flex; align-items: end; flex-wrap: wrap; justify-content: space-between;row-gap: 16px;">
  <div style="width: 45%;">
    <img src="images/prod_1.png" width="100%" alt="Front View" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Front View</div>
  </div>
  <div style="width: 45%;">
    <img src="images/prod_3.png" width="100%" alt="Side View" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Side View</div>
  </div>
    <div style="width: 18%;">
    <img src="images/prod_2.png" width="100%" alt="Interface View" />
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


<div style="page-break-after: always;"></div>


# <span style="color: green;">3. Hardware Specifications</span>

| Category / Parameter | Specification |
|--------------------------|------|
| <span style="color: green;">**Hardware Platform**</span> | |
| CPU | TI AM62A74, 4 × Cortex-A53 @ 1.4 GHz |
| AI Accelerator | C7x DSP + Deep Learning Accelerator, 2 TOPS |
| ISP / Vision | On-chip ISP + VPAC (RGB-IR, WDR, LDC) |
| Memory | LPDDR4 2GB (default) / 4GB |
| <span style="color: green;">**Interfaces and Connectivity**</span> | |
| Ethernet | 1 × Gigabit Ethernet |
| USB | 4 × USB 2.0 Type-A |
| Display | 1 × Micro HDMI |
| Camera | 1 × 4-lane MIPI CSI-2 |
| Audio | 3.5 mm jack + PCM via 40-pin connector |
| 40-pin Connector | GPIO / I²C / SPI / UART / PCM, HAT-compatible |
| Storage | Micro SD |
| Debug UART | 1 × TTL UART |
| Fan Connector | 1 × 4-pin fan connector |
| Button | 1 × Power button |
| LED | PWR, USER |
| <span style="color: green;">**Wireless**</span> | |
| Wi-Fi | Wi-Fi 5 (802.11ac), dual-band 2.4/5 GHz |
| Bluetooth | BLE 4.2 |
| Antenna Connector | Wi-Fi / BLE: on-board snap-on antenna |
| <span style="color: green;">**Security**</span> | |
| Secure Boot | Support (ARM TrustZone + OP-TEE) |
| <span style="color: green;">**Power**</span> | |
| Power Input | USB Type-C 5V/5A DC |
| Power Consumption | 25W (MAX) |
| <span style="color: green;">**Mechanical**</span> | |
| Dimensions | 85 × 56 mm |
| Weight | 47 g |
| Housing | PCB |
| Cooling | Active fan (optional) |
| <span style="color: green;">**Others**</span> | |
| RTC | Support (battery backup) |
| Watchdog | Hardware watchdog |
| <span style="color: green;">**Environmental**</span> | |
| Operating Temperature | 0 ~ 50 °C |
| Storage Temperature | -20 ~ 70 °C |

# <span style="color: green;">4. Software Specifications</span>

| Category / Parameter | Specification |
|--------------------------|------|
| <span style="color: green;">**Operating System**</span> | |
| OS | Debian 13.2 Trixie |
| Kernel | Linux Kernel 6.12 |
| <span style="color: green;">**AI & Vision**</span> | |
| AI Runtime | TI TIDL, supports TFLite / ONNX |
| Vision SDK | TI EdgeAI SDK |
| Camera Framework | V4L2 |
| Display Framework | DRM / KMS |
| <span style="color: green;">**Network Protocol**</span> | |
| IP Application | TCP/UDP, ICMP, DNS, DHCP |
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

# <span style="color: green;">5. Ordering Information</span>

## <span style="color: green;">Model Code Rule</span>

**Model code:** MO62A-\<DRAM\>

MO62A: Base Model

\<-DRAM\>: Memory

## <span style="color: green;">Product Models</span>

| Model | Memory |
|---------|-----------|
| MO62A-2G | 2GB |
| MO62A-4G | 4GB |

**Example**<br/>
Model: MO62A-2G<br/>
Mo 62A board with 2GB memory.

# <span style="color: green;">6. Contact Us</span>

- **Official Website:** [InHand Networks](https://www.inhand.com)
- **Copyright Notice:** © InHand Networks. All rights reserved.
