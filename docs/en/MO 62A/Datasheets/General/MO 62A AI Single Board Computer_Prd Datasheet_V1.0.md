<div style="width: 100%;height: 100%;background: url(images/62A.jpg); background-size: 100% 100%;">
  <div style="height:75%;">
    <div style="width:35%; padding: 40px 40px">
      <img src="images/logo.png" alt="logo" />
    </div>
    <div style="font-size: 28px; font-weight: bold; color:#000;text-align: center; margin-bottom: 60px;">
      Edge AI Computing, Open SDK, Debian Linux, HAT-Compatible
    </div>
  </div>
  <div style="padding-left: 40px;">
    <div style="font-size: 40px; font-weight: bold; color:#000;margin-bottom: 30px;">
      MO 62A AI Single Board Computer
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

**The MO-62A is a 2 TOPS edge AI single-board computer based on the TI AM62A74 SoC, designed for AI vision boxes, intelligent cameras, and edge AI inference terminals.**

**Product Features:**
- **Edge AI Acceleration:** 2 TOPS on-device AI inference with C7x DSP and deep-learning accelerator
- **Open Ecosystem:** Debian Linux, open SDK, Python/C/C++ development with Docker support
- **Rich Interfaces:** Gigabit Ethernet, 4 × USB 2.0, micro HDMI, 4-lane MIPI CSI-2, 40-pin HAT connector
- **Wireless Connectivity:** Wi-Fi 5 dual-band and BLE for flexible deployment
- **HAT Compatible:** Standard SBC form factor, mechanically compatible with mainstream enclosures and accessories

## <span style="color: green;">Core Technical Specifications</span>

| Technical Indicator | Specification |
|---|---|
| OS | Debian 13 (Embedded Linux) |
| AI Accelerator | C7x DSP + Deep Learning Accelerator, 2 TOPS |
| AI Runtime | TI TIDL, supports TFLite / ONNX |
| Wi-Fi | Wi-Fi 5 (802.11ac), dual-band 2.4 / 5 GHz |
| Bluetooth | BLE 4.2 |
| Security | Secure Boot, TrustZone, OP-TEE, Hardware AES-256 |
| CPU | 4 × Cortex-A53 @ 1.4 GHz |
| RAM | LPDDR4 4 GB (default) / 2 GB / 8 GB |
| Interface | 1 × GbE, 4 × USB 2.0, micro HDMI, MIPI CSI-2, 40-pin HAT |
| Power | USB Type-C 5 V / 5 A DC; ≤ 25 W |
| Dimensions (W × D × H) | 85 × 56 mm |
| Operating Temperature | 0 °C ~ +50 °C |

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

# <span style="color: green;">3. Hardware Specifications</span>

| Category / Parameter | Specification |
|--------------------------|------|
| <span style="color: green;">**Hardware Platform**</span> | |
| CPU | TI AM62A74, 4 × Cortex-A53 @ 1.4 GHz |
| AI Accelerator | C7x DSP + Deep Learning Accelerator, 2 TOPS |
| ISP / Vision | On-chip ISP + VPAC (RGB-IR, WDR, LDC) |
| RAM | LPDDR4 4 GB (default) / 2 GB / 8 GB |
| <span style="color: green;">**Interface**</span> | |
| Ethernet | 1 × Gigabit Ethernet |
| USB | 4 × USB 2.0 Type-A |
| Display | 1 × micro HDMI |
| Camera | 1 × 4-lane MIPI CSI-2 |
| Audio | 3.5 mm jack + PCM via 40-pin connector |
| 40-pin Connector | GPIO / I²C / SPI / UART / PCM, HAT-compatible |
| Fan Connector | 1 × 4-pin fan connector |
| Button | 1 × Reset button |
| Storage | Micro SD |
| Debug UART | 1 × TTL UART |
| LED | PWR, USER |
| <span style="color: green;">**Wireless**</span> | |
| Wi-Fi | Wi-Fi 5 (802.11ac), dual-band 2.4 / 5 GHz |
| Bluetooth | BLE 4.2 |
| Antenna | Wi-Fi / BLE: on-board snap-on antenna |
| <span style="color: green;">**Power**</span> | |
| Power Input | USB Type-C 5 V / 5 A DC |
| Power Consumption | 25 W (MAX) |
| <span style="color: green;">**Mechanical**</span> | |
| Dimensions (W × D × H) | 85 × 56 mm |
| Weight | 47 g |
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
| OS | Debian 13.2 Trixie |
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

# <span style="color: green;">5. Ordering Information</span>

## <span style="color: green;">Model Code Rule</span>

**Model code:** MO-62A-\<Memory\>

\<Memory\>: RAM Capacity

## <span style="color: green;">Product Models</span>

| Model | \<Memory\>: RAM Capacity |
|-------|--------------------------|
| MO-62A-2G | 2 GB |
| MO-62A-4G | 4 GB |
| MO-62A-8G | 8 GB |

# <span style="color: green;">6. Contact Us</span>

- **Official Website:** [InHand Networks](https://www.inhand.com)
- **Copyright Notice:** © InHand Networks. All rights reserved.
