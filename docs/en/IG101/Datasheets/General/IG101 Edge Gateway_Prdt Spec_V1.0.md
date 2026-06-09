<div style="width: 100%;height: 100%;background: url(images/IG101.jpg); background-size: 100% 100%;">
  <div style="height:75%;">
    <div style="width:35%; padding: 40px 40px">
      <img src="images/logo.png" alt="logo" />
    </div>
    <div style="font-size: 28px; font-weight: bold; color:#000;text-align: center; margin-bottom: 60px;">
      Compact Edge Gateway, Reliable Connectivity, Industrial Design
    </div>
  </div>
  <div style="padding-left: 40px;">
    <div style="font-size: 40px; font-weight: bold; color:#000;margin-bottom: 30px;">
      IG101 Edge Gateway
    </div>
    <div style="text-align: center;">
      <div style="display: flex; flex-wrap: wrap; gap: 16px; ">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· LTE Cat1</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· Modbus to MQTT</div>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 16px;margin-top:16px">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· Edge Computing</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px; ">· Device Manager</div>
      </div>
    </div>
  </div>
</div>

<div style="page-break-after: always;"></div>

# <span style="color: green;">1. Product Overview</span>

**IG101 is a compact industrial edge gateway for IIoT applications, delivering cost-effective LTE connectivity and flexible edge data processing for large-scale device networking.**

**Product Highlights:**
- **Reliable Cellular Access:** LTE Cat1 connectivity for always-on remote access
- **Edge Data Processing:** Supports customized edge computing and data preprocessing
- **Industrial Reliability:** Metal housing, watchdog, and multi-level link detection
- **Cloud Integration:** Supports MQTT and fast integration with third-party cloud platforms
- **Scalable O&M:** Supports InHand Device Manager for large-scale deployment and management

## <span style="color: green;">Core Technical Specifications</span>

| Item | Specification |
|---|---|
| Cellular Network | LTE Cat1 |
| Network Access and Authentication | APN, VPDN; CHAP/PAP |
| Industrial Protocol | Modbus RTU |
| Cloud Connectivity | Standard MQTT protocol, connects to third-party cloud platforms |
| Remote Management | InHand Device Manager Platform |
| CPU | ARM Cortex-A5 |
| Memory and Flash | 4 MB RAM + 8 MB Flash |
| Interface Set | 1 x RS-485, 1 x RS-232, 1 x SIM, 7-PIN terminal |
| Power and Consumption | DC 7-38V; standby 150 mA @ 12V, working 280 mA @ 12V, peak 340 mA @ 12V |
| Operating Temperature | -20 ~ 70 ℃ |
| Dimensions and Protection | 76 x 108 x 37.5 mm, IP30 |

# <span style="color: green;">2. Product Dimensions & Terminal Definition</span>

<div style="display: flex; align-items: end; flex-wrap: wrap; justify-content: space-between;row-gap: 16px;">
  <div style="width: 45%;">
    <img src="images/prod_1.png" alt="Top view" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Top View</div>
  </div>
  <div style="width: 45%;">
    <img src="images/prod_2.png" alt="Interface side" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Interface Side</div>
  </div>
</div>

<div style="display: flex; align-items: end; flex-wrap: wrap; justify-content: space-between;row-gap: 16px;">
    <div style="width: 25%; margin-left: 45px;">
    <img src="images/prod_3.png" alt="Side view" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Side View</div>
  </div>
  <div style="width: 45%;">
    <div>Notes:</div>
    <div>1. All dimensions are in millimeters (mm).</div>
    <div>2. All dimensions are approximate and for reference only.</div>
    <div>3. Drawing dimensions are not intended for manufacturing.</div>
    <div>4. Dimensions are subject to part and process tolerances.</div>
    <div>5. Specifications are subject to change without notice.</div>
  </div>
</div>

## 7 PIN Definition

<table style="width:78%;">
  <colgroup>
    <col style="width:15%;">
    <col style="width:23%;">
    <col style="width:62%;">
  </colgroup>
  <tr><th align="center">PIN</th><th align="center">Definition</th><th align="left">Description</th></tr>
  <tr><td align="center">1</td><td align="center">V+</td><td>Positive electrode</td></tr>
  <tr><td align="center">2</td><td align="center">V-</td><td>Negative electrode</td></tr>
  <tr><td align="center">3</td><td align="center">B</td><td>RS-485- of serial 1</td></tr>
  <tr><td align="center">4</td><td align="center">A</td><td>RS-485+ of serial 1</td></tr>
  <tr><td align="center">5</td><td align="center">GND</td><td>Signal ground</td></tr>
  <tr><td align="center">6</td><td align="center">TXD</td><td>Serial RS232 send</td></tr>
  <tr><td align="center">7</td><td align="center">RXD</td><td>Serial RS232 receive</td></tr>
</table>

# <span style="color: green;">3. Hardware Specifications</span>

| Category/Parameter | Specification |
|--------------------|---------------|
| <span style="color: green;">**CPU and Storage**</span> | |
| CPU | ARM Cortex-A5 |
| RAM | 4 MB |
| Flash | 8 MB |
| <span style="color: green;">**Connectivity and Interfaces**</span> | |
| Serial Ports | 1 x RS-485, 1 x RS-232, industrial terminal block |
| SIM Card Slot | 1 x SIM, 1.8V/3V |
| Reset Button | Pinhole reset button |
| LED Indicators | PWR, NET, STATUS, WARN, Signal Strength (3) |
| TF Card Slot (Micro SD) | Micro SD, up to 32 GB |
| <span style="color: green;">**Power and Power Consumption**</span> | |
| Power Input | DC 7-38V, reverse polarity protection |
| Power Interface | Industrial terminal block |
| Standby Power | 150 mA @ 12V |
| Working Power | 280 mA @ 12V |
| Peak Power | 340 mA @ 12V |
| <span style="color: green;">**Mechanical Specifications**</span> | |
| Dimensions (L x W x H) | 76 x 108 x 37.5 mm |
| Mounting Method | DIN-rail, wall mounting |
| Protection Rating | IP30 |
| Housin | Metal housing |
| Hardware Watchdog | Device self-diagnosis and auto-recovery (fuzzy-mapped from Embedded Watchdog) |
| <span style="color: green;">**Environment and Certifications**</span> | |
| Storage Temperature | -40 ~ 85 C |
| Operating Temperature | -20 ~ 70 C |
| Ambient Humidity | 5 ~ 95% (non-condensing) |
| Physical Characteristics | IEC60068-2-27 shock resistance;<br/>IEC60068-2-6 vibration resistance;<br/>IEC60068-2-32 drop resistance |
| EMC Standard | EN61000-4-2, level 3, Static<br/>EN61000-4-3, level 3, Radiation Electric Field<br/>EN61000-4-4, level 3, Pulsed Electric Field<br/>EN61000-4-5, level 3, Surge<br/>EN61000-4-6, level 3, Conducted Distubance Immunity<br/>EN61000-4-8, Power Frequency Field Resistance, horizontal / vertical 400A/m (>level 3)<br/>EN61000-4-12, level 3, Shock Wave Resistance |

# <span style="color: green;">4. Software Specifications</span>

| Category/Parameter | Specification |
|--------------------|---------------|
| <span style="color: green;">**Operating System**</span> | |
| OS | FreeRTOS |
| <span style="color: green;">**Network Features**</span> | |
| Network Access | APN, VPDN |
| Access Authentication | CHAP/PAP |
| Network Types/Standards | LTE Cat1 |
| IP Applications | ICMP, DNS, TCP/UDP, TCP Server |
| <span style="color: green;">**Security**</span> | |
| User Management | Multi-level user authorization |
| AAA (Authentication, Authorization, Accounting) | CHAP/PAP |
| <span style="color: green;">**Reliability**</span> | |
| Link Detection/Probing | Heartbeat packet detection, auto-redial after disconnection |
| Embedded Watchdog | Device self-diagnosis and auto-recovery |
| <span style="color: green;">**Open Platform and Data Acquisition Protocols (DSA)**</span> | |
| Python Secondary Development | Customization development platform |
| DSA Protocol Engine | Standard MQTT protocol, connects to third-party cloud platforms |
| Industrial Protocols | Modbus RTU |
| <span style="color: green;">**Network Management**</span> | |
| Configuration Methods | Local/remote configuration tools |
| Upgrade Methods | Local or remote firmware upgrade |
| Log Function | Local logs, remote logs, important log power-off preservation |
| Configuration Backup | Import/export configuration files |
| Remote Management | InHand Device Manager Platform |
| Network Management Functions | InHand Device Manager Platform |
| Network Diagnostics | Ping |

# <span style="color: green;">5. Ordering Information</span>

## <span style="color: green;">Model Rule</span>

**Model code:** IG101-\<WMNN\>-\<IO/NA\>

\<WMNN\>: WLAN & MODULE

## <span style="color: green;">Model List</span>

| Model | Region | \<WMNN\>: WLAN & MODULE | \<IO/NA\> |
|------|--------|--------------------------|-----------|
| IG101-LQA3-STD | China | LTE-FDD: B1/B3/B5/B8<br/>LTE-TDD: B34/B38/B39/B40/B41<br/>GSM: B3/B5/B8 | 1 x RS485 + 1 x RS232, no I/O |
| IG101-FQ53-STD | EMEA | LTE-FDD: B1/B3/B5/B7/B8/B20/B28<br/>LTE-TDD: B38/B40/B41<br/>GSM: B2/B3/B5/B8 | 1 x RS485 + 1 x RS232, no I/O |

# <span style="color: green;">6. Contact Us</span>

- **Website:** [InHand Networks](https://www.inhand.com)
- **Copyright:** © InHand Networks. All rights reserved.

