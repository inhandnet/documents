# InHand VG710 Series User's Manual V1.4

About The Document

Revision History

| **Version** | Data | Author | Description |
| --- | --- | --- | --- |
| 1.0  | 2021-5-10 | Sun Zhandong | Creation of the document |
| 1.2 | 2022-8-15 | Sun Zhandong | Add Product picture into document |
| 1.3 | 2023-06-10 | Sun Zhandong | Add 5G Verison |
| 1.4 | 2024-05-01 | Sol. Sun | Add VG710-M Verison |

Declaration

Thank you for choosing our product. Before using the product, read this manual carefully.

The contents of this manual cannot be copied or reproduced in any form without the written permission of InHand.

Due to continuous updating, InHand cannot promise that the contents are consistent with the actual product information, and does not assume any disputes caused by the inconsistency of technical parameters. The information in this document is subject to change without notice. InHand reserves the right of final change and interpretation.

© 2020 InHand Networks. All rights reserved.

Conventions

| **Symbol** | **Indication** |
| :---: | --- |
| > | Indicates a button name, for example, the OK button. |
| "" | Indicates a window name or menu name, for example, the pop-up window "New User". |
| >> | Separates a multi-level menu. For example, the multi-level menu File >> New >> Folder indicates the menu item "Folder" under the sub-menu "New", which is under the menu "File". |
| ![1690880111327-cfc9b837-dc61-4948-a6b7-0a7c99d7a8a6.png](./img/Gs3dvISjhRc0qruU/1690880111327-cfc9b837-dc61-4948-a6b7-0a7c99d7a8a6-686137.png) | Reminds readers to be careful. Improper action may result in loss of data or device damage. |
| ![1690880111626-19f0e794-a520-428a-978b-5b50fbabf8e4.png](./img/Gs3dvISjhRc0qruU/1690880111626-19f0e794-a520-428a-978b-5b50fbabf8e4-827017.png) | Notes contain detailed descriptions and helpful suggestions. |

Technical support:

43671 Trade Center Place, Suite 100, Dulles, VA 20166

T: +1 (703) 348-2988

<www.inhandnetworks.com>

Inquiry: <info@inhandnetworks.com> | Support: <support@inhandnetworks.com>

## Chapter I

## Overview

InHand VG710 is a new-generation 4G in-vehicle gateway oriented at the Internet of Vehicles (IoV). It provides fast and safe networks for automobiles and transport service vehicles, meeting the requirements of police vehicles, emergency command vehicles, engineering vehicles, medical vehicles, and logistics vehicles for fast mobile networks. It is used with a cloud-based remote vehicle management platform to provide ubiquitous accessible networks and uninterrupted operation supervision for logistics management, asset tracking, mobile office, and government security.

![1690880112079-f2155ddb-2325-49c0-bd37-df0d0b52033b.png](./img/Gs3dvISjhRc0qruU/1690880112079-f2155ddb-2325-49c0-bd37-df0d0b52033b-303914.png)

Fig. 1 Application case

## Hardware

### Indicator Description

| VG710 Indicator | Status and Definition |
| :---: | --- |
| System | Steady off --- The device is powered off.<br/>Steady red --- The system is starting.<br/>Steady blue --- The IGT signal is not connected.<br/>Blinking green --- The system operates properly.<br/>Blinking red --- The system is faulty.<br/>Blinking blue --- The system is being upgraded. |
| Cellular | Steady off --- The dialup function is disabled.<br/>Blinking green --- Dialup is in progress.<br/>Steady green --- Dialup succeeds.<br/>Blinking red --- Dialup fails (no module or SIM card is detected). |
| Signal | Steady off --- The current dialup card has no signal.<br/>Steady red --- The current dialup card has weak signals (signal strength: ≤ 9 asu).<br/>Steady blue --- The current dialup card has moderate signals (signal strength: 10–19 asu).<br/>Steady green --- The current dialup card has strong signals (signal strength: ≥ 20 asu). |
| GNSS | Steady off --- GNSS is disabled.<br/>Blinking green --- Positioning is in progress.<br/>Steady green --- Positioning is completed. |
| Wi-Fi 2.4G | Used as an AP:<br/>Steady off --- The AP is disabled.<br/>Blinking green --- The AP operates properly.<br/>Used as a STA:<br/>Steady off --- The STA is disabled, or no AP is associated.<br/>Steady green --- Connection fails due to a wrong password after an AP is associated.<br/>Blinking green --- An AP is associated. |
| Wi-Fi 5G | Used as an AP:<br/>Steady off --- The AP is disabled.<br/>Blinking blue --- The AP operates properly.<br/>Used as a STA:<br/>Steady off --- The STA is disabled, or no AP is associated.<br/>Steady blue --- Connection fails due to a wrong password after an AP is associated.<br/>Blinking blue --- An AP is associated. |
| U1 and U2 | U1:<br/>Steady off --- The APP is disabled.<br/>Steady green --- The APP is enabled.<br/>U2:<br/>Steady off --- The virtual private network (VPN) is disabled or abnormal.<br/>Steady green --- The VPN operates properly. |

### Restoring Default Settings via the Reset Button

To restore default settings via the Reset button, perform the following steps:

1. Power on the device and immediately press and hold the Reset button. After about 15s, only the System indicator is steady red.

2. When the System indicator turns off and becomes red again, immediately release the Reset button.

3. When the System indicator turns off, press the Reset button (ensure that it blinks red twice) and then release it. The device is restored to the default settings.

### Panel interface introduction

### VG710-H 5G verison

![1690881199640-3a26cd84-18fa-402a-a817-4ee0b07a9573.png](./img/Gs3dvISjhRc0qruU/1690881199640-3a26cd84-18fa-402a-a817-4ee0b07a9573-434155.png)

**IO 20PIN Definition**

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Def. | L_Channel | Mic IN | RS485A | GND | RS232_TX | 1Wire | DO1 | GND | AI1/DI1 | AI3/DI3/FWD* |
| PIN | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Def. | R_Channel | GND | RS485B | GND | RS232_RX | GNSS_1PPS | DO2 | GND | AI2/DI2 | AI4/DI4/WHEELTICK* |

**Support GNSS ADR model is FWD and WHEEL TICK function.*

__

**EXT 10PIN Definition**

| PIN | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Def. | K_LINE    | CAN1_H | GND | CAN2_H | J1708_A |
| PIN | 6 | 7 | 8 | 9 | 10 |
| Def. | L_LINE | CAN1_L | GND | CAN2_L | J1708_B |

### VG710 4G verison

![1690881776766-4b617745-7a03-461f-ad10-16c7c69efc68.png](./img/Gs3dvISjhRc0qruU/1690881776766-4b617745-7a03-461f-ad10-16c7c69efc68-795989.png)

**IO 20PIN Definition**

| PIN | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Def. | RS485B | CAN1_L | 1-Wire | DO4 | DO2 | GND | AI/DI6 | AI/DI4 | AI/DI2 | GND |
| PIN | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Def. | RS485A | CAN1_H | GND | DO3 | DO1 | GND | AI/DI5 | AI/DI3 | AI/DI1 | GND |

### VG710-M Version

![1743158312047-32fea94d-3a9c-47a8-88cc-52d32312a40c.png](./img/Gs3dvISjhRc0qruU/1743158312047-32fea94d-3a9c-47a8-88cc-52d32312a40c-086330.png)

The VG710-M power connector features a 8-pin design,  VIN+, VIN-, CAN-H, and CAN-L , AI/DI. There is no IGT/ACC signal available. Once the device is connected to the positive and negative terminals of a direct current power supply, it can operate normally.

![VG710-M Power Calbe Connector](./img/Gs3dvISjhRc0qruU/1730495909926-5ba4cdd0-436d-4819-8a4b-185d81854f25-301923.png)

To power the VG710-M Version: Connect the red wire of cable P2 to the positive terminal of the direct current (DC) power supply, and the black wire to the negative terminal. The acceptable voltage range for the power supply is 9 to 36V DC.

| PIN | 5 | 6 | 7 | 8 |
| :---: | :---: | :---: | :---: | :---: |
| Def. | V- | AI/DI | GND | CAN-L |
| PIN | 1 | 2 | 3 | 4 |
| Def. | V+ | IGT | GND | CAN-H |

⚠️  IGT is the vehicle ignition signal. If during an office test, please connect IGT to the positive pole (V+) of the power supply.

## Default Settings

| **No.** | **Function** | **Default Settings** |
| :---: | --- | --- |
| **1** | **Dialup over the cellular network** | − Enabled (The Cellular indicator is steady green after dialup succeeds.)<br/>By default, the dual-SIM function is disabled, and SIM1 is enabled. |
| **2** | **Satellite positioning and inertial navigation service** | − Enabled (The GNSS indicator is steady green after positioning succeeds.)<br/>− The inertial navigation function is enabled. |
| **3** | **On-board diagnostics (OBD)** | − Enabled<br/>− The CANbus baud rate is automatically detected.<br/>− The OBD protocol is automatically detected.<br/>− OBD data is automatically scanned. |
| **4** | **Default settings of Wi-Fi** | − The Wi-Fi 2.4G AP is enabled. The SSID starts with VG710-, followed by six digits.<br/>− The Wi-Fi 5G AP is enabled. The SSID starts with VG710-5G-, followed by six digits.<br/>− WPA2-PSK is used for authentication.<br/>− The password contains the last eight digits of the SN. |
| **5** | **Default settings of Ethernet** | − Four LAN ports are enabled.<br/>− The IP address is 192.168.2.1.<br/>− The subnet mask is 255.255.255.0.<br/>− The DHCP server is enabled. The IP address pool is 192.168.2.2–192.168.2.100, and IP addresses can be automatically allocated to downstream devices. |
| **6** | **Network access control for the gateway** | − HTTP and HTTPS are enabled, with the port numbers of 80 and 443 respectively.<br/>− Telnet is disabled.<br/>− SSH is disabled.<br/>− Access from the cellular network is allowed only over HTTPS. |
| **7** | **User name and password** | − **adm/123456** (super administrator) |
| **8** | **Power management** | − shutdown-delay 30: The power-off delay is 30s.<br/>− standby-mode 1: The power-off function is enabled.<br/>− standby-check-interval 20 indicates the power check interval in standby mode.<br/>− standby-voltage 90: The standby threshold voltage is 9 V.<br/>− standby-resume-voltage 105: The threshold voltage for resuming normal operating in standby mode is 10.5 V. |
| **9** | **IO** | − Four digital output channels generate output at low level by default, and the pull-up resistor is disabled.<br/>− The pull-up resistor for six digital input channels is disabled. |
| **10** | **Serial port** | − RS232<br/>Baud rate: 9600<br/>Data bits: 8 bits<br/>Parity bit: none<br/>Stop bit: 1 bit<br/>− RS485<br/>Baud rate: 9600<br/>Data bits: 8 bits<br/>Parity bit: none<br/>Stop bit: 1 bit |

## Login and Network Access

### Network Access via the Dialup Card

1. Insert the SIM card, connect the GNSS and cellular antennas, and connect the power supply and PC. Insert the diversity dialup antenna when the dialup card has poor signals.

![1690880112706-56cb14d4-ddf0-46e4-83ea-5bff313dccf4.png](./img/Gs3dvISjhRc0qruU/1690880112706-56cb14d4-ddf0-46e4-83ea-5bff313dccf4-590820.png)

![1690880113045-0f6c8eb5-0fac-4b18-b3e3-881b880b7c5d.png](./img/Gs3dvISjhRc0qruU/1690880113045-0f6c8eb5-0fac-4b18-b3e3-881b880b7c5d-696897.png)

| ![1690880113377-06d3be22-3197-4e1f-83e7-a9bd303c1de5.png](./img/Gs3dvISjhRc0qruU/1690880113377-06d3be22-3197-4e1f-83e7-a9bd303c1de5-398139.png)Note:<br/>Before inserting or removing the SIM card, unplug the power cable; otherwise, the operation will cause data loss or damage the gateway. |
| :--- |

1. Assign an IP address to the PC, which is on the same network segment as the IP address of the gateway.

Method 1: Enable the PC to obtain an IP address automatically (recommended).

Method 2: Configure a fixed IP address on the same network segment as the gateway address for the PC.

Step: Select "Use the following IP address", enter any IP address in the range of 192.168.2.2 to 192.168.2.254 (different from the initial IP address 192.168.2.1 of the gateway), the subnet mask 255.255.255.0, and the default gateway address 192.168.2.1, and then click OK.

![1690880113718-d8794b12-f66a-40e4-b176-bbb101a4f49f.png](./img/Gs3dvISjhRc0qruU/1690880113718-d8794b12-f66a-40e4-b176-bbb101a4f49f-121837.png)![1690880114159-4d7ce142-40d5-4891-b362-f9c2bdf17938.png](./img/Gs3dvISjhRc0qruU/1690880114159-4d7ce142-40d5-4891-b362-f9c2bdf17938-658839.png)

Obtain an IP address automatically Use a fixed IP address

1. Open the browser, enter the default IP address 192.168.2.1 of the gateway in the address bar, and press Enter.（Edge Firefox or Chrome recommended）

![1690880114506-5d0b9241-cb39-4090-8488-fdd90e58e32f.png](./img/Gs3dvISjhRc0qruU/1690880114506-5d0b9241-cb39-4090-8488-fdd90e58e32f-337014.png)

1. Log in (if a blocking prompt is displayed, click "Advanced >> Continue"). Enter the default username adm and password 123456 to go to the web interface.

![1690880114870-e6c2cbf8-4bbf-4980-a8b2-31686726c2ba.png](./img/Gs3dvISjhRc0qruU/1690880114870-e6c2cbf8-4bbf-4980-a8b2-31686726c2ba-766947.png)

Method 3

Step 1: Connect to the device through the network cable or Wi-Fi (see the SSID and key on the nameplate). If you use Wi-Fi, the Wi-Fi indicator is steady on in green or blinks.

Step 2: Enter the default device IP address 192.168.2.1 in the address bar of the web browser to open the login page.

Step 3: Enter the default username adm and password 123456 to go to the web interface.

1. Click "Network >> Cellular", check "Enable", and click Apply & Save. If the network connection status is "Connected" and an IP address has been allocated, the SIM card has been connected to the network.

(Set the APN parameters for a private-network card.)

![1690880115161-a28f6495-c92f-40dd-be73-c6c612c19b89.png](./img/Gs3dvISjhRc0qruU/1690880115161-a28f6495-c92f-40dd-be73-c6c612c19b89-214386.png)![1690880115496-b3fca2d7-683b-4df3-9ef7-1a049e58a496.png](./img/Gs3dvISjhRc0qruU/1690880115496-b3fca2d7-683b-4df3-9ef7-1a049e58a496-341600.png)

1. Ping a common website in China with a ping detection tool. If there is data transmission, the device has been successfully connected to the network.

![1690880115784-fbe801ca-50db-432f-9eb1-9f601a778cff.png](./img/Gs3dvISjhRc0qruU/1690880115784-fbe801ca-50db-432f-9eb1-9f601a778cff-022692.png)

1. Enable the dual-SIM function when two SIM cards are used.

![1690880116134-e336754e-ba5a-4276-aa29-f5b6cdfb388c.png](./img/Gs3dvISjhRc0qruU/1690880116134-e336754e-ba5a-4276-aa29-f5b6cdfb388c-653519.png)

### Network Access via Wi-Fi

1. Complete the connection shown in the following figure.The Wi-Fi antenna is screwed into the panel Wi-Fi antenna interface.

Connect to the device through the network cable or Wi-Fi (see the SSID and key on the nameplate). If you use Wi-Fi, the Wi-Fi indicator is steady on in green or blinks.

![1690880116449-7e4ad4a3-0b04-45d9-ab49-6a93dba6789b.png](./img/Gs3dvISjhRc0qruU/1690880116449-7e4ad4a3-0b04-45d9-ab49-6a93dba6789b-795302.png)

1. Assign an IP address to the PC, which is on the same network segment as the IP address of the gateway. Log in to the web page. For details, see <u>4.1 Network Access via the Dialup Card</u>.

2. Click " Network >> Wi-Fi" and select Wi-Fi 2.4G or Wi-Fi 5G as a client. Enter the name, authentication method, and key of an available wireless access point (AP). Click Apply & Save.

![1690880116864-ab0a1e9e-3678-4761-8a49-a02ca35237a3.png](./img/Gs3dvISjhRc0qruU/1690880116864-ab0a1e9e-3678-4761-8a49-a02ca35237a3-776783.png)

1. Click "Status". The current network status is "Connected", and an IP address is obtained successfully, indicating that the device has been successfully connected to the network via Wi-Fi.

![1690880117149-40343889-8271-44cf-8beb-61fc6231ae1b.png](./img/Gs3dvISjhRc0qruU/1690880117149-40343889-8271-44cf-8beb-61fc6231ae1b-984116.png)

## Network

In parameter settings, a green text box ![1690880117430-a2ed27b1-6e49-499b-908e-0ffa15339cf5.png](./img/Gs3dvISjhRc0qruU/1690880117430-a2ed27b1-6e49-499b-908e-0ffa15339cf5-999133.png)indicates a mandatory item, and a pure white text box ![1690880117682-32bd3ad4-fded-48d7-a521-cdd68e7aa652.png](./img/Gs3dvISjhRc0qruU/1690880117682-32bd3ad4-fded-48d7-a521-cdd68e7aa652-149046.png)indicates an optional item.

### Celluar Interface

![Celluar Interface](./img/Gs3dvISjhRc0qruU/1748932304889-ce7e51df-18d8-440e-be53-991c952366b5-269923.png)

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

![1748932514263-0541c1f9-662c-4be8-85f7-0b77d6333a86.png](./img/Gs3dvISjhRc0qruU/1748932514263-0541c1f9-662c-4be8-85f7-0b77d6333a86-579551.png)

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
- **Network Type**: Select the type of network you want to connect to. The options include "Auto", "GSM", "3G"，"4G"，"5G", etc. Recommend setting it to Auto.
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

![1748933002589-fd75ef9e-935d-40d2-9cac-d44c31bb30a4.png](./img/Gs3dvISjhRc0qruU/1748933002589-fd75ef9e-935d-40d2-9cac-d44c31bb30a4-533798.png)

1. **Access Advanced Options**:
    - On the "Cellular" configuration page, check the "Show Advanced Options" checkbox. This will display additional advanced settings that allow for more detailed configuration.
2. **Configure Advanced Options**:
    - **Initial Commands**: In this field, you can enter initial commands that the device needs to execute upon startup. This is often used for specific network configurations or device initialization.
    - **RSSI Poll Interval**: Set the polling interval for the Received Signal Strength Indicator (RSSI). The default is 120 seconds, which you can adjust as needed. Setting it to 0 disables this feature.
    - **Dial Timeout**: Set the dial timeout duration. The default is 120 seconds, which you can adjust based on network conditions.
    - **Infinitely Dial Retry**: Check this option to allow the device to retry dialing indefinitely upon failure. This is useful for ensuring the device always attempts to connect to the network.
    - **Dual SIM Enable**: Check this option to enable dual SIM functionality, allowing the device to use two SIM cards for network connectivity.

### Enabling Dual SIM Functionality

![1748933044448-ab099121-be02-433c-ad0a-31cc3bacadcb.png](./img/Gs3dvISjhRc0qruU/1748933044448-ab099121-be02-433c-ad0a-31cc3bacadcb-299710.png)

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

### Network For LAN

### Bridge Port

A bridge port is intended to connect two different physical LANs over a bridge, to enable storage and forwarding across LANs at the link layer.

**Method for modifying the IP address of a bridge port and bridge members:**

1. Click "Network >> Bridge" and select "Bridge >> Modify".

![1690880118001-993435d6-b55e-4e06-92ef-aaf74f2d01d3.png](./img/Gs3dvISjhRc0qruU/1690880118001-993435d6-b55e-4e06-92ef-aaf74f2d01d3-926891.png)

1. Modify the IP address of the bridge port or bridge members. Among the bridge members, dot11radio1 and dot11radio2 are Wi-Fi 2.4G and Wi-Fi 5G ports respectively.

![1690880118408-49b2bfb3-754f-4bc1-95e9-6a78d69c4956.png](./img/Gs3dvISjhRc0qruU/1690880118408-49b2bfb3-754f-4bc1-95e9-6a78d69c4956-528091.png)

### VLAN Port

A virtual LAN (VLAN) comprises a group of logical devices and users. These devices and users are not limited by physical locations, but can be organized based on functions, departments, applications, and other factors. They communicate with each other as if they are on the same network segment, which contributes to the name of VLAN.

**Method for adding a port of VLAN 2:**

1. Click "Network >> VLAN >> Configure VLAN Parameters >> Add". Set the virtual IP address of the port of VLAN 2 and select the member port of VLAN 2 as required. Click Apply & Save.

![1690880118656-e404e33a-1fc6-40fe-a1a6-0c16789baf7a.png](./img/Gs3dvISjhRc0qruU/1690880118656-e404e33a-1fc6-40fe-a1a6-0c16789baf7a-939460.png)

1. Return to the VLAN list. The port of VLAN 2 has been successfully added.

![1690880118966-6e7318b8-9a6a-446c-b3ea-a8b9d8c314ea.png](./img/Gs3dvISjhRc0qruU/1690880118966-6e7318b8-9a6a-446c-b3ea-a8b9d8c314ea-188261.png)

Currently, VLAN ports of the device support two link types: access and trunk. An access port belongs to only one VLAN and is generally connected to a computer. A trunk port can be used for multiple VLANs and can receive messages from or send messages to multiple VLANs. It can be connected to a switch or a user's computer. You can select the link type as required on the "VLAN Trunk" page.

![1690880119241-4d9ee44c-d292-4991-9730-adc83867fdd4.png](./img/Gs3dvISjhRc0qruU/1690880119241-4d9ee44c-d292-4991-9730-adc83867fdd4-622421.png)

### ADSL Dialup (PPPoE)

**Method for connecting the gateway to the PPPoE server:**

1. Click "Network > > ADSL Dialup (PPPoE)", select the VG710 interface for connecting to the PPPoE server in the "Dial Pool" bar, and click Add.

2. Enter the user name, password, and pool ID of the PPPoE server in the "PPPoE List" bar. The pool ID must be the same as that in the "Dial Pool" bar. Click Add, and then click Apply & Save.

![1690880119598-e15ad61f-c18b-4439-9138-fc911d0cb9c4.png](./img/Gs3dvISjhRc0qruU/1690880119598-e15ad61f-c18b-4439-9138-fc911d0cb9c4-833472.png)

### Wi-Fi

The gateway can be used as an AP or a client. When it is used as an AP, other users can access the Internet through the gateway via Wi-Fi. When it is used as a client, the gateway connects to an AP for Internet access. The status bar shows the current Wi-Fi connection status of the gateway.

![1690880119901-933471ec-5b7b-44a0-84b5-63c9a0f9b5b3.png](./img/Gs3dvISjhRc0qruU/1690880119901-933471ec-5b7b-44a0-84b5-63c9a0f9b5b3-518830.png)

**Method for providing network access services for wireless terminals when the gateway is used as an AP:**

Click "Wi-Fi >> Wi-Fi 2.4 or Wi-Fi 5G" and select "AP" for "Station Role". Enter the SSID, authentication method, and key consistent with those of the wireless AP. Click Apply & Save.

![1690880120198-15638125-3546-45e4-a2ab-3acd738fb142.png](./img/Gs3dvISjhRc0qruU/1690880120198-15638125-3546-45e4-a2ab-3acd738fb142-530226.png)

**Method for connecting to an AP for Internet access when VG710 is used as a client:**

Select "Client", enter the Wi-Fi SSID and key, and click Apply & Save.

![1690880120505-f380fbec-4d5a-4f90-9385-f0594ca42eb6.png](./img/Gs3dvISjhRc0qruU/1690880120505-f380fbec-4d5a-4f90-9385-f0594ca42eb6-137433.png)

### Loopback Port

**Method for adding multiple loopback ports:**

Click "Network >> Loopback >> Multi-IP Settings", configure any IP address for the gateway, click Add, and then click Apply & Save.

![1690880120766-bbcfb3c4-85fd-42a4-b1c2-4253437fd975.png](./img/Gs3dvISjhRc0qruU/1690880120766-bbcfb3c4-85fd-42a4-b1c2-4253437fd975-632794.png)

### Layer 2 Switch

Check the network connection status of GE 1 to GE 4. LINK UP indicates that the network is connected. LINK DOWN indicates that the network is disconnected.

![1690880121059-25fd5590-2de9-4b78-a3f4-7b01badcc82c.png](./img/Gs3dvISjhRc0qruU/1690880121059-25fd5590-2de9-4b78-a3f4-7b01badcc82c-966371.png)

### OBD

OBD is used to collect vehicle condition data, obtain emission information, and perform fault diagnosis in real time. Vehicle condition data includes key parameters such as the fuel level, mileage, driving speed, engine speed, engine load, coolant temperature, and brake pressure. Emission information includes the volume of AdBlue, the operating and monitoring status of various exhaust post-processing sensors (such as the exhaust gas sensor and diesel particle filter) and catalysts, etc. In fault diagnosis, standard fault codes of vehicles and description information can be obtained in real time, so that vehicle maintenance personnel can learn the vehicle health status in time and locate the faults.

To collect vehicle data, the gateway is connected to the diagnostic port of the vehicle through the I/O port of the gateway over the OBD-II or J1939 cable. The cable accessories can be selected or customized during purchasing. For details about the access method, see Section 4.4 in the *VG710 Quick Start Guide*. After the gateway starts, the OBD service is automatically enabled to collect key vehicle condition data and fault code information.

| ![1690880121339-6091928d-5ba1-4a6e-86a6-bfe121289895.png](./img/Gs3dvISjhRc0qruU/1690880121339-6091928d-5ba1-4a6e-86a6-bfe121289895-387227.png)Note:<br/>The power supply and OBD cable of the gateway shall be installed when the vehicle is off. |
| :--- |

The vehicle status information is displayed on the OBD status page.

**OBD Status:**

**CAN Link Status** (ERROR-ACTIVE indicates that the gateway has successfully connected to the diagnostic port of the vehicle. Other status indicates that the connection is abnormal or the diagnostic port of the vehicle is not identified.)

**CAN Bitrate** (In OBD, the CAN bitrate is automatically adapted, generally 250 kbps or 500 kbps.)

**CAN Bind** ("OBD" (default) or "Custom")

**OBD Connection Status** ("Disconnected", "Connecting", or "Connected")

**OBD Protocol Type** (OBD-II or J1939)

![1690880121759-5f4e132d-8c8d-4cc9-9d8c-ceb838692b9c.png](./img/Gs3dvISjhRc0qruU/1690880121759-5f4e132d-8c8d-4cc9-9d8c-ceb838692b9c-947046.png)

**Scan OBD Data and Export OBD Report:**

Click the <u>Scan OBD Data</u> button to generate a OBD data report containing detailed vehicle condition data and diagnostic information. Click the <u>Export OBD Report</u> button to save the generated OBD data report to the local storage.

**OBD Data Stream:** The real-time vehicle condition data is displayed.

![1690880122039-eea6b3ca-976d-4fcd-a686-c0302b9ca588.png](./img/Gs3dvISjhRc0qruU/1690880122039-eea6b3ca-976d-4fcd-a686-c0302b9ca588-777297.png)

**OBD Ability:**

Version of the OBD ability;

Type of the OBD protocol;

Vehicle identification number (VIN);

Valid variables and reference values that can be collected by the gateway.

![1690880122354-a34a0e99-30ec-4bba-bb1a-db121ded6e06.png](./img/Gs3dvISjhRc0qruU/1690880122354-a34a0e99-30ec-4bba-bb1a-db121ded6e06-840149.png)

### VPN Application

The VPN is intended to establish a private network on the public network for encrypted communication. A VPN gateway enables remote access by encrypting data packets and converting the destination address of data packets. The VPN can be realized by a server, hardware, or software, or in other ways. Compared with the traditional DDN private line or frame relay, the VPN provides a more secure and convenient remote access solution.

**Common VPN application scenario:**For example, an employee on a business trip accesses the enterprise's intranet. The employee connects to the enterprise's VPN server and then accesses the enterprise's intranet through the VPN server. Communication data between the VPN server and the client is encrypted and can be regarded as being transmitted on a dedicated data network. This ensures data security.

### IPsec

IPsec is a group of open network security protocols developed by IETF. At the IP layer, the data source authentication, data encryption, data integrity, and anti-replay functions are used to ensure the security of data transmission between communication parties on the Internet. This reduces the risk of leakage and eavesdropping, ensures the integrity and confidentiality of data, and ensures the security of service transmission for users.

**Scenario:** Data is transmitted between the subnet (192.168.1.0/24) of headquarters A and the subnet (172.16.1.0/24) of customer branch B through gateway A and gateway B. The transmission channels of gateway A and gateway B are encrypted over IPsec, to protect the security of data transmission between headquarters A and customer branch B.

![1690880122810-1a78999c-8ba7-4a64-ace8-3d682958f9d1.png](./img/Gs3dvISjhRc0qruU/1690880122810-1a78999c-8ba7-4a64-ace8-3d682958f9d1-194148.png)

**Method for encrypting the transmission channels of gateway A and gateway B over IPsec:**

**Parameter settings:**

| **Gateway A** | | | **Gateway B** |
| :--- | --- | --- | :--- |
| **Set IKEv1/v2 parameters** | | | **Set IKEv1/v2 parameters** |
| ID | Custom | | ID | Custom |
| Encryption algorithm | AES128 | | Encryption algorithm | Same as that of gateway A |
| Hash algorithm | SHA1 | | Hash algorithm | |
| Diffie-Hellman key exchange | Group2 | | Diffie-Hellman key exchange | |
| Lifecycle | 86400 | | Lifecycle | |
| **IPsec policy** | | | **IPsec policy** |
| Name | Custom | | Name | Custom |
| Encapsulation | ESP | | Encapsulation | Same as that of gateway A |
| Encryption algorithm | AES128 | | Encryption algorithm | |
| Authentication method | SHA1 | | Authentication method | |
| IPsec mode | Tunnel mode | | IPsec mode | |
| **IPsec tunnel configuration** | | | **IPsec tunnel configuration** |
| Peer address | Address where gateway B establishes the IPsec service | | Peer address | Address where gateway A establishes the IPsec service |
| Interface | Interface for establishing the IPsec service | | Interface | Interface for establishing the IPsec service |
| IKE version | IKE version used | | IKE version | Same as that of gateway A |
| Authentication method | Shared key | | Authentication method | |
| Local subnet | IP address of the subnet of gateway A | | Local subnet | IP address of the subnet of gateway B |
| Peer subnet | IP address of the subnet of gateway B | | Peer subnet | IP address of the subnet of gateway A |

**Detailed configuration steps:**

1. Configure gateway A and gateway B.

(1) Add IKE and IPsec policies, and click Apply & Save.

(2) Add IPsec tunnels and click Apply & Save.

![1690880123258-0dadbafa-9337-4298-88e8-e251895a41a3.png](./img/Gs3dvISjhRc0qruU/1690880123258-0dadbafa-9337-4298-88e8-e251895a41a3-686038.png)

![1690880123536-f9cd0182-163e-4729-a323-f12abaf7e637.png](./img/Gs3dvISjhRc0qruU/1690880123536-f9cd0182-163e-4729-a323-f12abaf7e637-839150.png)

1. Access the IPsec status page. The IPsec VPN is established successfully if the page is shown as below.

![1690880123906-edcf12d8-fc1a-4ac1-b31c-b05e27adfcf2.png](./img/Gs3dvISjhRc0qruU/1690880123906-edcf12d8-fc1a-4ac1-b31c-b05e27adfcf2-036673.png)

| ![1690880124176-7059a33e-f355-4c97-a64f-f7ea2f76bdc4.png](./img/Gs3dvISjhRc0qruU/1690880124176-7059a33e-f355-4c97-a64f-f7ea2f76bdc4-344704.png)Note:<br/>The IPsec profile does not need to be configured for establishing an IPsec VPN, but needs to be configured for establishing a DM VPN. |
| :--- |

### GRE

The Generic Routing Encapsulation (GRE) protocol can be used to encapsulate datagrams of some network layer protocols, so that these encapsulated datagrams can be transmitted on the IPv4 network.

**Scenario:** GRE is enabled for VG710**_** A and VG710_B through the public network.

![1690880124481-15e26ca2-65fe-447b-ad56-4dae36c525b7.png](./img/Gs3dvISjhRc0qruU/1690880124481-15e26ca2-65fe-447b-ad56-4dae36c525b7-125872.png)

**Method for enabling GRE for transmission channels of VG710_A and VG710_B:**

1. Click "VPN >> GRE" and then click Add.

![1690880124936-13c2273e-7c02-4b51-a748-0027ce968df0.png](./img/Gs3dvISjhRc0qruU/1690880124936-13c2273e-7c02-4b51-a748-0027ce968df0-179080.png)

1. Set "Index" as required. Select "Point to Point" or "Subnet" for "Network Type". Set "Local Virtual IP" and "Peer Virtual IP", ensuring that they are on the same network segment. Enter the source and peer IP addresses or interfaces and the key. Click Apply & Save.

![1690880125306-7b8266fa-b785-4d53-a476-3354fb2e64d5.png](./img/Gs3dvISjhRc0qruU/1690880125306-7b8266fa-b785-4d53-a476-3354fb2e64d5-619744.png)

1. Set VG710_B in the same way. The virtual and peer IP addresses of VG710_B must correspond to those of VG710_A, and the key must be the same as that of VG710_A.

### L2TP

The Layer 2 Tunneling Protocol (L2TP) is an industrial-standard Internet tunneling protocol used to encrypt network data streams.

**Method for settings when the gateway is used as an L2TP client:**

1. Click "VPN >> L2TP >> L2TP Client >> L2TP Class", enter a name of an L2TP class, and click Add.

![1690880125594-1c7a2f67-b338-4426-8428-48c818600170.png](./img/Gs3dvISjhRc0qruU/1690880125594-1c7a2f67-b338-4426-8428-48c818600170-255174.png)

1. Configure the pseudowire class: Enter a name of any pseudowire class. "L2TP Class" is the same as that on the "L2TP Class" page. Set "Source Interface" to the interface connecting to the server. Select L2TPV2 for "Protocol" and click Add.

![1690880125921-9b0f0663-f5d4-49f4-89e5-a1fc122ae283.png](./img/Gs3dvISjhRc0qruU/1690880125921-9b0f0663-f5d4-49f4-89e5-a1fc122ae283-657412.png)

1. Set L2TPV2 tunnel parameters: Enter the server's domain name or IP address for "L2TP Server". "Pseudowire Class" is the same as that on the "Pseudowire Class" page. Enter the user name and password created on the server. Set other parameters as required. Click Apply & Save.

![1690880126213-62583bb3-6fc0-4f3c-8f99-53d115182d0c.png](./img/Gs3dvISjhRc0qruU/1690880126213-62583bb3-6fc0-4f3c-8f99-53d115182d0c-774191.png)

1. After gateway A and gateway B are configured, access the L2TP status page to view the L2TP connection status.

![1690880126520-f679fa5f-88ea-46b7-9eda-c1b3531b43a5.png](./img/Gs3dvISjhRc0qruU/1690880126520-f679fa5f-88ea-46b7-9eda-c1b3531b43a5-141661.png)

### OpenVPN

OpenVPN is realized based on the application-layer VPN of the OpenSSL library. It supports multiple authentication methods such as the certificate, key, and user name/password. Compared with the traditional VPN, it is simpler and easier to use.

**Authentication methods:**

| **Authentication method** | **Operation on the web page** |
| --- | --- |
| **None** | No authentication is required. |
| **User name/password** | Enter the user name and password created on the OpenVPN server, click "VPN >> Certificate Management", and import the CA certificate, public key, and private key for authentication. |
| **Pre-shared key** | Enter the pre-shared key created on the OpenVPN server. |
| **Digital certificate** | Click "VPN >> Certificate Management" and import the CA certificate, public key, and private key. |
| **Digital certificate/user name/password** | Enter the user name and password created on the OpenVPN server, click "VPN >> Certificate Management", and import the CA certificate, public key, and private key for authentication. |
| **Digital certificate/TLS authentication** | Enter the pre-shared key created on the OpenVPN server, click "VPN >> Certificate Management", and import the CA certificate, public key, and private key for authentication. |
| **Digital certificate/TLS authentication/user name/password** | Enter the pre-shared key, user name, and password created on the OpenVPN server, click "VPN >> Certificate Management", and import the CA certificate, public key, and private key for authentication. |

**Method for settings when the gateway is connected to the OpenVPN server as a client:**

OpenVPN can be configured manually, or OpenVPN configurations can be imported. In the following example, the authentication type is a digital certificate.

1. Set the OpenVPN parameters for the gateway as shown in the figure below, ensuring that the network parameters at both ends of the tunnel are consistent. Click Apply & Save.

![1690880126877-993e3101-96a9-4e70-af1e-6d5e46941242.png](./img/Gs3dvISjhRc0qruU/1690880126877-993e3101-96a9-4e70-af1e-6d5e46941242-356608.png)

1. Select a digital certificate for "Authentication Type", click "VPN >> Certificate Management", and import the CA certificate, public key, and private key.

2. Click Apply & Save. Return to the "Status" page and view the tunnel status.

![1690880127135-2c85488f-f9ef-47ca-b2a2-da4258d7ebe2.png](./img/Gs3dvISjhRc0qruU/1690880127135-2c85488f-f9ef-47ca-b2a2-da4258d7ebe2-753787.png)

**5.3.5 Certificate Management**

Certificates can be imported or exported on this page. Certificates are used for IPsec and OpenVPN services.

**Method for importing a certificate:**

Click "VPN >> Certificate Management >> Browse", select the certificate obtained from the certificate server, click Import *XX* Certificate, and then click Apply & Save.

![1690880127386-f445f1fb-3b32-4db0-973b-6e7d84d645a2.png](./img/Gs3dvISjhRc0qruU/1690880127386-f445f1fb-3b32-4db0-973b-6e7d84d645a2-353969.png)

![1690880127652-7f11ceee-3d82-4a15-b40f-66403cc24729.png](./img/Gs3dvISjhRc0qruU/1690880127652-7f11ceee-3d82-4a15-b40f-66403cc24729-231453.png)

If no local certificate is available, check "Enable SCEP (Simple Certificate Enrollment Protocol)" to apply for a certificate online.

**Method for applying for a certificate for the gateway online:**

1. Click "VPN >> Certificate Management". Check "Enable SCEP (Simple Certificate Enrollment Protocol)" and "Force to re-enroll". Enter the certificate protection key and confirm it. Enter the URL of the certificate server, the certificate name, and the FQDN. Click Apply & Save.

2. After the server issues the certificate, check the application status. If the application status is "Completion", the certificate application succeeds.

![1690880127948-485355ed-2305-48e9-9cb6-aecc13c1fa0b.png](./img/Gs3dvISjhRc0qruU/1690880127948-485355ed-2305-48e9-9cb6-aecc13c1fa0b-744736.png)

### Services

**5.4.1 DHCP (Automatic IP Address Allocation)**

DHCP uses the client/server communication mode. The client submits a configuration application to the server, and the server returns the IP address assigned to the client to realize the dynamic configuration of the IP address.

**The DHCP server and DHCP forwarding function are mutually exclusive.**

**Method for settings when the gateway is used as a DHCP server:**

Click "Services >> DHCP >> DHCP Server". In the "DHCP Server" bar, check "Enable", select an interface, set the start and end IP addresses, click Add, and then click Apply & Save.

![1690880128257-7f7b2e95-4265-4623-bf4f-d7edd4266a03.png](./img/Gs3dvISjhRc0qruU/1690880128257-7f7b2e95-4265-4623-bf4f-d7edd4266a03-315686.png)

**Method for settings when the gateway is used as a DHCP client:**

Click "Services >> DHCP >> DHCP Client", select the gateway interface, and click Apply & Save.

![1690880128530-e17b4baf-f7a6-4904-9d29-138f378a75e9.png](./img/Gs3dvISjhRc0qruU/1690880128530-e17b4baf-f7a6-4904-9d29-138f378a75e9-114809.png)

**Method for enabling DHCP forwarding for the gateway:**

DHCP forwarding is also referred to as a DHCP relay agent. It can process and forward DHCP information between different subnets and physical network segments.

Click "Services >> DHCP >> DHCP Relay", check "Enable", enter the server address, select the gateway interface, and click Apply & Save.

![1690880128839-068ad701-6691-474a-b3b4-8677dbd3cdec.png](./img/Gs3dvISjhRc0qruU/1690880128839-068ad701-6691-474a-b3b4-8677dbd3cdec-781006.png)

**5.4.2 DNS**

The domain name service (DNS) is a distributed network directory service mainly used for mutual conversion between a domain name and an IP address.

**Method for enabling the DNS server for the gateway:**

Click "Services >> DNS >> DNS Server", enter the address of the DNS server, and click Apply & Save.

![1690880129065-318eb9d9-bc4b-4c3c-912f-eaa48d2eb085.png](./img/Gs3dvISjhRc0qruU/1690880129065-318eb9d9-bc4b-4c3c-912f-eaa48d2eb085-990024.png)

**Method for enabling DNS forwarding for the gateway:**

As a DNS agent, the gateway forwards DNS request and response messages between the DNS client and the DNS server, and replaces the DNS client for domain name resolution.

**If the DHCP service is enabled for the gateway, DNS forwarding is enabled by default and cannot be disabled.**

Click "Services >> DNS >> DNS Relay", check "Enable DNS Relay", set the mapping between the domain name and the IP address, click Add, and then click Apply & Save. After the settings are completed, when a DNS client on the LAN requests a host domain name in the list, the DNS agent server returns the corresponding IP address to the client.

![1690880129355-ce59175a-d5ba-4ce7-866f-c81a1a95fc00.png](./img/Gs3dvISjhRc0qruU/1690880129355-ce59175a-d5ba-4ce7-866f-c81a1a95fc00-286779.png)

**5.4.3 DDNS**

The dynamic domain name server (DDNS) maps the dynamic IP address of the gateway to a fixed DNS. Each time a user connects to the Internet, the client program transmits the dynamic IP address of the host to the server program on the server host through information transfer. The server program provides the DDNS service and realizes dynamic domain name resolution. In this way, you can access the Internet by entering the domain name, even if the IP address is changed.

**Method for enabling the DDNS service for the gateway:**

1. If the Custom service is used, set "Method Name" as required, select "Custom" for "Service Type", and enter the DDNS expression "<http://user> name:[<u>password@ddns.oray.com/ph/update?hostname=</u>](mailto:password@ddns.oray.com/ph/update?hostname=)host name" of the server for "Url". This expression is only for reference. The actual URL is provided by the service provider (usually available on the official website of the service provider). Click Add.

If a common domain name server other than the Custom service is used, set "Method Name" and "Service Type" as required, enter the user name, password, and host name obtained from the server, and click Add.

If "Disable" is selected, the DDNS service is not used.

1. Select the gateway interface, enter the name of the DDNS update method, click Add, and then click Apply & Save to apply the DDNS update method to the gateway interface.

![1690880129654-b51dbe56-7564-413a-a684-7e8d42d71b03.png](./img/Gs3dvISjhRc0qruU/1690880129654-b51dbe56-7564-413a-a684-7e8d42d71b03-758789.png)

1. Wait several minutes after the DDNS settings are applied and saved. Then ping the host name (domain name) of the domain name server to confirm the successful application of the DDNS service.

![1690880129938-ddcc9109-f1ec-4570-8700-d1e7ebc2f758.png](./img/Gs3dvISjhRc0qruU/1690880129938-ddcc9109-f1ec-4570-8700-d1e7ebc2f758-464401.png)

![1690880130332-a5491407-9957-45b6-a167-6daefcc534e7.png](./img/Gs3dvISjhRc0qruU/1690880130332-a5491407-9957-45b6-a167-6daefcc534e7-252183.png)

**5.4.4 SMS**

The short message service (SMS) is enabled for gateway restart and manual dialup via SMS messages. Some gateways can receive alarm information in the SMS whitelist.

**Method for controlling gateway restart and manual dialup via SMS messages**

Click "Services >> SMS" and check "Enable". In the "SMS Access Control" bar, set "ID" as required, select "permit" for "Action", enter the phone number, and click Apply & Save. When you activate the dialup port via SMS, after the configuration is completed, you can send the **reboot** command to restart the gateway by using the mobile phone number, or send the **cellular 1 ppp up/down** command to make the gateway redial or interrupt the dialup.

![1690880130961-fc3cc6e1-cfe9-458c-934f-830e59b67ed1.png](./img/Gs3dvISjhRc0qruU/1690880130961-fc3cc6e1-cfe9-458c-934f-830e59b67ed1-929509.png)

**5.4.5 GPS**

**Position:** You can view the current positioning information.

![1690880131286-c612ce95-6346-4132-b839-0b0d2161d979.png](./img/Gs3dvISjhRc0qruU/1690880131286-c612ce95-6346-4132-b839-0b0d2161d979-808881.png)

**Method for enabling GPS for the gateway:**

Click "Services >> Enable GPS", check "Enable", and click Apply & Save. By default, GPS is enabled for the gateway.

![1690880131625-48986eb8-680a-48c5-a87f-80bfd28700bf.png](./img/Gs3dvISjhRc0qruU/1690880131625-48986eb8-680a-48c5-a87f-80bfd28700bf-041155.png)

**Method for forwarding GPS data to the server over IP when VG710 is used as a client:**

Click "Services >> GPS IP Forwarding", check "Enable", select "Client" for "Type", enter the server address and port in the "Destination IP Address" bar, click Add, and then click Apply & Save.

![1690880131928-c03bd9e4-8278-4427-8976-9469d425e478.png](./img/Gs3dvISjhRc0qruU/1690880131928-c03bd9e4-8278-4427-8976-9469d425e478-982368.png)

**Method for forwarding GPS data over IP when VG710 is used as a server:**

Click "Services >> GPS IP Forwarding", check "Enable", select "Server" for "Type", and click Apply & Save.

![1690880132261-ebfb6098-f1cd-49c1-900b-a97cbec1f229.png](./img/Gs3dvISjhRc0qruU/1690880132261-ebfb6098-f1cd-49c1-900b-a97cbec1f229-295871.png)

**Method for forwarding GPS data by VG710 through a serial port:**

Click "Services >> GPS Serial Forwarding", check "Enable", and select a serial port type based on the data transmission port used. Ensure that the baud rate, data bits, parity bit, and stop bit are the same as the current settings. Click Apply & Save.

![1690880132607-e7445fdc-b1fc-4b3d-945b-34eec917ea19.png](./img/Gs3dvISjhRc0qruU/1690880132607-e7445fdc-b1fc-4b3d-945b-34eec917ea19-795831.png)

**5.4.6 QoS**

Quality of service (QoS) is a network security mechanism that enables a network to provide better services for designated network communication by using various basic technologies. It is a technology for solving problems such as network delays and blocking.

**Method for setting the egress maximum bandwidth for the gateway through QoS control:**

Click "QoS >> Traffic Control >> Apply QoS", select the gateway interface, enter the egress maximum bandwidth, click Add, and then click Apply & Save.

![1690880132896-f9fdf330-0481-4f5a-9e63-44cb974a5170.png](./img/Gs3dvISjhRc0qruU/1690880132896-f9fdf330-0481-4f5a-9e63-44cb974a5170-835705.png)

**Method for applying the ingress and egress policies for the gateway through QoS control:**

1. Add a network link classifier. Click "QoS >> Traffic Control >> Classifier", check "Any Packets", set the source and destination addresses of the link, select transmit protocols for QoS control, and click Add.

2. Set transmission policies. Click "QoS >> Traffic Control >> Policy", enter a custom policy name for "Name", enter the classifier name for "Classifier", set the guaranteed bandwidth, maximum bandwidth, and policy priority, and click Add.

3. Click "QoS >> Traffic Control >> Apply QoS", select the gateway interface, enter the policy name for "Ingress Policy" and "Egress Policy", click Add, and then click Apply & Save.

![1690880133262-10a30c8d-c739-4f12-a74b-b42d4ffaf0c4.png](./img/Gs3dvISjhRc0qruU/1690880133262-10a30c8d-c739-4f12-a74b-b42d4ffaf0c4-985847.png)

**5.4.7 Traffic Control**

**Method for enabling traffic control for the gateway:**

Click "Services >> Traffic Control", enable traffic control, set traffic control parameters, and click Apply & Save. After the settings are completed, the system generates an alarm, stops forwarding, or disables the interface when the traffic exceeds the limit according to the settings on this page.

![1690880133584-46dd9d48-91b6-40af-8f3f-293569b2c1f3.png](./img/Gs3dvISjhRc0qruU/1690880133584-46dd9d48-91b6-40af-8f3f-293569b2c1f3-502839.png)

### Firewall

**5.5.1 ACL**

The access control list (ACL) is an access control technology based on packet filtering. It can filter the packets on the interface based on preset conditions and allow them to pass or discard them.

**Common scenario:** By default, all devices on the LAN (bridge 1) can access the Internet, except the device with the IP address of 192.168.2.100.

**Method for setting VG710:**

1. Click "Firewall >> ACL >> Add". Enter the ID and sequence number. A smaller sequence number indicates a higher priority. Select "deny" for "Action". Set "Source IP" to "192.168.2.100" and "Source Wildcard" to "0.0.0.0". Leave "Destination IP" empty, which indicates 0.0.0.0/0, that is, all IP addresses. Click Apply & Save.

![1690880133856-419ba223-87fc-45d9-96dc-702e39a8c315.png](./img/Gs3dvISjhRc0qruU/1690880133856-419ba223-87fc-45d9-96dc-702e39a8c315-974663.png)

1. Return to the ACL page, add the rule with the ID of 101 to the management rule of bridge 1, and click Add. Click Apply & Save.

![1690880134227-6ac22859-a304-4d81-9189-e6593c0469a0.png](./img/Gs3dvISjhRc0qruU/1690880134227-6ac22859-a304-4d81-9189-e6593c0469a0-937116.png)

**5.5.2 NAT**

Network address translation (NAT) can be used when some hosts on a private network have been assigned with local IP addresses (that is, private IP addresses used only on the private network), but expect to communicate with hosts on the Internet (without encryption).

**Common scenario:** A user expects to access a camera on the LAN of the device through the public network to view the current driving conditions of the vehicle. The camera address is 192.168.2.100, and the open port 18000 provides video services.

1. Click "Firewall >> NAT", and select "DNAT" for "Action", and "Outside" for "Source Network". Select "IP PORT to IP PORT" or "INTERFACE PORT to IP PORT" for "Translation Type". The public IP address obtained through dial-up is not fixed, so "INTERFACE PORT to IP PORT" is more convenient. Select "TCP" for "Transmit Protocol" because video services are transmitted over TCP. Select "cellular 1" (dialup interface for the cellular network) for "Interface" and set "Port" to "20000". Set "IP Address" and "Port" under "Translated Address" to "192.168.200" and "18000" respectively. Click Apply & Save.

The gateway redirects the TCP service destined for port 20000 of the cellular 1 interface to the internal IP address 192.168.2.100 and port 18000, to enable access to the internal services.

![1690880134575-914d9367-b590-4845-b6c4-a521f6751b2c.png](./img/Gs3dvISjhRc0qruU/1690880134575-914d9367-b590-4845-b6c4-a521f6751b2c-914122.png)

**5.5.3 MAC-IP Binding**

After MAC-IP binding, the PC can access the public network through the gateway only by using the IP address bound to the MAC address of the PC.

**Method for binding the MAC address and IP address of a connected device:**

1. Click "Firewall >> ACL" and select "Block" for "Default Filter Policy".

![1690880134881-1e308486-f427-4829-8810-83268b1728a5.png](./img/Gs3dvISjhRc0qruU/1690880134881-1e308486-f427-4829-8810-83268b1728a5-537789.png)

1. Click "Firewall >> MAC-IP Binding", check "Enable", enter the MAC address and IP address of the connected device, click Add, and click Apply & Save.

![1690880135179-9a69879c-25f4-4081-89b2-a5c6847f60c7.png](./img/Gs3dvISjhRc0qruU/1690880135179-9a69879c-25f4-4081-89b2-a5c6847f60c7-835836.png)

### Routing

**5.6.1 Static Routing**

Set the destination network, subnet mask, and interface or gateway as required.

![1690880135440-6112d7b5-9bd1-4bf4-9620-424867abdb28.png](./img/Gs3dvISjhRc0qruU/1690880135440-6112d7b5-9bd1-4bf4-9620-424867abdb28-274879.png)

**5.6.2 Dynamic Routing**

**Scenario:**Enable dynamic routing between two LANs for mutual communication between them. The topology is shown below.

![1690880135819-fb2dea07-59ed-4dc6-8e46-7af5af7ef3b6.png](./img/Gs3dvISjhRc0qruU/1690880135819-fb2dea07-59ed-4dc6-8e46-7af5af7ef3b6-439856.png)

**5.6.2.1 RIP**

The Routing Information Protocol (RIP) is a simple internal dynamic routing protocol mainly used on small-scale networks.

**Method for enabling dynamic routing between VG710_A and VG710_B over RIP in the scenario:**

1. Configure VG710_A. Click "Routing >> Dynamic Routing >> RIP", check "Enable", and configure VG710_A in the "Network" bar to announce the routing entry of VG710_A.

![1690880136322-01a03f1a-19bc-4c39-8fab-40fecfcbf96d.png](./img/Gs3dvISjhRc0qruU/1690880136322-01a03f1a-19bc-4c39-8fab-40fecfcbf96d-919309.png)

1. Configure VG710_B.

![1690880136679-39350476-8b41-42b1-99ba-f8efa4e50f77.png](./img/Gs3dvISjhRc0qruU/1690880136679-39350476-8b41-42b1-99ba-f8efa4e50f77-060981.png)

1. After the configuration is completed, check whether PC 1 can communicate with PC 2. If yes, the dynamic route is added successfully. The RIP route learned by VG710_B is shown in the figure below.

![1690880136963-44f01c98-3736-4472-acfa-0b2ca46f2d31.png](./img/Gs3dvISjhRc0qruU/1690880136963-44f01c98-3736-4472-acfa-0b2ca46f2d31-726688.png)

**5.6.2.2 OSPF**

The Open Shortest Path First (OSPF) protocol is a link-status-based internal gateway protocol mainly used on large-scale networks.

**Method for enabling dynamic routing between VG710_A and VG710_B over OSPF in the scenario:**

1. Configure VG710_A. Click "Routing >> Dynamic Routing >> OSPF", check "Enable", enter a valid IP address for "Router ID", and configure VG710_A in the "Network" bar to announce the routing entry of VG710_A.

![1690880137273-72a36788-cf69-43bd-95cd-ddf159670123.png](./img/Gs3dvISjhRc0qruU/1690880137273-72a36788-cf69-43bd-95cd-ddf159670123-954569.png)

1. Set parameters for VG710_B.

![1690880137549-ba16c6bc-49db-44e6-aed9-9eeefa1f8d6e.png](./img/Gs3dvISjhRc0qruU/1690880137549-ba16c6bc-49db-44e6-aed9-9eeefa1f8d6e-506823.png)

1. After the configuration is completed, check whether PC 1 can communicate with PC 2. If yes, the dynamic route is added successfully. The OSPF route learned by VG710_B is shown in the figure below.

![1690880137854-e2756be0-85a6-4501-97e6-1f6d081f1d6c.png](./img/Gs3dvISjhRc0qruU/1690880137854-e2756be0-85a6-4501-97e6-1f6d081f1d6c-739860.png)

**5.6.2.3 BGP**

**Method for enabling dynamic routing between VG710_A and VG710_B over BGP in the scenario:**

1. Configure VG710_A. Click "Routing >> Dynamic Routing >> BGP", check "Enable", and set "AS number" as required.

![1690880138642-a026f48b-ffcc-45b8-9d65-8cf8f0932d0f.png](./img/Gs3dvISjhRc0qruU/1690880138642-a026f48b-ffcc-45b8-9d65-8cf8f0932d0f-639062.png)

1. In the "Neighbor" bar, click Add, enter the IP address 192.168.1.2 of VG710_B, set "AS number" as required, and click Apply & Save.

![1690880139168-8ec3f21c-32f3-41bf-bd2f-84189b1b749a.png](./img/Gs3dvISjhRc0qruU/1690880139168-8ec3f21c-32f3-41bf-bd2f-84189b1b749a-001995.png)

1. Enter a valid IP address for "Router ID", configure VG710_A in the "Network" bar, and click Add, to announce the routing entry of VG710_A. Then click Apply & Save.

![1690880139512-ae00c464-4a75-4acc-9bdf-d3a424c3bfd4.png](./img/Gs3dvISjhRc0qruU/1690880139512-ae00c464-4a75-4acc-9bdf-d3a424c3bfd4-872026.png)

1. Set parameters for VG710_B. The parameters are the same as or corresponding to those of VG710_A.

![1690880139827-80a6d9a4-28ea-4ff1-ac63-882c2b9333df.png](./img/Gs3dvISjhRc0qruU/1690880139827-80a6d9a4-28ea-4ff1-ac63-882c2b9333df-235541.png)

1. After the configuration is completed, check whether PC 1 can communicate with PC 2. If yes, the dynamic route is added successfully. The BGP route learned by VG710_B is shown in the figure below.

![1690880140133-a87ea157-0b43-4ed0-bf2c-f6887496a89a.png](./img/Gs3dvISjhRc0qruU/1690880140133-a87ea157-0b43-4ed0-bf2c-f6887496a89a-277665.png)

### Link Backup

**5.7.1 SLA**

The service level agreement (SLA) is used to detect whether the link between the gateway and the ISP fails.

**Method for adding an SLA entry for the gateway:**

Click "Link Backup >> SLA >> Add", enter the detected IP address for "Destination Address", set other parameters as required, click Add, and then click Apply & Save.

**Timeout (ms)** indicates the duration for determining a detection failure. **Consecutive** indicates the number of detection failures resulting in a link failure.

![1690880140527-61af777e-909d-45b4-a84e-9a0e7358d3bb.png](./img/Gs3dvISjhRc0qruU/1690880140527-61af777e-909d-45b4-a84e-9a0e7358d3bb-949475.png)

**5.7.2 Track**

Currently, linkage is enabled between the track module and the following application modules: VRRP, static routing, and interface backup. If detection succeeds, the corresponding track entry is in the Positive state. If detection fails, the corresponding track entry is in the Negative state.

**Method for adding a track entry for VG710:**

Click "Link Backup >> Track >> Track", set "Index" as required, select "sla", "interface", or "vrrp" for "Type", set "SLA/VRRP ID" based on the ID in the SLA list, set "Negative Delay (s)" and "Positive Delay (s)" as required, click Add, and then click Apply & Save.

**Negative Delay (s):** In case of an abnormal state, switching can be delayed based on the delay setting (0 indicates immediate switching).

**Positive Delay (s):** When a failure is recovered, switching can be delayed based on the delay setting (0 indicates immediate switching).

![1690880140836-bcd061ce-c37c-4c83-95d8-607d513fe7ec.png](./img/Gs3dvISjhRc0qruU/1690880140836-bcd061ce-c37c-4c83-95d8-607d513fe7ec-535471.png)

**Method for adding an IPsec track entry for VG710:**

Click "Link Backup >> Track >> Track" and set "Index" as required. "positive-start/negative-stop" means starting the IPsec service when the track detection state is Positive and stopping the IPsec service when the track detection state is Negative.

![1690880141130-d18524cc-8121-4b65-ae9a-ec8031b66c34.png](./img/Gs3dvISjhRc0qruU/1690880141130-d18524cc-8121-4b65-ae9a-ec8031b66c34-717569.png)

**5.7.3 VRRP**

**Scenario:**Multiple gateways are connected to a network at the same time. Gateway A acts as the host, and gateway B acts as a backup for gateway A. When gateway A fails, gateway B temporarily replaces gateway A as the host.

**1. Networking requirement**

Host A uses the VRRP backup group comprising gateway A and gateway B as its default gateway to access host B on the Internet.

Information of the VRRP backup group:

● The backup group ID is 1.

● The IP address of the virtual gateway of the backup group is 10.5.16.88.

● Gateway A acts as the master gateway.

● Gateway A acts as a backup gateway that can be preempted.

**2. Networking diagram**

![1690880141534-542c9dbe-858e-4ec6-b74b-a061a6e613f1.png](./img/Gs3dvISjhRc0qruU/1690880141534-542c9dbe-858e-4ec6-b74b-a061a6e613f1-028844.png)

| **Gateway** | **Ethernet port connected to host A** | **IP address of the port connected to host A** | **Priority** | **Work mode** | |
| :---: | :---: | :---: | :---: | :---: | --- |
| VG710_A | bridge 1 | 10.5.16.80 | 110 | | Preemption |
| VG710_B | bridge 1 | 10.5.16.81 | 100 | | Preemption |

**Method for settings when VG710_A acts as the master gateway and VG710_B as a backup gateway:**

1. Configure VG710_A.

Click "Link Backup >> VRRP", set "Virtual Route ID" as required, select the gateway interface of VG710_A, enter the virtual IP address, set the interface priority to 110, and click Add.

![1690880142080-a81df13a-72e1-4390-a9e4-2f3f24473e9e.png](./img/Gs3dvISjhRc0qruU/1690880142080-a81df13a-72e1-4390-a9e4-2f3f24473e9e-088423.png)

In the navigation tree, click "Link Backup >> VRRP >> Status" and view the VRRP status.

![1690880142365-b8e4c3ee-adff-4f30-93af-c400ca6d8eee.png](./img/Gs3dvISjhRc0qruU/1690880142365-b8e4c3ee-adff-4f30-93af-c400ca6d8eee-364959.png)

1. Configure VG710_B.

Click "Link Backup >> VRRP", set the interface priority to 100, and click Add.

![1690880142639-c1d375d5-6df0-460f-831c-5a30fc7096ec.png](./img/Gs3dvISjhRc0qruU/1690880142639-c1d375d5-6df0-460f-831c-5a30fc7096ec-581757.png)

In the navigation tree, click "Link Backup >> VRRP >> Status" and view the VRRP status.

![1690880142931-f483dfe4-f644-42ab-9c73-558bbd997295.png](./img/Gs3dvISjhRc0qruU/1690880142931-f483dfe4-f644-42ab-9c73-558bbd997295-785795.png)

Under normal circumstances, VG710_A performs gateway functions. When VG710_A is shut down or fails, VG710_B performs gateway functions. The preemption mode is intended to enable VG710_A to continue to act as the master gateway after it recovers.

**5.7.4 Interface Backup**

**Scenario:** VG710 accesses the Internet via Wi-Fi, and an interface backup is created to enable VG710 to access the Internet through dial-up upon Wi-Fi failure. The topology is shown below.

![1690880143209-bdb15d60-ff11-4650-a6f2-9764ac276e53.jpeg](./img/Gs3dvISjhRc0qruU/1690880143209-bdb15d60-ff11-4650-a6f2-9764ac276e53-661321.jpeg)

**Method for creating an interface backup for the gateway:**

1. Enable VG710 to access the Internet via Wi-Fi.

![1690880143627-e212e27e-c2d9-4867-b3be-77b7ddc261d4.png](./img/Gs3dvISjhRc0qruU/1690880143627-e212e27e-c2d9-4867-b3be-77b7ddc261d4-131329.png)

1. Click "Link Backup >> SLA >> SLA >> Add" to add an ICMP detection entry. Set the IP address to the host address that can be detected over ICMP on the public or private network, for example, the public IP address 118.122.120.22. Click Apply & Save.

![1690880143891-3d771bd7-aefe-4df7-9436-479ff54347fa.png](./img/Gs3dvISjhRc0qruU/1690880143891-3d771bd7-aefe-4df7-9436-479ff54347fa-782749.png)

1. Click "Link Backup >> Track >> Track >> Add" to add a track entry. Select "sla" for "Type" and "dot11radio1" for "Interface", click Add, and then click Apply & Save.

![1690880144180-a0af64b8-8281-48ff-8011-071ec1c00be7.png](./img/Gs3dvISjhRc0qruU/1690880144180-a0af64b8-8281-48ff-8011-071ec1c00be7-543579.png)

1. Click "Link Backup >> Interface Backup >> Add", select "dot11radio1" for "Main Interface" and "cellular1" for "Backup Interface", and click Apply & Save.

![1690880144412-f4ab4f8e-844a-45b1-95ab-3e4de4f5a0b2.png](./img/Gs3dvISjhRc0qruU/1690880144412-f4ab4f8e-844a-45b1-95ab-3e4de4f5a0b2-623545.png)

1. Click "Routing >> Static Routing >> Add" and add two routes for network access through the "dot11radio1" and "cellular1" interfaces. A smaller value of "Distance" indicates a higher priority.

![1690880144666-e51dd560-1237-439e-b476-70b141471592.png](./img/Gs3dvISjhRc0qruU/1690880144666-e51dd560-1237-439e-b476-70b141471592-889079.png)

1. Trigger a Wi-Fi failure. According to the preset link detection policy, VG710 accesses the Internet through dial-up via the cellular port, and when Wi-Fi recovers, immediately switches to Wi-Fi for Internet access.

### Bluetooth

![1742463833997-67616607-0b89-48e9-8327-a81e5a05d9e1.png](./img/Gs3dvISjhRc0qruU/1742463833997-67616607-0b89-48e9-8327-a81e5a05d9e1-878916.png)

### Wizards

The "Wizards" module incorporates some common communication parameters, simplifying the operations.

**5.8.1 New Cellular**

After a common network interface card (NIC) is inserted, click "Wizards >> New Cellular >> Apply & Save" and access the status page to view the network connection status of the device. The device is connected to the network.

![1690880144921-02cae75d-76e4-45a8-bb83-62ddc894e534.png](./img/Gs3dvISjhRc0qruU/1690880144921-02cae75d-76e4-45a8-bb83-62ddc894e534-966096.png)

![1690880145154-bed5a67f-4989-4b82-a2b1-7f2f045dfe0e.png](./img/Gs3dvISjhRc0qruU/1690880145154-bed5a67f-4989-4b82-a2b1-7f2f045dfe0e-719512.png)

**5.8.2 New IPsec Tunnel**

A dedicated virtual tunnel is established between the gateway and other devices or cloud platforms on the network.

**Method for establishing an IPsec tunnel for the gateway:**

Click "Wizards >> New IPsec Tunnel", set "Map Interface" to an interface ("bridge": bridge interface; "cellular": dialup interface; "dot11radio": Wi-Fi interface) for which you want to establish a tunnel, enter the peer IP address for "Destination Address", and enter the subnet IP addresses and masks at both ends of the tunnel. In Phase 1, enter the IDs at both ends of the tunnel and the connection key, and click Apply & Save.

![1690880145492-6cbc62dd-b0f7-429b-acdb-6db03bfbf9a8.png](./img/Gs3dvISjhRc0qruU/1690880145492-6cbc62dd-b0f7-429b-acdb-6db03bfbf9a8-433364.png)

**5.8.3 IPsec Experts' Configuration**

This function is available only for specific users. To activate this function, contact the technical support personnel.

**5.8.4 New L2TPv2 Tunnel**

**Method for creating an L2TPv2 tunnel for the gateway:**

Set the parameters of the L2TP server and the local/remote addresses. Click Apply & Save.

![1690880145821-1b9e561d-f7f3-4191-8f1b-5bf281b2eaaa.png](./img/Gs3dvISjhRc0qruU/1690880145821-1b9e561d-f7f3-4191-8f1b-5bf281b2eaaa-219762.png)

**5.8.5 New Port Mapping**

Port mapping is to map a port of a host on the intranet to a port of a host on the extranet to provide corresponding services. When a user accesses the port on the extranet, the server automatically maps the request to the internal machine on the corresponding LAN.

**Scenario:** Users on the extranet cannot directly access a web server on the intranet. In this case, a port mapping can be created on the gateway so that the gateway automatically transfers the data to port 80 of the web server on the intranet when a user on the extranet accesses port 1000 via the cellular interface of the gateway.

![1690880146153-39f53a15-dfb8-4f3f-9d14-6e03f60f812f.png](./img/Gs3dvISjhRc0qruU/1690880146153-39f53a15-dfb8-4f3f-9d14-6e03f60f812f-809504.png)

**Method for creating a port mapping for the gateway:**

Click Wizards >> New Port Mapping". Enter the gateway interface for "Outside Interface", gateway port for "Service Port", IP address of the internal host for "Internal Address", and port ID of the internal host for "Internal Port". Click Apply & Save.

![1690880146529-08b0b62c-9022-4389-8891-cd0f2d583b1b.png](./img/Gs3dvISjhRc0qruU/1690880146529-08b0b62c-9022-4389-8891-cd0f2d583b1b-171273.png)

## APP Management

App function is an important part of the gateway to realize edge computing. The prerequisite for using this feature is to install the python SDK.

### APP

Step 1: click "APP>>APP management · > > Open Python app management", click apply and save.

Export and import the compiled app installation package. After importing the app installation package, the system will automatically decompress and install it.

![1690880146844-fec996b9-e638-4e06-845d-84457f02c9e2.png](./img/Gs3dvISjhRc0qruU/1690880146844-fec996b9-e638-4e06-845d-84457f02c9e2-703161.png)

Step 2: click running status. If the app management running status is running, the operation is successful

![1690880147213-79396e6e-0238-4e8b-8700-6d89f23f440a.png](./img/Gs3dvISjhRc0qruU/1690880147213-79396e6e-0238-4e8b-8700-6d89f23f440a-308214.png)

### Docker

The docker SDK is installed before using the docker function .

Step 1: click "app>>docker>> enable", enter the user name, password and port number in the input box, click apply and save

![1690880147516-817b9f86-86cb-454e-b111-2795707a4a85.png](./img/Gs3dvISjhRc0qruU/1690880147516-817b9f86-86cb-454e-b111-2795707a4a85-349206.png)

### Third party cloud platform

The gateway device connects to the cloud platform as a client to realize communication, and obtains data in real time according to the corresponding configuration of the gateway device to achieve the purpose of data interaction.

**6.3.1 MQTT protocol connection to cloud platform**

Step 1: click "APP>> third party cloud platform > >mqtt>> enable", select the address and port of the cloud platform server, click apply and save.

Which fields are sent to the platform by default, and the FlexAPI config can be modified

![1690880147952-eb68e1e6-59cd-4d5f-88ab-7b9cd5e94d67.png](./img/Gs3dvISjhRc0qruU/1690880147952-eb68e1e6-59cd-4d5f-88ab-7b9cd5e94d67-454397.png)

Step 2: click status. If the connection status is connected, the connection is successful.

![1690880148274-a0d18a3c-0e43-4e73-b6c7-3c2c44cb3aca.png](./img/Gs3dvISjhRc0qruU/1690880148274-a0d18a3c-0e43-4e73-b6c7-3c2c44cb3aca-562455.png)

Note: if the server needs authentication and encryption, it needs to be enabled correspondingly. Click "app>> third party cloud platform > >mqtt>> enable", select the address and port of the cloud platform server, and enable mqtt authentication and TLS encryption.

![1690880148641-98cc412e-3d55-49e8-9fb2-f302a80829da.png](./img/Gs3dvISjhRc0qruU/1690880148641-98cc412e-3d55-49e8-9fb2-f302a80829da-191435.png)

**6.3.2 TCP protocol connection to cloud platform**

Step 1: click "app>> third party cloud platform > >tcp>> enable", select the address and port of the cloud platform server, click apply and save

![1690880148957-f068ee2b-a26f-4717-b7b0-ba0bca9762ef.png](./img/Gs3dvISjhRc0qruU/1690880148957-f068ee2b-a26f-4717-b7b0-ba0bca9762ef-065034.png)

Step 2: click status. If the connection status is connected, the connection is successful.

![1690880149222-3f797393-37f4-4440-baf7-548591d42cf0.png](./img/Gs3dvISjhRc0qruU/1690880149222-3f797393-37f4-4440-baf7-548591d42cf0-296217.png)

### Local MQTT Agent

The gateway device acts as an mqtt server to proxy messages. When users need messages, they use the mqtt client to subscribe to information. Python App or Doker program use gateway info, Subscribe to messages from the local mqtt agent.

Step 1: click "app>> local mqtt agent > > enable local / local &amp; Lan", click apply and save

![1690880149488-32b1c077-2496-459a-8f5d-e4e62cc69b81.png](./img/Gs3dvISjhRc0qruU/1690880149488-32b1c077-2496-459a-8f5d-e4e62cc69b81-552540.png)

Step 2: use mqtt client information: server address, port, authentication and other information

This document uses mqtt Take FX test tool as an example.

![1690880149898-abc53de8-e3ba-4945-a081-8bbb17b2f388.png](./img/Gs3dvISjhRc0qruU/1690880149898-abc53de8-e3ba-4945-a081-8bbb17b2f388-381129.png)

Step 3: click Connect. If the icon turns green, it means the connection is successful. Then subscribe to the information according to the topic document. The gateway will return data in JSON format. For example, subscribe to cellular information

![1690880150233-57e345f0-5523-48c9-8232-d660b9b7f7c9.png](./img/Gs3dvISjhRc0qruU/1690880150233-57e345f0-5523-48c9-8232-d660b9b7f7c9-453065.png)

### REST API

In addition to using mqtt and TCP to obtain data, users can also use rest APIs to call data according to interface documents

Step 1: click "app>>rest api>> enable", select the address and port of the cloud platform server, click apply and save

![1690880150608-881f776b-bb78-4201-a42c-d9fb188d657d.png](./img/Gs3dvISjhRc0qruU/1690880150608-881f776b-bb78-4201-a42c-d9fb188d657d-576638.png)

Step 2: use tools such as postman according to the interface document to call the interface to obtain data.

1. Fill in the URL, token, etc. in the interface document, and note whether it is a get or post request;

2. Click send;

3. Finally, the gateway device will return the corresponding data results in JSON format;

![1690880150895-c7b016cf-8284-4f4a-8b82-1c002b92be7e.png](./img/Gs3dvISjhRc0qruU/1690880150895-c7b016cf-8284-4f4a-8b82-1c002b92be7e-528810.png)

### Azure IoT Edge

Click "APP>>Azure IOT edge>> enable", click apply and save

![1690880151360-6d08b3ca-da87-46d0-ab5d-11d9860cc7f4.png](./img/Gs3dvISjhRc0qruU/1690880151360-6d08b3ca-da87-46d0-ab5d-11d9860cc7f4-234979.png)

Note: this function item depends on docker. The docker function should be opened before opening

**6.7 User Data**

Step 1: click "APP>> User Data> > User Data Management", then enter the name and corresponding value, click add, and finally click apply and save.

![1690880151653-a00acdbd-3d52-4f72-a9bb-be0e7745a3d3.png](./img/Gs3dvISjhRc0qruU/1690880151653-a00acdbd-3d52-4f72-a9bb-be0e7745a3d3-086859.png)

Step 2: click "status". If the data exists in the status bar, it means that the addition is successful.

![1690880151937-dcee1879-c8c0-42f9-a4cc-6d5f63ad6c2f.png](./img/Gs3dvISjhRc0qruU/1690880151937-dcee1879-c8c0-42f9-a4cc-6d5f63ad6c2f-983296.png)

## Connecting the Gateway to a Cloud Platform

1. Click "Administration >> Device Manager >> Device Manager", check "Device Manager Enable", select the server address of the cloud platform, enter the registered account and license plate number of the cloud platform, and click Apply & Save.

![1690880152209-24063c00-110e-45ae-9674-b619f7c525b1.png](./img/Gs3dvISjhRc0qruU/1690880152209-24063c00-110e-45ae-9674-b619f7c525b1-422077.png)

1. Click "Status". "Connected" indicates that the gateway is successfully connected to the cloud platform.

## Industrial Ports (Serial Ports)

The industrial ports of VG710 include RS232 serial ports, RS485 serial ports, and IO ports.

### DTU

RS232 provides full-serial communication, enabling hardware-based traffic control.

RS485 provides half-duplex communication, enabling remote transmission of serial communication data.

**Method for setting web pages when the gateway is used as a DTU:**

1. Enable DTU 1 (RS232) or DTU 2 (RS-485).

2. Set the connection parameters of the gateway interface and industrial device. Communication is available only when the parameters at both ends of the network link are consistent.

![1690880152539-bffe6902-2e4f-4d1b-a7c3-eddd4aa09d56.png](./img/Gs3dvISjhRc0qruU/1690880152539-bffe6902-2e4f-4d1b-a7c3-eddd4aa09d56-269586.png)

1. Set the IP address and transmit protocol (TCP or UDP) of the server.

![1690880152874-b7fe162c-a18f-4653-ac23-dee4304458c7.png](./img/Gs3dvISjhRc0qruU/1690880152874-b7fe162c-a18f-4653-ac23-dee4304458c7-798173.png)

1. Check that the gateway-connected PC and the server exchange data through DTU.

![1690880153265-94ba34e3-1e13-4328-8dbb-b72beea3a570.png](./img/Gs3dvISjhRc0qruU/1690880153265-94ba34e3-1e13-4328-8dbb-b72beea3a570-717922.png)

### IO Ports

IO ports provide six analog inputs, six digital inputs, and four digital outputs. The analog and digital inputs share the ports. The digital parameters correspond to two states: HIGH (1) and LOW (0).

Dry Connect: determines the I/O interface status based on whether the input is on or off.

Wet Connect: determines the I/O interface status based on the input voltage.

| **No.** | **Function** | |
| :---: | --- | --- |
| **1** | **DI** | + When the digital input mode is wet contact, the voltage of +2.7 V to +36 V maps to state 1.<br/>+ When the digital input mode is wet contact, the voltage of +0 V to +1 V maps to state 0. |
| **2** | **AI** | + The analog input status is determined based on the current or voltage obtained from the analog input interface. Voltage range: +0.5 V ~ +36 V<br/>+ Analog input current detection is not support |
| **3** | **DO** | + Default：Low state，not pull-up<br/>+ Set Low pull-up or not pull-up, no voltage<br/>+ Set Hight state and pull-up, output power supply voltage<br/>+ Set Hight state and not pull-up, high resistance state |

![1690880153633-2867552a-6b0a-4537-b0d0-4879ed0d8e13.png](./img/Gs3dvISjhRc0qruU/1690880153633-2867552a-6b0a-4537-b0d0-4879ed0d8e13-071313.png)

DO: the power supply voltage limit is the maximum voltage; the maximum input voltage is DC 36V; Typical input current can reach 300mA.

DO: When do is used as open drain output, the typical perfusion current can reach 300mA.

When do pull-up is used as output, it can output high-level signal. The open circuit test voltage is the same as the power supply voltage. The pull-up resistance is 20K Ω and has no load capacity.

## System Management

### System

### System Status

Click "Administration >> System >> Status" and view the current system and network status of the device.

![1742460344752-6b3934c7-c622-42a7-aa5d-acce943cc967.png](./img/Gs3dvISjhRc0qruU/1742460344752-6b3934c7-c622-42a7-aa5d-acce943cc967-996374.png)

### Basic Setup

Click "Basic Setup" and modify the system language and device name.

![1742460361133-a4dfb974-b2e5-4c9a-90ef-1f58b5272acf.png](./img/Gs3dvISjhRc0qruU/1742460361133-a4dfb974-b2e5-4c9a-90ef-1f58b5272acf-725183.png)

### Advanced Stetup

1. **Shortcut Forward Engine**

After enabling the fast forwarding engine function, it will significantly improve the upload and download speed of 5G cellular networks. However, please note that network address translation (NAT) penetration, quality of service (QoS), and client traffic statistics will not be available under this setting.

1. **ITxPT**

After enabling DI1 (Industrial>> IO >>Digital Input 1 ) is used for low battery state detection. After turning on ITxPT, if DI1 is not connected to low battery detection, the device will enter**sleep state**.

1. **FlexAPI Interface Compatible**

Starting from version V1.2.1.r30062.bin, FlexAPI field updates have been implemented. The "FlexAPI Interface Compatible" option is enabled by default to maintain compatibility with previous versions. If you uncheck this option and save changes, a system reboot will be required to take effect. This action will also clear the cache and third-party platform database stored locally on the gateway. **Important Notes:**

    1. This operation is irreversible. Once new API fields are applied, you cannot roll back to previous configurations in Web config page. Enter CLI configuration mode use command：

```plain
VG814(config)#advanced-option flexapi compatible
VG814(config)#write
VG814(config)#reboot
```

![1742464101243-d0c6e83d-e750-4e56-afa9-74a1e3f5c23c.png](./img/Gs3dvISjhRc0qruU/1742464101243-d0c6e83d-e750-4e56-afa9-74a1e3f5c23c-855839.png)

    2. For the latest FlexAPI field specifications, refer to the **FlexAPI User Manual** available on official website.

![1742460280835-2012c999-f9db-4c63-aa1b-72343807dc8a.png](./img/Gs3dvISjhRc0qruU/1742460280835-2012c999-f9db-4c63-aa1b-72343807dc8a-013201.png)

### System Time

To ensure the coordination between the device and other devices, set the system time accurately.

**Manual time synchronization:**Click "Administration >> System Time >> System Time >> Sync Time" to ensure consistency between the gateway time and host time.

![1690880154497-bf4143d9-8d43-4fc2-95fd-fc276364812e.png](./img/Gs3dvISjhRc0qruU/1690880154497-bf4143d9-8d43-4fc2-95fd-fc276364812e-699552.png)

Alternatively, click "Administration >> System >> Status" to synchronize the time.

![1690880154782-c112a5a1-180a-4efd-a8f2-a1de90501016.png](./img/Gs3dvISjhRc0qruU/1690880154782-c112a5a1-180a-4efd-a8f2-a1de90501016-685800.png)

**Automatic time synchronization:** Click "Administration >> System Time >> SNTP Client or NTP Server" and check "Enable" to synchronize the time between the gateway and the SNTP or NTP server.

After NTP is enabled, the gateway can synchronize time for all devices on the network.

![1690880155038-9645bc78-8644-4f37-976d-f0315284988f.png](./img/Gs3dvISjhRc0qruU/1690880155038-9645bc78-8644-4f37-976d-f0315284988f-531576.png)

### Management Services

When the gateway requires the HTTP, HTTPS, TELNET, and SSH functions, click "Administration >> Management Services", enable the services, and click Apply & Save.

![1690880155346-142f498a-db5a-4623-8540-fb97e8b13802.png](./img/Gs3dvISjhRc0qruU/1690880155346-142f498a-db5a-4623-8540-fb97e8b13802-733167.png)

![1690880155600-8e10154b-f1df-407a-9d35-68c80cfc4068.png](./img/Gs3dvISjhRc0qruU/1690880155600-8e10154b-f1df-407a-9d35-68c80cfc4068-875043.png)

### User Management

Click "Administration >> User Management" and create users, modify passwords, or delete users on the user management page.

**Superuser and common user:**

● Superuser: By default, only one superuser is automatically created by the system, with the user name of **adm** and the default password of **123456**. It has full access rights for the gateway.

● Common user: A common user is created by the superuser. It can view or modify gateway configurations.

| Note: You cannot delete the superuser (**adm**) or modify its user name, but can modify its password. |
| :--- |

### AAA

Authentication, authorization, and accounting (AAA) is a security management mechanism for access control in network security, which provides three security services: authentication, authorization, and accounting.

<u>It provides modular methods for the following services:</u>

● Authentication: Verify whether a user has the right for network access.

● Authorization: Authorize a user to use specific services.

● Accounting: Record network resource usage of a user.

You can use only one or two of the security services provided by AAA. For example, if a company only expects to authenticate employees when they access specific resources, the network administrator only needs to configure the authentication server. However, if the company expects to record the network usage of employees, the accounting server must be configured.

AAA usually works in the client/server structure, which is highly scalable and is convenient for centralized management of user information, as shown in the figure below.

![1690880156136-b4a1b778-a484-4c32-a4c9-ebeed35875ce.png](./img/Gs3dvISjhRc0qruU/1690880156136-b4a1b778-a484-4c32-a4c9-ebeed35875ce-231979.png)

| Note: **Radius**, **Tacacs+**, and **LDAP** indicate authentication and authorization servers. **Local** indicates the local user name and password of the gateway. |
| :--- |

**9.5.1 Radius**

The Remote Authentication Dial In User Service (Radius) is a distributed information exchange protocol based on the client/server structure. It protects the network from unauthorized access, and is usually used in various network environments that require high security and allow remote user access.

**Method for enabling the Radius server for the gateway:**

Click "Administration >> AAA >> Radius". In "Server List", enter the server address (domain name/IP address), port ID, and authentication key, click Add, and then click Apply & Save.

![1690880156629-f122e30b-3fc3-45f6-b094-37ff6016d001.png](./img/Gs3dvISjhRc0qruU/1690880156629-f122e30b-3fc3-45f6-b094-37ff6016d001-275569.png)

**9.5.2 Tacacs+**

The Terminal Access Controller Access Control System + (Tacacs+) protocol is similar to the Radius protocol. It uses the client/server mode for communication between the network access server (NAS) and the Tacacs+ server. However, Tacacs+ works based on TCP, and Radius works based on UDP.

The Tacacs+ protocol is mainly used for AAA of end users and Point-to-Point Protocol (PPP) and virtual private dial-up network (VPDN) access users. Its typical application is to authenticate, authorize, and perform accounting for an end user who needs to log in to the device for operations. As a Tacacs+ client, the device sends the user name and password to the Tacacs+ server for verification. After authentication and authorization, the user can log in to the device for operations.

**Method for enabling the Tacacs+ server for the gateway:**

Click "Administration >> AAA >> Tacacs+". In "Server List", enter the server address (domain name/IP address), port ID, and authentication key, click Add, and then click Apply & Save.

![1690880156935-bc1fb7e3-2748-4037-9bfc-a28305b0b870.png](./img/Gs3dvISjhRc0qruU/1690880156935-bc1fb7e3-2748-4037-9bfc-a28305b0b870-408035.png)

**9.5.3 LDAP**

The main advantage of the Lightweight Directory Access Protocol (LDAP) lies in its quick response to users' search operations. For example, massive user authentication operations may be performed concurrently. If a database is used, because the database is divided into various tables, to meet this simple authentication requirement, the database must be searched each time, along with synthesis and filtering. This results in low efficiency. LDAP is equivalent to one table, and requires only the user name and password, with some other parameters, which is quite simple. It can meet the authentication requirement regarding the efficiency and structure.

**Method for enabling the LDAP server for the gateway:**

Click "Administration >> AAA >> LDAP". In "Server List", enter any name for "Name", enter the server address (domain name/IP address) and port ID, and enter the base DN obtained from the server. Set the user name and password for accessing the server. Select "None", "SSL", or "StartTLS" for "Security". Click Add, and then click Apply & Save.

![1690880157321-1c8ca4eb-c5cb-4b76-a114-fe700863db92.png](./img/Gs3dvISjhRc0qruU/1690880157321-1c8ca4eb-c5cb-4b76-a114-fe700863db92-297132.png)

**9.5.4 AAA Authentication**

**AAA authentication methods:**

● No authentication (**none**): No validity check is performed. Generally, this method is not used.

● Local authentication (**local**): User information is configured on the NAS. Local authentication is fast, which can reduce the operational costs, but the information storage amount is limited by hardware.

● Remote authentication: User information is configured on the authentication server. Remote authentication is supported over Radius, Tacacs+, and LDAP.

**AAA authorization methods:**

● No authorization (**none**): No authorization is performed for users.

● Local authorization (**local**): Authorization is performed based on the properties configured by the NAS for the local account.

● Tacacs+ authorization: Users are authorized by the Tacacs+ server.

● Authorization after successful Radius authentication: Authorization is bound to authentication, and cannot be performed independently over Radius.

● LDAP authorization

**Method for enabling authentication and authorization for the gateway:**

Click "Administration >> AAA >> AAA Settings". 1, 2, and 3 are corresponding to Radius, Tacacs, ad LDAP respectively. Authentication entries 1, 2, and 3 must be corresponding to authorization entries 1, 2, and 3 respectively. When all of **radius**, **tacacs+**, and **local** are set, the priority sequence is as follows: 1 > 2 > 3.

![1690880157696-a92f634f-8980-4c39-906a-74aba3d4e4d4.png](./img/Gs3dvISjhRc0qruU/1690880157696-a92f634f-8980-4c39-906a-74aba3d4e4d4-236031.png)

### Configuration Management

**Method for importing configurations:** Click "Administration >> Config Management >> Config Management >> Browse", select a configuration file, and click Import to import the configuration file to the gateway.

**Method for backing up current running configurations to the PC (common)**: Click Backup running-config.

**Method for backing up the startup file to the PC:** Click Backup startup-config.

**Method for restoring default configurations:** Click Restore default configuration and then click OK**.**

![1690880157937-ed7a2a91-83d6-4afd-920f-38cd9fb49bdb.png](./img/Gs3dvISjhRc0qruU/1690880157937-ed7a2a91-83d6-4afd-920f-38cd9fb49bdb-386107.png)

### Device Manager of InHand Cloud

Click "Administration >>Device Manger>>Device Manger" config InHand Cloud service.

**9.7.1 Config DeviceManger**

Device ManagerWith a visualization user interface and simple operation steps, the Device Manager platform enables you to manage and monitor InHand’s hardware devices, such as routers and gateways with convenience. It can quickly integrate devices and manage them with just a few clicks. The cloud deployment delivers easy-to-use experience, allowing you to focus on your core business and empowering your growth.

Step1: Register a user Global site [<u>https://iot.inhandnetworks.com</u>](https://iot.inhandnetworks.com/user/login)

![1690880158244-08b62ab5-5b31-4b04-933a-d2f8a3f4e9ab.png](./img/Gs3dvISjhRc0qruU/1690880158244-08b62ab5-5b31-4b04-933a-d2f8a3f4e9ab-101185.png)

Step2:

- Config Service Type "Device Manager"
- Server Address "iot.inhandnetworks.com" If you have already privatized the deployed Device Manager Cloud, fill in the private deployment server IP or domain name. Server Typy select "Coustomer".
- Secure Channel, After checking, it will be transmitted with SSL encryption.
- Registered Account: Use step 1 registed account email address.
- Site name and Asset Number customer defined.
- Make sure the VG710 is connected to the Internet.

![1690880158558-4723bec9-3a9b-4974-ba32-86eb6d60ed69.png](./img/Gs3dvISjhRc0qruU/1690880158558-4723bec9-3a9b-4974-ba32-86eb6d60ed69-431315.png)

Step3:

- Login Device Manager cloud.
- Check Gateways, VG710 will auto login server.
- For more usage reference manuals:

![1690880158842-34f79691-e44c-414b-bc9a-b317c8d69085.png](./img/Gs3dvISjhRc0qruU/1690880158842-34f79691-e44c-414b-bc9a-b317c8d69085-600898.png)

- For more usage reference manual.

![1690880159142-3d043020-329e-4001-95b3-deb3b266685c.png](./img/Gs3dvISjhRc0qruU/1690880159142-3d043020-329e-4001-95b3-deb3b266685c-703757.png)

**9.7.1 InConnect Service**

The InConnect is a simple “plug & play” service which builds secure remote networks for your machines (IPCs, servers, IP cameras, PLCs, HMIs, RTUs, controllers, etc.). Featuring user-friendly interfaces and simple operation, the SaaS (Software as a Service) based solution enables you to access your devices anytime from anywhere, and stay connected with your business and with the world – especially in these challenging times when normal working routines have been disrupted. Support VPN networking in the way of subnet to subnet.

Step1: Register a user Global site [<u>hthttps://ics.inhandnetworks.com</u>](https://ics.inhandnetworks.com/user/register)

Step2:

- Config Service Type "InConnect Service"
- Server Address "ics.inhandnetworks.com" If you have already privatized the deployed Device Manager Cloud, fill in the private deployment server IP or domain name. Server Typy select "Coustomer".
- Secure Channel , After checking, it will be transmitted with SSL encryption.
- Registered Account : Use step 1 registed account email address.
- Site name and Asset Number customer defined.
- Make sure the VG710 is connected to the Internet.

![1690880159476-d1e054a5-ebfc-4ba0-8272-9d227d3fec32.png](./img/Gs3dvISjhRc0qruU/1690880159476-d1e054a5-ebfc-4ba0-8272-9d227d3fec32-458945.png)

Step3:

- Login InConnect service.
- Check Gateways, VG710 will auto login server.
- Add VG710 SN to Server:

![1690880159996-d43bd240-baa7-43ee-8628-194cbdfe0bca.png](./img/Gs3dvISjhRc0qruU/1690880159996-d43bd240-baa7-43ee-8628-194cbdfe0bca-861556.png)

- For more usage reference manuals:

![1690880160503-a0373ae9-754d-4438-badf-3f44dffbc046.png](./img/Gs3dvISjhRc0qruU/1690880160503-a0373ae9-754d-4438-badf-3f44dffbc046-484203.png)

**9.7.1 Smart Fleet Service**

InHand Smart Fleet Cloud Platform, referred to as Smart Fleet, is a business platform that provides enterprise-level vehicle monitoring and management services for enterprise customers. Smart Fleet can help you manage vehicles intelligently and efficiently, break down vehicle data barriers, and realize multi-data joint analysis, vehicle Full life cycle management and control, intelligent vehicle operation and maintenance, help the informatization construction and digital transformation of engineering vehicles.

Smart Fleet can connect multiple vehicles to the same network. You can centrally monitor and manage vehicles, issue configurations, and upgrade firmware in a unified manner.

Smart Fleet helps users to quickly build an IoT network and master vehicle operation data in real time, allowing you to easily implement centralized monitoring and management of vehicles and gateways through the cloud platform. Effectively solve the problems of data isolation, collaboration bottlenecks, and lack of management.

Step1: Register a user Global site [<u>https://smartfleet.cloud</u>](https://smartfleet.cloud/user/login)

Step2:

- Config Service Type "InVehicle Service"
- Server Address "smartfleet.cloud" If you have already privatized the deployed Device Manager Cloud, fill in the private deployment server IP or domain name. Server Typy select "Coustomer".
- Secure Channel , After checking, it will be transmitted with SSL encryption.
- Registered Account : Use step 1 registed account email address
- License Plate Number is required.
- Asset Number Group ID is customer defined.
- Other interface information of the gateway can be reported to the platform in seconds.
- Make sure the VG710 is connected to the Internet.

![1690880160913-8f202e18-381f-4b2a-8d4e-affc25dd5e44.png](./img/Gs3dvISjhRc0qruU/1690880160913-8f202e18-381f-4b2a-8d4e-affc25dd5e44-755465.png)

Step3:

- Login InConnect service.
- Check Gateways, VG710 will auto login server.

![1690880161336-64c6ddfe-436b-4e70-93f5-776d7f11b4f6.png](./img/Gs3dvISjhRc0qruU/1690880161336-64c6ddfe-436b-4e70-93f5-776d7f11b4f6-965963.png)

### SNMP

**9.8.1 SNMP**

Currently, the SNMP Agent of VG710 supports SNMPv1, SNMPv2c, and SNMPv3.

● SNMPv1 and SNMPv2c use community names for authentication.

● SNMPv3 uses user names and passwords for authentication.

**Method for enabling SNMP for VG710:**

Click "Administration >> SNMP >> SNMP", check "Enable", select "v1c" for "v2c" for "SNMP Version", and click Apply & Save.

![1690880161733-2c0381b7-c8e4-4624-a8c4-ee1b1b0ecc04.png](./img/Gs3dvISjhRc0qruU/1690880161733-2c0381b7-c8e4-4624-a8c4-ee1b1b0ecc04-866439.png)

If v3c is selected, the corresponding user and user group need to be configured. Enter any name for "Groupname", select a security level, and click Add. Enter any name for "Username", select the new group name for "Groupname", set "Authentication" and "Authentication password", click Add, and then click Apply & Save.

![1690880162047-1e3972d5-d570-46e8-b500-b0aa82669245.png](./img/Gs3dvISjhRc0qruU/1690880162047-1e3972d5-d570-46e8-b500-b0aa82669245-383052.png)

**9.8.2 SnmpTrap (Alarm)**

The SNMP trap is a type of entrance. When this entrance is reached, the SNMP managed devices actively notify the NMS, instead of waiting for the polling of NMS. On an SNMP-enabled network, the agents on managed devices can report errors to the NMS anytime, without the need of waiting for the polling of NMS. The errors are reported to the NMS through traps.

**Method for enabling SnmpTrap for the gateway:**

Click "Administration >> NMP >> SnmpTrap". Enter the IP address of the NMS. Enter the corresponding group name when v1c or v2c is selected, or the corresponding user name when v3c is selected, ensuring that the name consists of 1–32 characters. By default, the UDP port ID ranges from 1 to 65535.

![1690880162283-0a8ccc8c-1b52-48ec-bd8e-01040d6ca79e.png](./img/Gs3dvISjhRc0qruU/1690880162283-0a8ccc8c-1b52-48ec-bd8e-01040d6ca79e-797114.png)

**9.8.3 SnmpMibs**

In SNMP messages, management variables are used to describe the managed objects on the device. To uniquely identify the managed objects on the device, SNMP uses a hierarchical naming scheme to identify the managed objects The entire hierarchical structure is like a tree. The nodes of the tree represent the managed objects, as shown in the figure below. Each node can be uniquely identified by a path starting from the root.

![1690880162715-aba0347b-c367-481a-910a-c83f9f9741e4.png](./img/Gs3dvISjhRc0qruU/1690880162715-aba0347b-c367-481a-910a-c83f9f9741e4-421197.png)

The management information base (MIB) is used to describe the hierarchical structure of the tree. It is a set of standard variable definitions for the monitored network device. In the above figure, managed object B can be uniquely determined based on a string of numbers {1.2.1.1}, which form the object identifier (OID) of the managed object.

**Method for downloading a SnmpMibs file to the PC via the gateway:**

Click "Administration >> SNMP >> SnmpMibs", select a folder, and click download to download it to the PC. Find the folder on the PC and import it to the NMS.

![1690880162972-01b79e3c-e291-4358-9b05-a86846f33a3e.png](./img/Gs3dvISjhRc0qruU/1690880162972-01b79e3c-e291-4358-9b05-a86846f33a3e-567017.png)

### Alarm

The alarm function enables users to identify gateway abnormalities in time. When an abnormality occurs, the gateway reports an alarm. You can select system-defined abnormalities and choose an appropriate notification way to obtain the abnormality information. All alarms are recorded in alarm logs so that users can identify abnormalities and perform troubleshooting in time.

**Alarm states:**

● **Raise**: indicates that the alarm has been generated but not been confirmed.

● **Confirm**: indicates that the alarm cannot be solved currently.

● **All**: indicates all generated alarms.

**Alarm levels:**

● **EMERG**: The device undergoes a serious error that causes a system reboot.

● **CRIT**: The device undergoes an unrecoverable error.

● **WARN**: The device undergoes an error that affects system functions.

● **NOTICE**: The device undergoes an error that affects system performance.

● **INFO**: A normal event occurs.

(1) **Status**: Click "Administration >> Alarm >> Status" and view all alarms generated in the system since power-on.

![1690880163282-9292a469-6089-41d8-8dd2-aa0888ec6301.png](./img/Gs3dvISjhRc0qruU/1690880163282-9292a469-6089-41d8-8dd2-aa0888ec6301-081884.png)

(2) **Alarm Input**: Select an alarm type as required. When this item is abnormal, an alarm is generated.

(3) **Alarm Output**: When an alarm is generated, the system automatically sends the alarm content to the destination email address via an email. This function is not available for common users. Set the sender mail address in "Email Alarm" and the receiver mail address in "Mail Address". "Mail Server IP/Name" can be found on the browser (for example, enter "smtp.exmail.qq.com" if you use a Tencent Enterprise mailbox.)

![1690880163612-5c00931b-93c4-49ea-9779-6f10a479ac32.png](./img/Gs3dvISjhRc0qruU/1690880163612-5c00931b-93c4-49ea-9779-6f10a479ac32-814734.png)

(4) **Alarm Map**: Alarms can be received in two ways: command line interface (CLI) (console interface) and Email. Some devices support SMS alarms. To enable email-based mapping, enable and set the email address on the "Alarm Output" page.

### System Logs

**Method for viewing system logs:**

Click "Administration >> System Log" to view system logs.

This page also provides the following operations: "Clear Log", "Download Log File", "Download Diagnose Data", "Clear History Log", and "Download History Log". History logs are those stored for extended time as specified on the "System Log" page.

The diagnose data file is encrypted, because the gateway configuration information is downloaded together with the diagnose data. You need to decrypt the file with the decryption tool provided by InHand.

![1690880163984-24db70d0-76b2-43ba-9a5a-9cd01b86f39f.png](./img/Gs3dvISjhRc0qruU/1690880163984-24db70d0-76b2-43ba-9a5a-9cd01b86f39f-147647.png)

The storage capacity of the gateway is limited (512 KB by default). To save all the logs, you need to use a remote log server (for example, [<u>Kiwi Syslog Daemon</u>](#_Kiwi_Syslog_Ademon)). Set the address and port of the log server on the web page. The gateway uploads all the system logs to the remote log server.

![1690880164274-3b9b5359-2321-4aa3-b69e-c8a0c1d3c8f3.png](./img/Gs3dvISjhRc0qruU/1690880164274-3b9b5359-2321-4aa3-b69e-c8a0c1d3c8f3-358057.png)

### System Upgrade

Click "Administration >> Upgrade >> Browse", select an upgrade file, and click Upgrade. Restart the system after the upgrade is completed.

![1690880164527-9e1ddf65-a83d-472b-904d-143a0966806e.png](./img/Gs3dvISjhRc0qruU/1690880164527-9e1ddf65-a83d-472b-904d-143a0966806e-853542.png)

| ![1690880164775-1e4ee242-1e7b-4fb3-8e7a-f102eda454c7.png](./img/Gs3dvISjhRc0qruU/1690880164775-1e4ee242-1e7b-4fb3-8e7a-f102eda454c7-257126.png)Note:<br/>During the software upgrade, do not perform any operation on the web page; otherwise, the software upgrade may be interrupted. |
| :--- |

**9.12 System Reboot**

Click "Administration >> Reboot >> OK to reboot the system.

![1690880165036-17a6eb4b-c7b1-4057-a7ca-2995a370a879.png](./img/Gs3dvISjhRc0qruU/1690880165036-17a6eb4b-c7b1-4057-a7ca-2995a370a879-388329.png)

## Diagnostic Tools

Diagnostic tools are used to detect the network connection of the gateway: **Ping**, **Traceroute**, **Tcpdump**, and **Link Speed Test**.

**Ping:** It is used to detect the external network connection of the device. Enter any common website in China for "Host" and click "Ping". If data transmission occurs, the network is connected properly.

![1690880165445-7e347f10-3fe2-4c8d-8816-1ca4303bffda.png](./img/Gs3dvISjhRc0qruU/1690880165445-7e347f10-3fe2-4c8d-8816-1ca4303bffda-020114.png)

**Traceroute:** Enter the IP address of the peer host and click "Trace" to detect the route connection.

![1690880165748-457edcdc-8250-41fb-95d5-de9134a40914.png](./img/Gs3dvISjhRc0qruU/1690880165748-457edcdc-8250-41fb-95d5-de9134a40914-762295.png)

**Tcpdump:**

Select an interface ("any" or "bridge1"), set "Capture Number", and click Start Capture >> Stop Capture >> Download Capture File.

![1690880166071-a0e7d50a-650d-4306-a109-e23567df2dbb.png](./img/Gs3dvISjhRc0qruU/1690880166071-a0e7d50a-650d-4306-a109-e23567df2dbb-975748.png)

Download wireshark from the browser to open the downloaded file and analyze the messages to understand the network connection of the interface.

![1690880166434-b06e5e35-9bb3-4825-88df-670a64391396.png](./img/Gs3dvISjhRc0qruU/1690880166434-b06e5e35-9bb3-4825-88df-670a64391396-160714.png)

**Link Speed Test:** Upload and download files to test the link speed.

![1690880166692-451815fe-3a2a-4084-a406-f7741baa8d6c.png](./img/Gs3dvISjhRc0qruU/1690880166692-451815fe-3a2a-4084-a406-f7741baa8d6c-649148.png)

## Chapter II Edge calculation

Powerful edge computing capabilities facilitate the development of custom applications. The remote fleet management platform is easy for secondary development by third-party software developers. With an open cloud ecosystem that supports Microsoft Azure and AWS, the VG710 offers more options for application developers. It supports Node-RED dokcer image low code edge computing solutions.

![1690880167104-2003302e-abb0-4745-8cfe-d3b37270eb52.png](./img/Gs3dvISjhRc0qruU/1690880167104-2003302e-abb0-4745-8cfe-d3b37270eb52-686717.png)

More Document ：

[https://github.com/inhandnet/InVehicle-Docs/tree/main/PDF](https://github.com/inhandnet/InVehicle-Docs/tree/main/PDF)

## Chapter III Accessories

| **VG710  4G Verison Accessories** | | | | |
| --- | --- | --- | --- | --- |
| **Product Name** | **MLFB** | **Specifications** | | **Product Pictures/** |
| VG710 Power Cable | **SCAB000216** | This cable has  A and B ends: A end has 4 pins, is to connect to VG710; B end is bare wire ends.    Suitable for field engineering projects. To perform indoor testing, a power adapter needs to be prepared separately.  Cable length 3000mm. | Required | ![1769766035691-07e6e4ae-c543-478f-8430-75abf9728c6f.png](./img/Gs3dvISjhRc0qruU/1769766035691-07e6e4ae-c543-478f-8430-75abf9728c6f-330079.png) |
| 5G/4G  Antenna | **AANT110016** | Antenna - 5G 3M adhesive-backed antenna, cable length 2000±20mm, SMA connector | Optional | ![1769766044169-1b1e0dd6-7960-4a68-969e-86226960a749.png](./img/Gs3dvISjhRc0qruU/1769766044169-1b1e0dd6-7960-4a68-969e-86226960a749-119862.png) |
| GNSS Antenna | **AANT040006** | GPS/GALILEO: 1575.42±1.023 MHz     GLONASS: 1602±8 MHz       Dimensions: 55.6x50.5mm , cable length 2000mm | Optional | ![1769766058656-8ea8de86-463f-4f55-bb50-5cca72f93cc1.png](./img/Gs3dvISjhRc0qruU/1769766058656-8ea8de86-463f-4f55-bb50-5cca72f93cc1-891730.png) |
| Wi-Fi Antenna | **AANT060018** | 2400~2500MHz/4900~5850MHz, cable length 2000mm | Optional | ![1769766045878-1e09b95c-cff5-4016-9ded-29bc55c1f759.png](./img/Gs3dvISjhRc0qruU/1769766045878-1e09b95c-cff5-4016-9ded-29bc55c1f759-904261.png) |
| VG710-4G 20 PIN Extension Cable | **SCAB000219** | This cable has  A and B ends: A end has 20 pins, is to connect to VG710; B end is bare wire ends.    Suitable for field engineering projects and testing.  Cable length 500mm. | Optional | ![1769766070052-97147b2b-19ea-49d1-8cfc-c1eb09b0d38e.png](./img/Gs3dvISjhRc0qruU/1769766070052-97147b2b-19ea-49d1-8cfc-c1eb09b0d38e-290306.png) |
| VG710 OBD-II Cable | **SCAB000215** | This cable has  A, B, C and D ends: A end has 20 pins, female; B end is OBD female, C end replicates A end but is male, D end is OBD male.    Suitable for field engineering projects and testing. Cable length 5000mm. | Optional | ![1769766076834-6b56efab-be00-420f-9ab8-9cd3db15f7c8.png](./img/Gs3dvISjhRc0qruU/1769766076834-6b56efab-be00-420f-9ab8-9cd3db15f7c8-064768.png) |
| VG710 J1939 9PIN Cable | **SCAB000235** |  P1 is 20PIN; P3 is OBD-II male; P4 is I/O open end, suitable for engineering projects; P5 is ignition signal cable, please connect to the ignition signal of the vehicle before use. | Optional | ![1769766086881-7d3c12df-9005-4ffb-b8a9-60a2fab9da01.png](./img/Gs3dvISjhRc0qruU/1769766086881-7d3c12df-9005-4ffb-b8a9-60a2fab9da01-045196.png) |
| VG710-4G  J1939 9PIN All-in-one Cable | **SCAB000234** |  P1 is 20PIN; P3 is J1939 9PIN female; P4 is I/O open end, suitable for engineering projects; P5 is ignition signal cable, please connect to the ignition signal of the vehicle before use. | Optional | ![1769766096059-d3ec636c-69ad-468b-a1d0-49dbe3495982.png](./img/Gs3dvISjhRc0qruU/1769766096059-d3ec636c-69ad-468b-a1d0-49dbe3495982-744926.png) |
| VG710 J1939 6PIN Cable | **SCAB000233** |  P1 is 20PIN; P3 is J1939 6PIN female; P4 is I/O open ed, suitable for engineering projects; P5 is ignition signal cable, please connect to the ignition signal of the vehicle before use. | Optional | ![1769766104753-532a66aa-3910-48ac-850e-de0ad4555c64.png](./img/Gs3dvISjhRc0qruU/1769766104753-532a66aa-3910-48ac-850e-de0ad4555c64-067997.png) |
| VG710-4G M12 5PIN to OBD CAN Cable | **SCAB000394** | M12 5PIN to 20PIN CAN-H/L  design of grounding screw hole with shielding layer | Optional | ![1769766112113-901c3098-71fe-4e1a-97f3-353e65118957.png](./img/Gs3dvISjhRc0qruU/1769766112113-901c3098-71fe-4e1a-97f3-353e65118957-239139.png) |

| **VG710-H  5G Verison Accessories** | | | | |
| --- | --- | --- | --- | --- |
| **Product Name** | **MLFB** | **Specifications** | | **Product Pictures** |
| VG710 Power Cable | **SCAB000216** | This cable has  A and B ends: A end has 4 pins, is to connect to VG710; B end is bare wire ends.    Suitable for field engineering projects. To perform indoor testing, a power adapter needs to be prepared separately. Cable length 3000mm. | Required | ![1769766035691-07e6e4ae-c543-478f-8430-75abf9728c6f.png](./img/Gs3dvISjhRc0qruU/1769766035691-07e6e4ae-c543-478f-8430-75abf9728c6f-330079.png) |
| 5G  Antenna | **AANT110016** | Antenna - 5G 3M adhesive-backed antenna, cable length 2000±20mm, SMA connector | Optional | ![1769766044169-1b1e0dd6-7960-4a68-969e-86226960a749.png](./img/Gs3dvISjhRc0qruU/1769766044169-1b1e0dd6-7960-4a68-969e-86226960a749-119862.png) |
| Wi-Fi Antenna | **AANT060018** | 2400~2500MHz/4900~5850MHz. Cable length 2000mm. | Optional | ![1769766045878-1e09b95c-cff5-4016-9ded-29bc55c1f759.png](./img/Gs3dvISjhRc0qruU/1769766045878-1e09b95c-cff5-4016-9ded-29bc55c1f759-904261.png) |
| Bluetooth Antenna | **AANT060017** | 2.4GHz, peak gain 3dBI | Optional | ![1769766254668-bcc909ff-21da-4a3e-89eb-20b37cfca539.png](./img/Gs3dvISjhRc0qruU/1769766254668-bcc909ff-21da-4a3e-89eb-20b37cfca539-299695.png) |
| VG710-H 20 PIN IO  All-in-one Cable | **SCAB000390** | VG710-5G with 3.5mm earphone microphone 20PIN. Cable length 1000mm | Optional | ![1769766276099-c1b25c45-1c66-44b0-9808-cad1da28abd9.png](./img/Gs3dvISjhRc0qruU/1769766276099-c1b25c45-1c66-44b0-9808-cad1da28abd9-047384.png) |
| VG710-H 10PIN  EXT All-in-one Extension Cable | **SCAB000400** | VG710-H 2CAN、LINE、J1708 Interface Cable length 1000mm | Optional | ![1769766282079-8639fe20-e76f-417e-850d-0c4286a8755a.png](./img/Gs3dvISjhRc0qruU/1769766282079-8639fe20-e76f-417e-850d-0c4286a8755a-528549.png) |
| Cable-OBD 16PIN Extension Cable | **SCAB000399** | ODB Cable 16PIN 1500mm | Optional | ![1769766287789-163c7b60-33ec-4401-9e10-f105663070fd.png](./img/Gs3dvISjhRc0qruU/1769766287789-163c7b60-33ec-4401-9e10-f105663070fd-278795.png) |

| **VG710-M Version Accessories** | | | | |
| --- | --- | --- | --- | --- |
| **Product Name** | **MLFB** | **Specifications** | | **Product Pictures** |
| VG710-M12 Version Power Cable | **SCAB000564** | VG710-M12 Version Power Cable, 8PIN, Cable length 2000mm | Required | ![1769766545676-694c7b49-ca66-4db5-a29f-28e74be30f58.png](./img/Gs3dvISjhRc0qruU/1769766545676-694c7b49-ca66-4db5-a29f-28e74be30f58-011354.png) |
| 4G FAKRA Antenna | **AANT090038** | 4G Antenna FAKRA Purple connector,Cable length 2000mm | Optional | ![1769766551078-e2c5e3eb-17b3-402c-9350-769ecdb602fc.png](./img/Gs3dvISjhRc0qruU/1769766551078-e2c5e3eb-17b3-402c-9350-769ecdb602fc-354489.png) |
| 5G FAKRA Antenna | **AANT110017** | 5G Antenna FAKRA Purple connector,Cable length 2000mm | Optional | ![1769766556929-d5dea37d-aa8d-42da-9eda-8144718245c1.png](./img/Gs3dvISjhRc0qruU/1769766556929-d5dea37d-aa8d-42da-9eda-8144718245c1-288774.png) |
| Wi-Fi  FAKRA Antenna | **AANT060024** | Wi-Fi/BLE 2.4-2.5GHz 5-5.8GHz Antenna FAKRA Beige connector.Cable length 2000mm. | Optional | ![1769766580432-72439b19-7273-4a74-8e96-9a49e3ec0d8a.png](./img/Gs3dvISjhRc0qruU/1769766580432-72439b19-7273-4a74-8e96-9a49e3ec0d8a-008357.png) |
| GNSS FAKRA Antenna | **AANT040013** | GPS L1 1575.42MHZ & BD  1561.098MHz &GLONASS 1602MHz. Cable length 2000mm. | Optional | ![1769766595794-58463819-8120-4941-9d1a-a3387de08dd1.png](./img/Gs3dvISjhRc0qruU/1769766595794-58463819-8120-4941-9d1a-a3387de08dd1-721066.png) |
| Network Cable M12 X Male to RJ45 | **AETH050002** | Network Cable M12 X to RJ45 , Cable length 1000mm | Optional | ![1769766607762-91773103-cb05-4914-988c-42c410a1d4f6.png](./img/Gs3dvISjhRc0qruU/1769766607762-91773103-cb05-4914-988c-42c410a1d4f6-046151.png) |

| **Public Accessories** | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Product Name** | **MLFB** | **Specifications** | | | | | **Product Pictures** |
| Quick terminal -3in3out  | **ECON060255** | Rated voltage 600V, rated current 30A，40*18.6*14.5mm、 Flame retardant grade V0. | | | | Optional | ![1769766754339-4b9c7244-df9f-4d8d-9593-22144f27c6d5.png](./img/Gs3dvISjhRc0qruU/1769766754339-4b9c7244-df9f-4d8d-9593-22144f27c6d5-246875.png) |
| ODB 16PIN Test Cable | **SCAB000399** | OBD 16PIN interface test line,Cable standard UL2464,wire length 1500mm | | | | Optional | ![1769766772521-9168bba5-621b-4e00-8e58-819e036d888a.png](./img/Gs3dvISjhRc0qruU/1769766772521-9168bba5-621b-4e00-8e58-819e036d888a-652222.png) |
| J1939 6PIN Test Cable | **SCAB000409** | J1939 6PIN interface test line,Cable standard UL2464, wire length 1500mm | | | | Optional | ![1769766778464-ee8b7877-62a9-43b2-a075-e8268c069db9.png](./img/Gs3dvISjhRc0qruU/1769766778464-ee8b7877-62a9-43b2-a075-e8268c069db9-947940.png) |
| J1939 9PIN Test Cable | **SCAB000410** | J1939 9PIN interface test line,Cable standard UL2464, wire length 1500mm | | | | Optional | ![1769766784687-5145d3df-7076-4f52-88cc-e9f9055751d1.png](./img/Gs3dvISjhRc0qruU/1769766784687-5145d3df-7076-4f52-88cc-e9f9055751d1-800634.png) |
| DC 5.5*2.1mm Female Connector | **ECON000047** | Power connector - DC 5.5 * 2.1mm female head welding free | | | | Optional | ![1769766792542-eece3cad-4aac-4225-a627-caad3c234679.png](./img/Gs3dvISjhRc0qruU/1769766792542-eece3cad-4aac-4225-a627-caad3c234679-765806.png) |
| USB to 485 / 232 connector | **ASER010009** | USB to 485 / 232 connector | | | | Optional | ![1769766797888-1a9ca563-f27a-40f1-9306-984a7af148ab.png](./img/Gs3dvISjhRc0qruU/1769766797888-1a9ca563-f27a-40f1-9306-984a7af148ab-440534.png) |
| Switching power  | **APWR000122** | Switching power supply - 12V/2A - round connector - horizontal**(American standard)** - DC line length 1.5M - single magnetic ring | | | | Optional | ![1769766806376-effe1727-3855-4fab-9f8d-55ae8968cad5.png](./img/Gs3dvISjhRc0qruU/1769766806376-effe1727-3855-4fab-9f8d-55ae8968cad5-117397.png) |
| Power adapter 12V/2A | **APWR000121** | Switching power supply - 12V/2A - round connector - vertical **(European standard) -** DC line length 1.5M - single magnetic ring | | | | Optional | ![1769766807056-84edef41-753d-4f6a-ba1c-f9008f6fc61a.png](./img/Gs3dvISjhRc0qruU/1769766807056-84edef41-753d-4f6a-ba1c-f9008f6fc61a-860155.png) |
| Power adapter 12V/2A | **APWR000138** | Switching power supply - 12V/2A - round connector - vertical **(UK standard)** - DC line length 1.5M - single magnetic ring | | | | Optional | ![1769766815989-d6f2cc5b-ab3a-4079-9a8f-156732ae1d19.png](./img/Gs3dvISjhRc0qruU/1769766815989-d6f2cc5b-ab3a-4079-9a8f-156732ae1d19-492796.png) |
