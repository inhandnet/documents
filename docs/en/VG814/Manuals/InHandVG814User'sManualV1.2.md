# InHand VG814 User's Manual V1.2

About The Document

Revision History

| **Version** | Data | Auther | Descripition |
| --- | --- | --- | --- |
| 1.0  | 2022-5-10 | Sun Zhandong | Creation of the document |
| 1.2 | 2022-8-15 | Sun Zhandong | Add Product picture into document |

**Declaration**

Thank you for choosing our product. Before using the product, read this manual carefully.

The contents of this manual cannot be copied or reproduced in any form without the written permission of InHand.

Due to continuous updating, InHand cannot promise that the contents are consistent with the actual product information and does not assume any disputes caused by the inconsistency of technical parameters. The information in this document is subject to change without notice. InHand reserves the right of final change and interpretation.

© 2020 InHand Networks. All rights reserved.

Conventions

| Symbol | Indication |
| --- | --- |
| > | Indicates a button name, for example, the OK button. |
| "" | Indicates a window name or menu name, for example, the pop-up window "New User". |
| >> | Separates a multi-level menu. For example, the multi-level menu File >> New >> Folder indicates the menu item "Folder" under the sub-menu "New", which is under the menu "File". |
| ![1679982439558-9d160dde-af70-49c5-bb26-280d64573ee2.png](./img/TFRyisVs9_mw-DgG/1679982439558-9d160dde-af70-49c5-bb26-280d64573ee2-117116.png) | Reminds readers to be careful. Improper action may result in loss of data or device damage. |
| ![1679982439886-c3444f6a-f709-45d0-b4fc-7f8c6bef0b25.png](./img/TFRyisVs9_mw-DgG/1679982439886-c3444f6a-f709-45d0-b4fc-7f8c6bef0b25-619303.png) | Notes contain detailed descriptions and helpful suggestions. |

Technical support:

Support: <support@inhandnetworks.com>

Inquiry: <info@inhandnetworks.com>

T: +1 (703) 348-2988

43671 Trade Center Place, Suite 100, Dulles, VA 20166

## Overview

InHand VG814 is a new-generation 4G in-vehicle gateway oriented at the Internet of Vehicles (IoV). It provides fast and safe networks for automobiles and transport service vehicles, meeting the requirements of police vehicles, emergency command vehicles, engineering vehicles, medical vehicles, and logistics vehicles for fast mobile networks. It is used with a cloud-based remote vehicle management platform to provide ubiquitous accessible networks and uninterrupted operation supervision for logistics management, asset tracking, mobile office, and government security.

![1699289648314-c38635b7-f2f0-41f7-b808-6f6dd1918299.png](./img/TFRyisVs9_mw-DgG/1699289648314-c38635b7-f2f0-41f7-b808-6f6dd1918299-935070.webp)

 Application

## Hardware

### 2.1 Indicator Description

| VG814 Indicator | Status and Definition |
| --- | --- |
| System | Steady off --- The device is powered off.<br/>Steady red --- The system is starting.<br/>Steady blue --- IGT is not correctly installed.<br/>Blinking green --- The system operates properly.<br/>Blinking red --- The system is faulty.<br/>Blinking blue --- The system is being upgraded. |
| Cellular | Steady off --- The dialup function is disabled.<br/>Blinking green --- Dialup is in progress.<br/>Steady green --- Dialup succeeds.<br/>Blinking red --- Dialup fails (no module or SIM card is detected). |
| Signal | Steady off --- The current dialup card has no signal.<br/>Steady red --- The current dialup card has weak signals (signal strength: ≤ 9 asu).<br/>Steady blue --- The current dialup card has moderate signals (signal strength: 10–19 asu).<br/>Steady green --- The current dialup card has strong signals (signal strength: ≥ 20 asu). |
| GNSS | Steady off --- GNSS is disabled.<br/>Blinking green --- Positioning is in progress.<br/>Steady green --- Positioning is completed. |
| Wi-Fi 2.4G | Used as an AP:<br/>Steady off --- The AP is disabled.<br/>Blinking green --- The AP operates properly.<br/>Used as a STA:<br/>Steady off --- The STA is disabled, or no AP is associated.<br/>Steady green --- Connection fails due to a wrong password after an AP is associated.<br/>Blinking green --- An AP is associated. |
| Wi-Fi 5G | Used as an AP:<br/>Steady off --- The AP is disabled.<br/>Blinking blue --- The AP operates properly.<br/>Used as a STA:<br/>Steady off --- The STA is disabled, or no AP is associated.<br/>Steady blue --- Connection fails due to a wrong password after an AP is associated.<br/>Blinking blue --- An AP is associated. |

### 2.2 Restoring Default Settings via the Reset Button

![1679982771610-7185bf84-0ede-41eb-a638-d07693031ed6.png](./img/TFRyisVs9_mw-DgG/1679982771610-7185bf84-0ede-41eb-a638-d07693031ed6-214796.webp)

To restore default settings via the Reset button, perform the following steps:

1. Power on the device and immediately press and hold the Reset button. After about 15s, only the System indicator is steady red.

2. When the System indicator turns off and becomes red again, immediately release the Reset button.

3. When the System indicator turns off, press the Reset button (ensure that it blinks red twice) and then release it. The device is restored to the default settings.

### 2.3 Panel interface introduction

### 2.3.1 VG814 Road（Bus） version

![1679982441635-76691a87-791e-4b10-9ead-65c734988648.png](./img/TFRyisVs9_mw-DgG/1679982441635-76691a87-791e-4b10-9ead-65c734988648-397544.webp)

Antenna Panel

| Antenna and SIM | |
| --- | --- |
| GNSS Connector | FAKRA C-coded male |
| Wi-Fi Connector | FAKRA I-coded male |
| Cellular Connector | 4G version 2*FAKRA D-coded male<br/>5G version 4* FAKRA D-coded male |
| SIM | 2* Mini SIM 2FF |

| Interface Info | |
| --- | --- |
| Gigabit Ethernet | M12 X-Coded female |
| FMS | M12 A-Coded female |
| Power | M12 A-Coded male |
| ETX | 20 Pin industrial segment |
| AUX | 18 Pin industrial segment |

![1679982442324-dd0e5fd6-c466-4d55-a9d0-4cec8267979f.png](./img/TFRyisVs9_mw-DgG/1679982442324-dd0e5fd6-c466-4d55-a9d0-4cec8267979f-836936.webp)

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Signal | GND | DO2 | DO4 | WHEELTICK | GND | RS232_RX1 | L- Channel | GND | CAN1_L | RS485_A |
| PIN | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Signal | GND | DO3 | PPS | FWD | GND | RS232_TX1 | R- Channel | Mic In | CAN1_H | RS485_B |

![1679982443191-9f38b2a1-7260-4ce9-80b1-468608ad4a68.png](./img/TFRyisVs9_mw-DgG/1679982443191-9f38b2a1-7260-4ce9-80b1-468608ad4a68-111109.webp)

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Signal | DI1 | DI2 | DI3 | DI4 | DI5 | DI6 | DI7 | DI8 | GND |
| PIN | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| Signal | GND | GND | GND | GND | DI9 | DO1 | DI10 | DI11 | GND |

### 2.3.2 VG814 Rail version

![1679982444302-a6088a2a-3e76-4c36-a87c-7bd01645a40e.png](./img/TFRyisVs9_mw-DgG/1679982444302-a6088a2a-3e76-4c36-a87c-7bd01645a40e-589398.webp)

Antenna Panel

| Antenna and SIM | |
| --- | --- |
| GNSS Connector | TNC Female |
| Wi-Fi Connector | TNC Female |
| Cellular Connector | TNC Female |
| SIM | 2* Mini SIM 2FF |

![1679982444908-c2ad0a8e-72be-4985-9aa4-2e3d65489a1e.png](./img/TFRyisVs9_mw-DgG/1679982444908-c2ad0a8e-72be-4985-9aa4-2e3d65489a1e-520731.webp)

Interface Panel

| Interface Info | |
| --- | --- |
| Gigabit Ethernet | M12 X-Coded female |
| FMS | M12 A-Coded female |
| Power | M12 A-Coded male |
| ETX | 20 Pin industrial segment |
| AUX | 18 Pin industrial segment |

![1679982445459-7b0ae386-e1cd-4896-9be6-2b61c7a8463f.png](./img/TFRyisVs9_mw-DgG/1679982445459-7b0ae386-e1cd-4896-9be6-2b61c7a8463f-396957.webp)

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Signal | GND | DO2 | DO4 | DO6 | GND | RS232_RX1 | RS232_RX2 | GND | CAN_L | RS485_A |
| PIN | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Signal | GND | DO3 | DO5 | DO7 | GND | RS232_TX1 | RS232_TX2 | GND | CAN_H | RS485_B |

![1679982445909-cf9825df-07d3-4ff6-a6e0-233fcda558cc.png](./img/TFRyisVs9_mw-DgG/1679982445909-cf9825df-07d3-4ff6-a6e0-233fcda558cc-047979.webp)

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Signal | DI1 | DI2 | DI3 | DI4 | DI5 | DI6 | DI7 | DI8 | GND |
| PIN | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| Signal | GND | GND | GND | GND | DI9 | DO1 | DI10 | DI11 | GND |

### 2.3.3 Power and FMS

VG814 Road / Bus version and Railway verion Power connector and FMS are same.

![Power Connector](./img/TFRyisVs9_mw-DgG/1679982446304-20575d55-2743-4299-a5af-d35277a63721-217925.webp)

| PWR PIN | Signal |
| --- | --- |
| 1 | VIN+ |
| 2 | IGT（ACC） |
| 3 | VIN- |
| 4 | NC |

When testing the VG814 in the office, the red V+ wire and the white IGT wire shall be simultaneously connected to the positive pole of the DC power supply. The black V- wire shall be connected to the negative pole of the DC power supply.

![FMS Connector](./img/TFRyisVs9_mw-DgG/1679982446729-a9ee88b4-3509-4489-aefe-38cd033adc69-021646.webp)

| FMS PIN | Signal |
| --- | --- |
| 1 | CAN_H |
| 2 | CAN_L |
| 3 | GND |
| 4 | NC |

### Definition of Ethernet Interface

VG814 Ethernet  port definition.

![M12 Ethernet connector with 8 pins X-coded (female)](./img/TFRyisVs9_mw-DgG/1747711356745-c9676cb2-43e0-4fac-bfea-ff8aa63c000f-926914.webp)

In case M12 is implemented as cable end, cable connectors shall be of type inner

screw with male housing and male pin:

![M12 Ethernet connector with 8 pins X-coded (male)](./img/TFRyisVs9_mw-DgG/1747710924782-80d3a42f-9030-4a01-b609-4a6d65ec2681-291297.webp)

| M12 PINs | T568B Colour | Data |
| --- | --- | --- |
| 1 | white/orange stripe  | TxRx A +  |
| 2 | orange solid  | TxRx A -  |
| 3 | white/green stripe  | TxRx B + |
| 8 | blue solid  | TxRx C +   |
| 7 | white/blue stripe  | TxRx C - |
| 4 | green solid  | TxRx B - |
| 5 | white/brown stripe  | TxRx D + |
| 6 | brown solid  | TxRx D - |

## Default Settings

| No. | Function | Default Settings |
| --- | --- | --- |
| 1 | Dialup over the cellular network | − Enabled (The Cellular indicator is steady green after dialup succeeds.)<br/>By default, the dual-SIM function is disabled, and SIM1 is enabled. |
| 2 | Satellite positioning and inertial navigation service | − Enabled (The GNSS indicator is steady green after positioning succeeds.)<br/>− The inertial navigation function is enabled. |
| 3 | On-board diagnostics (OBD) | − Enabled<br/>− The CANbus baud rate is automatically detected.<br/>− The OBD protocol is automatically detected.<br/>− OBD data is automatically scanned. |
| 4 | Default settings of Wi-Fi | − The Wi-Fi 2.4G AP is enabled. The SSID starts with VG814-, followed by six digits.<br/>− The Wi-Fi 5G AP is enabled. The SSID starts with VG814-5G-, followed by six digits.<br/>− WPA2-PSK is used for authentication.<br/>− The password contains the last eight digits of the SN. |
| 5 | Default settings of Ethernet | − Four LAN ports are enabled.<br/>− The IP address is 192.168.2.1.<br/>− The subnet mask is 255.255.255.0.<br/>− The DHCP server is enabled. The IP address pool is 192.168.2.2–192.168.2.100, and IP addresses can be automatically allocated to downstream devices. |
| 6 | Network access control for the gateway | − HTTP and HTTPS are enabled, with the port numbers of 80 and 443 respectively.<br/>− Telnet is disabled.<br/>− SSH is disabled.<br/>− Access from the cellular network is allowed only over HTTPS. |
| 7 | Username and password | − adm/123456 (super administrator) |
| 8 | Power management | − shutdown-delay 30: The power-off delay is 30s.<br/>− standby-mode 1: The power-off function is enabled.<br/>− standby-check-interval 20 indicates the power check interval in standby mode.<br/>− standby-voltage 90: The standby threshold voltage is 9 V.<br/>− standby-resume-voltage 105: The threshold voltage for resuming normal operating in standby mode is 10.5 V. |
| 9 | IO | − Four digital output channels generate output at low level by default, and the pull-up resistor is disabled.<br/>− The pull-up resistor for six digital input channels is disabled. |
| 10 | Serial port | − RS232<br/>Baud rate: 9600<br/>Data bits: 8 bits<br/>Parity bit: none<br/>Stop bit: 1 bit<br/>− RS485<br/>Baud rate: 9600<br/>Data bits: 8 bits<br/>Parity bit: none<br/>Stop bit: 1 bit |

### Power ON

When testing the VG814 in the office, the red V+ wire and the white IGT wire shall be simultaneously connected to the positive pole of the DC power supply. The **black V-** wire shall be connected to the negative pole of the DC power supply.

![Schematic Diagram of Power Cable Connection](./img/TFRyisVs9_mw-DgG/1747637663870-5a23bbc7-3914-40c7-8e29-202528ce99c4-884043.webp)

VG814 power cable design diagram：

[附件: SCAB000339 Power Cable 9 VG814 M12 A Code 4PIN-EN.pdf](./attachments/TFRyisVs9_mw-DgG/SCAB000339 Power Cable 9 VG814 M12 A Code 4PIN-EN.pdf)

## Login and Network Access

### 4.1 Network Access via the Dialup Card

1. Insert the SIM card, connect the GNSS and cellular antennas, and connect the power supply and PC. Insert the diversity dialup antenna when the dialup card has poor signals.

![1679983129418-6b3f88fb-6308-42a0-86aa-9ec393723ffc.png](./img/TFRyisVs9_mw-DgG/1679983129418-6b3f88fb-6308-42a0-86aa-9ec393723ffc-680710.webp)

VG814 railway version, appearance drawing of single cellular network module

| ![1679982439558-9d160dde-af70-49c5-bb26-280d64573ee2.png](./img/TFRyisVs9_mw-DgG/1679982439558-9d160dde-af70-49c5-bb26-280d64573ee2-117116.png)Note:<br/>Before inserting or removing the SIM card, unplug the power cable; otherwise, the operation will cause data loss or damage the gateway. |
| --- |

1. Assign an IP address to the PC, which is on the same network segment as the IP address of the gateway.

Method 1: Enable the PC to obtain an IP address automatically (recommended).

Method 2: Configure a fixed IP address on the same network segment as the gateway address for the PC.

Step: Select "Use the following IP address", enter any IP address in the range of 192.168.2.2 to 192.168.2.254 (different from the initial IP address 192.168.2.1 of the gateway), the subnet mask 255.255.255.0, and the default gateway address 192.168.2.1, and then click OK.

![1679982448109-3c005a53-c3ed-40ce-beea-543128365b4c.png](./img/TFRyisVs9_mw-DgG/1679982448109-3c005a53-c3ed-40ce-beea-543128365b4c-067941.webp)![1679982448494-008183f7-0694-4d84-b94f-d954a29ab7d8.png](./img/TFRyisVs9_mw-DgG/1679982448494-008183f7-0694-4d84-b94f-d954a29ab7d8-264882.webp)

Obtain an IP address automatically Use a fixed IP address

1. Open the browser, enter the default IP address 192.168.2.1 of the gateway in the address bar, and press Enter.

![1679982448808-256119d6-8700-4cff-93c9-59fd9eaeb55b.png](./img/TFRyisVs9_mw-DgG/1679982448808-256119d6-8700-4cff-93c9-59fd9eaeb55b-925241.webp)

1. Log in (if a blocking prompt is displayed, click "Advanced >> Continue").

Default Username adm Password 123456

![1679982449138-b1fb779e-5e24-4dc5-afa1-cf456a255b65.png](./img/TFRyisVs9_mw-DgG/1679982449138-b1fb779e-5e24-4dc5-afa1-cf456a255b65-069077.webp)

1. Click "Network >> Cellular", check "Enable", and click Apply & Save. If the network connection status is "Connected" and an IP address has been allocated, the SIM card has been connected to the network.

(Set the APN parameters for a private-network card.)

![1679982449570-ed1bdb77-5191-43d4-b8a9-64b2f84491f9.png](./img/TFRyisVs9_mw-DgG/1679982449570-ed1bdb77-5191-43d4-b8a9-64b2f84491f9-756048.webp)![1679982450088-55c973b4-eb00-4096-a1c9-0983954ec2b2.png](./img/TFRyisVs9_mw-DgG/1679982450088-55c973b4-eb00-4096-a1c9-0983954ec2b2-208711.webp)

1. Ping a common website in China with a ping detection tool. If there is data transmission, the device has been successfully connected to the network.

![1679982450670-b44765c6-cb89-4379-9d34-1ee7e3816bac.png](./img/TFRyisVs9_mw-DgG/1679982450670-b44765c6-cb89-4379-9d34-1ee7e3816bac-074388.webp)

1. Enable the dual-SIM function when two SIM cards are used.

![1679982451113-331b8345-257b-4dd2-9ed9-0b84846b42d1.png](./img/TFRyisVs9_mw-DgG/1679982451113-331b8345-257b-4dd2-9ed9-0b84846b42d1-224503.webp)

### 4.2 Network Access via Wi-Fi

1. Complete the connection shown in the following figure. Please connect the Wi-Fi antenna before logging in to the device.

![1679982451669-6a152433-5062-4c2a-9bbd-74adce93d44d.png](./img/TFRyisVs9_mw-DgG/1679982451669-6a152433-5062-4c2a-9bbd-74adce93d44d-553895.webp)

1. Assign an IP address to the PC, which is on the same network segment as the IP address of the gateway. Log in to the web page. For details, see 4.1 Network Access via the Dialup Card.

2. Click " Network >> Wi-Fi" and select Wi-Fi 2.4G or Wi-Fi 5G as a client. Enter the name, authentication method, and key of an available wireless access point (AP). Click Apply & Save.

![1679982452192-d3630988-c6e7-4f91-8472-8a5c73f15b1d.png](./img/TFRyisVs9_mw-DgG/1679982452192-d3630988-c6e7-4f91-8472-8a5c73f15b1d-015083.webp)

1. Click "Status". The current network status is "Connected", and an IP address is obtained successfully, indicating that the device has been successfully connected to the network via Wi-Fi.

![1679982452682-3a6e156c-af6d-474c-ac81-a1e9f46ad75b.png](./img/TFRyisVs9_mw-DgG/1679982452682-3a6e156c-af6d-474c-ac81-a1e9f46ad75b-908132.webp)

## Network Management

In parameter settings, a green text box ![1679982453133-d49f3f83-d26a-4457-9995-db5d07f8cd1b.png](./img/TFRyisVs9_mw-DgG/1679982453133-d49f3f83-d26a-4457-9995-db5d07f8cd1b-156568.png) indicates a mandatory item, and a pure white text box ![1679982453520-41a59010-7533-4cf3-a12f-5c9319099619.png](./img/TFRyisVs9_mw-DgG/1679982453520-41a59010-7533-4cf3-a12f-5c9319099619-454871.png) indicates an optional item.

### Celluar Interface

![Celluar Interface](./img/TFRyisVs9_mw-DgG/1748932304889-ce7e51df-18d8-440e-be53-991c952366b5-207172.webp)

| Parameter | Description |
| --- | --- |
| **Active SIM** | The SIM card currently in use. SIM1 or SIM2 |
| **IMEI Code** | The International Mobile Equipment Identity (IMEI) number of the device. |
| **IMSI Code** | The International Mobile Subscriber Identity (IMSI) number associated with the SIM card. |
| **ICCID Code** | The Integrated Circuit Card Identifier (ICCID) of the SIM card. |
| **Phone Number** | The phone number associated with the SIM card. |
| **Signal Level** | The strength of the cellular signal received by the device.ASU is an Arbitrary Strength Unit, which can be seen as a relative value of signal strength. The Level **0-31 signal value** (often called **ASU** in engineering menus) and **dBm** are linearly converted using this formula:**ASU = RSRP (dBm) + 14.** |
| **RSSI** | The Received Signal Strength Indicator (RSSI) of the signal strength. |
| **RSRP** | The Reference Signal Received Power (RSRP) of the signal strength. |
| **RSRQ** | The Reference Signal Received Quality (RSRQ) of the signal quality. |
| **SINR** | The Signal to Interference plus Noise Ratio (SINR) of the signal quality. |
| **Register Status** | Whether the device is registered to the network. |
| **Operator** | The name of the network operator. e.g. China Unicom |
| **Network Type** | The type of cellular network being used. |
| **PCI** | The Physical Cell Identity (PCI) of the cell within the network. |
| **Band** | The frequency band used for the cellular connection. |
| **LAC** | The Location Area Code (LAC) of the location area within the network. |
| **Cell ID** | The unique identifier for the cell. |
| **APN Status** | The status of the APN connection. |
| **IP Address** | The IP address assigned to the device. e.g. 10.51.158.84 |
| **Netmask** | The netmask of the network. |
| **Gateway** | The gateway IP address. e.g. 10.51.158.1 |
| **DNS** | The DNS server addresses. |
| **MTU** | The Maximum Transmission Unit (MTU) size of the data packet that can be transmitted. |
| **Connection Time** | The duration of the current connection. |

### **Signal Quality Reference**

| **Level (ASU Range)** | **RSRP (dBm)** | **Real-World Performance** |
| --- | --- | --- |
| 28–31 | -112 to -109 | Excellent (HD video) |
| 24–27 | -116 to -113 | Good (stable browsing) |
| 20–23 | -120 to -117 | Fair (basic web) |
| 16–19 | -124 to -121 | Weak (call drops) |
| 0–15 | -140 to -125 | Unusable (no service) |

### Cellular Network Configuration Guide

This guide will walk you through the process of configuring your VG814 gateway's cellular network settings. Follow these steps to ensure your device is correctly set up for cellular connectivity.

![1748932514263-0541c1f9-662c-4be8-85f7-0b77d6333a86.png](./img/TFRyisVs9_mw-DgG/1748932514263-0541c1f9-662c-4be8-85f7-0b77d6333a86-012736.webp)

### Step 1: Accessing the Cellular Configuration Page

1. Log in to your VG814 gateway's web interface.
2. Navigate to the **Network** section in the left-hand menu.
3. Click on **Cellular** to access the cellular configuration settings.

### Step 2: General Cellular Settings
- **Enable**: Check this box to activate the cellular connection.
- **SIM1 / SIM2**: Select the SIM card you want to use for the cellular connection. You can choose either SIM1 or SIM2.
- **Profile**: Choose the profile you want to apply. The default setting is "Auto", which allows the device to automatically select the best settings.
- **Roaming**: Check this box if you want the device to enable roaming when necessary.
- **IMS**: Leave this unchecked unless you have specific requirements for IMS (IP Multimedia Subsystem) services.
- **PIN Code**: Enter the PIN code for your SIM card if required.
- **Network Type**: Select the type of network you want to connect to. The options include "Auto", "GSM", "3G", etc.
- **5GNR Mode**: Choose the mode for 5G connectivity. Options include "NSA/SA".
- **Connection Mode**: Select how you want the device to maintain its connection. "Always Online" ensures the device stays connected at all times.
- **Redial Interval**: Set the time interval (in seconds) for the device to attempt reconnecting if the connection is lost. The default is 10 seconds.
- **Detection Method**: Choose the method for detecting network availability. "none" is the default setting.
- **Show Advanced Options**: Uncheck this box unless you need to configure advanced settings.

### Step 3: Configuring Profiles

In the **Profile** section, you can set up different profiles for various network types:

- **Index**: The order of the profiles. Lower numbers have higher priority.
- **Network Type**: Select the type of network (e.g., GSM, 3G).
- **APN**: Enter the Access Point Name provided by your network operator.
- **Access Number**: Enter the access number if required by your network operator.
- **Auth Method**: Choose the authentication method. "Auto" allows the device to automatically select the best method.
- **Username**: Enter the username for the APN if required.
- **Password**: Enter the password for the APN if required.
- **Metered Connection**: Check this box if your connection is metered (i.e., limited by data usage).

### Step 4: Applying and Saving Settings

1. After configuring the settings, click on **Apply & Save** to apply the changes.
2. Click **Cancel** if you want to discard any changes made.

#### Additional Tips
- Ensure that the SIM card is properly inserted and activated by your network operator.
- Regularly check for updates to the firmware of your VG814 gateway to ensure optimal performance and security.

### Enabling Advanced Options

![1748933002589-fd75ef9e-935d-40d2-9cac-d44c31bb30a4.png](./img/TFRyisVs9_mw-DgG/1748933002589-fd75ef9e-935d-40d2-9cac-d44c31bb30a4-430674.webp)

1. **Access Advanced Options**:
    - On the "Cellular" configuration page, check the "Show Advanced Options" checkbox. This will display additional advanced settings that allow for more detailed configuration.
2. **Configure Advanced Options**:
    - **Initial Commands**: In this field, you can enter initial commands that the device needs to execute upon startup. This is often used for specific network configurations or device initialization.
    - **RSSI Poll Interval**: Set the polling interval for the Received Signal Strength Indicator (RSSI). The default is 120 seconds, which you can adjust as needed. Setting it to 0 disables this feature.
    - **Dial Timeout**: Set the dial timeout duration. The default is 120 seconds, which you can adjust based on network conditions.
    - **Infinitely Dial Retry**: Check this option to allow the device to retry dialing indefinitely upon failure. This is useful for ensuring the device always attempts to connect to the network.
    - **Dual SIM Enable**: Check this option to enable dual SIM functionality, allowing the device to use two SIM cards for network connectivity.

### Enabling Dual SIM Functionality

![1748933044448-ab099121-be02-433c-ad0a-31cc3bacadcb.png](./img/TFRyisVs9_mw-DgG/1748933044448-ab099121-be02-433c-ad0a-31cc3bacadcb-006957.webp)

1. **Enable Dual SIM**:
    - Check the "Dual SIM Enable" checkbox to activate the dual SIM feature. This allows the device to use two SIM cards for network connectivity.
2. **Configure Primary SIM**:
    - In the "Main SIM" dropdown menu, select the primary SIM card. The primary SIM card is typically used for the main network connection and data transmission.
3. **Configure Secondary SIM**:
    - If necessary, you can configure the secondary SIM to automatically switch when the primary SIM is unavailable. This provides additional network redundancy and stability.
4. **Set Dial Attempt Limit**:
    - In the "Max Number of Dial" field, set the maximum number of dial attempts the device should make. The default is 5 times, which you can adjust as needed.
5. **Set Minimum Connection Time**:
    - In the "Min Connected Time" field, set the minimum time the device must stay connected before attempting to redial. The default is 0, indicating this feature is disabled.

### Applying and Saving Settings

1. After completing all configurations, click the "Apply & Save" button to apply and save your settings.
2. Click the "Cancel" button to discard any unsaved changes.

#### Notes
- Ensure both of your SIM cards are activated and have sufficient credit.
- Regularly check and update your network configurations to ensure optimal network performance and compatibility.
- If you encounter any connection issues, contact your network service provider or technical support team.

### Network

### Bridge Port

A bridge port is intended to connect two different physical LANs over a bridge, to enable storage and forwarding across LANs at the link layer.

Method for modifying the IP address of a bridge port and bridge members:

1. Click "Network >> Bridge" and select "Bridge >> Modify".

![1679982453865-c91b0d48-cbf5-437f-a19e-1cfa3c13eeac.png](./img/TFRyisVs9_mw-DgG/1679982453865-c91b0d48-cbf5-437f-a19e-1cfa3c13eeac-383095.webp)

1. Modify the IP address of the bridge port or bridge members. Among the bridge members, dot11radio1 and dot11radio2 are Wi-Fi 2.4G and Wi-Fi 5G ports respectively.

![1679982454234-2f1396e8-1113-42f2-b391-2a612b79218f.png](./img/TFRyisVs9_mw-DgG/1679982454234-2f1396e8-1113-42f2-b391-2a612b79218f-629581.webp)

### VLAN Port

A virtual LAN (VLAN) comprises a group of logical devices and users. These devices and users are not limited by physical locations, but can be organized based on functions, departments, applications, and other factors. They communicate with each other as if they are on the same network segment, which contributes to the name of VLAN.

Method for adding a port of VLAN 2:

1. Click "Network >> VLAN >> Configure VLAN Parameters >> Add". Set the virtual IP address of the port of VLAN 2 and select the member port of VLAN 2 as required. Click Apply & Save.

![1679982454636-0b05fa09-fbf1-42d7-bdaa-319ac8c6bb0a.png](./img/TFRyisVs9_mw-DgG/1679982454636-0b05fa09-fbf1-42d7-bdaa-319ac8c6bb0a-656576.webp)

1. Return to the VLAN list. The port of VLAN 2 has been successfully added.

![1679982454994-130ad59b-7313-477f-aa7c-a26ff2b88fc1.png](./img/TFRyisVs9_mw-DgG/1679982454994-130ad59b-7313-477f-aa7c-a26ff2b88fc1-899317.webp)

Currently, VLAN ports of the device support two link types: access and trunk. An access port belongs to only one VLAN and is generally connected to a computer. A trunk port can be used for multiple VLANs and can receive messages from or send messages to multiple VLANs. It can be connected to a switch or a user's computer. You can select the link type as required on the "VLAN Trunk" page.

![1679982455468-931b2409-41cb-45a3-bc92-84bc2d8ed124.png](./img/TFRyisVs9_mw-DgG/1679982455468-931b2409-41cb-45a3-bc92-84bc2d8ed124-860287.webp)

### ADSL Dialup (PPPoE)

Method for connecting the gateway to the PPPoE server:

1. Click "Network > > ADSL Dialup (PPPoE)", select the VG814 interface for connecting to the PPPoE server in the "Dial Pool" bar, and click Add.

2. Enter the user name, password, and pool ID of the PPPoE server in the "PPPoE List" bar. The pool ID must be the same as that in the "Dial Pool" bar. Click Add, and then click Apply & Save.

![1679982455842-cff7d239-2d4a-45c2-824a-b34c3096aab5.png](./img/TFRyisVs9_mw-DgG/1679982455842-cff7d239-2d4a-45c2-824a-b34c3096aab5-866486.webp)

### Wi-Fi

The gateway can be used as an AP or a client. When it is used as an AP, other users can access the Internet through the gateway via Wi-Fi. When it is used as a client, the gateway connects to an AP for Internet access. The status bar shows the current Wi-Fi connection status of the gateway.

![1679982456300-3018447f-6e9f-4fa0-bae7-fe58332f711a.png](./img/TFRyisVs9_mw-DgG/1679982456300-3018447f-6e9f-4fa0-bae7-fe58332f711a-013462.webp)

Method for providing network access services for wireless terminals when the gateway is used as an AP:

Click "Wi-Fi >> Wi-Fi 2.4 or Wi-Fi 5G" and select "AP" for "Station Role". Enter the SSID, authentication method, and key consistent with those of the wireless AP. Click Apply & Save.

![1679982456700-be2b24cd-1688-4b7f-8274-09210ab9ece4.png](./img/TFRyisVs9_mw-DgG/1679982456700-be2b24cd-1688-4b7f-8274-09210ab9ece4-512296.webp)

Method for connecting to an AP for Internet access when VG814 is used as a client:

Select "Client", enter the Wi-Fi SSID and key, and click Apply & Save.

![1679982457074-3d0280e4-f378-4d4e-a6a6-efd8984f6658.png](./img/TFRyisVs9_mw-DgG/1679982457074-3d0280e4-f378-4d4e-a6a6-efd8984f6658-787047.webp)

### Loopback Port

Method for adding multiple loopback ports:

Click "Network >> Loopback >> Multi-IP Settings", configure any IP address for the gateway, click Add, and then click Apply & Save.

![1679982457510-d63b51e7-ec86-46d9-9bdc-cb1242887265.png](./img/TFRyisVs9_mw-DgG/1679982457510-d63b51e7-ec86-46d9-9bdc-cb1242887265-410697.webp)

### Layer 2 Switch

Check the network connection status of GE 1 to GE 4. LINK UP indicates that the network is connected. LINK DOWN indicates that the network is disconnected.

![1679982457890-aea8873f-6138-4ac3-adf3-c1bdb0d76296.png](./img/TFRyisVs9_mw-DgG/1679982457890-aea8873f-6138-4ac3-adf3-c1bdb0d76296-214612.webp)

### OBD

OBD is used to collect vehicle condition data from CAN or LIN, obtain emission information, and perform fault diagnosis in real time. Vehicle condition data includes key parameters such as the fuel level, mileage, driving speed, engine speed, engine load, coolant temperature, and brake pressure. Emission information includes the volume of AdBlue, the operating and monitoring status of various exhaust post-processing sensors (such as the exhaust gas sensor and diesel particle filter) and catalysts, etc. In fault diagnosis, standard fault codes of vehicles and description information can be obtained in real time, so that vehicle maintenance personnel can learn the vehicle health status in time and locate the faults.

To collect vehicle data, the gateway is connected to the diagnostic port of the vehicle through the I/O port of the gateway over the OBD-II or J1939 cable. The cable accessories can be selected or customized during purchasing. For details about the access method, see Section 4.4 in the VG814 Quick Start Guide. After the gateway starts, the OBD service is automatically enabled to collect key vehicle condition data and fault code information.

| ![1679982458344-13144f43-705d-4db0-a63d-15d30db73eb6.png](./img/TFRyisVs9_mw-DgG/1679982458344-13144f43-705d-4db0-a63d-15d30db73eb6-226894.png)Note:<br/>The power supply and OBD cable of the gateway shall be installed when the vehicle is off. |
| --- |

The vehicle status information is displayed on the OBD status page.

OBD Status:

CAN Link Status (ERROR-ACTIVE indicates that the gateway has successfully connected to the diagnostic port of the vehicle. Other status indicates that the connection is abnormal or the diagnostic port of the vehicle is not identified.)

CAN Bitrate (In OBD, the CAN bitrate is automatically adapted, generally 250 kbps or 500 kbps.)

CAN Bind ("OBD" (default) or "Custom")

OBD Connection Status ("Disconnected", "Connecting", or "Connected")

OBD Protocol Type (OBD-II or J1939)

![1679982459102-74732367-aa97-48fa-b0df-2b46bad10493.png](./img/TFRyisVs9_mw-DgG/1679982459102-74732367-aa97-48fa-b0df-2b46bad10493-816251.webp)

Scan OBD Data and Export OBD Report:

Click the Scan OBD Data button to generate a OBD data report containing detailed vehicle condition data and diagnostic information. Click the Export OBD Report button to save the generated OBD data report to the local storage.

OBD Data Stream: The real-time vehicle condition data is displayed.

![1679982459498-fca8c309-150f-486d-acc3-2833d0e063b2.png](./img/TFRyisVs9_mw-DgG/1679982459498-fca8c309-150f-486d-acc3-2833d0e063b2-911447.webp)

OBD Ability:

Version of the OBD ability;

Type of the OBD protocol;

Vehicle identification number (VIN);

Valid variables and reference values that can be collected by the gateway.

![1679982459849-c1746b0f-400e-42af-82e2-3cc31d89a6aa.png](./img/TFRyisVs9_mw-DgG/1679982459849-c1746b0f-400e-42af-82e2-3cc31d89a6aa-131004.webp)

### VPN Application

The VPN is intended to establish a private network on the public network for encrypted communication. A VPN gateway enables remote access by encrypting data packets and converting the destination address of data packets. The VPN can be realized by a server, hardware, or software, or in other ways. Compared with the traditional DDN private line or frame relay, the VPN provides a more secure and convenient remote access solution.

Common VPN application scenario: For example, an employee on a business trip accesses the enterprise's intranet. The employee connects to the enterprise's VPN server and then accesses the enterprise's intranet through the VPN server. Communication data between the VPN server and the client is encrypted and can be regarded as being transmitted on a dedicated data network. This ensures data security.

### IPsec

IPsec is a group of open network security protocols developed by IETF. At the IP layer, the data source authentication, data encryption, data integrity, and anti-replay functions are used to ensure the security of data transmission between communication parties on the Internet. This reduces the risk of leakage and eavesdropping, ensures the integrity and confidentiality of data, and ensures the security of service transmission for users.

Scenario: Data is transmitted between the subnet (192.168.1.0/24) of headquarters A and the subnet (172.16.1.0/24) of customer branch B through gateway A and gateway B. The transmission channels of gateway A and gateway B are encrypted over IPsec, to protect the security of data transmission between headquarters A and customer branch B.

![1679982460293-facf6645-970a-4b4e-9864-5495085bd4a6.png](./img/TFRyisVs9_mw-DgG/1679982460293-facf6645-970a-4b4e-9864-5495085bd4a6-748046.webp)

Method for encrypting the transmission channels of gateway A and gateway B over IPsec:

Parameter settings:

| Gateway A | |  | Gateway B |
| --- | --- | --- | --- |
| Set IKEv1/v2 parameters | |  | Set IKEv1/v2 parameters |
| ID | Custom |  | ID | Custom |
| Encryption algorithm | AES128 |  | Encryption algorithm | Same as that of gateway A |
| Hash algorithm | SHA1 |  | Hash algorithm | |
| Diffie-Hellman key exchange | Group2 |  | Diffie-Hellman key exchange | |
| Lifecycle | 86400 |  | Lifecycle | |
| IPsec policy | |  | IPsec policy |
| Name | Custom |  | Name | Custom |
| Encapsulation | ESP |  | Encapsulation | Same as that of gateway A |
| Encryption algorithm | AES128 |  | Encryption algorithm | |
| Authentication method | SHA1 |  | Authentication method | |
| IPsec mode | Tunnel mode |  | IPsec mode | |
| IPsec tunnel configuration | |  | IPsec tunnel configuration |
| Peer address | Address where gateway B establishes the IPsec service |  | Peer address | Address where gateway A establishes the IPsec service |
| Interface | Interface for establishing the IPsec service |  | Interface | Interface for establishing the IPsec service |
| IKE version | IKE version used |  | IKE version | Same as that of gateway A |
| Authentication method | Shared key |  | Authentication method | |
| Local subnet | IP address of the subnet of gateway A |  | Local subnet | IP address of the subnet of gateway B |
| Peer subnet | IP address of the subnet of gateway B |  | Peer subnet | IP address of the subnet of gateway A |

Detailed configuration steps:

1. Configure gateway A and gateway B.

(1) Add IKE and IPsec policies, and click Apply & Save.

(2) Add IPsec tunnels and click Apply & Save.

![1679982460690-fbc698e3-d9b6-4b85-ba17-54e9960b4094.png](./img/TFRyisVs9_mw-DgG/1679982460690-fbc698e3-d9b6-4b85-ba17-54e9960b4094-300935.webp)

![1679982461079-3ade1e62-dbe9-4631-bef1-76e5a94f523c.png](./img/TFRyisVs9_mw-DgG/1679982461079-3ade1e62-dbe9-4631-bef1-76e5a94f523c-261176.webp)

1. Access the IPsec status page. The IPsec VPN is established successfully if the page is shown as below.

![1679982461423-8532decd-2242-4514-b0bf-807978c2c815.png](./img/TFRyisVs9_mw-DgG/1679982461423-8532decd-2242-4514-b0bf-807978c2c815-970670.webp)

| ![1679982439558-9d160dde-af70-49c5-bb26-280d64573ee2.png](./img/TFRyisVs9_mw-DgG/1679982439558-9d160dde-af70-49c5-bb26-280d64573ee2-117116.png)Note:<br/>The IPsec profile does not need to be configured for establishing an IPsec VPN, but needs to be configured for establishing a DM VPN. |
| --- |

### GRE

The Generic Routing Encapsulation (GRE) protocol can be used to encapsulate datagrams of some network layer protocols, so that these encapsulated datagrams can be transmitted on the IPv4 network.

Scenario: GRE is enabled for VG814_A and VG814_B through the public network.

![1679982462171-c8a97dec-61b9-42cd-a20a-8d657cb4a7ba.png](./img/TFRyisVs9_mw-DgG/1679982462171-c8a97dec-61b9-42cd-a20a-8d657cb4a7ba-448894.webp)

Method for enabling GRE for transmission channels of VG814_A and VG814_B:

1. Click "VPN >> GRE" and then click Add.

![1679982462544-444f6871-4273-4d95-92fa-57187ae250f8.png](./img/TFRyisVs9_mw-DgG/1679982462544-444f6871-4273-4d95-92fa-57187ae250f8-769232.webp)

1. Set "Index" as required. Select "Point to Point" or "Subnet" for "Network Type". Set "Local Virtual IP" and "Peer Virtual IP", ensuring that they are on the same network segment. Enter the source and peer IP addresses or interfaces and the key. Click Apply & Save.

![1679982462954-04d43e48-1597-459c-977b-d540d51c05ad.png](./img/TFRyisVs9_mw-DgG/1679982462954-04d43e48-1597-459c-977b-d540d51c05ad-644217.webp)

1. Set VG814_B in the same way. The virtual and peer IP addresses of VG814_B must correspond to those of VG814_A, and the key must be the same as that of VG814_A.

### 5.3.3 L2TP

The Layer 2 Tunneling Protocol (L2TP) is an industrial-standard Internet tunneling protocol used to encrypt network data streams.

Method for settings when the gateway is used as an L2TP client:

1. Click "VPN >> L2TP >> L2TP Client >> L2TP Class", enter a name of an L2TP class, and click Add.

![1679982463307-3a8c1cec-8c5a-410d-8657-222957a6b116.png](./img/TFRyisVs9_mw-DgG/1679982463307-3a8c1cec-8c5a-410d-8657-222957a6b116-906157.webp)

1. Configure the pseudowire class: Enter a name of any pseudowire class. "L2TP Class" is the same as that on the "L2TP Class" page. Set "Source Interface" to the interface connecting to the server. Select L2TPV2 for "Protocol" and click Add.

![1679982463623-8f0a15ad-b344-4020-87ba-04114145f125.png](./img/TFRyisVs9_mw-DgG/1679982463623-8f0a15ad-b344-4020-87ba-04114145f125-614430.webp)

1. Set L2TPV2 tunnel parameters: Enter the server's domain name or IP address for "L2TP Server". "Pseudowire Class" is the same as that on the "Pseudowire Class" page. Enter the user name and password created on the server. Set other parameters as required. Click Apply & Save.

![1679982464076-9baa7545-1d6d-49c0-bd87-a476fbafb100.png](./img/TFRyisVs9_mw-DgG/1679982464076-9baa7545-1d6d-49c0-bd87-a476fbafb100-590088.webp)

1. After gateway A and gateway B are configured, access the L2TP status page to view the L2TP connection status.

![1679982464423-cdb3082f-305e-4e53-84a1-bbab42c84fca.png](./img/TFRyisVs9_mw-DgG/1679982464423-cdb3082f-305e-4e53-84a1-bbab42c84fca-325311.webp)

### 5.3.4 OpenVPN

OpenVPN is realized based on the application-layer VPN of the OpenSSL library. It supports multiple authentication methods such as the certificate, key, and user name/password. Compared with the traditional VPN, it is simpler and easier to use.

Authentication methods:

| Authentication method | Operation on the web page |
| --- | --- |
| None | No authentication is required. |
| User name/password | Enter the user name and password created on the OpenVPN server, click "VPN >> Certificate Management", and import the CA certificate, public key, and private key for authentication. |
| Pre-shared key | Enter the pre-shared key created on the OpenVPN server. |
| Digital certificate | Click "VPN >> Certificate Management" and import the CA certificate, public key, and private key. |
| Digital certificate/user name/password | Enter the user name and password created on the OpenVPN server, click "VPN >> Certificate Management", and import the CA certificate, public key, and private key for authentication. |
| Digital certificate/TLS authentication | Enter the pre-shared key created on the OpenVPN server, click "VPN >> Certificate Management", and import the CA certificate, public key, and private key for authentication. |
| Digital certificate/TLS authentication/user name/password | Enter the pre-shared key, user name, and password created on the OpenVPN server, click "VPN >> Certificate Management", and import the CA certificate, public key, and private key for authentication. |

Method for settings when the gateway is connected to the OpenVPN server as a client:

OpenVPN can be configured manually, or OpenVPN configurations can be imported. In the following example, the authentication type is a digital certificate.

1. Set the OpenVPN parameters for the gateway as shown in the figure below, ensuring that the network parameters at both ends of the tunnel are consistent. Click Apply & Save.

![1679982464764-ccf44013-0ce7-4070-af4d-6a91f46661ee.png](./img/TFRyisVs9_mw-DgG/1679982464764-ccf44013-0ce7-4070-af4d-6a91f46661ee-873592.webp)

1. Select a digital certificate for "Authentication Type", click "VPN >> Certificate Management", and import the CA certificate, public key, and private key.

2. Click Apply & Save. Return to the "Status" page and view the tunnel status.

![1679982465119-cf8ba624-34df-4b09-9095-b60d8ecd1d7d.png](./img/TFRyisVs9_mw-DgG/1679982465119-cf8ba624-34df-4b09-9095-b60d8ecd1d7d-995019.webp)

### 5.3.5 Certificate Management

Certificates can be imported or exported on this page. Certificates are used for IPsec and OpenVPN services.

Method for importing a certificate:

Click "VPN >> Certificate Management >> Browse", select the certificate obtained from the certificate server, click Import XX Certificate, and then click Apply & Save.

![1679982465536-78973d7a-c640-4675-b831-490019e923e8.png](./img/TFRyisVs9_mw-DgG/1679982465536-78973d7a-c640-4675-b831-490019e923e8-458470.webp)

![1679982465994-048b3fbc-341d-41b7-91aa-49d2f4c769c1.png](./img/TFRyisVs9_mw-DgG/1679982465994-048b3fbc-341d-41b7-91aa-49d2f4c769c1-549904.webp)

If no local certificate is available, check "Enable SCEP (Simple Certificate Enrollment Protocol)" to apply for a certificate online.

Method for applying for a certificate for the gateway online:

1. Click "VPN >> Certificate Management". Check "Enable SCEP (Simple Certificate Enrollment Protocol)" and "Force to re-enroll". Enter the certificate protection key and confirm it. Enter the URL of the certificate server, the certificate name, and the FQDN. Click Apply & Save.

2. After the server issues the certificate, check the application status. If the application status is "Completion", the certificate application succeeds.

![1679982466346-7367f7b3-04b6-456b-a668-fc18d2271542.png](./img/TFRyisVs9_mw-DgG/1679982466346-7367f7b3-04b6-456b-a668-fc18d2271542-278486.webp)

### Services

### DHCP (Automatic IP Address Allocation)

DHCP uses the client/server communication mode. The client submits a configuration application to the server, and the server returns the IP address assigned to the client to realize the dynamic configuration of the IP address.

The DHCP server and DHCP forwarding function are mutually exclusive.

Method for settings when the gateway is used as a DHCP server:

Click "Services >> DHCP >> DHCP Server". In the "DHCP Server" bar, check "Enable", select an interface, set the start and end IP addresses, click Add, and then click Apply & Save.

![1679982466666-2739e16a-fc43-4753-b50f-a711228881ca.png](./img/TFRyisVs9_mw-DgG/1679982466666-2739e16a-fc43-4753-b50f-a711228881ca-836939.webp)

Method for settings when the gateway is used as a DHCP client:

Click "Services >> DHCP >> DHCP Client", select the gateway interface, and click Apply & Save.

![1679982467010-7769f644-46c9-4e19-bfb4-fcf3ff691e08.png](./img/TFRyisVs9_mw-DgG/1679982467010-7769f644-46c9-4e19-bfb4-fcf3ff691e08-463210.webp)

Method for enabling DHCP forwarding for the gateway:

DHCP forwarding is also referred to as a DHCP relay agent. It can process and forward DHCP information between different subnets and physical network segments.

Click "Services >> DHCP >> DHCP Relay", check "Enable", enter the server address, select the gateway interface, and click Apply & Save.

![1679982467572-752ca4c6-5859-46fa-b52f-fb64c9c54c4d.png](./img/TFRyisVs9_mw-DgG/1679982467572-752ca4c6-5859-46fa-b52f-fb64c9c54c4d-911473.webp)

### DNS

The domain name service (DNS) is a distributed network directory service mainly used for mutual conversion between a domain name and an IP address.

Method for enabling the DNS server for the gateway:

Click "Services >> DNS >> DNS Server", enter the address of the DNS server, and click Apply & Save.

![1679982468039-a46f5c3b-8074-4881-8e12-4d89d4a6a619.png](./img/TFRyisVs9_mw-DgG/1679982468039-a46f5c3b-8074-4881-8e12-4d89d4a6a619-042607.webp)

Method for enabling DNS forwarding for the gateway:

As a DNS agent, the gateway forwards DNS request and response messages between the DNS client and the DNS server, and replaces the DNS client for domain name resolution.

If the DHCP service is enabled for the gateway, DNS forwarding is enabled by default and cannot be disabled.

Click "Services >> DNS >> DNS Relay", check "Enable DNS Relay", set the mapping between the domain name and the IP address, click Add, and then click Apply & Save. After the settings are completed, when a DNS client on the LAN requests a host domain name in the list, the DNS agent server returns the corresponding IP address to the client.

![1679982468494-011493f5-e16e-45c8-b1f0-ce89323a3b55.png](./img/TFRyisVs9_mw-DgG/1679982468494-011493f5-e16e-45c8-b1f0-ce89323a3b55-586783.webp)

### DDNS

The dynamic domain name server (DDNS) maps the dynamic IP address of the gateway to a fixed DNS. Each time a user connects to the Internet, the client program transmits the dynamic IP address of the host to the server program on the server host through information transfer. The server program provides the DDNS service and realizes dynamic domain name resolution. In this way, you can access the Internet by entering the domain name, even if the IP address is changed.

Method for enabling the DDNS service for the gateway:

1. If the Custom service is used, set "Method Name" as required, select "Custom" for "Service Type", and enter the DDNS expression "<http://user> name:[password@ddns.oray.com/ph/update?hostname=](mailto:password@ddns.oray.com/ph/update?hostname=)host name" of the server for "Url". This expression is only for reference. The actual URL is provided by the service provider (usually available on the official website of the service provider). Click Add.

If a common domain name server other than the Custom service is used, set "Method Name" and "Service Type" as required, enter the user name, password, and host name obtained from the server, and click Add.

If "Disable" is selected, the DDNS service is not used.

1. Select the gateway interface, enter the name of the DDNS update method, click Add, and then click Apply & Save to apply the DDNS update method to the gateway interface.

![1679982468873-6337b550-0f4d-4ff1-a290-8a1145b5376f.png](./img/TFRyisVs9_mw-DgG/1679982468873-6337b550-0f4d-4ff1-a290-8a1145b5376f-382066.webp)

1. Wait several minutes after the DDNS settings are applied and saved. Then ping the host name (domain name) of the domain name server to confirm the successful application of the DDNS service.

![1679982469362-2f009b9a-fa20-436a-b447-c19f1f47489c.png](./img/TFRyisVs9_mw-DgG/1679982469362-2f009b9a-fa20-436a-b447-c19f1f47489c-312898.webp)

![1679982469821-607e852e-4583-4da9-a924-61b77925b779.png](./img/TFRyisVs9_mw-DgG/1679982469821-607e852e-4583-4da9-a924-61b77925b779-937249.png)

### SMS

The short message service (SMS) is enabled for gateway restart and manual dialup via SMS messages. Some gateways can receive alarm information in the SMS whitelist.

Method for controlling gateway restart and manual dialup via SMS messages

Click "Services >> SMS" and check "Enable". In the "SMS Access Control" bar, set "ID" as required, select "permit" for "Action", enter the phone number, and click Apply & Save. When you activate the dialup port via SMS, after the configuration is completed, you can send the reboot command to restart the gateway by using the mobile phone number, or send the cellular 1 ppp up/down command to make the gateway redial or interrupt the dialup.

![1679982470213-9e8bc5af-7753-45db-8eff-4728784c594e.png](./img/TFRyisVs9_mw-DgG/1679982470213-9e8bc5af-7753-45db-8eff-4728784c594e-727260.webp)

### GPS

Position: You can view the current positioning information.

![1679982470595-70b84a90-3171-4272-b43e-ede1cc2fff7a.png](./img/TFRyisVs9_mw-DgG/1679982470595-70b84a90-3171-4272-b43e-ede1cc2fff7a-251623.webp)

Method for enabling GPS for the gateway:

Click "Services >> Enable GPS", check "Enable", and click Apply & Save. By default, GPS is enabled for the gateway.

![1679982470941-31ff282a-8578-41e2-8c0e-141907534eb9.png](./img/TFRyisVs9_mw-DgG/1679982470941-31ff282a-8578-41e2-8c0e-141907534eb9-195665.webp)

Method for forwarding GPS data to the server over IP when VG814 is used as a client:

Click "Services >> GPS IP Forwarding", check "Enable", select "Client" for "Type", enter the server address and port in the "Destination IP Address" bar, click Add, and then click Apply & Save.

![1679982471307-517777ba-6460-4654-b5ef-61d7e0b34be6.png](./img/TFRyisVs9_mw-DgG/1679982471307-517777ba-6460-4654-b5ef-61d7e0b34be6-438393.webp)

Method for forwarding GPS data over IP when VG814 is used as a server:

Click "Services >> GPS IP Forwarding", check "Enable", select "Server" for "Type", and click Apply & Save.

![1679982471770-b5e03fd4-0c0a-48df-875d-5835ffbe32a6.png](./img/TFRyisVs9_mw-DgG/1679982471770-b5e03fd4-0c0a-48df-875d-5835ffbe32a6-655425.webp)

Method for forwarding GPS data by VG814 through a serial port:

Click "Services >> GPS Serial Forwarding", check "Enable", and select a serial port type based on the data transmission port used. Ensure that the baud rate, data bits, parity bit, and stop bit are the same as the current settings. Click Apply & Save.

![1679982472281-e3751051-fb31-4820-aed4-b5e3a33b3965.png](./img/TFRyisVs9_mw-DgG/1679982472281-e3751051-fb31-4820-aed4-b5e3a33b3965-759530.webp)

### QoS

Quality of service (QoS) is a network security mechanism that enables a network to provide better services for designated network communication by using various basic technologies. It is a technology for solving problems such as network delays and blocking.

Method for setting the egress maximum bandwidth for the gateway through QoS control:

Click "QoS >> Traffic Control >> Apply QoS", select the gateway interface, enter the egress maximum bandwidth, click Add, and then click Apply & Save.

![1679982472661-382de9fb-6b36-44b4-b306-7c5b21e0ece3.png](./img/TFRyisVs9_mw-DgG/1679982472661-382de9fb-6b36-44b4-b306-7c5b21e0ece3-459491.webp)

Method for applying the ingress and egress policies for the gateway through QoS control:

1. Add a network link classifier. Click "QoS >> Traffic Control >> Classifier", check "Any Packets", set the source and destination addresses of the link, select transmit protocols for QoS control, and click Add.

2. Set transmission policies. Click "QoS >> Traffic Control >> Policy", enter a custom policy name for "Name", enter the classifier name for "Classifier", set the guaranteed bandwidth, maximum bandwidth, and policy priority, and click Add.

3. Click "QoS >> Traffic Control >> Apply QoS", select the gateway interface, enter the policy name for "Ingress Policy" and "Egress Policy", click Add, and then click Apply & Save.

![1679982473080-7b4450d1-a653-4364-89dd-34616981d8b9.png](./img/TFRyisVs9_mw-DgG/1679982473080-7b4450d1-a653-4364-89dd-34616981d8b9-981704.webp)

### Traffic Control

Method for enabling traffic control for the gateway:

Click "Services >> Traffic Control", enable traffic control, set traffic control parameters, and click Apply & Save. After the settings are completed, the system generates an alarm, stops forwarding, or disables the interface when the traffic exceeds the limit according to the settings on this page.

![1679982473458-b5bfe800-ced7-43e0-bc60-c6c46a84387e.png](./img/TFRyisVs9_mw-DgG/1679982473458-b5bfe800-ced7-43e0-bc60-c6c46a84387e-361279.webp)

### Firewall

### ACL

The access control list (ACL) is an access control technology based on packet filtering. It can filter the packets on the interface based on preset conditions and allow them to pass or discard them.

Common scenario: By default, all devices on the LAN (bridge 1) can access the Internet, except the device with the IP address of 192.168.2.100.

Method for setting VG814:

1. Click "Firewall >> ACL >> Add". Enter the ID and sequence number. A smaller sequence number indicates a higher priority. Select "deny" for "Action". Set "Source IP" to "192.168.2.100" and "Source Wildcard" to "0.0.0.0". Leave "Destination IP" empty, which indicates 0.0.0.0/0, that is, all IP addresses. Click Apply & Save.

![1679982473900-f8bec30c-d534-4ec8-99ba-c31335ed58ab.png](./img/TFRyisVs9_mw-DgG/1679982473900-f8bec30c-d534-4ec8-99ba-c31335ed58ab-607793.webp)

1. Return to the ACL page, add the rule with the ID of 101 to the management rule of bridge 1, and click Add. Click Apply & Save.

![1679982474345-53c7ee90-4238-40ce-9f22-07357df5930c.png](./img/TFRyisVs9_mw-DgG/1679982474345-53c7ee90-4238-40ce-9f22-07357df5930c-200989.webp)

### NAT

Network address translation (NAT) can be used when some hosts on a private network have been assigned with local IP addresses (that is, private IP addresses used only on the private network), but expect to communicate with hosts on the Internet (without encryption).

Common scenario: A user expects to access a camera on the LAN of the device through the public network to view the current driving conditions of the vehicle. The camera address is 192.168.2.100, and the open port 18000 provides video services.

1. Click "Firewall >> NAT", and select "DNAT" for "Action", and "Outside" for "Source Network". Select "IP PORT to IP PORT" or "INTERFACE PORT to IP PORT" for "Translation Type". The public IP address obtained through dial-up is not fixed, so "INTERFACE PORT to IP PORT" is more convenient. Select "TCP" for "Transmit Protocol" because video services are transmitted over TCP. Select "cellular 1" (dialup interface for the cellular network) for "Interface" and set "Port" to "20000". Set "IP Address" and "Port" under "Translated Address" to "192.168.200" and "18000" respectively. Click Apply & Save.

The gateway redirects the TCP service destined for port 20000 of the cellular 1 interface to the internal IP address 192.168.2.100 and port 18000, to enable access to the internal services.

![1679982474853-8afdd117-7468-4c61-ab96-b9599d383ebf.png](./img/TFRyisVs9_mw-DgG/1679982474853-8afdd117-7468-4c61-ab96-b9599d383ebf-738345.webp)

### MAC-IP Binding

After MAC-IP binding, the PC can access the public network through the gateway only by using the IP address bound to the MAC address of the PC.

Method for binding the MAC address and IP address of a connected device:

1. Click "Firewall >> ACL" and select "Block" for "Default Filter Policy".

![1679982475273-5ada5f1e-d24f-49fa-b9ca-255b54445ebf.png](./img/TFRyisVs9_mw-DgG/1679982475273-5ada5f1e-d24f-49fa-b9ca-255b54445ebf-840767.webp)

1. Click "Firewall >> MAC-IP Binding", check "Enable", enter the MAC address and IP address of the connected device, click Add, and click Apply & Save.

![1679982475725-a6594a46-3375-4aae-bc72-d6d02c5965ff.png](./img/TFRyisVs9_mw-DgG/1679982475725-a6594a46-3375-4aae-bc72-d6d02c5965ff-678535.webp)

### Routing

### Static Routing

Set the destination network, subnet mask, and interface or gateway as required.

![1679982476130-97e1ccbc-9e8e-435b-8cce-f5ef54aec7b4.png](./img/TFRyisVs9_mw-DgG/1679982476130-97e1ccbc-9e8e-435b-8cce-f5ef54aec7b4-390484.webp)

### Dynamic Routing

Scenario: Enable dynamic routing between two LANs for mutual communication between them. The topology is shown below.

![1679982476516-ded1b557-fb55-4eb8-9556-b2f21f382d79.png](./img/TFRyisVs9_mw-DgG/1679982476516-ded1b557-fb55-4eb8-9556-b2f21f382d79-215280.webp)

#### RIP

The Routing Information Protocol (RIP) is a simple internal dynamic routing protocol mainly used on small-scale networks.

Method for enabling dynamic routing between VG814_A and VG814_B over RIP in the scenario:

1. Configure VG814_A. Click "Routing >> Dynamic Routing >> RIP", check "Enable", and configure VG814_A in the "Network" bar to announce the routing entry of VG814_A.

![1679982476966-640350d9-0690-45b0-8194-97f28ec21e83.png](./img/TFRyisVs9_mw-DgG/1679982476966-640350d9-0690-45b0-8194-97f28ec21e83-405471.webp)

1. Configure VG814_B.

![1679982477341-7a8c01d8-f42c-4414-9523-4cd18782bab7.png](./img/TFRyisVs9_mw-DgG/1679982477341-7a8c01d8-f42c-4414-9523-4cd18782bab7-523863.webp)

1. After the configuration is completed, check whether PC 1 can communicate with PC 2. If yes, the dynamic route is added successfully. The RIP route learned by VG814_B is shown in the figure below.

![1679982477787-b5e824bd-f320-425b-82b5-c8d2e87fb7a3.png](./img/TFRyisVs9_mw-DgG/1679982477787-b5e824bd-f320-425b-82b5-c8d2e87fb7a3-922303.webp)

#### OSPF

The Open Shortest Path First (OSPF) protocol is a link-status-based internal gateway protocol mainly used on large-scale networks.

Method for enabling dynamic routing between VG814_A and VG814_B over OSPF in the scenario:

1. Configure VG814_A. Click "Routing >> Dynamic Routing >> OSPF", check "Enable", enter a valid IP address for "Router ID", and configure VG814_A in the "Network" bar to announce the routing entry of VG814_A.

![1679982478180-24f48e17-3b7c-4341-86d5-f765bb875739.png](./img/TFRyisVs9_mw-DgG/1679982478180-24f48e17-3b7c-4341-86d5-f765bb875739-798830.webp)

1. Set parameters for VG814_B.

![1679982478598-5b3e5359-f759-4f84-bf72-19dc6bc124dc.png](./img/TFRyisVs9_mw-DgG/1679982478598-5b3e5359-f759-4f84-bf72-19dc6bc124dc-422630.webp)

1. After the configuration is completed, check whether PC 1 can communicate with PC 2. If yes, the dynamic route is added successfully. The OSPF route learned by VG814_B is shown in the figure below.

![1679982479037-174c65d0-ddd4-4b0c-be79-76d688483c21.png](./img/TFRyisVs9_mw-DgG/1679982479037-174c65d0-ddd4-4b0c-be79-76d688483c21-894448.webp)

#### BGP

Method for enabling dynamic routing between VG814_A and VG814_B over BGP in the scenario:

1. Configure VG814_A. Click "Routing >> Dynamic Routing >> BGP", check "Enable", and set "AS number" as required.

![1679982479405-ded080dd-ea75-40ff-93fe-071023c7871b.png](./img/TFRyisVs9_mw-DgG/1679982479405-ded080dd-ea75-40ff-93fe-071023c7871b-979093.webp)

1. In the "Neighbor" bar, click Add, enter the IP address 192.168.1.2 of VG814_B, set "AS number" as required, and click Apply & Save.

![1679982479862-69db06a1-9720-483c-a0c6-c4f3c7b494cb.png](./img/TFRyisVs9_mw-DgG/1679982479862-69db06a1-9720-483c-a0c6-c4f3c7b494cb-235134.webp)

1. Enter a valid IP address for "Router ID", configure VG814_A in the "Network" bar, and click Add, to announce the routing entry of VG814_A. Then click Apply & Save.

![1679982480215-8404451a-ea14-4644-927b-67b15e86db2f.png](./img/TFRyisVs9_mw-DgG/1679982480215-8404451a-ea14-4644-927b-67b15e86db2f-230584.webp)

1. Set parameters for VG814_B. The parameters are the same as or corresponding to those of VG814_A.

![1679982480628-0490a555-175d-4d60-a45d-14ba2f13dc3a.png](./img/TFRyisVs9_mw-DgG/1679982480628-0490a555-175d-4d60-a45d-14ba2f13dc3a-644273.webp)

1. After the configuration is completed, check whether PC 1 can communicate with PC 2. If yes, the dynamic route is added successfully. The BGP route learned by VG814_B is shown in the figure below.

![1679982481059-0c1d50d1-9010-4a80-b2c9-c4ddfd5817cf.png](./img/TFRyisVs9_mw-DgG/1679982481059-0c1d50d1-9010-4a80-b2c9-c4ddfd5817cf-325879.webp)

### Link Backup

### SLA

The service level agreement (SLA) is used to detect whether the link between the gateway and the ISP fails.

Method for adding an SLA entry for the gateway:

Click "Link Backup >> SLA >> Add", enter the detected IP address for "Destination Address", set other parameters as required, click Add, and then click Apply & Save.

Timeout (ms) indicates the duration for determining a detection failure. Consecutive indicates the number of detection failures resulting in a link failure.

![1679982481511-1f9e547d-3459-4ac5-9c57-034b4be5ef73.png](./img/TFRyisVs9_mw-DgG/1679982481511-1f9e547d-3459-4ac5-9c57-034b4be5ef73-920805.webp)

### Track

Currently, linkage is enabled between the track module and the following application modules: VRRP, static routing, and interface backup. If detection succeeds, the corresponding track entry is in the Positive state. If detection fails, the corresponding track entry is in the Negative state.

Method for adding a track entry for VG814:

Click "Link Backup >> Track >> Track", set "Index" as required, select "sla", "interface", or "vrrp" for "Type", set "SLA/VRRP ID" based on the ID in the SLA list, set "Negative Delay (s)" and "Positive Delay (s)" as required, click Add, and then click Apply & Save.

Negative Delay (s): In case of an abnormal state, switching can be delayed based on the delay setting (0 indicates immediate switching).

Positive Delay (s): When a failure is recovered, switching can be delayed based on the delay setting (0 indicates immediate switching).

![1679982481996-3bbcc2dc-eacd-4c92-abfa-0e422bb09a46.png](./img/TFRyisVs9_mw-DgG/1679982481996-3bbcc2dc-eacd-4c92-abfa-0e422bb09a46-548642.webp)

Method for adding an IPsec track entry for VG814:

Click "Link Backup >> Track >> Track" and set "Index" as required. "positive-start/negative-stop" means starting the IPsec service when the track detection state is Positive and stopping the IPsec service when the track detection state is Negative.

![1679982482400-299de8b1-015e-4822-b10e-8fb4a4fe2707.png](./img/TFRyisVs9_mw-DgG/1679982482400-299de8b1-015e-4822-b10e-8fb4a4fe2707-150934.webp)

### VRRP

Scenario: Multiple gateways are connected to a network at the same time. Gateway A acts as the host, and gateway B acts as a backup for gateway A. When gateway A fails, gateway B temporarily replaces gateway A as the host.

1. Networking requirement

Host A uses the VRRP backup group comprising gateway A and gateway B as its default gateway to access host B on the Internet.

Information of the VRRP backup group:

● The backup group ID is 1.

● The IP address of the virtual gateway of the backup group is 10.5.16.88.

● Gateway A acts as the master gateway.

● Gateway A acts as a backup gateway that can be preempted.

1. Networking diagram

![1679982482837-1545c79f-fa84-41f6-992e-d7fb5e1edef2.png](./img/TFRyisVs9_mw-DgG/1679982482837-1545c79f-fa84-41f6-992e-d7fb5e1edef2-738688.webp)

| Gateway | Ethernet port connected to host A | IP address of the port connected to host A | Priority | Work mode |
| --- | --- | --- | --- | --- |
| VG814_A | bridge 1 | 10.5.16.80 | 110 | Preemption |
| VG814_B | bridge 1 | 10.5.16.81 | 100 | Preemption |

Method for settings when VG814_A acts as the master gateway and VG814_B as a backup gateway:

1. Configure VG814_A.

Click "Link Backup >> VRRP", set "Virtual Route ID" as required, select the gateway interface of VG814_A, enter the virtual IP address, set the interface priority to 110, and click Add.

![1679982483192-bd7eb48a-d05c-4215-8819-0f4bd45fcba6.png](./img/TFRyisVs9_mw-DgG/1679982483192-bd7eb48a-d05c-4215-8819-0f4bd45fcba6-573755.webp)

In the navigation tree, click "Link Backup >> VRRP >> Status" and view the VRRP status.

![1679982483554-7c980083-5555-46ec-bfde-c450640b2bd4.png](./img/TFRyisVs9_mw-DgG/1679982483554-7c980083-5555-46ec-bfde-c450640b2bd4-973414.webp)

1. Configure VG814_B.

Click "Link Backup >> VRRP", set the interface priority to 100, and click Add.

![1679982484031-28061002-b074-43a2-bbd3-d20735e22e7f.png](./img/TFRyisVs9_mw-DgG/1679982484031-28061002-b074-43a2-bbd3-d20735e22e7f-976629.webp)

In the navigation tree, click "Link Backup >> VRRP >> Status" and view the VRRP status.

![1679982484429-7ee0f610-3462-4322-ad0b-3d7429ddb9dc.png](./img/TFRyisVs9_mw-DgG/1679982484429-7ee0f610-3462-4322-ad0b-3d7429ddb9dc-837721.webp)

Under normal circumstances, VG814_A performs gateway functions. When VG814_A is shut down or fails, VG814_B performs gateway functions. The preemption mode is intended to enable VG814_A to continue to act as the master gateway after it recovers.

#### Interface Backup

Scenario: VG814 accesses the Internet via Wi-Fi, and an interface backup is created to enable VG814 to access the Internet through dial-up upon Wi-Fi failure. The topology is shown below.

![1679982484844-3d42e55d-0a75-44fb-85e1-741fb2f843e4.png](./img/TFRyisVs9_mw-DgG/1679982484844-3d42e55d-0a75-44fb-85e1-741fb2f843e4-230197.webp)

Method for creating an interface backup for the gateway:

1. Enable VG814 to access the Internet via Wi-Fi.

![1679982485173-c8276204-307f-4e0f-a5e9-f285f099bb4a.png](./img/TFRyisVs9_mw-DgG/1679982485173-c8276204-307f-4e0f-a5e9-f285f099bb4a-750913.webp)

1. Click "Link Backup >> SLA >> SLA >> Add" to add an ICMP detection entry. Set the IP address to the host address that can be detected over ICMP on the public or private network, for example, the public IP address 118.122.120.22. Click Apply & Save.

![1679982485556-a686663b-4734-4474-93e0-b9c37e1c3e17.png](./img/TFRyisVs9_mw-DgG/1679982485556-a686663b-4734-4474-93e0-b9c37e1c3e17-788650.webp)

1. Click "Link Backup >> Track >> Track >> Add" to add a track entry. Select "sla" for "Type" and "dot11radio1" for "Interface", click Add, and then click Apply & Save.

![1679982485987-bff88041-8696-499d-9141-1e94cc68b3c5.png](./img/TFRyisVs9_mw-DgG/1679982485987-bff88041-8696-499d-9141-1e94cc68b3c5-575276.webp)

1. Click "Link Backup >> Interface Backup >> Add", select "dot11radio1" for "Main Interface" and "cellular1" for "Backup Interface", and click Apply & Save.

![1679982486381-7b589dce-e04e-4eec-9e99-27e9b0e088d1.png](./img/TFRyisVs9_mw-DgG/1679982486381-7b589dce-e04e-4eec-9e99-27e9b0e088d1-940827.webp)

1. Click "Routing >> Static Routing >> Add" and add two routes for network access through the "dot11radio1" and "cellular1" interfaces. A smaller value of "Distance" indicates a higher priority.

![1679982486710-7b862095-4b09-483e-aa70-4b502792b745.png](./img/TFRyisVs9_mw-DgG/1679982486710-7b862095-4b09-483e-aa70-4b502792b745-747571.webp)

1. Trigger a Wi-Fi failure. According to the preset link detection policy, VG814 accesses the Internet through dial-up via the cellular port, and when Wi-Fi recovers, immediately switches to Wi-Fi for Internet access.

### Wizards

The "Wizards" module incorporates some common communication parameters, simplifying the operations.

New Cellular

After a common network interface card (NIC) is inserted, click "Wizards >> New Cellular >> Apply & Save" and access the status page to view the network connection status of the device. The device is connected to the network.

![1679982487077-89182127-e2cd-439b-b0c4-92636643333d.png](./img/TFRyisVs9_mw-DgG/1679982487077-89182127-e2cd-439b-b0c4-92636643333d-735316.webp)

![1679982487420-6e8f461c-0951-4b92-a2d4-595dd8fb06d8.png](./img/TFRyisVs9_mw-DgG/1679982487420-6e8f461c-0951-4b92-a2d4-595dd8fb06d8-669116.webp)

### New IPsec Tunnel

A dedicated virtual tunnel is established between the gateway and other devices or cloud platforms on the network.

Method for establishing an IPsec tunnel for the gateway:

Click "Wizards >> New IPsec Tunnel", set "Map Interface" to an interface ("bridge": bridge interface; "cellular": dialup interface; "dot11radio": Wi-Fi interface) for which you want to establish a tunnel, enter the peer IP address for "Destination Address", and enter the subnet IP addresses and masks at both ends of the tunnel. In Phase 1, enter the IDs at both ends of the tunnel and the connection key, and click Apply & Save.

![1679982487827-4c89e8c8-34a6-4f67-b89d-2a6642c74c0c.png](./img/TFRyisVs9_mw-DgG/1679982487827-4c89e8c8-34a6-4f67-b89d-2a6642c74c0c-562218.webp)

### IPsec Experts' Configuration

This function is available only for specific users. To activate this function, contact the technical support personnel.

### New L2TPv2 Tunnel

Method for creating an L2TPv2 tunnel for the gateway:

Set the parameters of the L2TP server and the local/remote addresses. Click Apply & Save.

![1679982488226-4b816847-5e62-457a-bf6a-85efe41e7ad6.png](./img/TFRyisVs9_mw-DgG/1679982488226-4b816847-5e62-457a-bf6a-85efe41e7ad6-086000.webp)

### New Port Mapping

Port mapping is to map a port of a host on the intranet to a port of a host on the extranet to provide corresponding services. When a user accesses the port on the extranet, the server automatically maps the request to the internal machine on the corresponding LAN.

Scenario: Users on the extranet cannot directly access a web server on the intranet. In this case, a port mapping can be created on the gateway so that the gateway automatically transfers the data to port 80 of the web server on the intranet when a user on the extranet accesses port 1000 via the cellular interface of the gateway.

![1679982488558-b391fe5c-24ff-428b-84dc-0f3a23cc2fc1.png](./img/TFRyisVs9_mw-DgG/1679982488558-b391fe5c-24ff-428b-84dc-0f3a23cc2fc1-146314.webp)

Method for creating a port mapping for the gateway:

Click Wizards >> New Port Mapping". Enter the gateway interface for "Outside Interface", gateway port for "Service Port", IP address of the internal host for "Internal Address", and port ID of the internal host for "Internal Port". Click Apply & Save.

![1679982488927-de7b22c3-7f72-4f0a-b395-7682b7c46f00.png](./img/TFRyisVs9_mw-DgG/1679982488927-de7b22c3-7f72-4f0a-b395-7682b7c46f00-838881.webp)

### Captive Portal

![Network Captive Portal](./img/TFRyisVs9_mw-DgG/1748930749207-fff4d235-5f5d-4f6a-a6d5-d006da832c35-697692.webp)

At present, the implementation of VG710/VG814 Captive Portal adopts a combination of WiFi dog open source project and Captive Portal application program. WiFidog mainly handles network level related content, such as intercepting any requests from unverified clients, whitelist processing, and port 80

HTTP request redirection, related iptables rules distribution, and billing related content (such as receiving and sending statistics).

The Captive Portal service has enabled an HTTP server, which mainly cooperates with Wifido to handle authentication related processing logic and configure access rules

(Based on time and traffic).

![1695883248919-ca39ae9a-af0b-417a-badb-ef8f9939cdf5.png](./img/TFRyisVs9_mw-DgG/1695883248919-ca39ae9a-af0b-417a-badb-ef8f9939cdf5-661087.webp)

## 6. Edge computing and app functions

App function is an important part of the gateway to realize edge computing. The prerequisite for using this feature is to install the python SDK.

### 6.1 APP Status

This page is to upgrade the SDK of Python to view the edge computing environment.

![1679982489296-67d29b21-c4af-4282-899f-a05fb6b8c32c.png](./img/TFRyisVs9_mw-DgG/1679982489296-67d29b21-c4af-4282-899f-a05fb6b8c32c-620057.webp)

### 6.1.2 APP Management

This page opens app management to manage Python apps.

If you need to link the gateway for development, you need to Enable the IDE debug function

![1679982489808-4a7b3fd9-f24b-4545-8e95-0182695a7c66.png](./img/TFRyisVs9_mw-DgG/1679982489808-4a7b3fd9-f24b-4545-8e95-0182695a7c66-922601.webp)

Open the imported app, check it in the app list, and then click button Apply & Save button

![1679982490327-026f5687-ccb8-49b7-96a1-441732783f65.png](./img/TFRyisVs9_mw-DgG/1679982490327-026f5687-ccb8-49b7-96a1-441732783f65-664710.webp)

For more guidance on app development, please refer to the development documentation. [https://www.inhandnetworks.com/downlist/cid-114](https://www.inhandnetworks.com/downlist/cid-114)

### 6.2 APP Docker function

Enable the docker function of the gateway.

![1679982490849-87969775-e0ae-457a-aa88-3f80ec9eab50.png](./img/TFRyisVs9_mw-DgG/1679982490849-87969775-e0ae-457a-aa88-3f80ec9eab50-988210.webp)

Click the “Go to the docker management page” default username admin password 12345678

Enter the docker management page.

![1679982491323-56b39c88-3a39-4ac4-9e4c-9b98459b0cea.png](./img/TFRyisVs9_mw-DgG/1679982491323-56b39c88-3a39-4ac4-9e4c-9b98459b0cea-513111.webp)

![1679982491783-05eb69db-88db-49a8-9242-ee3ed6cc1703.png](./img/TFRyisVs9_mw-DgG/1679982491783-05eb69db-88db-49a8-9242-ee3ed6cc1703-461039.webp)

![1679982492305-65ae439f-e1f3-494e-81b7-48f424a7a730.png](./img/TFRyisVs9_mw-DgG/1679982492305-65ae439f-e1f3-494e-81b7-48f424a7a730-443350.webp)

For container management tools, visit: [https://www.portainer.io/](https://www.portainer.io/)

### 6.3 Third party cloud platform

The gateway device connects to the cloud platform as a client to realize communication, and obtains data in real time according to the corresponding configuration of the gateway device to achieve the purpose of data interaction.

### 6.3.1 MQTT protocol connection to cloud platform

Step 1: click "APP>> third party cloud platform > >mqtt>> enable", select the address and port of the cloud platform server, click apply and save.

Which fields are sent to the platform by default, and the FlexAPI config can be config.

![1679982492866-f98dbf3a-d695-4071-a1af-9678cbdb1c87.png](./img/TFRyisVs9_mw-DgG/1679982492866-f98dbf3a-d695-4071-a1af-9678cbdb1c87-703315.webp)

Step 2: click status. If the connection status is connected, the connection is successful.

![1679982493392-46694676-4a08-4272-ae57-7372710bba9d.png](./img/TFRyisVs9_mw-DgG/1679982493392-46694676-4a08-4272-ae57-7372710bba9d-689955.webp)

Note: if the server needs authentication and encryption, it needs to be enabled correspondingly. Click "app>> third party cloud platform > >mqtt>> enable", select the address and port of the cloud platform server, and enable mqtt authentication and TLS encryption.

![1679982494018-a8f7791d-9c37-4ebe-8e32-26720cad839a.png](./img/TFRyisVs9_mw-DgG/1679982494018-a8f7791d-9c37-4ebe-8e32-26720cad839a-694618.webp)

### 6.3.2 TCP protocol connection to cloud platform

Step 1: click "app>> third party cloud platform > >tcp>> enable", select the address and port of the cloud platform server, click apply and save

![1679982494918-b9ad4a00-4dbc-4bef-a1c3-229a5bc4f245.png](./img/TFRyisVs9_mw-DgG/1679982494918-b9ad4a00-4dbc-4bef-a1c3-229a5bc4f245-602845.webp)

Step 2: click status. If the connection status is connected, the connection is successful.

![1679982495430-0ec63929-6048-456a-8350-cf4f50065f0d.png](./img/TFRyisVs9_mw-DgG/1679982495430-0ec63929-6048-456a-8350-cf4f50065f0d-031732.webp)

### 6.4 Local MQTT Agent

The gateway device acts as an mqtt server to proxy messages. When users need messages, they use the mqtt client to subscribe to information. Python App or Doker program use gateway info, Subscribe to messages from the local mqtt agent.

Step 1: click "app>> local mqtt agent > > enable local / local &amp; Lan", click apply and save

![1679982495932-97fb57eb-b0f9-4fed-a285-1d13c99bbb02.png](./img/TFRyisVs9_mw-DgG/1679982495932-97fb57eb-b0f9-4fed-a285-1d13c99bbb02-921402.webp)

Step 2: use mqtt client information: server address, port, authentication and other information

This document uses mqtt Take FX test tool as an example.

![1679982496368-b8a0ca11-8b56-442e-8d44-72be76a6c6b6.png](./img/TFRyisVs9_mw-DgG/1679982496368-b8a0ca11-8b56-442e-8d44-72be76a6c6b6-638190.webp)

Step 3: click Connect. If the icon turns green, it means the connection is successful. Then subscribe to the information according to the topic document. The gateway will return data in JSON format. For example, subscribe to cellular information

![1679982496888-4bbcdf51-bb19-4744-94db-d5c65bed62b1.png](./img/TFRyisVs9_mw-DgG/1679982496888-4bbcdf51-bb19-4744-94db-d5c65bed62b1-801287.webp)

### 6.5 REST API

In addition to using mqtt and TCP to obtain data, users can also use rest APIs to call data according to interface documents

Step 1: click "app>>rest api>> enable", select the address and port of the cloud platform server, click apply and save

![1679982497402-2fa76d77-db71-4cb6-9e87-b9382555323b.png](./img/TFRyisVs9_mw-DgG/1679982497402-2fa76d77-db71-4cb6-9e87-b9382555323b-139166.webp)

Step 2: use tools such as postman according to the interface document to call the interface to obtain data.

1. Fill in the URL, token, etc. in the interface document, and note whether it is a get or post request;

2. Click send;

3. Finally, the gateway device will return the corresponding data results in JSON format;

![1679982497912-698c790f-3abc-409f-8d8f-b733f777b917.png](./img/TFRyisVs9_mw-DgG/1679982497912-698c790f-3abc-409f-8d8f-b733f777b917-366101.webp)

### 6.6 Azure IoT Edge

Click "APP>>Azure IOT edge>> enable", click apply and save

![1679982498409-6cde74dd-9d2d-4b28-ac48-9170c033ae31.png](./img/TFRyisVs9_mw-DgG/1679982498409-6cde74dd-9d2d-4b28-ac48-9170c033ae31-630533.webp)

Note: this function item depends on docker. The docker function should be opened before opening

### 6.7 User Data

Step 1: click "APP>> User Data> > User Data Management", then enter the name and corresponding value, click add, and finally click apply and save.

![1679982498871-f8e54bab-5679-440a-8dc1-ece60b2d5179.png](./img/TFRyisVs9_mw-DgG/1679982498871-f8e54bab-5679-440a-8dc1-ece60b2d5179-201736.webp)

Step 2: click "status". If the data exists in the status bar, it means that the addition is successful.

![1679982499357-9fdb178c-a790-4c1f-8d5a-54400991860e.png](./img/TFRyisVs9_mw-DgG/1679982499357-9fdb178c-a790-4c1f-8d5a-54400991860e-349059.webp)

## 7. Connecting the Gateway to a Cloud Platform

1. Click "Administration >> Device Manager >> Device Manager", check "Device Manager Enable", select the server address of the cloud platform, enter the registered account and license plate number of the cloud platform, and click Apply & Save.

![1679982499815-14eac0a7-99ed-479a-9a90-5ab3bc9918ac.png](./img/TFRyisVs9_mw-DgG/1679982499815-14eac0a7-99ed-479a-9a90-5ab3bc9918ac-562375.webp)

1. Click "Status". "Connected" indicates that the gateway is successfully connected to the cloud platform.

## 8. Industrial Ports (Serial Ports)

The industrial ports of VG814 include RS232 serial ports, RS485 serial ports, and IO ports.

![1679982500478-6510ef78-618e-4b3c-b6dc-08b438d6d465.png](./img/TFRyisVs9_mw-DgG/1679982500478-6510ef78-618e-4b3c-b6dc-08b438d6d465-316496.webp)

VG814 Rail version

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Signal | GND | DO2 | DO4 | DO6 | GND | RS232_RX1 | RS232_RX2 | GND | CAN_L | RS485_A |
| PIN | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Signal | GND | DO3 | DO5 | DO7 | GND | RS232_TX1 | RS232_TX2 | GND | CAN_H | RS485_B |

VG814 Road version

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Signal | GND | DO2 | DO4 | WHEEL TICK* | GND | RS232_RX1 | L-Channel | GND | CAN0_L | RS485_B |
| PIN | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Signal | GND | DO3 | PPS | FWD* | GND | RS232_TX1 | R-Channel | Mic In | CAN0_H | RS485_A |

### 8.1 DTU

1. Method for setting web pages when the gateway is used as a DTU:

Enable DTU 1 (RS232-1) DTU 2 (RS232-2) or DTU 3 (RS-485). Set the connection parameters of the gateway interface and industrial device.

1. Communication is available only when the parameters at both ends of the network link are consistent.

![1679982501152-ff16726f-5750-41c3-9c78-e9bf62dea667.png](./img/TFRyisVs9_mw-DgG/1679982501152-ff16726f-5750-41c3-9c78-e9bf62dea667-150063.webp)

1. Set the IP address and transmit protocol (TCP or UDP) of the server.

![1679982501663-5c99f9c4-4899-4db0-95a6-07f57ef98b61.png](./img/TFRyisVs9_mw-DgG/1679982501663-5c99f9c4-4899-4db0-95a6-07f57ef98b61-915845.webp)

1. Check that the gateway-connected PC and the server exchange data through DTU.

![1679982502092-5321b07e-1c0a-4a4b-9ef2-2679c260b4ec.png](./img/TFRyisVs9_mw-DgG/1679982502092-5321b07e-1c0a-4a4b-9ef2-2679c260b4ec-057825.webp)

### 8.2 IO Ports

The AUX port has 11 digital inputs，ETX port has 7 digital inputs. The digital parameters correspond to two states: HIGH (1) and LOW (0).

![1679982502643-611f095a-51fa-4da3-bb2f-bbbe7e8b2df0.png](./img/TFRyisVs9_mw-DgG/1679982502643-611f095a-51fa-4da3-bb2f-bbbe7e8b2df0-277275.webp)

VG814 railway version:

Power input range: DC 9V ~ 36V.

DI: at present, this version takes the power supply voltage limit as the maximum voltage, that is, the input voltage range is DC 0V ~ 36V; It is determined as low (L) below 5V and high (H) above 7.2V.

DO: at present, this version takes the power supply voltage limit as the maximum voltage, that is, the maximum input voltage is DC 36V; The typical input current can reach 450mA.

Supplement:

1.The above DIis the voltage range given for the external wet contact. At this time, the internal pull-up of VG814 cannot be used.

1. When the di external is connected to the dry contact, the vg814 can provide 12V pull-up level internally, and the pull-up resistance is 20K Ω.

2. When do is used as open drain output, the typical perfusion current can reach 450mA.

3. When do pull-up is used as output, it can output high-level signal. The open circuit test voltage is 12V, and the pull-up resistance is 20K Ω. It has no load capacity.

VG814 vehicle version

Power input range: DC 9V ~ 48V.

DI: at present, this version takes the power supply voltage limit as the maximum voltage, that is, the input voltage range is DC 0V ~ 48V; It is determined as low below 1V and high above 2.7V.

DO: at present, this version takes the power supply voltage limit as the maximum voltage, that is, the maximum input voltage is DC 48V; The typical input current can reach 450mA.

Supplement:

1. The above DI is the voltage range given for the external wet contact. At this time, the internal pull-up of vg814 cannot be used.

2. When Di external dry contact is connected, vg814 can provide the same pull-up level as the power supply voltage internally, and the pull-up resistance is 20K Ω.

3. When do is used as open drain output, the typical perfusion current can reach 450mA.

4. When do pull-up is used as output, it can output high-level signal. The open circuit test voltage is the same as the power supply voltage. The pull-up resistance is 20K Ω and has no load capacity.

### 8.2.1 IO link mode

Wet node link mode, need config : DI1 disable pull up use CLI. Off is 0, On is 1.

![1679982503168-c0f21b56-2385-4fda-902f-1a8edcaedf4f.png](./img/TFRyisVs9_mw-DgG/1679982503168-c0f21b56-2385-4fda-902f-1a8edcaedf4f-515066.webp)

Dry node link mode, need config : DI1 pull up use CLI. On is 1, Off is 0.

![1679982503595-32c13f2b-aa62-46d3-83c9-f880ecbb2196.png](./img/TFRyisVs9_mw-DgG/1679982503595-32c13f2b-aa62-46d3-83c9-f880ecbb2196-867755.webp)

Dry node link mode, need config : DO1 pull up use CLI. On is 1, Off is 0.

![1679982503991-edbfb1c6-3179-40a9-9737-4845f7e41b8a.png](./img/TFRyisVs9_mw-DgG/1679982503991-edbfb1c6-3179-40a9-9737-4845f7e41b8a-391328.webp)

## 9. System Management

### 9.1 System

Click "Administration >> System >> Status" and view the current system and network status of the device.

![1679982505326-f2ce37f8-e5f6-4f12-8e5c-0b1a4245bdb9.png](./img/TFRyisVs9_mw-DgG/1679982505326-f2ce37f8-e5f6-4f12-8e5c-0b1a4245bdb9-811477.webp)

Click "Basic Setup" and modify the system language and device name.

![1679982505724-549bf5b6-7783-4d00-9e20-ace2ef06518b.png](./img/TFRyisVs9_mw-DgG/1679982505724-549bf5b6-7783-4d00-9e20-ace2ef06518b-242674.webp)

### 9.2 System Time

To ensure the coordination between the device and other devices, set the system time accurately.

Manual time synchronization: Click "Administration >> System Time >> System Time >> Sync Time" to ensure consistency between the gateway time and host time.

![1679982506146-aa3ac0f2-f750-4d0d-b52c-14c7450ff29d.png](./img/TFRyisVs9_mw-DgG/1679982506146-aa3ac0f2-f750-4d0d-b52c-14c7450ff29d-670056.webp)

Alternatively, click "Administration >> System >> Status" to synchronize the time.

![1679982506559-9db809bd-ebca-429e-8430-5af523e96fce.png](./img/TFRyisVs9_mw-DgG/1679982506559-9db809bd-ebca-429e-8430-5af523e96fce-268735.webp)

Automatic time synchronization: Click "Administration >> System Time >> SNTP Client or NTP Server" and check "Enable" to synchronize the time between the gateway and the SNTP or NTP server.

After NTP is enabled, the gateway can synchronize time for all devices on the network.

![1679982506985-e77070b6-77eb-4c11-a605-cdcc14d3f56e.png](./img/TFRyisVs9_mw-DgG/1679982506985-e77070b6-77eb-4c11-a605-cdcc14d3f56e-506240.webp)

### 9.3 Management Services

When the gateway requires the HTTP, HTTPS, TELNET, and SSH functions, click "Administration >> Management Services", enable the services, and click Apply & Save.

![1679982507404-408d697a-aa29-430f-a990-e146dadc6ce6.png](./img/TFRyisVs9_mw-DgG/1679982507404-408d697a-aa29-430f-a990-e146dadc6ce6-125609.webp)

![1679982507784-1fedf7d5-9069-441d-9b61-1bc80c9f8fb0.png](./img/TFRyisVs9_mw-DgG/1679982507784-1fedf7d5-9069-441d-9b61-1bc80c9f8fb0-931349.webp)

### 9.4 User Management

Click "Administration >> User Management" and create users, modify passwords, or delete users on the user management page.

Superuser and common user:

● Superuser: By default, only one superuser is automatically created by the system, with the username of adm and the default password of 123456. It has full access rights for the gateway.

● Common user: A common user is created by the superuser. It can view or modify gateway configurations.

| ![1679982508079-c7073083-0cbd-4450-9cb3-59fcb67f8d4a.png](./img/TFRyisVs9_mw-DgG/1679982508079-c7073083-0cbd-4450-9cb3-59fcb67f8d4a-175293.png)Note: You cannot delete the superuser (adm) or modify its username, but can modify its password. |
| --- |

### 9.5 AAA

Authentication, authorization, and accounting (AAA) is a security management mechanism for access control in network security, which provides three security services: authentication, authorization, and accounting.

It provides modular methods for the following services:

● Authentication: Verify whether a user has the right for network access.

● Authorization: Authorize a user to use specific services.

● Accounting: Record network resource usage of a user.

You can use only one or two of the security services provided by AAA. For example, if a company only expects to authenticate employees when they access specific resources, the network administrator only needs to configure the authentication server. However, if the company expects to record the network usage of employees, the accounting server must be configured.

AAA usually works in the client/server structure, which is highly scalable and is convenient for centralized management of user information, as shown in the figure below.

![1679982508391-22ef6977-3b7e-4cc5-8127-d297cd9d5722.png](./img/TFRyisVs9_mw-DgG/1679982508391-22ef6977-3b7e-4cc5-8127-d297cd9d5722-484903.webp)

| ![1679982508774-4d1400ff-1385-48d5-8334-84171306b31f.png](./img/TFRyisVs9_mw-DgG/1679982508774-4d1400ff-1385-48d5-8334-84171306b31f-707724.png) Note: Radius, Tacacs+, and LDAP indicate authentication and authorization servers. Local indicates the local user name and password of the gateway. |
| --- |

### 9.5.1 Radius

The Remote Authentication Dial In User Service (Radius) is a distributed information exchange protocol based on the client/server structure. It protects the network from unauthorized access, and is usually used in various network environments that require high security and allow remote user access.

Method for enabling the Radius server for the gateway:

Click "Administration >> AAA >> Radius". In "Server List", enter the server address (domain name/IP address), port ID, and authentication key, click Add, and then click Apply & Save.

![1679982509070-ed71b004-724b-455e-9435-735c4b71a15b.png](./img/TFRyisVs9_mw-DgG/1679982509070-ed71b004-724b-455e-9435-735c4b71a15b-126517.webp)

### 9.5.2 Tacacs+

The Terminal Access Controller Access Control System + (Tacacs+) protocol is similar to the Radius protocol. It uses the client/server mode for communication between the network access server (NAS) and the Tacacs+ server. However, Tacacs+ works based on TCP, and Radius works based on UDP.

The Tacacs+ protocol is mainly used for AAA of end users and Point-to-Point Protocol (PPP) and virtual private dial-up network (VPDN) access users. Its typical application is to authenticate, authorize, and perform accounting for an end user who needs to log in to the device for operations. As a Tacacs+ client, the device sends the user name and password to the Tacacs+ server for verification. After authentication and authorization, the user can log in to the device for operations.

Method for enabling the Tacacs+ server for the gateway:

Click "Administration >> AAA >> Tacacs+". In "Server List", enter the server address (domain name/IP address), port ID, and authentication key, click Add, and then click Apply & Save.

![1679982509485-5176fbc6-7612-4ed2-b02c-db1d63655d69.png](./img/TFRyisVs9_mw-DgG/1679982509485-5176fbc6-7612-4ed2-b02c-db1d63655d69-435756.webp)

### 9.5.3 LDAP

The main advantage of the Lightweight Directory Access Protocol (LDAP) lies in its quick response to users' search operations. For example, massive user authentication operations may be performed concurrently. If a database is used, because the database is divided into various tables, to meet this simple authentication requirement, the database must be searched each time, along with synthesis and filtering. This results in low efficiency. LDAP is equivalent to one table, and requires only the user name and password, with some other parameters, which is quite simple. It can meet the authentication requirement regarding the efficiency and structure.

Method for enabling the LDAP server for the gateway:

Click "Administration >> AAA >> LDAP". In "Server List", enter any name for "Name", enter the server address (domain name/IP address) and port ID, and enter the base DN obtained from the server. Set the user name and password for accessing the server. Select "None", "SSL", or "StartTLS" for "Security". Click Add, and then click Apply & Save.

![1679982509927-9b655074-5d96-47f2-aa6c-6795268211ae.png](./img/TFRyisVs9_mw-DgG/1679982509927-9b655074-5d96-47f2-aa6c-6795268211ae-090340.webp)

### 9.5.4 AAA Authentication

AAA authentication methods:

● No authentication (none): No validity check is performed. Generally, this method is not used.

● Local authentication (local): User information is configured on the NAS. Local authentication is fast, which can reduce the operational costs, but the information storage amount is limited by hardware.

● Remote authentication: User information is configured on the authentication server. Remote authentication is supported over Radius, Tacacs+, and LDAP.

AAA authorization methods:

● No authorization (none): No authorization is performed for users.

● Local authorization (local): Authorization is performed based on the properties configured by the NAS for the local account.

● Tacacs+ authorization: Users are authorized by the Tacacs+ server.

● Authorization after successful Radius authentication: Authorization is bound to authentication, and cannot be performed independently over Radius.

● LDAP authorization

Method for enabling authentication and authorization for the gateway:

Click "Administration >> AAA >> AAA Settings". 1, 2, and 3 are corresponding to Radius, Tacacs, ad LDAP respectively. Authentication entries 1, 2, and 3 must be corresponding to authorization entries 1, 2, and 3 respectively. When all of radius, tacacs+, and local are set, the priority sequence is as follows: 1 > 2 > 3.

![1679982510364-beb7e794-5930-4929-b6b3-546c17a4554e.png](./img/TFRyisVs9_mw-DgG/1679982510364-beb7e794-5930-4929-b6b3-546c17a4554e-978641.webp)

### 9.6 Configuration Management

Method for importing configurations: Click "Administration >> Config Management >> Config Management >> Browse", select a configuration file, and click Import to import the configuration file to the gateway.

Method for backing up current running configurations to the PC (common): Click Backup running-config.

Method for backing up the startup file to the PC: Click Backup startup-config.

Method for restoring default configurations: Click Restore default configuration and then click OK.

![1679982510769-fbf88001-9a19-4461-a062-64a304c1a862.png](./img/TFRyisVs9_mw-DgG/1679982510769-fbf88001-9a19-4461-a062-64a304c1a862-361176.webp)

### 9.7 Device Manager of InHand Cloud

Click "Administration >>Device Manger>>Device Manger" config InHand Cloud service.

### 9.7.1 Config DeviceManger

Device ManagerWith a visualization user interface and simple operation steps, the Device Manager platform enables you to manage and monitor InHand’s hardware devices, such as routers and gateways with convenience. It can quickly integrate devices and manage them with just a few clicks. The cloud deployment delivers easy-to-use experience, allowing you to focus on your core business and empowering your growth.

Step1: Register a user Global site [https://iot.inhandnetworks.com](https://iot.inhandnetworks.com/user/login)

![1679982511177-70e416b0-485f-464a-a46c-a486f41f2ddb.png](./img/TFRyisVs9_mw-DgG/1679982511177-70e416b0-485f-464a-a46c-a486f41f2ddb-795366.webp)

Step2:

- Config Service Type "Device Manager"
- Server Address "iot.inhandnetworks.com" If you have already privatized the deployed Device Manager Cloud, fill in the private deployment server IP or domain name. Server Typy select "Coustomer".
- Secure Channel , After checking, it will be transmitted with SSL encryption.
- Registered Account : Use step 1 registed account email address.
- Site name and Asset Number customer defined.
- Make sure the VG710 is connected to the Internet.

![1679982511599-7d2bd07a-fe99-4aaa-927a-61cda7ac7cb2.png](./img/TFRyisVs9_mw-DgG/1679982511599-7d2bd07a-fe99-4aaa-927a-61cda7ac7cb2-166679.webp)

Step3:

- Login Device Manager cloud.
- Check Gateways, VG710 will auto login server.
- For more usage reference manuals:

![1679982511976-5b9bc17c-a451-4834-8b92-1c5442390956.png](./img/TFRyisVs9_mw-DgG/1679982511976-5b9bc17c-a451-4834-8b92-1c5442390956-746093.webp)

- For more usage reference manual.

![1679982512377-75042069-15f9-45ab-94f6-85835273e6af.png](./img/TFRyisVs9_mw-DgG/1679982512377-75042069-15f9-45ab-94f6-85835273e6af-917098.webp)

### 9.7.1 InConnect Service

The InConnect is a simple “plug & play” service which builds secure remote networks for your machines (IPCs, servers, IP cameras, PLCs, HMIs, RTUs, controllers, etc.). Featuring user-friendly interfaces and simple operation, the SaaS (Software as a Service) based solution enables you to access your devices anytime from anywhere, and stay connected with your business and with the world – especially in these challenging times when normal working routines have been disrupted. Support VPN networking in the way of subnet to subnet.

Step1: Register a user Global site [hthttps://ics.inhandnetworks.com](https://ics.inhandnetworks.com/user/register)

Step2:

- Config Service Type "InConnect Service"
- Server Address "ics.inhandnetworks.com" If you have already privatized the deployed Device Manager Cloud, fill in the private deployment server IP or domain name. Server Typy select "Coustomer".
- Secure Channel , After checking, it will be transmitted with SSL encryption.
- Registered Account : Use step 1 registed account email address.
- Site name and Asset Number customer defined.
- Make sure the VG710 is connected to the Internet.

![1679982513109-341bfcc0-6e9a-403b-abd1-39ae4e2844f7.png](./img/TFRyisVs9_mw-DgG/1679982513109-341bfcc0-6e9a-403b-abd1-39ae4e2844f7-695814.webp)

Step3:

- Login InConnect service.
- Check Gateways, VG710 will auto login server.
- Add VG710 SN to Server:

![1679982513801-7563bbce-025a-4c6b-9689-9f6f9faaa974.png](./img/TFRyisVs9_mw-DgG/1679982513801-7563bbce-025a-4c6b-9689-9f6f9faaa974-140138.webp)

- For more usage reference manuals:

![1679982514406-8128f9f9-bd5e-455d-a958-5e2657986788.png](./img/TFRyisVs9_mw-DgG/1679982514406-8128f9f9-bd5e-455d-a958-5e2657986788-179434.webp)

### 9.7.1 Smart Fleet Service

InHand Smart Fleet Cloud Platform, referred to as Smart Fleet, is a business platform that provides enterprise-level vehicle monitoring and management services for enterprise customers. Smart Fleet can help you manage vehicles intelligently and efficiently, break down vehicle data barriers, and realize multi-data joint analysis, vehicle Full life cycle management and control, intelligent vehicle operation and maintenance, help the informatization construction and digital transformation of engineering vehicles.

Smart Fleet can connect multiple vehicles to the same network. You can centrally monitor and manage vehicles, issue configurations, and upgrade firmware in a unified manner.

Smart Fleet helps users to quickly build an IoT network and master vehicle operation data in real time, allowing you to easily implement centralized monitoring and management of vehicles and gateways through the cloud platform. Effectively solve the problems of data isolation, collaboration bottlenecks, and lack of management.

Step1: Register a user Global site [https://smartfleet.cloud](https://smartfleet.cloud/user/login)

Step2:

- Config Service Type "InVehicle Service"
- Server Address "smartfleet.cloud" If you have already privatized the deployed Device Manager Cloud, fill in the private deployment server IP or domain name. Server Typy select "Coustomer".
- Secure Channel , After checking, it will be transmitted with SSL encryption.
- Registered Account : Use step 1 registed account email address
- License Plate Number is  required.
- Asset Number Group ID is customer defined.
- Other interface information of the gateway can be reported to the platform in seconds.
- Make sure the VG710 is connected to the Internet.

![1679982514849-3b295d30-13cb-41f0-8edb-119fcb482c78.png](./img/TFRyisVs9_mw-DgG/1679982514849-3b295d30-13cb-41f0-8edb-119fcb482c78-337111.webp)

Step3:

- Login InConnect service.
- Check Gateways, VG710 will auto login server.

![1679982515345-eb07ce43-c500-4382-aa1e-dba2d4c1452c.png](./img/TFRyisVs9_mw-DgG/1679982515345-eb07ce43-c500-4382-aa1e-dba2d4c1452c-442123.webp)

### 9.8 SNMP

### 9.8.1 SNMP

Currently, the SNMP Agent of VG814 supports SNMPv1, SNMPv2c, and SNMPv3.

● SNMPv1 and SNMPv2c use community names for authentication.

● SNMPv3 uses user names and passwords for authentication.

Method for enabling SNMP for VG814:

Click "Administration >> SNMP >> SNMP", check "Enable", select "v1c" for "v2c" for "SNMP Version", and click Apply & Save.

![1679982515672-6f59f1df-93be-4d67-812d-f30d950c2330.png](./img/TFRyisVs9_mw-DgG/1679982515672-6f59f1df-93be-4d67-812d-f30d950c2330-284606.webp)

If v3c is selected, the corresponding user and user group need to be configured. Enter any name for "Groupname", select a security level, and click Add. Enter any name for "Username", select the new group name for "Groupname", set "Authentication" and "Authentication password", click Add, and then click Apply & Save.

![1679982516085-6693058c-c7ee-432b-b613-91529a815c6f.png](./img/TFRyisVs9_mw-DgG/1679982516085-6693058c-c7ee-432b-b613-91529a815c6f-899518.webp)

### 9.8.2 SnmpTrap (Alarm)

The SNMP trap is a type of entrance. When this entrance is reached, the SNMP managed devices actively notify the NMS, instead of waiting for the polling of NMS. On an SNMP-enabled network, the agents on managed devices can report errors to the NMS anytime, without the need of waiting for the polling of NMS. The errors are reported to the NMS through traps.

Method for enabling SnmpTrap for the gateway:

Click "Administration >> NMP >> SnmpTrap". Enter the IP address of the NMS. Enter the corresponding group name when v1c or v2c is selected, or the corresponding user name when v3c is selected, ensuring that the name consists of 1–32 characters. By default, the UDP port ID ranges from 1 to 65535.

![1679982516495-4ad5f391-0fc1-46e8-bb15-7d2fd9a2679d.png](./img/TFRyisVs9_mw-DgG/1679982516495-4ad5f391-0fc1-46e8-bb15-7d2fd9a2679d-515835.webp)

### 9.8.3 SnmpMibs

In SNMP messages, management variables are used to describe the managed objects on the device. To uniquely identify the managed objects on the device, SNMP uses a hierarchical naming scheme to identify the managed objects The entire hierarchical structure is like a tree. The nodes of the tree represent the managed objects, as shown in the figure below. Each node can be uniquely identified by a path starting from the root.

![1679982516941-9b1b2a54-2a8e-49b5-ad39-9e879e6be59d.png](./img/TFRyisVs9_mw-DgG/1679982516941-9b1b2a54-2a8e-49b5-ad39-9e879e6be59d-062792.png)

The management information base (MIB) is used to describe the hierarchical structure of the tree. It is a set of standard variable definitions for the monitored network device. In the above figure, managed object B can be uniquely determined based on a string of numbers {1.2.1.1}, which form the object identifier (OID) of the managed object.

Method for downloading a SnmpMibs file to the PC via the gateway:

Click "Administration >> SNMP >> SnmpMibs", select a folder, and click download to download it to the PC. Find the folder on the PC and import it to the NMS.

![1679982517460-742ae7ea-cf96-44b9-89b4-634a5ec1e26c.png](./img/TFRyisVs9_mw-DgG/1679982517460-742ae7ea-cf96-44b9-89b4-634a5ec1e26c-235069.webp)

### 9.10 Alarm

The alarm function enables users to identify gateway abnormalities in time. When an abnormality occurs, the gateway reports an alarm. You can select system-defined abnormalities and choose an appropriate notification way to obtain the abnormality information. All alarms are recorded in alarm logs so that users can identify abnormalities and perform troubleshooting in time.

Alarm states:

● Raise: indicates that the alarm has been generated but not been confirmed.

● Confirm: indicates that the alarm cannot be solved currently.

● All: indicates all generated alarms.

Alarm levels:

● EMERG: The device undergoes a serious error that causes a system reboot.

● CRIT: The device undergoes an unrecoverable error.

● WARN: The device undergoes an error that affects system functions.

● NOTICE: The device undergoes an error that affects system performance.

● INFO: A normal event occurs.

(1) Status: Click "Administration >> Alarm >> Status" and view all alarms generated in the system since power-on.

![1679982517904-d963e6ce-c874-4cce-9c40-e4504cdaed0d.png](./img/TFRyisVs9_mw-DgG/1679982517904-d963e6ce-c874-4cce-9c40-e4504cdaed0d-817007.webp)

(2) Alarm Input: Select an alarm type as required. When this item is abnormal, an alarm is generated.

(3) Alarm Output: When an alarm is generated, the system automatically sends the alarm content to the destination email address via an email. This function is not available for common users. Set the sender mail address in "Email Alarm" and the receiver mail address in "Mail Address". "Mail Server IP/Name" can be found on the browser (for example, enter "smtp.exmail.qq.com" if you use a Tencent Enterprise mailbox.)

![1679982518304-63e5cec9-7437-4f52-a12b-475f4b2c0fe9.png](./img/TFRyisVs9_mw-DgG/1679982518304-63e5cec9-7437-4f52-a12b-475f4b2c0fe9-402632.webp)

(4) Alarm Map: Alarms can be received in two ways: command line interface (CLI) (console interface) and Email. Some devices support SMS alarms. To enable email-based mapping, enable and set the email address on the "Alarm Output" page.

### 9.11 System Logs

Method for viewing system logs:

Click "Administration >> System Log" to view system logs.

This page also provides the following operations: "Clear Log", "Download Log File", "Download Diagnose Data", "Clear History Log", and "Download History Log". History logs are those stored for extended time as specified on the "System Log" page.

The diagnose data file is encrypted, because the gateway configuration information is downloaded together with the diagnose data. You need to decrypt the file with the decryption tool provided by InHand.

![1679982518665-7f619b8d-995c-448e-92a3-4cf26d7dacc6.png](./img/TFRyisVs9_mw-DgG/1679982518665-7f619b8d-995c-448e-92a3-4cf26d7dacc6-478980.webp)

The storage capacity of the gateway is limited (512 KB by default). To save all the logs, you need to use a remote log server (for example, [Kiwi Syslog Daemon](#_Kiwi_Syslog_Ademon)). Set the address and port of the log server on the web page. The gateway uploads all the system logs to the remote log server.

![1679982519132-17a895da-4bde-489c-a0cb-d90f7d4fc349.png](./img/TFRyisVs9_mw-DgG/1679982519132-17a895da-4bde-489c-a0cb-d90f7d4fc349-072190.webp)

### 9.12 System Upgrade

Click "Administration >> Upgrade >> Browse", select an upgrade file, and click Upgrade. Restart the system after the upgrade is completed.

![1679982519626-b77cf01c-fb15-4ce0-8e27-df9949d63e10.png](./img/TFRyisVs9_mw-DgG/1679982519626-b77cf01c-fb15-4ce0-8e27-df9949d63e10-277048.webp)

Firmware degradation:

Downgrading from V1.2.X to 1.2.1.r300xx (X is greater than 2).

```plain
//Telnet or SSH login VG814
VG814 login: adm
Password: 


                     Welcome to INOS console

                Copyright (c)2001-2024 InHand Networks Co., Ltd.
                     http://www.inhandnetworks.com
--------------------------------------------------------------------------------
Model                : 814
Serial Number        : VF8102041000762
Firmware Version     : V1.2.5
Bootloader Version   : 2012.07.r238
--------------------------------------------------------------------------------
VG814#enable
VG814#fwsign disable
VG814#verify disable  //Turn off version validation
VG814#
```

Log in to the Web page again to upload firmware.

| ![1679982520025-86a5f138-d24e-4bb2-aeac-3b1a4870ff6b.png](./img/TFRyisVs9_mw-DgG/1679982520025-86a5f138-d24e-4bb2-aeac-3b1a4870ff6b-565309.png)Note:<br/>During the software upgrade, do not perform any operation on the web page; otherwise, the software upgrade may be interrupted. |
| --- |

### 9.13 System Reboot

Click "Administration >> Reboot >> OK to reboot the system.

![1679982520390-7a46627f-1f76-4712-a2c1-b34fa5ec9ab6.png](./img/TFRyisVs9_mw-DgG/1679982520390-7a46627f-1f76-4712-a2c1-b34fa5ec9ab6-888239.webp)

## 10. Diagnostic Tools

Diagnostic tools are used to detect the network connection of the gateway: Ping, Traceroute, Tcpdump, and Link Speed Test.

Ping: It is used to detect the external network connection of the device. Enter any common website in China for "Host" and click "Ping". If data transmission occurs, the network is connected properly.

![1679982520826-f5e952c5-160c-441f-a8e9-c795ef83a19f.png](./img/TFRyisVs9_mw-DgG/1679982520826-f5e952c5-160c-441f-a8e9-c795ef83a19f-099809.webp)

Traceroute: Enter the IP address of the peer host and click "Trace" to detect the route connection.

![1679982521282-f618261a-9f62-400b-9357-40bc6b23268e.png](./img/TFRyisVs9_mw-DgG/1679982521282-f618261a-9f62-400b-9357-40bc6b23268e-030406.webp)

Tcpdump:

Select an interface ("any" or "bridge1"), set "Capture Number", and click Start Capture >> Stop Capture >> Download Capture File.

![1679982521696-e450fa14-492e-4ed0-bd9c-be6327306506.png](./img/TFRyisVs9_mw-DgG/1679982521696-e450fa14-492e-4ed0-bd9c-be6327306506-486353.webp)

Download wireshark from the browser to open the downloaded file and analyze the messages to understand the network connection of the interface.

![1679982522153-d08490fc-0321-4516-9752-d67bf4dc8274.png](./img/TFRyisVs9_mw-DgG/1679982522153-d08490fc-0321-4516-9752-d67bf4dc8274-121505.webp)

Link Speed Test: Upload and download files to test the link speed.

![1679982522554-3e6b43b7-2bd8-452a-8c87-dc6e3177282b.png](./img/TFRyisVs9_mw-DgG/1679982522554-3e6b43b7-2bd8-452a-8c87-dc6e3177282b-353150.webp)

## 11. Hardware installation

The installation position is recommended to be installed in the air conditioning duct of the vehicle：

![1679982522934-bc7889f4-fc6d-485a-8410-d42770dcb5e1.png](./img/TFRyisVs9_mw-DgG/1679982522934-bc7889f4-fc6d-485a-8410-d42770dcb5e1-573469.webp)

![1679982523379-4cdaa6f2-3696-4913-a3ed-11262b07621f.png](./img/TFRyisVs9_mw-DgG/1679982523379-4cdaa6f2-3696-4913-a3ed-11262b07621f-684877.webp)

## 12. More reference documents

[https://github.com/inhandnet/InVehicle-Docs](https://github.com/inhandnet/InVehicle-Docs)

For 3rd party platform integration:

FlexAPI_Reference_for_3rd_party_platform_v1.0.8.pdf FlexAPI_Reference_for_3rd_party_platform_TCP_version_v1.0.2.pdf For LAN Edge computing application: FlexAPI_Reference_for_LAN_application_v1.0.8.pdf FlexAPI_Reference_for_LAN_application_REST_API_Version_v1.0.5.pdf

#

#
