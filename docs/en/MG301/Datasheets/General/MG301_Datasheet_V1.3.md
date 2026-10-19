<div style="width: 100%; height: 100%; background: url(images/); background-size: 100% 100%;">
  <div style="height:75%;"><div style="width:35%; padding:40px 40px;"></div><div style="font-size:28px; font-weight:bold; color:#000; text-align:center; margin-bottom:60px;">Enabling Power Meter Reading Applications</div></div>
  <div style="padding-left:40px;"><div style="font-size:40px; font-weight:bold; color:#000; margin-bottom:30px;">MG301 Series Metering Gateway</div><div style="display:flex; flex-wrap:wrap; gap:16px;">
    <div style="width:200px;background-color:#4CAF50;color:white;padding:8px;border-radius:6px;font-size:18px;">· LTE CAT 1/4</div>
    <div style="width:200px;background-color:#4CAF50;color:white;padding:8px;border-radius:6px;font-size:18px;">· Rich Interfaces</div>
    <div style="width:200px;background-color:#4CAF50;color:white;padding:8px;border-radius:6px;font-size:18px;">· IEC62056-21</div>
    <div style="width:200px;background-color:#4CAF50;color:white;padding:8px;border-radius:6px;font-size:18px;">· DLMS/COSEM</div>
    <div style="width:200px;background-color:#4CAF50;color:white;padding:8px;border-radius:6px;font-size:18px;">· Li-ion Battery</div>
  </div></div>
</div>

<div style="page-break-after: always;"></div>

# <span style="color: green;">1. Product Overview</span>

MG301 is a wireless metering gateway designed according to the requirements of the Automatic Meter Reading System for communication via cellular networks. MG301 enables the server to access the connected metering devices via the cellular network, allowing the server to obtain the operational parameters of the meters at any time and record detailed traceability information. MG301 is equipped with various hardware interfaces such as Ethernet port, serial port, digital input, relay output, etc., enabling it to connect to various meters on-site and achieve multiple applications.

## <span style="color: green;">Key Technical Specifications</span>

| Specification | Details |
| --- | --- |
| Cellular | 4G cellular module, CAT1/CAT4 |
| Hardware Platform | MIPS24KEc (575/580 MHz); 128MB RAM; 64MB Flash |
| Metering Protocols | IEC62056-21 Mode-C; DLMS/COSEM; Modbus RTU |
| Platform Access | MQTT/MQTTS/MASS/TeleMetriX Head-End |
| Interfaces | 2 × isolated RS485; 1 × USB2.0 Type-C; 4 × DI; 2 × DO; 2 × latching relay outputs (optional); 1 × 100Mbps Ethernet (optional) |
| Power | 55–270 VAC, nominal 230 V; 20 VA (max.) |
| Dimensions | 130 × 125 × 68 mm (specification table) |
| Operating Environment | -30 to 70 °C; 0–93% ambient humidity |
| Protection | IP40 |

<div style="margin-top:32px;"></div>

# <span style="color: green;">2. Features and Advantages</span>

| Feature | Description |
| --- | --- |
| Stable Communication | 2G/4G (LTE CAT 1)/NB-IoT (optional); independent hardware and software watchdog; multilevel link detection and communication self-healing |
| Rich Interfaces | 2 × RS-485; 1 × USB2.0; 2 × latching relay outputs; 4 × DI + 2 × DO; 1 × 10/100Mbps Ethernet (optional) |
| Performance and Platform | MIPS24KEc (575/580 MHz); 128MB RAM; 64MB Flash |
| Multiple Protocols | IEC62056-21; DLMS/COSEM; Modbus RTU; MQTT/MQTTS; MASS; TeleMetriX Head-End; FTP |
| Industrial-grade Design | Operating temperature -30 to 70 °C; +55 to 270 VAC power input; IP40; Li-ion battery or supercapacitor |

# <span style="color: green;">3. Product Dimensions</span>

<div style="display:flex; align-items:end; flex-wrap:wrap; justify-content:space-between;">
  <div style="width:100%;"><img src="images/MG301-dimensions.png" width="100%" alt="MG301 dimension drawing placeholder" /></div>
</div>
**Dimension (specification table):** 130 × 125 × 61 mm.

<div style="page-break-after: always;"></div>

# <span style="color: green;">4. Product Interfaces</span>

| Interface | Description |
| --- | --- |
| Ethernet | 1 × 100Mbps Ethernet port, RJ45 connector (optional) |
| Cellular | 4G cellular module, CAT1/CAT4 |
| USB | 1 × USB2.0, Type-C |
| Serial Port | 2 × RS485, isolated, terminal-block connector; RS485: Data+, Data-, GND |
| SIM Card | Mini SIM-2FF card, supports 1.8/3V SIM/UIM card; eSIM |
| Antenna Connector | 1 × Cellular Antenna |
| Button | 1 × System reset button |
| Open Lid Detection | 1 × Open Cover Inspection key |
| Relay Outputs | 2 × relay outputs: 240VAC/5A, latching relay output (optional) |
| Digital Inputs | 4 × digital inputs; isolation voltage: 3500 V; dry contact: Logic 1, Open; Logic 0, Close to ground; wet contact: VIH(max.) = 30 VDC, VIH(min.) = 5 VDC, VIL(max.) = 2 VDC |
| Digital Outputs | 2 × digital outputs; isolation voltage: 3500 V; supply voltage: 20 V max.; sink current: 0.5 A max. |

## <span style="color: green;">LED Indicators</span>

<div style="display: flex; align-items: start; flex-wrap: wrap; justify-content: space-between;">
  <div style="width: 35%;">
    <img src="images/MG301-led.png" width="100%" alt="MG301 LED indicators image placeholder" />
  </div>
  <div style="width: 55%;">
    <table>
      <thead>
        <tr><th>LED</th><th>Status Description</th></tr>
      </thead>
      <tbody>
        <tr><td>PWR</td><td>Steady on: The power supply is normal<br/>Off: No external power supply is available</td></tr>
        <tr><td>Relay-2</td><td>Steady on: Closing</td></tr>
        <tr><td>Relay-1</td><td>Steady on: Closing</td></tr>
        <tr><td>RS485-2</td><td>Blinking: Data is being exchanged through serial port 2<br/>Off: No data is being exchanged over serial port 2</td></tr>
        <tr><td>RS485-1</td><td>Blinking: Data is being exchanged through serial port 1<br/>Off: No data is being exchanged over serial port 1</td></tr>
        <tr><td>IP</td><td>Steady on: The device obtains an IP address for network communication<br/>Off: The device does not obtain an IP address for network communication</td></tr>
        <tr><td>GPRS</td><td>Steady on: 2G<br/>Off: Not 2G</td></tr>
        <tr><td>4G</td><td>Steady on: 4G<br/>Off: Not 4G</td></tr>
      </tbody>
    </table>
  </div>
</div>

# <span style="color: green;">5. Hardware Specifications</span>

| Category / Parameter | MG301 |
| --- | --- |
| <span style="color: green;">**Hardware Platform**</span> | |
| CPU | MIPS24KEc (575/580 MHz) |
| RAM | 128MB |
| FLASH | 64MB |
| <span style="color: green;">**Interfaces**</span> | |
| Ethernet Port | 1 × 100Mbps Ethernet port, RJ45 connector (optional) |
| Cellular | 4G cellular module, CAT1/CAT4 |
| USB | 1 × USB2.0, Type-C |
| Serial Port | 2 × RS485, isolated, terminal-block connector; RS485: Data+, Data-, GND |
| SIM Card | Mini SIM-2FF, supports 1.8/3V SIM/UIM card; eSIM |
| Antenna Connector | 1 × Cellular Antenna |
| Button | 1 × System reset button |
| Open Lid Detection Device | 1 × Open Cover Inspection key |
| Relay Outputs | 2 × relay outputs: 240VAC/5A, latching relay output (optional) |
| Digital Inputs | 4 × digital inputs; isolation voltage: 3500 V; dry contact: Logic 1, Open; Logic 0, Close to ground; wet contact: VIH(max.) = 30 VDC, VIH(min.) = 5 VDC, VIL(max.) = 2 VDC |
| Digital Outputs | 2 × digital outputs; isolation voltage: 3500 V; supply voltage: 20 V max.; sink current: 0.5 A max. |
| <span style="color: green;">**Other Hardware**</span> | |
| RTC | Real time clock operated from on-board coin-cell battery |
| Punctuality Accuracy | 0.5 S/day |
| Battery | Li-ion battery (500mAh) or supercapacitor (Li-ion battery default) |
| <span style="color: green;">**Power**</span> | |
| Power Supply | AC input: unregulated 55V to 270 VAC, nominal 230V, instantaneous voltage protection of 6KV; reverse voltage protection |
| Power Consumption | 20VA (max.) |
| <span style="color: green;">**Mechanical Characteristics**</span> | |
| Mounting | DIN rail / mounting ear (default) |
| Enclosure Material | Plastic |
| Dimension | 130 × 125 × 61 mm |
| Protection | IP40 |
| <span style="color: green;">**Ambient Temperature and Humidity**</span> | |
| Operating Temperature | -30 to 70 °C |
| Ambient Humidity | 0–93% |
| Declared Pollution Degree | 3 |
| Overvoltage Category | CAT III |
| <span style="color: green;">**LED**</span> | |
| System | 1 × Power, 3 × CSQ, 1 × IP, 1 × 4G, 1 × GPRS, 2 × RS485, 2 × Relay |
| <span style="color: green;">**Safety & EMC**</span> | |
| Safety & EMC | IEC 62368-1; EN 55032 Class B; EN 55035 Level 3 |
| <span style="color: green;">**Other Standards**</span> | |
| Others | EN 60068-2-30; EN 60068-2-31; EN 60068-2-1; EN 60068-2-2; EN 62262; IEC 60529; IEC 60695-11-10 standard V-0 class |

# <span style="color: green;">6. Software Specifications</span>

| Parameter | Specification |
| --- | --- |
| <span style="color: green;">**Operating System**</span> | |
| OS | Linux |
| <span style="color: green;">**Internet**</span> | |
| Access Authentication | APN, VPDN |
| Internet Access | CHAP, PAP |
| Network Format | LTE CAT 1 |
| <span style="color: green;">**Network Protocol**</span> | |
| IP Application | ICMP, DNS, TCP/UDP, TCP Server, DHCP, NTP |
| IP Routing | Static routing |
| <span style="color: green;">**Reliability**</span> | |
| Cover Opening Alarm | Detection lid is opened |
| Power Failure Alarm | Detecting an external power failure |
| Link Detection | Sends heartbeat packets to detect, auto redials when disconnected |
| Embedded Watchdog | Device runs self-detection, auto recovers from malfunctions |
| Temperature Detection | The CPU temperature can be detected and recorded in logs |
| <span style="color: green;">**Communication Protocol**</span> | |
| Acquisition Protocol | IEC62056-21 Mode-C; DLMS/COSEM; Modbus RTU |
| Access Platform | MQTT/MQTTS/MASS/TeleMetriX Head-End |
| <span style="color: green;">**Network Management**</span> | |
| Configuration | Web via USB/ETH |
| Upgrade | Local via USB/ETH; remote via FTP/InHand DM platform |
| Log | Support local system log and important log power-off autosave |

# <span style="color: green;">7. Ordering Information</span>

## <span style="color: green;">Model Code</span>

**Model:** MG301-FQ53 / MG301-FQ33 / MG301-FQ68

## <span style="color: green;">Product Models</span>

<table style="font-size:10px; width:100%;">
<thead><tr><th>Model</th><th>Cellular Type &amp; Frequency Band</th><th>Serial Port</th><th>USB</th><th>I/O</th><th>Ethernet (Optional)</th></tr></thead>
<tbody>
<tr><td>MG301-FQ53</td><td>EMEA, LTE CAT1<br/>FDD: B1/B3/B5/B7/B8/B20/B28<br/>TDD: B38/B40/B41<br/>GSM: B2/B3/B5/B8</td><td>2 × RS485</td><td>1 × USB2.0</td><td>2 × relay outputs, 4 × DI, 2 × DO</td><td>1 × 100Mbps Ethernet</td></tr>
<tr><td>MG301-FQ33</td><td>North America, LTE CAT1<br/>FDD: B2/B4/B5/B12/B13/B25/B26<br/>WCDMA: B2/B4/B6</td><td>2 × RS485</td><td>1 × USB2.0</td><td>2 × relay outputs, 4 × DI, 2 × DO</td><td>1 × 100Mbps Ethernet</td></tr>
<tr><td>MG301-FQ68</td><td>LATAM, LTE CAT4<br/>FDD: B1/B2/B3/B4/B5/B7/B8/B28<br/>TDD: B40<br/>WCDMA: B1/B2/B5/B8<br/>GSM: B2/B3/B5/B8</td><td>2 × RS485</td><td>1 × USB2.0</td><td>2 × relay outputs, 4 × DI, 2 × DO</td><td>1 × 100Mbps Ethernet</td></tr>
</tbody></table>

# <span style="color: green;">8. Contact Us</span>

- **Website:** [InHand Networks](https://www.inhand.com)
- **Copyright:** © InHand Networks. All rights reserved.
