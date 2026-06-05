<div style="width: 100%;height: 100%;background: url(images/IG502.jpg); background-size: 100% 100%;">
  <div style="height:75%;">
    <div style="width:35%; padding: 40px 40px">
      <img src="images/logo.png" alt="logo" />
    </div>
    <div style="font-size: 28px; font-weight: bold; color:#000;text-align: center; margin-bottom: 60px;">
      Embrace edge computing to empower industrial digitization
    </div>
  </div>
  <div style="padding-left: 40px;">
    <div style="font-size: 40px; font-weight: bold; color:#000;margin-bottom: 30px;">
      IG502 Series Cost-effective Edge Gateway
    </div>
    <div style="text-align: center;">
      <div style="display: flex; flex-wrap: wrap; gap: 16px; ">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· Multiple Access</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· Rich Interfaces</div>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 16px;margin-top:16px">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· Built-in DSA</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px; ">· Cloud Management</div>
      </div>
    </div>
  </div>
</div>

<div style="page-break-after: always;"></div>

# <span style="color: green;">1. Product Overview</span>

**IG502 is a compact and cost-effective industrial edge gateway for global cellular connectivity, protocol conversion, and cloud-managed remote operations.**

**Key features:**
- **Flexible connectivity:** Supports cellular, Ethernet, Wi-Fi backup, and dual SIM failover
- **Industrial interfaces:** 2×FE, serial, USB, MicroSD, optional DI/DO and GPS/Wi-Fi/BLE
- **Edge intelligence:** Python secondary development with built-in DSA service
- **Reliable design:** Hardware/software watchdog and multi-level link self-healing
- **Cloud operations:** DeviceLive remote access, batch management, and DSA lifecycle control

## <span style="color: green;">Core Technical Specifications</span>

| Specification Item | Value |
|---|---|
| Cellular Network | 5G SA/NSA (China models) and LTE Cat1/Cat4 (model dependent) |
| Network Features | APN, VPDN, CHAP/PAP; Static IP/DHCP; ICMP, DNS, TCP/UDP, TCP Server, static routing |
| Security | Multi-level user permissions, firewall, OpenVPN, IPSec VPN |
| Cloud Management | DeviceLive remote access, batch operations, and remote upgrades |
| Secondary Development | Python development environment |
| Industrial Protocols | Modbus RTU/TCP, OPC UA, EtherNet/IP, IEC101/104, DNP3.0, etc. |
| Dimensions (W × D × H) | 110 × 127 × 35 mm |
| Weight | 420 g |
| Ethernet Ports | 2 × 10/100Mbps |
| Serial Interfaces | 1 × RS232 + 1 × RS485, or 2 × RS485 (model dependent) |
| Power Supply | 12~48V DC, industrial terminal block |
| Operating Temperature & Protection | -20~70℃, IP30 |

# <span style="color: green;">2. Product Dimensions & Terminal Definition</span>

<div style="display: flex; align-items: end; justify-content: space-evenly; column-gap: 1.5%; transform: translateX(-7%);">

  <div style="width: 36%;">
    <img src="images/prod_1.png" alt="Front View" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Front View</div>
  </div>

  <div style="width: 13%;">
    <img src="images/prod_3.png" alt="Side View" style="display: block; margin: 0 auto;" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Side View</div>
  </div>
  <div style="width: 14%;">
    <img src="images/prod_2.png" alt="Interface Diagram" style="display: block; margin: 0 auto;" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Interface Diagram</div>
  </div>
</div>


<div style="margin-top: 12px;">
  <div style="width: 80%;">
    <div>Note:</div><div>1. All dimensions are in millimeters (mm).</div><div>2. All dimensions are approximate and for reference only.</div><div>3. Dimensioned drawings are not intended for machining.</div><div>4. Dimensions are subject to part and manufacturing tolerances.</div><div>5. Specifications may change without prior notice.</div>
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
  <tr><td align="center">3</td><td align="center">TXD or 1A</td><td>Serial RS232 send or RS485+</td></tr>
  <tr><td align="center">4</td><td align="center">RXD or 1B</td><td>Serial RS232 receive or RS485-</td></tr>
  <tr><td align="center">5</td><td align="center">GND</td><td>Serial RS232 signal ground</td></tr>
  <tr><td align="center">6</td><td align="center">A or 2A</td><td>Serial RS485+</td></tr>
  <tr><td align="center">7</td><td align="center">B or 2B</td><td>Serial RS485-</td></tr>
</table>

## I/O Definition

<table style="width:78%;">
  <colgroup>
    <col style="width:15%;">
    <col style="width:23%;">
    <col style="width:62%;">
  </colgroup>
  <tr><th align="center">PIN</th><th align="center">Definition</th><th align="left">Description</th></tr>
  <tr><td align="center">1</td><td align="center">PCOM</td><td>Dry contact access point</td></tr>
  <tr><td align="center">2</td><td align="center">DGND</td><td>Dry contact ground point</td></tr>
  <tr><td align="center">3</td><td align="center">DICOM</td><td>Digital input common port</td></tr>
  <tr><td align="center">4</td><td align="center">DI0</td><td>Digital/pulse input port 0</td></tr>
  <tr><td align="center">5</td><td align="center">DI1</td><td>Digital/pulse input port 1</td></tr>
  <tr><td align="center">6</td><td align="center">DI2</td><td>Digital/pulse input port 2</td></tr>
  <tr><td align="center">7</td><td align="center">DI3</td><td>Digital/pulse input port 3</td></tr>
  <tr><td align="center">8</td><td align="center">NC</td><td>None</td></tr>
  <tr><td align="center">9</td><td align="center">DO0</td><td>Digital/pulse output port 0</td></tr>
  <tr><td align="center">10</td><td align="center">DGND</td><td>Digital ground</td></tr>
  <tr><td align="center">11</td><td align="center">DO1</td><td>Digital/pulse output port 1</td></tr>
  <tr><td align="center">12</td><td align="center">DGND</td><td>Digital ground</td></tr>
  <tr><td align="center">13</td><td align="center">DO2</td><td>Digital/pulse output port 2</td></tr>
  <tr><td align="center">14</td><td align="center">DGND</td><td>Digital ground</td></tr>
  <tr><td align="center">15</td><td align="center">DO3</td><td>Digital/pulse output port 3</td></tr>
  <tr><td align="center">16</td><td align="center">DGND</td><td>Digital ground</td></tr>
</table>

**DI input specs:**
- 4x  Digital/pulse input DI,
- 2x  Dry contact control port,
- 1x  Common port,  1x  Idle,
- Dry contact status "1": closed
- Dry contact status "0": disconnected
- Wet contact status "1": +10 ~ +30V/-30 ~ - 10VDC
- Wet contact status "0": 0 ~ +3V/-3 ~ 0V
- Isolation 3000VDC
- Pulse signal counter supported
- Supports up to  100Hz pulse signal (32-bit counter +1-bit overflow mark)

**DO output specs:**
- 3x Digital/pulse output DO
- 1x Digital output
- 4x Digital ground
- Isolation: 3000VDC

# <span style="color: green;">3. Hardware Specifications</span>

| Category/Parameter | Specification |
|--------------------------|------|
| <span style="color: green;">**CPU and Storage**</span> | |
| CPU | ARM Cortex-A8 @600MHz |
| RAM | 512MB |
| Flash | 8GB eMMC |
| <span style="color: green;">**Connectivity and Interfaces**</span> | |
| Ethernet Ports | 2×10/100Mbps Ethernet |
| I/O Ports | Up to 4×DI + 4×DO (optional) |
| Serial Ports | 1×RS232 + 1×RS485, or 2×RS485, industrial terminal block, ordering guide for details |
| SIM Card Slot | Dual Micro SIM |
| Antenna Connectors | LTE：SMA x 1, Wi-Fi：SMA x 1, GNSS：SMA x 1, <br/>Note: North America models: 2 x SMA 4G antenna connectors. |
| USB | USB2.0 Type-A |
| TF | MicroSD up to 32GB |
| Wi-Fi(optional) | Wi-Fi STA 802.11 b/g/n 2.4G |
| Bluetooth(optional) | BLE4.2 (optional) |
| GNSS(optional) | Satellite location GPS |
| <span style="color: green;">**Power and Power Consumption**</span> | |
| Input Voltage | 12~48V DC input |
| Power Interface | Industrial terminal block |
| Power | 250mA@12V |
| <span style="color: green;">**Mechanical Specifications**</span> | |
| Product Dimensions | 110×127×35mm |
| Product Weight | 420g |
| Mounting Method | Panel, DIN-rail mounting |
| Protection Rating | IP30 |
| Housing and Cooling | Fanless metal housing |
| RTC | Support (button battery backup) |
| Hardware Watchdog | support |
| <span style="color: green;">**Environment and Certifications**</span> | |
| Storage Temperature | -40~85℃ |
| Operating Temperature | -20~70℃ |
| Ambient Humidity | 5~95% RH non-condensing |
| Physical Characteristics | IEC60068-2-27 shock resistance<br/>IEC60068-2-6 vibration resistance<br/>IEC60068-2-32 drop resistance |
| EMC Standard | EN61000-4-2, level 3, Static<br/>EN61000-4-3, level 3, Radiation Electric Field<br/>EN61000-4-4, level 3, Pulsed Electric Field<br/>EN61000-4-5, level 3, Surge<br/>EN61000-4-6, level 3, Conducted Distubance Immunity<br/>EN61000-4-8, Power Frequency Field Resistance, horizontal / vertical 400A/m (>level 2)<br/>EN61000-4-12, level 3, Shock Wave Resistance |
| Certifications | CE, UKCA, FCC, PTCRB, UL, C1D2 (Class1 Division 2), MIC&JATE, VerizonWireless, AT&T, IC, RCM, NBTC, ANATEL, IEC62443-4-2, IEC61850-3 |

# <span style="color: green;">4. Software Specifications</span>

| Category/Parameter | Specification |
|--------------------------|------|
| <span style="color: green;">**Operating System**</span> | Custom Linux |
| <span style="color: green;">**Network Features**</span> | |
| Network Access | APN, VPDN |
| Access Authentication | CHAP/PAP |
| Network Types/Standards | 5G SA/NSA and LTE Cat1/Cat4 by model |
| WAN Protocols | Static IP, DHCP |
| LAN Protocols | ARP, Ethernet |
| IP Applications | ICMP, DNS, TCP/UDP, TCP Server, DHCP |
| IP Routing | Static routing |
| <span style="color: green;">**Security**</span> | |
| User Management | Multi-level user permissions |
| Network Security | Firewall |
| Data Security | OpenVPN, IPSec VPN |
| <span style="color: green;">**Reliability**</span> | |
| Link Detection | Sends heartbeat packets to detect, auto redials when disconnected |
| Embedded Watchdog | Embedded watchdog auto-recovery |
| Dual-SIM Switching | Dual SIM failover |
| <span style="color: green;">**Open Platform and Data Acquisition Protocols (DSA)**</span> | |
| Development Environment| Python development environment |
| Cloud Integration | AWS, Azure, AliCloud and other cloud platforms |
| Industrial Protocols | Modbus RTU/TCP, EtherNet/IP, ISO on TCP, OPC UA, Mitsubishi MC/CPU Port, FINSUDP, HostLink, PPI |
| Electricity Protocol | DLT645-2007, IEC101/104, DNP3.0, IEC61850-MMS |
| Other Protocols | BACnet, CNC |
| <span style="color: green;">**Network Management**</span> | |
| Configuration | Web/Telnet/SSH configuration |
| Upgrade | Web/DeviceLive upgrade |
| Log | Support local system logs, remote logs, and important log power-off preservation |
| Configuration Backup | Config import/export |
| Remote Management | DeviceLive/HTTP/HTTPS/SSH remote management |

# <span style="color: green;">5. Ordering Information</span>

## <span style="color: green;">Model Rule</span>

**Model code:** IG502-\<WMNN\>-\<S\>-\<IO/NA\>-\<W/NA\>-\<G/NA\>[-TH]

\<WMNN\>: Cellular Type & Frequency Band (or EN00 for no cellular)  
\<S\>: Serial option (`S`=RS232×1+RS485×1, `D485`=RS485×2)  
\<IO/NA\>: DI/DO option (`IO`=4DI+4DO)  
\<W/NA\>: WLAN & BLE option  
\<G/NA\>: GPS option  
[-TH]: Thailand regional variant (for specific FQ58 models)

## <span style="color: green;">Model List</span>

| Model | Region | \<WMNN\>: Cellular Type & Frequency Band | \<S\> | \<IO/NA\> | \<W/NA\> | \<G/NA\> |
|------|--------|-------------------------------------------|------|-----------|----------|----------|
| IG502-LQA3 | China | CAT1; LTE-FDD B1/B3/B5/B8; LTE-TDD B34/B38/B39/B40/B41; GSM 900/1800 | S | NA | NA | NA |
| IG502-LQA3-IO | China | CAT1; LTE-FDD B1/B3/B5/B8; LTE-TDD B34/B38/B39/B40/B41; GSM 900/1800 | S | IO | NA | NA |
| IG502-LQA3-W-G | China | CAT1; LTE-FDD B1/B3/B5/B8; LTE-TDD B34/B38/B39/B40/B41; GSM 900/1800 | S | NA | W | G |
| IG502-LQA3-IO-W-G | China | CAT1; LTE-FDD B1/B3/B5/B8; LTE-TDD B34/B38/B39/B40/B41; GSM 900/1800 | S | IO | W | G |
| IG502-LQA3-D485 | China | CAT1; LTE-FDD B1/B3/B5/B8; LTE-TDD B34/B38/B39/B40/B41; GSM 900/1800 | D485 | NA | NA | NA |
| IG502-LQA3-D485-IO | China | CAT1; LTE-FDD B1/B3/B5/B8; LTE-TDD B34/B38/B39/B40/B41; GSM 900/1800 | D485 | IO | NA | NA |
| IG502-LQA3-D485-W-G | China | CAT1; LTE-FDD B1/B3/B5/B8; LTE-TDD B34/B38/B39/B40/B41; GSM 900/1800 | D485 | NA | W | G |
| IG502-LQA3-D485-IO-W-G | China | CAT1; LTE-FDD B1/B3/B5/B8; LTE-TDD B34/B38/B39/B40/B41; GSM 900/1800 | D485 | IO | W | G |
| IG502-NRQ1 | China | 5G NR NSA n41/n78/n79; SA n1/n28/n41/n77/n78/n79; LTE-FDD B1/B3/B5/B8; LTE-TDD B34/B38/B39/B40/B41; WCDMA B1/B5/B8 | S | NA | NA | NA |
| IG502-NRQ1-D485 | China | 5G NR NSA n41/n78/n79; SA n1/n28/n41/n77/n78/n79; LTE-FDD B1/B3/B5/B8; LTE-TDD B34/B38/B39/B40/B41; WCDMA B1/B5/B8 | D485 | NA | NA | NA |
| IG502-FQ33 | North America | CAT1; LTE-FDD B2/B4/B5/B12/B13/B25/B26; WCDMA B2/B4/B5 | S | NA | NA | NA |
| IG502-FQ33-IO | North America | CAT1; LTE-FDD B2/B4/B5/B12/B13/B25/B26; WCDMA B2/B4/B5 | S | IO | NA | NA |
| IG502-FQ33-W-G | North America | CAT1; LTE-FDD B2/B4/B5/B12/B13/B25/B26; WCDMA B2/B4/B5 | S | NA | W | G |
| IG502-FQ33-IO-W-G | North America | CAT1; LTE-FDD B2/B4/B5/B12/B13/B25/B26; WCDMA B2/B4/B5 | S | IO | W | G |
| IG502-FQ33-D485-IO-W-G | North America | CAT1; LTE-FDD B2/B4/B5/B12/B13/B25/B26; WCDMA B2/B4/B5 | D485 | IO | W | G |
| IG502-FF53 | EMEA | CAT1; LTE-FDD B1/B3/B7/B8/B20/B28; GSM/GPRS/EDGE B3/B8 | S | NA | NA | NA |
| IG502-FF53-IO | EMEA | CAT1; LTE-FDD B1/B3/B7/B8/B20/B28; GSM/GPRS/EDGE B3/B8 | S | IO | NA | NA |
| IG502-FF53-W-G | EMEA | CAT1; LTE-FDD B1/B3/B7/B8/B20/B28; GSM/GPRS/EDGE B3/B8 | S | NA | W | G |
| IG502-FF53-IO-W-G | EMEA | CAT1; LTE-FDD B1/B3/B7/B8/B20/B28; GSM/GPRS/EDGE B3/B8 | S | IO | W | G |
| IG502-FF53-D485-IO-W-G | EMEA | CAT1; LTE-FDD B1/B3/B7/B8/B20/B28; GSM/GPRS/EDGE B3/B8 | D485 | IO | W | G |
| IG502-FQ58 | EMEA | CAT4; LTE-FDD B1/B3/B7/B8/B20/B28A; WCDMA B1/B8; GSM B3/B8 | S | NA | NA | NA |
| IG502-FQ58-IO | EMEA | CAT4; LTE-FDD B1/B3/B7/B8/B20/B28A; WCDMA B1/B8; GSM B3/B8 | S | IO | NA | NA |
| IG502-FQ58-W-G | EMEA | CAT4; LTE-FDD B1/B3/B7/B8/B20/B28A; WCDMA B1/B8; GSM B3/B8 | S | NA | W | G |
| IG502-FQ58-IO-W-G | EMEA | CAT4; LTE-FDD B1/B3/B7/B8/B20/B28A; WCDMA B1/B8; GSM B3/B8 | S | IO | W | G |
| IG502-FQ58-D485-IO-W-G | EMEA | CAT4; LTE-FDD B1/B3/B7/B8/B20/B28A; WCDMA B1/B8; GSM B3/B8 | D485 | IO | W | G |
| IG502-FQ58-TH | Thailand | CAT4; LTE-FDD B1/B3/B7/B8/B20; WCDMA B1/B8; GSM B3/B8 | S | NA | NA | NA |
| IG502-FQ58-IO-TH | Thailand | CAT4; LTE-FDD B1/B3/B7/B8/B20; WCDMA B1/B8; GSM B3/B8 | S | IO | NA | NA |
| IG502-FQ58-W-G-TH | Thailand | CAT4; LTE-FDD B1/B3/B7/B8/B20; WCDMA B1/B8; GSM B3/B8 | S | NA | W | G |
| IG502-FQ58-IO-W-G-TH | Thailand | CAT4; LTE-FDD B1/B3/B7/B8/B20; WCDMA B1/B8; GSM B3/B8 | S | IO | W | G |
| IG502-FQ58-D485-IO-W-G-TH | Thailand | CAT4; LTE-FDD B1/B3/B7/B8/B20; WCDMA B1/B8; GSM B3/B8 | D485 | IO | W | G |
| IG502-FQ78 | Australia & Latin America | CAT4; LTE-FDD B1/B2/B3/B4/B5/B7/B8/B28; LTE-TDD B40; UMTS B1/B2/B5/B8; GSM 850/900/1800/1900 | S | NA | NA | NA |
| IG502-FQ78-IO | Australia & Latin America | CAT4; LTE-FDD B1/B2/B3/B4/B5/B7/B8/B28; LTE-TDD B40; UMTS B1/B2/B5/B8; GSM 850/900/1800/1900 | S | IO | NA | NA |
| IG502-FQ78-W-G | Australia & Latin America | CAT4; LTE-FDD B1/B2/B3/B4/B5/B7/B8/B28; LTE-TDD B40; UMTS B1/B2/B5/B8; GSM 850/900/1800/1900 | S | NA | W | G |
| IG502-FQ78-IO-W-G | Australia & Latin America | CAT4; LTE-FDD B1/B2/B3/B4/B5/B7/B8/B28; LTE-TDD B40; UMTS B1/B2/B5/B8; GSM 850/900/1800/1900 | S | IO | W | G |
| IG502-FQ78-D485-IO-W-G | Australia & Latin America | CAT4; LTE-FDD B1/B2/B3/B4/B5/B7/B8/B28; LTE-TDD B40; UMTS B1/B2/B5/B8; GSM 850/900/1800/1900 | D485 | IO | W | G |
| IG502-EN00 | Global (No Cellular) | No cellular | S | NA | NA | NA |
| IG502-EN00-IO | Global (No Cellular) | No cellular | S | IO | NA | NA |
| IG502-EN00-W-G | Global (No Cellular) | No cellular | S | NA | W | G |
| IG502-EN00-IO-W-G | Global (No Cellular) | No cellular | S | IO | W | G |
| IG502-EN00-D485-IO-W-G | Global (No Cellular) | No cellular | D485 | IO | W | G |

# <span style="color: green;">6. Contact Us</span>

- **Website:** [InHand Networks](https://www.inhand.com)
- **Copyright:** © InHand Networks. All rights reserved.
