# InHand VG814 User Manual (Standard Edition) V1.2

## Front Matter

### Copyright and Conventions

This user manual contains copyrighted content, and the copyright belongs to InHand Networks and its licensors. Without written permission, no organization or individual may excerpt, copy any part of the content of this manual, or distribute it in any form.

Due to ongoing updates in product technology and specifications, the company cannot guarantee that the information in the user manual is entirely consistent with the actual product. Therefore, no disputes arising from any discrepancies between the actual technical parameters and the user manual are accepted. Any changes to the product will not be notified in advance, and the company reserves the right to make the final changes and interpretations.

### Conventions

| Symbol | Indication |
| --- | --- |
| > | Indicates a button name, for example, the OK button |
| "" | Indicates a window name or menu name, for example, the pop-up window "New User" |
| >> | Separates a multi-level menu. For example, "File >> New >> Folder" indicates the menu item "Folder" under the sub-menu "New", which is under the menu "File" |
| Cautions | Points to note during operation; improper actions may result in data loss or device damage |
| Note | Supplement and provide necessary explanations for the description of the operation |

### Technical Support

T: +1 (703) 348-2988  
43671 Trade Center Place, Suite 100, Dulles, VA 20166  
Inquiry: [info@inhandnetworks.com](mailto:info@inhandnetworks.com) | Support: [support@inhandnetworks.com](mailto:support@inhandnetworks.com)  
URL: [www.inhandnetworks.com](http://www.inhandnetworks.com/)

### How to Use This Manual

**Find Your Path**

- First-time users: Read in order: "Know the Device" → "Installation and First Use" → "Common Scenarios" → "Function Reference"
- Existing users: Go directly to "Function Reference" or "Appendix A Troubleshooting"

**Quick Jump by Task**

| Task | Section | Est. Time |
|------|---------|-----------|
| Know the device and indicators | [1. Know the Device](#1-know-the-device) | ~3 min |
| Hardware setup and first Web access | [2. Installation and First Use](#2-installation-and-first-use) | ~5 min |
| Cellular connection | [3.1 Cellular Connection](#31-cellular-connection) | ~5 min |
| Wi-Fi connection | [3.2 Wi-Fi Connection](#32-wi-fi-connection) | ~5 min |
| Configure Network, VPN, Services, etc. | [4. Function Reference](#4-function-reference) | As needed |
| Troubleshooting | [Appendix A Troubleshooting](#appendix-a-troubleshooting) | As needed |

---

## 1. Know the Device

### 1.1 Overview

The InHand VG814 is a new-generation 4G in-vehicle gateway oriented at the Internet of Vehicles (IoV). It provides fast and safe networks for automobiles and transport service vehicles, meeting the requirements of police vehicles, emergency command vehicles, engineering vehicles, medical vehicles, and logistics vehicles for fast mobile networks. It is used with a cloud-based remote vehicle management platform to provide ubiquitous accessible networks and uninterrupted operation supervision for logistics management, asset tracking, mobile office, and government security.

![1699289648314-c38635b7-f2f0-41f7-b808-6f6dd1918299.png](./img/TFRyisVs9_mw-DgG/1699289648314-c38635b7-f2f0-41f7-b808-6f6dd1918299-935070.webp)

**Fig. 1-1 VG814 Application**

The device is available in VG814 Road (Bus) and VG814 Rail versions.

### 1.2 Packaging List

(Original document does not specify; to be supplemented)

### 1.3 LED Indicators

| Indicator | Status and Definition |
| :---: | --- |
| System | Steady off — Powered off<br/>Steady red — System starting<br/>Steady blue — IGT not correctly installed<br/>Blink green — System operating normally<br/>Blink red — System faulty<br/>Blink blue — System upgrading |
| Cellular | Steady off — Dialup disabled<br/>Blink green — Dialup in progress<br/>Steady green — Dialup succeeded<br/>Blink red — Dialup failed (no module or SIM detected) |
| Signal | Steady off — No signal<br/>Steady red — Weak signal (≤ 9 asu)<br/>Steady blue — Moderate signal (10–19 asu)<br/>Steady green — Strong signal (≥ 20 asu) |
| GNSS | Steady off — GNSS disabled<br/>Blink green — Positioning in progress<br/>Steady green — Positioning completed |
| Wi-Fi 2.4G | AP: Off — Disabled; Blink green — Operating<br/>STA: Off — Disabled or no AP; Steady green — Wrong password; Blink green — AP associated |
| Wi-Fi 5G | AP: Off — Disabled; Blink blue — Operating<br/>STA: Off — Disabled or no AP; Steady blue — Wrong password; Blink blue — AP associated |

### 1.4 Restore to Factory Defaults

![1679982771610-7185bf84-0ede-41eb-a638-d07693031ed6.png](./img/TFRyisVs9_mw-DgG/1679982771610-7185bf84-0ede-41eb-a638-d07693031ed6-214796.webp)

**Fig. 1-2 Reset Button**

1. Power on the device and immediately press and hold the Reset button. After about 15 s, only the System indicator is steady red.
2. When the System indicator turns off and becomes red again, immediately release the Reset button.
3. When the System indicator turns off, press the Reset button (ensure it blinks red twice) and then release it. The device is restored to the default settings.

### 1.5 Default Settings

| No. | Function | Default Settings |
| --- | --- | --- |
| 1 | Cellular | Enabled; dual-SIM disabled, SIM1 enabled |
| 2 | GNSS / Inertial navigation | Enabled |
| 3 | OBD | Enabled; CANbus baud rate and OBD protocol auto-detected |
| 4 | Wi-Fi | 2.4G/5G AP enabled; SSID VG814- or VG814-5G- + 6 digits; WPA2-PSK; password is last 8 digits of SN |
| 5 | Ethernet | 4 LAN ports enabled; IP 192.168.2.1; subnet 255.255.255.0; DHCP (Dynamic Host Configuration Protocol, can be understood as: the network's "automatic assigner" that assigns IP addresses and other parameters to connected devices) server enabled, pool 192.168.2.2–192.168.2.100 |
| 6 | Network access control | HTTP/HTTPS enabled on ports 80/443; Telnet/SSH disabled; cellular access allowed only over HTTPS |
| 7 | Username/Password | adm / 123456 |
| 8 | Power management | shutdown-delay 30; standby-mode 1; standby-check-interval 20; standby-voltage 90; standby-resume-voltage 105 |
| 9 | IO | Four digital output channels output at low level by default; pull-up resistor disabled for six digital input channels |
| 10 | Serial port | RS232/RS485: 9600 baud, 8 data bits, no parity, 1 stop bit |

### 1.6 Panel Interface

#### VG814 Road (Bus) Version

![1679982441635-76691a87-791e-4b10-9ead-65c734988648.png](./img/TFRyisVs9_mw-DgG/1679982441635-76691a87-791e-4b10-9ead-65c734988648-397544.webp)

**Fig. 1-3 VG814 Road (Bus) Antenna Panel**

**Antenna and SIM**

| Item | Specification |
| --- | --- |
| GNSS Connector | FAKRA C-coded male |
| Wi-Fi Connector | FAKRA I-coded male |
| Cellular Connector | 4G: 2× FAKRA D-coded male; 5G: 4× FAKRA D-coded male |
| SIM | 2× Mini SIM 2FF |

**Interface Info**

| Item | Specification |
| --- | --- |
| Gigabit Ethernet | M12 X-Coded female |
| FMS | M12 A-Coded female |
| Power | M12 A-Coded male |
| ETX | 20-pin industrial segment |
| AUX | 18-pin industrial segment |

**ETX 20PIN Definition**

![1679982442324-dd0e5fd6-c466-4d55-a9d0-4cec8267979f.png](./img/TFRyisVs9_mw-DgG/1679982442324-dd0e5fd6-c466-4d55-a9d0-4cec8267979f-836936.webp)

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Signal | GND | DO2 | DO4 | WHEELTICK | GND | RS232_RX1 | L-Channel | GND | CAN1_L | RS485_A |
| PIN | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Signal | GND | DO3 | PPS | FWD | GND | RS232_TX1 | R-Channel | Mic In | CAN1_H | RS485_B |

**AUX 18PIN Definition**

![1679982443191-9f38b2a1-7260-4ce9-80b1-468608ad4a68.png](./img/TFRyisVs9_mw-DgG/1679982443191-9f38b2a1-7260-4ce9-80b1-468608ad4a68-111109.webp)

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Signal | DI1 | DI2 | DI3 | DI4 | DI5 | DI6 | DI7 | DI8 | GND |
| PIN | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| Signal | GND | GND | GND | GND | DI9 | DO1 | DI10 | DI11 | GND |

#### VG814 Rail Version

![1679982444302-a6088a2a-3e76-4c36-a87c-7bd01645a40e.png](./img/TFRyisVs9_mw-DgG/1679982444302-a6088a2a-3e76-4c36-a87c-7bd01645a40e-589398.webp)

**Fig. 1-4 VG814 Rail Antenna Panel**

**Antenna and SIM**

| Item | Specification |
| --- | --- |
| GNSS Connector | TNC Female |
| Wi-Fi Connector | TNC Female |
| Cellular Connector | TNC Female |
| SIM | 2× Mini SIM 2FF |

![1679982444908-c2ad0a8e-72be-4985-9aa4-2e3d65489a1e.png](./img/TFRyisVs9_mw-DgG/1679982444908-c2ad0a8e-72be-4985-9aa4-2e3d65489a1e-520731.webp)

**Fig. 1-5 VG814 Rail Interface Panel**

**Interface Info**

| Item | Specification |
| --- | --- |
| Gigabit Ethernet | M12 X-Coded female |
| FMS | M12 A-Coded female |
| Power | M12 A-Coded male |
| ETX | 20-pin industrial segment |
| AUX | 18-pin industrial segment |

**ETX 20PIN Definition (Rail)**

![1679982445459-7b0ae386-e1cd-4896-9be6-2b61c7a8463f.png](./img/TFRyisVs9_mw-DgG/1679982445459-7b0ae386-e1cd-4896-9be6-2b61c7a8463f-396957.webp)

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Signal | GND | DO2 | DO4 | DO6 | GND | RS232_RX1 | RS232_RX2 | GND | CAN_L | RS485_A |
| PIN | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Signal | GND | DO3 | DO5 | DO7 | GND | RS232_TX1 | RS232_TX2 | GND | CAN_H | RS485_B |

**AUX 18PIN Definition (Rail)**

![1679982445909-cf9825df-07d3-4ff6-a6e0-233fcda558cc.png](./img/TFRyisVs9_mw-DgG/1679982445909-cf9825df-07d3-4ff6-a6e0-233fcda558cc-047979.webp)

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Signal | DI1 | DI2 | DI3 | DI4 | DI5 | DI6 | DI7 | DI8 | GND |
| PIN | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| Signal | GND | GND | GND | GND | DI9 | DO1 | DI10 | DI11 | GND |

#### Power and FMS Connectors

VG814 Road/Bus and Rail versions share the same power and FMS connectors.

![Power Connector](./img/TFRyisVs9_mw-DgG/1679982446304-20575d55-2743-4299-a5af-d35277a63721-217925.webp)

**Fig. 1-6 Power Connector**

| PWR PIN | Signal |
| --- | --- |
| 1 | VIN+ |
| 2 | IGT (ACC) |
| 3 | VIN- |
| 4 | NC |

![FMS Connector](./img/TFRyisVs9_mw-DgG/1679982446729-a9ee88b4-3509-4489-aefe-38cd033adc69-021646.webp)

**Fig. 1-7 FMS Connector**

| FMS PIN | Signal |
| --- | --- |
| 1 | CAN_H |
| 2 | CAN_L |
| 3 | GND |
| 4 | NC |

**Note:** For office testing, connect the red V+ wire and white IGT wire to the positive pole of the DC power supply, and the black V- wire to the negative pole.

![Schematic Diagram of Power Cable Connection](./img/TFRyisVs9_mw-DgG/1747637663870-5a23bbc7-3914-40c7-8e29-202528ce99c4-884043.webp)

**Fig. 1-8 Power Cable Connection**

---

## 2. Installation and First Use

### 2.1 Environment Setup

1. Insert the SIM card, connect the GNSS and cellular antennas, and connect the power supply and PC. Insert the diversity dialup antenna when the dialup card has poor signals. Connect the Wi-Fi antenna before logging in to the device.

![1679983129418-6b3f88fb-6308-42a0-86aa-9ec393723ffc.png](./img/TFRyisVs9_mw-DgG/1679983129418-6b3f88fb-6308-42a0-86aa-9ec393723ffc-680710.webp)

**Fig. 2-1 Hardware Connection**

**Note:** Before inserting or removing the SIM card, unplug the power cable; otherwise, the operation may cause data loss or damage the gateway.

2. Assign an IP address to the PC on the same network segment as the gateway. Method 1: Enable the PC to obtain an IP automatically (recommended). Method 2: Configure a fixed IP: 192.168.2.2–192.168.2.254, subnet 255.255.255.0, gateway 192.168.2.1.

![1679982448109-3c005a53-c3ed-40ce-beea-543128365b4c.png](./img/TFRyisVs9_mw-DgG/1679982448109-3c005a53-c3ed-40ce-beea-543128365b4c-067941.webp)

![1679982448494-008183f7-0694-4d84-b94f-d954a29ab7d8.png](./img/TFRyisVs9_mw-DgG/1679982448494-008183f7-0694-4d84-b94f-d954a29ab7d8-264882.webp)

**Fig. 2-2 Configure PC IP Address**

3. Open the browser, enter 192.168.2.1 in the address bar, and press Enter. Log in with the default username adm and password 123456 to access the web interface. If a blocking prompt is displayed, click "Advanced >> Continue".

![1679982448808-256119d6-8700-4cff-93c9-59fd9eaeb55b.png](./img/TFRyisVs9_mw-DgG/1679982448808-256119d6-8700-4cff-93c9-59fd9eaeb55b-925241.webp)

![1679982449138-b1fb779e-5e24-4dc5-afa1-cf456a255b65.png](./img/TFRyisVs9_mw-DgG/1679982449138-b1fb779e-5e24-4dc5-afa1-cf456a255b65-069077.webp)

**Fig. 2-3 Web Login**

**Method 3:** Connect via Wi-Fi (see SSID and key on the nameplate). Enter 192.168.2.1 in the browser and log in.

### 2.2 Hardware Installation

The recommended installation position is in the air conditioning duct of the vehicle.

![1679982522934-bc7889f4-fc6d-485a-8410-d42770dcb5e1.png](./img/TFRyisVs9_mw-DgG/1679982522934-bc7889f4-fc6d-485a-8410-d42770dcb5e1-573469.webp)

![1679982523379-4cdaa6f2-3696-4913-a3ed-11262b07621f.png](./img/TFRyisVs9_mw-DgG/1679982523379-4cdaa6f2-3696-4913-a3ed-11262b07621f-684877.webp)

**Fig. 2-4 Recommended Installation Position**

---

## 3. Common Scenarios

### 3.1 Cellular Connection

**Goal:** Connect to the internet via cellular dialup.  
**Prerequisites:** SIM card inserted, antennas connected, device powered on.  
**Est. time:** ~5 min.

1. Click "Network >> Cellular", check "Enable", and click Apply & Save. If the connection status is "Connected" and an IP address has been allocated, the SIM card has been connected to the network.

![1679982449570-ed1bdb77-5191-43d4-b8a9-64b2f84491f9.png](./img/TFRyisVs9_mw-DgG/1679982449570-ed1bdb77-5191-43d4-b8a9-64b2f84491f9-756048.webp)

![1679982450088-55c973b4-eb00-4096-a1c9-0983954ec2b2.png](./img/TFRyisVs9_mw-DgG/1679982450088-55c973b4-eb00-4096-a1c9-0983954ec2b2-208711.webp)

**Fig. 3-1 Cellular Configuration**

2. Use the Ping tool to test connectivity. If there is data transmission, the device has been successfully connected to the network.

![1679982450670-b44765c6-cb89-4379-9d34-1ee7e3816bac.png](./img/TFRyisVs9_mw-DgG/1679982450670-b44765c6-cb89-4379-9d34-1ee7e3816bac-074388.webp)

**Fig. 3-2 Ping Test**

3. Enable the dual-SIM function when two SIM cards are used.

### 3.2 Wi-Fi Connection

**Goal:** Connect as a client to an on-site AP network.  
**Prerequisites:** On-site Wi-Fi available.  
**Est. time:** ~5 min.

1. Connect to the device via network cable or Wi-Fi (see SSID and key on the nameplate). Assign an IP to the PC and log in to the web page (see 2.1).

2. Click "Network >> Wi-Fi" and select Wi-Fi 2.4G or Wi-Fi 5G as a client. Enter the name, authentication method, and key of an available AP. Click Apply & Save.

![1679982452192-d3630988-c6e7-4f91-8472-8a5c73f15b1d.png](./img/TFRyisVs9_mw-DgG/1679982452192-d3630988-c6e7-4f91-8472-8a5c73f15b1d-015083.webp)

**Fig. 3-3 Wi-Fi Client Configuration**

3. Check "Status". If the connection status is "Connected" and an IP address is obtained, the device has been successfully connected via Wi-Fi.

![1679982452682-3a6e156c-af6d-474c-ac81-a1e9f46ad75b.png](./img/TFRyisVs9_mw-DgG/1679982452682-3a6e156c-af6d-474c-ac81-a1e9f46ad75b-908132.webp)

**Fig. 3-4 Wi-Fi Status**

---

## 4. Function Reference

This section summarizes the main functions of the VG814. Full parameter tables and configuration details are in the original document.

### 4.1 Network

Includes Cellular interface, Bridge port, VLAN port, ADSL Dialup (PPPoE), Wi-Fi, Loopback port, and Layer 2 Switch.

**Entry:** [ Network ]

### 4.2 OBD

On-board diagnostics (OBD) for vehicle data from CAN or LIN. CANbus baud rate and OBD protocol are auto-detected by default.

**Entry:** [ OBD ]

### 4.3 VPN

Supports IPSec, GRE, L2TP, and OpenVPN for secure tunnel connections.

**Entry:** [ VPN ]

### 4.4 Services

Includes DHCP Server/Client/Relay, DNS Server/Relay, DDNS, SMS, GPS (IP/Serial forwarding), QoS, and Traffic Control.

**Entry:** [ Services ]

### 4.5 Security

Includes firewall (ACL, NAT, MAC-IP Binding) and routing (Static, RIP, OSPF, BGP).

**Entry:** [ Firewall ], [ Routing ]

### 4.6 Link Backup

Includes SLA, Track, VRRP, and Interface Backup for link redundancy and failover.

**Entry:** [ Link Backup ]

### 4.7 Administration

Includes system status, user management, AAA, SNMP, alarm, system logs, upgrade, and reboot.

**Entry:** [ Administration ]

### 4.8 Diagnostic Tools

Includes Ping, Traceroute, Tcpdump, and Link Speed Test.

**Entry:** [ Administration >> Diagnostic Tools ]

**See also:** [4.1 Network](#41-network) | [4.3 VPN](#43-vpn) | [4.4 Services](#44-services)

---

## 5. Typical Applications

(Original document does not specify; to be supplemented)

---

## Appendix A Troubleshooting

| Symptom | Possible Cause | Steps | Section |
|---------|----------------|-------|---------|
| Cannot access web interface | PC not on same subnet | Configure PC IP: 192.168.2.2–254, gateway 192.168.2.1, subnet 255.255.255.0 | [2. Installation and First Use](#2-installation-and-first-use) |
| Cellular dialup fails | SIM, antenna, APN | 1. Check SIM insertion and antenna installation<br/>2. Configure APN for private-network card<br/>3. Enable dual-SIM if using two SIMs | [3.1 Cellular Connection](#31-cellular-connection) |
| Wi-Fi client fails | Wrong SSID/password | Check AP name, authentication method, and key | [3.2 Wi-Fi Connection](#32-wi-fi-connection) |
| SIM card damage | Power on during insert/remove | Unplug power cable before inserting or removing SIM card | [2. Installation and First Use](#2-installation-and-first-use) |
| System indicator steady blue | IGT not correctly installed | For office testing, connect IGT to V+ of power supply | [1.6 Panel Interface](#16-panel-interface) |

---

## Appendix B Security Precautions

1. Use the original power adapter to avoid damage from mismatched adapters.
2. Do not install the device in strong electromagnetic interference environments or near high-power equipment.
3. Ensure the operating environment meets the temperature and humidity requirements in the specification.
4. Regularly inspect cables and replace damaged ones promptly.
5. When cleaning, avoid spraying chemicals directly on the device. Use a soft cloth.
6. Do not disassemble or modify the device; this may cause safety risks and void the warranty.
7. For OBD installation: the power supply and OBD cable of the gateway shall be installed when the vehicle is off.
8. During software upgrade, do not perform any operation on the web page; otherwise, the upgrade may be interrupted.

---

**Note:** Full descriptions of Network (Cellular, Bridge, VLAN, PPPoE, Wi-Fi, Loopback, Layer 2 Switch), OBD, VPN (IPsec, GRE, L2TP, OpenVPN), Services, Firewall, Routing, Link Backup, Administration, Diagnostic Tools, and M12 Ethernet connector definition, including screenshots and parameter tables, are in the original document. For more reference documents, see [InVehicle-Docs](https://github.com/inhandnet/InVehicle-Docs).
