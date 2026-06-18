<div style="width: 100%;height: 100%;background: url(images/EC300-lorawan.jpg); background-size: 100% 100%;">
  <div style="height:75%;">
    <div style="width:35%; padding: 40px 40px">
      <img src="images/logo.png" alt="logo" />
    </div>
    <div style="font-size: 28px; font-weight: bold; color:#000;text-align: center; margin-bottom: 60px;">
      Embrace LPWAN, Empower Industrial Digitalization
    </div>
  </div>
  <div style="padding-left: 40px;">
    <div style="font-size: 40px; font-weight: bold; color:#000;margin-bottom: 30px;">
      EC312 LoRaWAN Gateway
    </div>
    <div style="text-align: center;">
      <div style="display: flex; flex-wrap: wrap; gap: 16px; ">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· Multi-link</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· LoRaWAN</div>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 16px;margin-top:16px">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· Programmable</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px; ">· Cloud-managed</div>
      </div>
    </div>
  </div>
</div>

<div style="page-break-after: always;"></div>

# <span style="color: green;">1. Product Overview</span>

**EC312 is an industrial-grade LoRaWAN gateway designed for large-scale LPWAN deployments with secure, reliable, and cloud-manageable connectivity.**

**Key features:**
- **High-capacity LoRaWAN:** Semtech SX1302, up to 2,000 node access
- **Wide coverage:** Up to 15 km LOS / 2 km NLOS (deployment dependent)
- **Reliable communications:** Ethernet/cellular/Wi-Fi backup with dual SIM failover
- **Security architecture:** Secure Boot, TPM 2.0, TrustZone, firewall, VPN
- **Open edge platform:** Debian 11 + Docker + DeviceLive remote management

## <span style="color: green;">Core Technical Specifications</span>

| Technical Indicator | Specification |
|------|---------------|
| LoRaWAN Capability | SX1302, 8-channel half-duplex, up to 2,000 nodes |
| Cellular Access | LTE Cat1, APN/VPDN, CHAP/PAP |
| Network Features | ARP/Ethernet, static IP/DHCP, ICMP, DNS, TCP/UDP, static routing |
| Security | Multi-level user roles, firewall, OpenVPN, IPSec VPN |
| Open Platform | Debian 11 + Docker, cloud integration for AWS/Azure/AliCloud |
| Device Management | Web/Telnet/SSH, FOTA/DFOTA, local/remote logs, DeviceLive remote operations |
| Dimensions (W x D x H) | 145 x 106 x 36 mm |
| Weight | 339 g |
| Interfaces | 2xFE, 1xRS-232/485 + 1xRS-485, USB2.0 Type-A, Nano SIM x2 |
| Power Input | 9 to 48 V DC |
| Operating Temperature | -20 to 70 C |
| Protection and Certifications | IP30, CE/FCC/IC/PTCRB |

# <span style="color: green;">2. Product Dimensions</span>

<div style="display: flex; align-items: end; justify-content: space-between; column-gap: 2%;">

  <div style="width: 45%;">
    <img src="images/prod_1.png" alt="Front View" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Front View</div>
  </div>
  <div style="width: 45%;">
    <img src="images/prod_2.png" alt="Interface Diagram" style="display: block; margin: 0 auto;" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Interface Diagram</div>
  </div>
  
</div>
<div style="margin-top: 12px; display: flex; align-items: flex-end; justify-content: space-between; flex-wrap: nowrap;">
  <div style="width: 25%;">
    <img src="images/prod_3.png" alt="Side View" style="display: block; margin: 0 auto;" />
    <div style="width: 100%; text-align: center; font-size: 12px;">Side View</div>
  </div>  
  <div style="width: 45%;">
    <div>Note:</div><div>1. All dimensions are in millimeters (mm).</div><div>2. All dimensions are approximate and for reference only.</div><div>3. Dimensioned drawings are not intended for machining.</div><div>4. Dimensions are subject to part and manufacturing tolerances.</div><div>5. Specifications may change without prior notice.</div>
  </div>
</div>

# <span style="color: green;">3. Hardware Specifications</span>

| Category/Parameter | Specification |
|--------------------------|------|
| <span style="color: green;">**Hardware Platform**</span> |  |
| CPU | ARM Cortex-A53 @ 1.4 GHz |
| RAM | 1 GB DDR4 |
| FLASH | 8 GB eMMC |
| <span style="color: green;">**LoRaWAN Performance**</span> |  |
| LoRaWAN Baseband Chip | Semtech SX1302 |
| Channel | 8, half-duplex |
| Frequency | RU864/IN865/EU868/US915/AU915/KR920/AS923/CN470 |
| Maximum EIRP | 27 dBm |
| Receiver Sensitivity | -140 dBm (125KHz/SF12) |
| Node Capacity | Up to 2,000 nodes |
| Communication Range | 2 km NLOS / 15 km LOS (depending on environment and antenna installation) |
| <span style="color: green;">**Connectivity & Interfaces**</span> |  |
| Ethernet Ports | 2 x 10/100 Mbps FE |
| Serial Ports | 1 x RS-232/485 + 1 x RS-485 (isolated) |
| SIM Card Holders | Nano SIM x2 |
| Antenna Connectors | LTE: SMA x1, Wi-Fi: SMA x1, GPS: SMA x1, LoRaWAN: SMA x1 (North American LTE model: SMA x2) |
| USB | USB 2.0 Type-A |
| Buttons | Pinhole reset button x1; programmable button x1 |
| TF Card | MicroSD support, up to 32GB expansion |
| LED Indicators | PWR, STATUS, WARN, NET, USER x4 |
| WiFi | Wi-Fi STA (802.11ac/a/b/g/n, 2.4/5 GHz) |
| Bluetooth | BLE 4.2 |
| GPS | Satellite location GPS, 1 x SMA |
| <span style="color: green;">**Power & Power Consumption**</span> |  |
| Power Input | 9 to 48 V DC |
| Power Interface | DC terminal input (industrial terminal block) |
| Power Failure Protection | Hold for 20 seconds after power failure (safe shutdown) |
| Power Failure Alarm | Power failure alarms when power failure happens |
| <span style="color: green;">**Mechanical Specifications**</span> |  |
| Product Dimensions | 145 x 106 x 36 mm |
| Product Weight | 339 g |
| Mounting Method | Panel mounting / DIN-rail mounting |
| Protection Rating | IP30 |
| Enclosure & Heat Dissipation | Metal + plastic enclosure, fanless design |
| RTC |  Support (button battery backup) |
| Hardware Watchdog | Supported |
| TPM | TPM 2.0 |
| <span style="color: green;">**Environment & Certifications**</span> |  |
| Storage Temperature | -40 to 85 ℃ |
| Operating Temperature | -20 to 70 ℃ |
| Environmental Humidity | 5 to 95% RH (non-condensing) |
| Physical Characteristics | IEC60068-2-27 shock resistance<br>IEC60068-2-6 vibration resistance<br>IEC60068-2-32 drop resistance |
| EMC Standard | EN61000-4-2, level 3, Static<br>EN61000-4-3, level 3, Radiation Electric Field<br>EN61000-4-4, level 3, Pulsed Electric Field<br>EN61000-4-5, level 3, Surge<br>EN61000-4-6, level 3, Conducted Distubance Immunity<br>EN61000-4-8, Power Frequency Field Resistance, horizontal / vertical 400A/m (>level 2)<br>EN61000-4-12,level 3,Shock Wave Resistance |
| Certifications | CE, FCC, IC, PTCRB |

# <span style="color: green;">4. Software Specifications</span>

| Category/Parameter | Specification |
|--------------------------|------|
| <span style="color: green;">**Operating System**</span> |  |
| Operating System | Debian 11 (Kernel 5.10.168) |
| <span style="color: green;">**LoRaWAN**</span> |  |
| LoRaWAN LNS | Built-in LoRaWAN network server, compatible with The Things Stack and ChirpStack |
| LoRaWAN Protocol | LoRaWAN 1.0/1.0.2, Class A/B/C |
| <span style="color: green;">**Network Features**</span> |  |
| Network Type | LTE Cat1 |
| Network Access | APN, VPDN |
| Access Authentication | CHAP, PAP |
| WAN Protocols | Static IP, DHCP |
| LAN Protocols | ARP, Ethernet |
| IP Applications | ICMP, DNS, TCP/UDP, TCP Server, DHCP |
| IP Routing | Static routing |
| <span style="color: green;">**Security**</span> |  |
| Secure Boot | Supported |
| Trust Zone | TrustZone supported |
| Network Security | Firewall |
| Data Security |  OpenVPN, IPSec VPN |
| User Management | Multi-level user roles / management rights |
| <span style="color: green;">**Reliability**</span> |  |
| Link Detection | Heartbeat-based link detection with auto reconnect |
| Built-in Watchdog | Embedded watchdog |
| Dual SIM Switchover | Supported |
| <span style="color: green;">**Open Platform & Data Acquisition Protocols (DSA)**</span> |  |
| Secondary Development Environment | multi-programming language development platform |
| Access Cloud Platform | AWS, Azure, Ali and other cloud platforms |
| Docker | Supported |
| Industrial Protocols | Modbus RTU Master/Slave, Modbus TCP Master/Slave, EtherNet/IP, ISO on TCP, OPC UA Client/Server, Mitsubishi MC 3C/3E/3C Over TCP, Mitsubishi CPU Port, FINSUDP, HostLink, PPI, DLT645-2007, IEC104 Server |
| <span style="color: green;">**Network Management**</span> |  |
| Configuration Method | Web / Telnet / SSH |
| Upgrade Method | Web, FOTA, DFOTA |
| Log Functions | Support local system log, remote log, and important log power-off autosave |
| Configuration Backup | Import/export of configuration files |
| Remote Management | InHand DeviceLive or HTTP / HTTPS / Telnet / SSH |
| Platform Feature | Supports cloud-based parameter configuration, container management, application and firmware management |

# <span style="color: green;">5. Ordering Information</span>

## <span style="color: green;">Model Rule</span>

**Model code:** EC312-H-\<WMNN\>-\<Lxxx\>

\<WMNN\>: Cellular Type & Module  
\<Lxxx\>: LoRaWAN regional band

## <span style="color: green;">Model List</span>

<table style="width:100%; table-layout:fixed;">
  <colgroup>
    <col style="width:30%;">
    <col style="width:14%;">
    <col style="width:36%;">
    <col style="width:20%;">
  </colgroup>
  <tr><th>Model</th><th>Region</th><th>&lt;WMNN&gt;</th><th>&lt;Lxxx&gt;: LoRaWAN Band</th></tr>
  <tr><td style="white-space: nowrap;">EC312-H-FQ53-L868</td><td>EMEA</td><td>CAT1<br/>FDD: B1/B3/B7/B8/B20/B28<br/>TDD: B38/B40/B41<br/>GSM: B2/B3/B5/B8</td><td>EU868</td></tr>
  <tr><td style="white-space: nowrap;">EC312-H-FQ33-L915</td><td>North America</td><td>CAT1<br/>FDD: B2/B4/B5/B12/B13/B25/B26<br/>WCDMA: B2/B4/B5</td><td>US915/AS923</td></tr>
  <tr><td style="white-space: nowrap;">EC312-H-FQ53-L915</td><td>EMEA</td><td>CAT1<br/>FDD: B1/B3/B7/B8/B20/B28<br/>TDD: B38/B40/B41<br/>GSM: B2/B3/B5/B8</td><td>US915/AS923</td></tr>
  <tr><td style="white-space: nowrap;">EC312-H-LQA3-L470</td><td>China</td><td>CAT1<br/>LTE-FDD: B1/B3/B5/B8<br/>LTE-TDD: B34/B38/B39/B40/B41</td><td>CN470</td></tr>
</table>

# <span style="color: green;">6. Contact Us</span>

- **Website:** [InHand Networks](https://www.inhand.com)
- **Copyright:** © InHand Networks. All rights reserved.
