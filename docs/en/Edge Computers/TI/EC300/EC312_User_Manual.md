**Edge Computer EC300 Series**

**User Manual**

**(****Applicable for IEOS V2.0.0 and above****)**

Version1.1, February 2024

[www.inhand](http://www.inhandnetworks.com.cn/)[.com](http://www.inhandnetworks.com.cn/)

![](https://media-hub.inhand.com/edge_computers/EC300_EN/0427804c8180c650.png)

The software described in this manual is provided according to the license agreement and can only be used according to the terms of the agreement.

**Copyright Notice**

© 2024 InHand Networks.All rights reserved.

**Trademarks**

The InHand logo is a registered trademark of InHand Networks.

All other trademarks or registered trademarks in this manual belong to their respective manufacturers.

**Disclaimer**  

InHand Networks reserves the right to change this manual, and the product is subject to subsequent changes without prior notice. We will not be responsible for any direct, indirect, intentional, or unintentional damages and hidden dangers caused by improper installation and use.

# **1 Introduction**

This user's manual is for the Arm architecture based edge computer EC300 and covers a complete set of instructions for all supported models. Before referring to these chapters, verify that the hardware specifications of your computer model support the features covered.

In order to facilitate user configuration, InHand has developed a set of IEOS system programs, providing a web interface, users can easily through the web network management and system management, The IEOS is based on debian 11, so it can use native Linux commands for network management and system administration.but it should be noted that when the IEOS function is enabled, IEOS will take over the network management and system management. At this time through the Linux native command for network management and system management may fail; IEOS is enabled by default, if users need to perform network management and system management based on Linux native command line, they need to close IEOS first.

# **2 Hardware Installation Instructions** 

In this chapter, we will cover the external interface instructions of ARM-architecture-based edge computer EC300.



## **2.1 Introduction**

The following sections describe the application of external connectors and pin assignment.

## **2.2 EC300 Panel**

### **2.2.1 Front Panel**



![](https://media-hub.inhand.com/edge_computers/EC300_EN/0e4e5dfe182d6ad7.png)



### **2.2.2 Left Panel**

![](https://media-hub.inhand.com/edge_computers/EC300_EN/2f675abde156b143.png)

### **2.2.3 Right Panel**

![](https://media-hub.inhand.com/edge_computers/EC300_EN/873bfebaaf6163a3.png)

## **2.3 EC300 External Interface**

### **2.3.1 Ethernet**

This is a dual RJ45 connector for Ethernet connection.

The EC300 has 2 RJ45 Ethernet ports and supports 10M/100M adaptive rates.

Yellow light: LINK indicator light: When the device is LINK UP, the light remains on; when the device is LINK DOWN, the light remains off.

Green light: ACT light, flashing when there is data passing through.

### **2.3.2 Serial Port**

EC300 supports up to four serial ports: two standard serial ports and two expandable serial ports.

COM1(standard): RS-232 / RS-485 (RX1 TX1 / A1 B1),you can only choose to access RS-232 or RS-485 at the same time, they can't work at the same time.

COM2(standard): RS-485 (A2 B2)

COM3(extensible): RS232 / RS485 (Extended interface PIN1  Extended interface PIN2)

COM4(extensible): RS232 / RS485 (Extended interface PIN5  Extended interface PIN6)

### **2.3.3 CAN**

The EC300 is equipped with three expandable CAN bus interfaces, offering support for CAN FD with a maximum data rate of up to 5 Mbps. It is fully compliant with the CAN 2.0 A/B standards.

CAN1: Extended interface PIN1  Extended interface PIN2

CAN2: Extend interface PIN5  Extend interface PIN6

CAN3: Expand interface PIN9  Expand interface PIN10

### **2.3.4 Digital Input Interface**  

| Parameter | Description                              | Min  | Type | Max  | Unit |
| --------- | ---------------------------------------- | ---- | ---- | ---- | ---- |
| Vds       | Drain source voltage                     |      |      | 48   | V    |
| VIN Low   | Maximal input voltage recongnized as LOW |      |      | 3    | V    |
| VIN High  | Minimal input voltage recognized as HIGH | 10   |      | 30   | V    |

| **Interface identification** | **Features**                | **Description** |
| ---------------------------- | --------------------------- | --------------- |
| GND                          | Power reference ground  |                 |
| DICOM                        | Input public side           |                 |
| DI0                          | Digital input port 0        |                 |
| DI1                          | Digital input port number 1 |                 |
| DI2                          | Digital input port number 2 |                 |
| DI3                          | Digital input port number 3 |                 |

**Tips:**

4 digital input DI,

Wet contact state  

"1":+10~+30V/-30 ~ -10VDC

"0": 0 ~ +3V/-3 ~ 0V

Isolate 3000VDC

Wiring diagram(only supports wet contact wiring)

![](https://media-hub.inhand.com/edge_computers/EC300_EN/5b6be6ade47b91bd.png)

### **2.3.5 Digital Output Interface**  

| **Interface identification** | **Features**               | **Description** |
| ---------------------------- | -------------------------- | --------------- |
| DO0                          | Digital output port 0      |                 |
| DO1                          | Digital output port port 1 |                 |
| DO2                          | Digital output port 2      |                 |
| DO3                          | Digital output port port 3 |                 |
| GND                          | Power Reference Ground     |                 |

**Tips:**

4 DO OD output, isolated 3000VDC

Wiring Diagram

![](https://media-hub.inhand.com/edge_computers/EC300_EN/1bb7dbf57d8bd5ae.png)

### 2.3.6 **Analog Input Interface** 

The EC300 supports up to two expandable AIN analog current signal input interfaces with an input range of 4-20mA. It uses the TI TLA2022 12-bit ADC, featuring a sampling rate of 1.6kHz, a resolution of 16.6μA, and an accuracy of 1%.

Wiring Diagram

![](https://media-hub.inhand.com/edge_computers/EC300_EN/81164ea3197fd225.png)

### 2.3.7 USB 

The EC300 provides a USB 2.0 Host port.

### **2.3.8 LED**

EC300 has 8 LED lights to indicate the power supply and system operation status respectively.

| **Signage** | **Name**                                | **Definition**                                               |
| ----------- | --------------------------------------- | ------------------------------------------------------------ |
| PWR         | Power indicator                         | Solid on after power on.                                     |
| STATUS      | System operating status indicator light | When the system starts normally, the STATUS flashes. If the system fails to start due to an exception in the system startup phase; Or when the factory recovery operation has not been completed, STATUS is solid off. |
| WARN        | Warning indicator light                 | When the system has a warning abnormality, the WARN light flashes. Warning abnormalities include: the factory reset has not been completed; and the dialing abnormality (the cellular function needs to be turned on). |
| NET         | Cellular connection status indicator    | Dial function is not enabled, solid off.  Dialing, flashing.  Dialing is successful, solid on. |
| User1       | User programmable indicator 1           | It is off by default and can be controlled by user programming |
| User2       | User programmable indicator 2           | It is off by default and can be controlled by user programming |
| User3       | User programmable indicator 3           | It is off by default and can be controlled by user programming |
| User4       | User programmable indicator 4           | It is off by default and can be controlled by user programming |

### **2.3.9 User Programmable Keys**

EC300 provides an API interface. Users can call the API interface to detect the status of programmable keys and then implement their own key logic.

### **2.3.10 DC Input**

The EC300 supports 9 to 48V DC input

### **2.3.11 SIM Card Slot**

The EC300 supports 2 SIM card slots, and the SIM card needs to be installed with power off by pressing the SIM card into the slot.

### **2.3.12 MicroSD Card Slot**

The EC300 has a slot for the MicroSD card, SD needs to be plugged in and out with power off status.



### **2.3.13 Restore the Factory Keys**

There is a reset button for the system to reset to factory settings. Please refer [to Restore Factory Settings](#6 The System Restores Factory Settings) for more information



### **2.3.14 Antenna Interface**

There are 5 antenna interfaces in EC300, and the number of antennas standard with different models is different. Screw the antenna into the corresponding antenna interface to complete the antenna installation.

| **Identification** | **Name**                                    |
| ------------------ | ------------------------------------------- |
| ANT1               | 4G LTE main antenna                         |
| ANT2               | 4G LTE diversity receive antenna            |
| GPS                | GPS antenna(Please use passive GPS antenna) |
| Wi-Fi              | Wi-Fi antenna                               |
| Lora               | LoRa antenna                                |

### **2.3.15 Extended Interface**

EC300 can support interface expansion. For detailed selection instructions, please refer to the product specification. The currently supported expansion combinations are as follows:



| Extension module | Feature                            |
| ---------------- | ---------------------------------- |
| NAAD             | 2x 4-20mA analog input+4x DI+4x DO |
| N44C             | 2x RS-485+1x CAN FD                |
| N4CC             | 1x RS-485+2x CAN FD                |
| N44D             | 2x RS-485+4x DI+4x DO              |
| —                | NONE                               |

The extension interface is defined as follows:

![](https://media-hub.inhand.com/edge_computers/EC300_EN/9eb224f93b59cb2e.png)

| **PIN** | **NAAD**   | **N44C**    | **N4CC**    | **N44D**    |
|---------|------------|-------------|--------------|----------|
| 1   | AIN1+  | A_485_A | A_485_A | A_485_A |
| 2   | -      | A_485_B | A_485_B | A_485_B |
| 3   | AIN1-  | -       | -       | -       |
| 4   | GND    | GND     | GND     | GND     |
| 5   | AIN2+  | B_485_A | CAN2_H  | B_485_A |
| 6   | -      | B_485_B | CAN2_L  | B_485_B |
| 7   | AIN2-  | -       | -       | -       |
| 8   | GND    | GND     | GND     | GND     |
| 9   | -      | CAN3_H  | CAN3_H  | -       |
| 10  | -      | CAN3_L  | CAN3_L  | -       |
| 11  | DO0    | -       | -       | DO0     |
| 12  | DO1    | -       | -       | DO1     |
| 13  | DO2    | -       | -       | DO2     |
| 14  | DO3    | -       | -       | DO3     |
| 15  | DI0    | -       | -       | DI0     |
| 16  | DI1    | -       | -       | DI1     |
| 17  | DI2    | -       | -       | DI2     |
| 18  | DI3    | -       | -       | DI3     |
| 19  | DI_COM | -       | -       | DI_COM  |
| 20  | GND    | -       | -       | GND     |

# **3 Getting Started** 

In this chapter, we will introduce the basic configuration of EC300.



## **3.1 Connect to the EC300**

You will need a computer that you can use to connect to the EC300 and log in to the command line interface. It can be connected by means of an Ethernet cable.

Factory default username and password:

**Username: edge**

**Password: security@edge**

EC300 devices are factory created root by default, but login is disabled. If you need to use the root user, change the system configuration manually and type sudo -s to switch to the root user. The user edge is in the sudo group, so you can use sudo under the edge user to execute system-level commands. See the sudo Mechanism section in Chapter 5 for additional details.

**Tips:**

When **command not found** appears, type sudo -s to switch to the root user or use the sudo command to operate.

**Note:**

For security reasons, we recommend that you disable the default user account and create your own account.



### **3.1.1 Connecting via the SSH Console**

The EC300 supports SSH connections over Ethernet. Connect to the EC300 using the following default IP address.

| Port  | Default IP    |
| ----- | ------------- |
| ETH 1 | 192.168.3.100 |
| ETH 2 | 192.168.4.100 |

**3.1.1.1 Linux Users**

Tips

These steps apply if you are connecting to EC300 on a Linux PC. Please do not apply these steps to the EC300 device itself. Before you run the ssh command, be sure to configure your PC's Ethernet port IP address to be within a specific range. ETH1:192.168.3.0/24, ETH2:192.168.4.0/24.

Use the ssh command to access the ETH1 port of the EC300 on a Linux PC.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/a9f5fae6ea664215.png)

Type **yes to** continue to complete the connection.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/9603416fdc01ee27.png)

When the terminal prompt edge@edge-computer:~$ appears and shell commands can be entered, the connection is successful.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/a7596390cb4a8e79.png)

##### **3.1.1.2 Windows Users**

**Tips:**

These steps apply if you are connecting the EC300 on a Windows PC. Please do not apply these steps to the EC300 device itself.

Please perform the following steps on your Windows PC:

Click the link http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html, download PuTTY (free) software, SSH command in Windows environment to establish a connection to the edge computer EC300. The following is an example of using SSH to connect:

![](https://media-hub.inhand.com/edge_computers/EC300_EN/f09a5df29b34c263.png)

## **3.2 User Account Management**

### **3.2.1 Switch to the Root User**

You can use the sudo -s command to switch to the root user. For security reasons, do not operate all commands as root.

**Tips**

Click on the link for more information on **sudo** commands.

[https://wiki.debian.org/sudo](https://wiki.debian.org/sudo /h)

**Note**

You may get a "permission denied" message when using some pipe or redirect behavior without root permissions. In this case, you must use 'sudo su -c' instead of '>','<','>>','<<','etc', etc. You need to include the full command in single quotes.

### **3.2.2 Creating and Deleting User Accounts**

You can use the **useradd** and **userdel** commands to create and delete a user's account. Be sure to use these commands in the home screen to set the relevant access rights for that account. Here is an example of how to create test1 in the sudo group (the default login environment for test1 users is bash and their home directory is /home/test1).

![](https://media-hub.inhand.com/edge_computers/EC300_EN/1e511eb1a2a1815a.png)

To change test1's password, use the passwd command, enter the new password and repeat to confirm the change.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/35cb2731738e9bff.png)

If you want to remove user test1, use the command userdel.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/e300bb6fb55c1a75.png)

### **3.2.3 Disable the Default User Account**

Note

You should first create a user account before disabling the default account

Use the passwd command to lock the default user account so that edge users cannot log in

![](https://media-hub.inhand.com/edge_computers/EC300_EN/1adfd032479ebaac.png)

Unlock the edge user

![](https://media-hub.inhand.com/edge_computers/EC300_EN/ba6bd1ebfd69fc02.png)

## **3.3 Network Administration and System Administration**

### **3.3.1 Web Management based on IEOS**

IEOS is a set of network management and system management program running on Linux system developed by InHand. IEOS provides web interface, users can access Ethernet port ip address, cellular dial-up, Wi-Fi Station, DHCP Client/Server, static routing, and network management through the web. Firewalls and other network configuration; System time, time zone, firmware upgrade and system restart can also be operated; In addition, IEOS also supports docking with InHand device management platform DeviceLive. Users can remotely monitor and manage EC300 devices through DeviceLive platform.

IEOS adopts the design scheme of status and configuration separation, which is divided into three functional sections: network management, system management and status. The network management menu and the system management menu can only be used for network and system related configuration, and the status information needs to be unified to the status page.

Important note: When using IEOS program to manage network configuration and system configuration, if you use Linux native commands at the same time, the two may affect each other, resulting in abnormal running state. It is recommended that the configuration supported by IEOS be managed through IEOS web, and the configuration not supported by IEOS, such as VPN, can be combined with native Linux commands to achieve the configuration goal.

#### **3.3.1.1 Login to the Web**

Considering that the user's program may need to use the standard HTTP/HTTPS port number 80/443, IEOS uses the port number 9100 as the HTTPS connection port, and does not support access through HTTP; When the user uses HTTP to access the web, it will automatically jump to HTTPS. This document uses eth2's default address of 192.168.4.100 as an example.

Login Address:https://192.168.4.100:9100

login account: adm

login password: 123456

Important note: When IEOS program is enabled, it will reserve some port numbers for internal communication. The reserved port number ranges from 9100 to 9200. After IEOS is enabled, the client's program should avoid using these port numbers, otherwise it may cause conflicts and malfunction.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/4c3b3d9c2d23d33c.png)

#### **3.3.1.2 Network Management**

##### **3.3.1.2.1 Configuring the Ethernet Interface**

Configure the eth1 interface with a static IP address

![](https://media-hub.inhand.com/edge_computers/EC300_EN/3b3bd4f16c8f4b27.png)

Configure the eth1 interface with a DHCP Client

![](https://media-hub.inhand.com/edge_computers/EC300_EN/b53bb2866ed82979.png)

Start the dhcp server function on the eth1 interface and assign an address to the downstream device connected to eth1.



![](https://media-hub.inhand.com/edge_computers/EC300_EN/c2530864013183bd.png)

DHCP Server configuration parameters description:

**Enable DHCP Server**: The switch of DHCP Server function

**Starting Address**: Starting base address of DHCP Server address pool, network segment + starting address = starting ip address of address pool. In the screenshot, the network segment of eth1 is 192.168.3.0/24, and the base address is 1, then the starting address of the address pool is 192.168.3.1/24.

**Max Address Number**: The maximum number of addresses in the address pool.

**Lease period**: The length of the lease period

##### **3.3.1.2.2 Configure Cellular Dialing**

![img](https://support.inhandnetworks.com/DocsDisplay?zgId=664301991&mode=inline&blockId=gg4lg9aa1d3f313394db88dcbd083631a7c2c)

Cellular network parameters Description:

**Enabled**: The switch of cellular function; Enabled by default.

**Profiles**: A set of dial parameters used to configure APN, username, password, and authentication methods when dialing a dedicated network card. If you are not a dedicated network card, you usually do not need to change the configuration here. You can add up to 10 records to the dial-up parameter set.

**Network Mode**: The network mode of the cell, you can choose 3G, 4G and other related network mode, such as LTE, WCDMA, etc. If it is not clear which network mode to choose, select automatic; The program will automatically select the most appropriate network mode. The default is automatic.

**Enable Default Route**: Enable the add default route function, when enabled, when the dial is successful, it will add a default route of the cellular port. The default route is enabled.

**Metric**: This is the metric for the default routing of the cellular port. When default routing is configured on the cellular, Wi-Fi, and Ethernet ports, the metric with the lowest value is used.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/f6ebe965f6ae7df3.png)

**Dual SIM** Enabled: Dual Sim enabled. In order to improve the reliability of the network, EC300 supports dual SIM and single dial. Two sim cards need to be inserted into the device. If the sim1 card fails to dial because of unpaid charges, it will automatically switch to the sim2 card for dialing. By default, it is off.

**Main SIM**: The main sim card, when dialing, the selected sim card will be preferred for dialing. When dialing fails to reach a certain number of times, when switching to another sim card for dialing, the default is to use sim1 for dialing.

**Max Number of Dials**: When the dual-SIM single-dial function is enabled, the current sim card will be dialed to another sim card for dialing when the number of dials reaches a specified number.

**APN Profile**: sim card selected dialing parameters set, the default value is automatic. Usually special network card usually need to configure the dial parameter set, and select the Index of the dial parameter set here.

**PIN Code**: The PIN code of the sim card.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/b004787f37e06e5f.png)

Wireless cellular networks are complex, sometimes there will be dial-up false connection, that is, the dial-up state is successful, but the target address can not be ping; When this happens, you can simply dial again and get back to normal. IEOS cellular dialing supports ICMP probing to detect spurious connections. It is recommended that customers with cellular connections enable ICMP probing so that false connections can be quickly recovered.

ICMP probe parameters:

**ICMP Detection Server Probes**: ICMP probe address; 2 probe addresses can be configured, as long as 1 address is successfully probed, it means that there is no fake connection in the cell. When neither address is configured, ICMP probe is off.



**Detection** Interval: How often should ICMP probes be performed**?**

**Detection Timeout**: The duration of ICMP probe timeout. If no probe response packet is received, the probe is considered to have failed.

**Detection Max Retries**: the maximum number of probes; When a probe fails to reach this value, a redial is triggered. Range [1,5]

**Detection Strict**: Whether strict detection is enabled. When strict detection is turned off, the detection program will detect whether the packet received by the cellular interface has changed in each detection cycle. If there is a change, it means that the cellular network is working, and ICMP packets will not be sent for detection, so as to save some traffic; If the probe is turned on, ICMP probe packets will be sent periodically regardless of whether the number of packets received by the cellular interface has changed. By default, it is off.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/17b54dd47fc2fbe1.png)

In Advanced configuration are some less commonly used Settings options.

**Debug Mode enabled**: Whether the debug function is enabled. After enabled, some dial-related debugging information will be added to the log, and it is disabled by default.

**Enable Infinitely Redial**: In some cases, dialing will be in an abnormal state, which can be restored by rebooting the system; By default infinite redialing is turned off, and the system will be restarted to try to recover after a certain number of dialing failures. Since dialing is enabled by default, some customers without sim card, dialing failure, the system will restart, in this case, you can open unlimited redialing; In this way, no matter how many times the dialing fails, the system will not restart.

Dial Interval; But if a dial fails, the amount of time to wait before making another dial.

**Signal Query Interval**: Signal query interval. When the signal is bad, you may have problems with false connections; At this time, redialing has a certain probability to solve the problem of false connection. The dialing program will check the signal strength at regular intervals; here, the signal detection period is configured.

##### **3.3.1.2.3 Configure the Wi-Fi  **


The EC series supports both Station and AP modes.

##### 3.3.1.2.3.1 Station Mode

![](https://media-hub.inhand.com/edge_computers/EC300_EN/bb48a73c80d600bf.png)

**Enable Wi-Fi**: Enable the switch; Off by default

**Client SSID**: The ssid you want to connect to, you can enter it manually; You can also use the scan button to get nearby SSIDs that you can connect to

**Enable Default Route**: Enable the function of adding default route. If enabled, when the wifi connection is successful, a default route of wlan port will be added. The default route is enabled.

**Metric**: This is the metric for the default route of the wifi port. When the default route is configured for the cellular, Wi-Fi, and Ethernet ports, the metric with the lowest value is applied.

**Auth Method**: Auth method, supports no auth, WPA-PSK, WPA2-PSK, WPA-PSK/WPA2-PSK Mixed

Encrypt Mode:CCMP, TKIP, TKIP and CCMP are supported

**WPA/WPA2 PSK Key**: Key information

##### 3.3.1.2.3.2 Access Point Mode 

#### **![](https://media-hub.inhand.com/edge_computers/EC300_EN/ecfb911de1d13cc6.png) **

**SSID Broadcast:
**

Controls whether the SSID is broadcasted. Enabled by default.

- **Enabled:** The SSID can be detected by nearby devices.
- **Disabled:** The SSID is hidden and must be manually entered to connect.

**Band:**

Select the Wi-Fi frequency band, such as:

- **2.4G:** Suitable for longer coverage range.
- **5.8G:** Suitable for high-speed data transmission.

**Radio Type:**

Wireless standard, such as:

- **802.11a/n/ac:** Supports 5G.
- **802.11b/g/n:** Supports 2.4G.

**Channel:**

Specifies the wireless channel used. Can be manually selected or set to default.

**SSID:**

Set the Wi-Fi network name (SSID).

**Auth Method:**

Select the Wi-Fi authentication method:

- **Open:** No authentication.
- **WPA-PSK**
- **WPA2-PSK**
- **WPA-PSK/WPA2-PSK Mixed**

**Encryption Mode:**

Wireless encryption mode, supporting:

- **AES**
- **TKIP**

**WEP Key (Wi-Fi Password):**

Set the Wi-Fi access password.

**Bandwidth:**

Select the bandwidth range, such as:

- **20MHz:** Suitable for complex environments with strong anti-interference capabilities.
- **40MHz / 80MHz:** Suitable for high-speed transmission in low-interference environments.

**Stations Limit:**

Set the maximum number of clients allowed to connect to the AP.

**IP Address:**

Local IP address in Wi-Fi AP mode (default: 192.168.100.100).

**Subnet Mask:**

Subnet configuration parameter, default: 255.255.255.0.

##### **3.3.1.2.4 Configuring Static Routes **

This is a static routing for Ethernet. When the default routing for Ethernet, cellular, and wifi is configured, the default route with the lowest metric value will take effect. You need to make sure that the Metric value of the default route is different.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/78e42215e6aedece.png)

Static route configuration parameters:

**Interface**: The outgoing interface of the static route

**Target**: The target network

**Netmask**: Target network mask

**Gateway**: Next hop address

**Metric**: The metric for the static route

##### **3.3.1.2.5 Configuring the Firewall**

![](https://media-hub.inhand.com/edge_computers/EC300_EN/d8c48dd315b91109.png)

Only the iptables command is currently supported for configuration.

##### **3.3.1.2.6 Configuring DNS**

![](https://media-hub.inhand.com/edge_computers/EC300_EN/269e09ca5dd471e5.png)

**DNS Servers**: DNS Server address, up to 4 can be configured

**Domain name hijacking:** Domain name hijacking function, can realize the binding between IP address and domain name.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/ed3bf79f571bb804.png)

##### **3.3.1.2.7 Network Diagnostics**

Network diagnostics support ping, traceroute and nslookup functions.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/be0d1798f5b03574.png)

#### 3.3.1.2.8 Configuring OpenVPN 

##### 3.3.1.2.8.1 Configuring OpenVPN Server 

The configuration of OpenVPN can be configured manually on the web page or by importing a configuration file. 

1. Manual Configuration 

![](https://media-hub.inhand.com/edge_computers/EC300_EN/270ebf133ceba191.png)

1. **Server Name** : The string that uniquely identifies the server-side configuration. It can contain only English letters and numbers, start with a letter, and can be no more than 64 characters in length. 
2. **Status** : On or off, used to control the start or stop of the OpenVPN Server. 
3. **Interface Type** : Currently, only tun mode is supported. 
4. **Network Type** : Support p2p , net30 and subnet . p2p and net30 used to establish a point-to-point connection, subnet used to establish a virtual local area network. 
5. **Virtual Network** : In subnet mode, you need to configure the network segment information of the virtual network; If it is p2p or net30 configuration, it is the local IP address and the remote IP address. 
6. **Network Mask** : In subnet mode, you need to configure the subnet mask of the virtual network. 
7. **CA Certificate** : The CA certificate file needs to be imported here.
8. **Public Key Certificate** : You need to import the server's public key certificate file here. 
9. **Private Key Certificate** : The private key certificate file of the import server is required here.
10. **DH parameter** : The DH parameter file of the import server is required here.

In the advanced settings, you can configure some parameters with low frequency of change. 

1. **Server Address** : the IP address that OpenVPN listens to. By default, it listens to 0.0.0.0, that is, it listens to all IP addresses. 
2. **Protocol Type** : Support udp and tcp , default udp . 
3. **Server Port** : The port number that the server listens to. Default 1194 . 
4. **Encryption Algorithm** : Configure the encryption algorithm used to ensure the confidentiality of data transmission. 
5. **Hash Algorithm** : Configure the hash algorithm used to guarantee the integrity of data transmission. 
6. **Key retention** : after key retention is enabled, even if OpenVPN is temporarily disconnected due to network exceptions, it can be quickly recovered without the need for a new handshake. 
7. **The tunnel remains** : When tunnel maintenance is enabled, it can prevent the tunnel from being closed due to short-term network fluctuations. 
8. **LZO compression** : Whether to enable LZO compression. 
9. **Maximum number of clients** : Configure the number of clients that connect to the OpenVPN Server at the same time. 
10. **User** : Specifies the user running the OpenVPN process.
11. **User Group** : specify the user group to run the OpenVPN process.
12. **Log Level** : Value range 1 to 11 , the larger the value, the more detailed the log information, ALL view the OpenVPN log in the type log.
13. **Connection Detection Interval** : the cycle of sending heartbeat packets to check whether the VPN connection is alive. 
14. **Connection detection timeout** : If no response is received within the timeout period, determine that the connection is disconnected and try to restart.
15. **Allow client-to-client communication** : Whether to allow the client and the client to communicate with each other.
16. **Push to client** : can push information such as routing and DNS to the client. 


2. mport Configuration



![](https://media-hub.inhand.com/edge_computers/EC300_EN/f947ab70a92666c5.png)

1. **Server Name** : The string that uniquely identifies the server configuration. It can contain only English letters and numbers and start with a letter. The string must be no more than 64 characters in length. 
2. **Status** : On or off, used to control the start or stop of the OpenVPN Server. 
3. **Interface Type** : Currently, only tun mode is supported. 
4. **Profile** : import the OpenVPN Server configuration file, which must contain information such as the CA certificate, Server certificate, and Server key. 

##### 3.3.1.2.8.2 Configuring the OpenVPN Client 

1. Manual Configuration



![](https://media-hub.inhand.com/edge_computers/EC300_EN/1f6b0855b3a0cf1d.png)

1. **Client Name** : A string that uniquely identifies the server configuration. It can contain only English letters and numbers, start with a letter, and can be no more than 64 characters in length. 
2. **Status** : On or off, used to control the start or stop of the OpenVPN Server. 
3. **Interface Type** : Currently, only tun mode is supported. 
4. **Network Type** : Support p2p , net30 and subnet . p2p and net30 used to establish a point-to-point connection, subnet used to establish a virtual local area network. When the network type is p2p or net30 you need to configure the local IP address and remote IP address. 
5. **OpenVPN Server** : configure the ip address, port number, and protocol information of the OpenVPN Server in the format of ip port proto, for example: 192.168.3.200 1194 udp you can configure up to 10 server addresses. The OpenVPN client attempts to establish a connection one at a time in order until the OpenVPN tunnel is successfully established. 
6. **Log Level** : Value range 1 to 11 , the larger the value, the more detailed the log information, ALL view the OpenVPN log in the type log. 
7. **CA Certificate** : The CA certificate file needs to be imported here.
8. **Public Key Certificate** : The public key certificate file of the client needs to be imported here. 
9. **Private Key Certificate** : The private key certificate file of the client needs to be imported here. 

In the advanced settings, you can configure some parameters with low frequency of change. 

1. **Encryption Algorithm** : Configure the encryption algorithm used to ensure the confidentiality of data transmission. 
2. **Hash Algorithm** : Configure the hash algorithm used to guarantee the integrity of data transmission. 
3. **Key retention** : After key retention is enabled, even if OpenVPN is temporarily disconnected due to network exceptions, it can be quickly recovered without the need for a new handshake. 
4. **The tunnel remains** : When tunnel maintenance is enabled, it can prevent the tunnel from being closed due to short-term network fluctuations. 
5. **LZO compression** : Whether to enable LZO compression. 
6. **User** : Specifies the user running the OpenVPN process.
7. **User Group** : Specify the user group to run the OpenVPN process.
8. **Connection Detection Interval** : The cycle of sending heartbeat packets to check whether the VPN connection is alive. 
9. **Connection detection timeout** : If no response is received within the timeout period, determine that the connection is disconnected and try to restart.


2. Manual Configuration



![](https://media-hub.inhand.com/edge_computers/EC300_EN/db340c18b2d0c25a.png)

1. **Client Name** : The string that uniquely identifies the client configuration. It can contain only English letters and numbers and start with a letter. The string must be no more than 64 characters in length. 
2. **Status** : Turns on or off to control the start or stop of the OpenVPN client. 
3. **Interface Type** : Currently, only tun mode is supported. 
4. **Profile** : Import the OpenVPN Client configuration file. The configuration file must contain information such as the CA certificate, Client certificate, and Client key. 

#### 3.3.1.3 System Administration 

##### 3.3.1.3.1 Basic Configuration

Cloud management

![](https://media-hub.inhand.com/edge_computers/EC300_EN/54a3a2a0ea546243.png)

**Enabled**: the enable switch that connects to the DeviceLive platform; DeviceLive is the remote monitoring and management platform of Inhantong equipment;

**Cloud Server**: DeviceLive platform has 2 addresses; One is the address of the domestic platform, the other is the address of the overseas platform; Here you choose which platform to connect to.

Time zone and NTP client

![](https://media-hub.inhand.com/edge_computers/EC300_EN/5b51ab39fd1e81ce.png)

A maximum of 10 NTP Server addresses can be configured, and the program periodically sends synchronization requests to each server address in turn. After the synchronization is successful, the system time is written to the RTC and no longer continues to send synchronization requests to the later NTP servers.

In addition to using NTP to synchronize the time, there is a synchronization button in the Device Info status page to synchronize the time manually, but only when the device time and the local time (the time of accessing the computer used by the device) differ by more than 3s, this synchronization button will be displayed.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/c41eae7cd4d0e7b7.png)

Configuration import, export and factory restore are supported here.

##### **3.3.1.3.2 Firmware Upgrade**

##### ![](https://media-hub.inhand.com/edge_computers/EC300_EN/aaf74eceb2db940b.png)

The automatic restart option is turned off by default. After upgrading the firmware, you need to manually restart the system to take effect; When the automatic restart option is enabled, the system will be restarted automatically after the firmware upgrade is successful.

##### **3.3.1.3.3 Others**

![](https://media-hub.inhand.com/edge_computers/EC300_EN/01d4931755c6ba40.png)

This page has 2 functions: restart the system and reset the system. Resetting the system needs to be used carefully. The resetting system function will restore the system configuration status and file system status to the factory, which means that the software installed by the user will also be cleared.

#### **3.3.1.4 Status**

##### **3.3.1.4.1 Device Information**

The device information status page shows hostname, device model, serial number, firmware version, kernel version, filesystem version, and an overview of CPU, memory, and disk space usage.

##### ![](https://media-hub.inhand.com/edge_computers/EC300_EN/26329171e9d4a056.png)**3.3.1.4.2 Cellular Status Information**

The cellular status page shows IMEI, IMSI, ICCID, signal strength of the current SIM, as well as the IP address, DNS and other information obtained through dialing.



![](https://media-hub.inhand.com/edge_computers/EC300_EN/d599d3362fdbcaf4.png)

##### **3.3.1.4.3 Wi-Fi Status Information**

The Wi-Fi status page shows the IP address, gateway, and DNS information obtained after the Wi-Fi connection was successful.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/8b2836bb646d5a02.png)

##### **3.3.1.4.4 DHCP Server Status Information**

The DHCP Server status page shows the assigned IP address of the device as a DHCP Server, the client hostname, the client host mac, and the expiration time.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/d35abf9321e35ebf.png)

##### **3.3.1.4.5 Routing Status Information**

The route status page displays IPv4 direct route, static route and route neighbor information.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/838d9f284bd9353b.png)

##### **3.3.1.4.6 Firewall Status Information**

Firewall status information shows filtering rules, IP address mapping rules and other information.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/d62a203699432c6f.png)

##### **3.3.1.4.7 Log Information**

The log page can view the system log, user log and set the log level, including Error, Info, Debug and other levels. Logs can also be downloaded locally.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/4905ac3f506a8c2b.png)

### **3.3.1.4.8 OpenVPN Status Information** 

### **3.3.1.4.8.1 OpenVPN Server Status Information** 

On the OpenVPN Server Status page, you can view information such as the status update time and the connected OpenVPN clients. 

![](https://media-hub.inhand.com/edge_computers/EC300_EN/02405f04c426d29f.png)

### 3.3.1.4.8.2 OpenVPN Client Status Information 

On the OpenVPN Client Status page, you can view information such as the virtual IP address obtained by the client and the tunnel connection duration.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/eb4bb2c71ecd6290.png)

### 3.3.2 Linux-based command-line management

When using the Linux command line for network and system configuration, the first thing you need to do is close the IEOS program. IEOS is managed through systemctl,

How to turn off IEOS is as follows:

systemctl stop ieos_daemon

This shutdown only applies to this startup, and IEOS programs will still start after the system is rebooted. Here's how to prevent IEOS programs from starting:

systemctl disable ieos_daemon

Important note: After IEOS is turned off, wireless networking functions such as dialing and Wi-Fi require native Linux commands, and there is no way to remotely manage devices on the DeviceLive platform.

#### **3.3.2.1 Network management**

##### **3.3.2.1.1 Set up a Static IP Address**

If you want to set static IP address for EC300, through the command **vim/etc/network/interfaces.d/eth1** or **vim/etc/network/interfaces.d/eth2** to modify the corresponding network configuration file to set the default gateway, address, Network and subnet mask of Ethernet interface. As an example, let's set a static IP address for the eth2 port:



![](https://media-hub.inhand.com/edge_computers/EC300_EN/6ffb75821b5cdc01.png)

After changing the interface IP configuration, run /etc/init.d/networking restart to restart the network service for the configuration to take effect.

##### **3.3.2.1.2 Set up a Dynamic IP Address**

If you want to set dynamic IP address for EC300, through the command

**vim/etc/network/interfaces.d/eth1** or **vim/etc/network/interfaces.d/eth2** to modify the corresponding network configuration file. Set it to DHCP after **inet** will automatically get the IP address.



Here is an example of setting a dynamic IP to the eth1 port.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/303cb2d4180ba535.png)

After changing the interface IP configuration, run **/etc/init.d/networking** restart to restart the network service for the configuration to take effect.

#### **3.3.2.3 System Administration**

##### **3.3.2.3.1 Querying the Firmware Version**

To check the computer firmware version for the EC300, type:

![](https://media-hub.inhand.com/edge_computers/EC300_EN/d341ae3f8a564a47.png)

##### **3.3.2.3.2 Check Available Disk Space**

To determine the amount of available drive space, use the df command with the **-h** option. The system will return the amount of drive space broken down by file system. For EC300 products, the disk partition available to users is **/dev/mmcblk0p8**. Here's an example:

##### ![](https://media-hub.inhand.com/edge_computers/EC300_EN/118107440d9b9e14.png)

##### **3.3.2.3.3 Adjust the Time**

The EC300 has two time Settings. One is system time and the other is RTC (Real Time Clock) time, which is maintained by the EC300's hardware. Use the date command to query the current system time or to set a new system time. Use the **hwclock** command to query the current RTC time or set a new RTC time.

Set the system time with the command date **MMDDhhmmYYYY**:

MM: month

DD: day

hh: hour

mm: minutes

YYYY: Year

![](https://media-hub.inhand.com/edge_computers/EC300_EN/6ab384d98f999491.png)

RTC time can be set to system time using the following command

![](https://media-hub.inhand.com/edge_computers/EC300_EN/2466cc51828361d7.png)

Click on the link below for more details about the date and time:

https://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html

https://wiki.debian.org/DateTime

##### **3.3.2.3.4 Set Time Zone**

There are two ways to configure the time zone for the EC300. One is to use the command **tzselect**. The other is to use the **/etc/localtime** file.

##### **3.3.2.3.5 Use the Tzselect Command**

When you type the **tzselect** command, you will be taken to the area selection screen. Select the approximate area (divided by continent and ocean) and enter the number in front of the continent or ocean.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/1bbf4b04c439dd0c.png)

Then select the continent or the country under the ocean

![](https://media-hub.inhand.com/edge_computers/EC300_EN/f4161aa0c5820341.png)

Follow the steps above to get the China time zone keyword Asia/Shanghai and execute the following command to set the time zone.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/43410ef84664c25e.png)

##### **3.3.2.3.6 Using a Localtime File**

The localtime file is stored in **/etc/localtime** and is used by the GNU library for C (glibc) if no value is set for the TZ environment variable. This file is either a copy of **/usr/share/zoneinfo/file** or a symbolic link to it. If EC300 cannot find**/usr/share/zoneinfo/file**, please download from the website when you need the time zone information file (https://www.iana.org/time-zones), and links to the localtime file in the EC300.



**Note:**

After successfully downloading the required time zone information file, unzip it, and then compile and generate the corresponding binary file using zic command. The generated time zone file is "**/usr/share/zoneinfo/custom time zone filename**".

# **4 Advanced Configuration of the Peripheral Interface**

In this chapter, we will introduce the advanced configuration of peripheral interfaces for EC300, an edge computer based on Arm architecture.

This chapter covers the following topics:

## **4.1 Serial Ports**

EC300 has four serial ports, one serial port supports RS485, three serial ports support RS-232 or RS-485 mode.

The corresponding device node for COM1 is /dev/ttyS4

The device node for COM2 is /dev/ttyS5

The device node for COM3 is /dev/ttyS6

COM4 is represented by /dev/ttyS8

### **4.1.1 Change the Serial Port Settings**

Check and set the serial port with the **stty** command

To see the details, type **sudo stty --help**:

![](https://media-hub.inhand.com/edge_computers/EC300_EN/64e69c46084008ef.png)

![](https://media-hub.inhand.com/edge_computers/EC300_EN/d711a5ba352dbc6f.png)

![](https://media-hub.inhand.com/edge_computers/EC300_EN/e171774724ae4b68.png)

![](https://media-hub.inhand.com/edge_computers/EC300_EN/1b9ae03e5cfdb7a8.png)

![](https://media-hub.inhand.com/edge_computers/EC300_EN/1be3eb30a6f4b774.png)

### **4.1.2 Check the Serial Port Information**

![](https://media-hub.inhand.com/edge_computers/EC300_EN/14e8f9148852b2ff.png)

### **4.1.3 Set the Baud Rate of COM1 Serial Port**

![](https://media-hub.inhand.com/edge_computers/EC300_EN/9a48772b0eaf9287.png)

**Note**

Details about the stty command are available at the following link

http://www.gnu.org/software/coreutils/manual/coreutils.html

## **4.2 USB Interface**

The EC300 provides a USB 2.0 Host interface, which is mainly used to expand storage.

The EC300 supports USB storage device hotplugging.



**Note**

Remember to enter the sync sync command before disconnecting your USB mass storage device to prevent data loss. When you disconnect the storage device, exit from the mount directory.

## **4.3 MicroSD Card**

The partition of the SD card needs to be formatted as FAT32. The formatting method is as follows:

● SD card capacity <= 32GB: Insert the SD card into the card reader, and then insert the card reader into a computer using the Windows system. Most Windows systems only support SD cards with a capacity less than 32GB to be formatted as FAT32 system. A partition will be automatically created during formatting. You can also format it as FAT32 file system under Linux system. The method is the same as SD card capacity > 32GB.

● SD card capacity > 32GB: When the SD card capacity is greater than 32GB, you need to format it in FAT32 format under Linux. Insert the SD card into the card reader, and then insert the card reader into a computer using the Linux system or a computer with a Linux virtual machine installed.

a. Run **fdisk -l** to view the device node corresponding to the SD card, which is **/dev/sda** in the example

b. Run **fdisk/dev/sda** to partition (**p** to view the current partition, **d** to delete the existing partition, **n** to create a new partition, and **w** to save the changes) to create a partition

**/dev/sda1**

c. Run **sudo mkfs.vfat -F 32 /dev/sda1** to format the partition as FAT32.

d. After formatting, remove the SD card from the card reader and insert it into the device while the device is powered off

The EC300 doesn’t support hot swapping of micro SD memory card. Below is the link of mount reference: 

https://www.man7.org/linux/man-pages/man8/mount.8.html

## **4.4 CAN bus Interface**

The three-way CAN port of the EC300 supports the CAN bus.

### **4.4.1 Configure the connection CAN Interface**

By default, the CAN port will be initialized. If you need any other configuration, check the CAN device using the **ip link** command. To check the status of the CAN device, use the **ip link** command:

To configure a CAN device, use **ip link set can\* down** to first turn off the device

Where can* is selected from can1, can2, or can3.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/0ac9a23f0f765415.png)

Then configure the bit rate (here's a 50k bit rate example) :

![](https://media-hub.inhand.com/edge_computers/EC300_EN/ee0e5af222d3d451.png)

Finally turn the device back on

![](https://media-hub.inhand.com/edge_computers/EC300_EN/78873bc553e54edf.png)

## **4.5 IO Debugging**

The EC300 supports 4-way IO input and 4-way IO output.

| **Port number** | **Device description file**       |
| --------------- | --------------------------------- |
| **DI0**         | **/sys/class/gpio/gpio454/value** |
| **DI1**         | **/sys/class/gpio/gpio455/value** |
| **DI2**         | **/sys/class/gpio/gpio456/value** |
| **DI3**         | **/sys/class/gpio/gpio457/value** |
| **DO0**         | **/sys/class/gpio/gpio323/value** |
| **DO1**         | **/sys/class/gpio/gpio453/value** |
| **DO2**         | **/sys/class/gpio/gpio465/value** |
| **DO3**         | **/sys/class/gpio/gpio461/value** |

Reading the DI status can be done using cat **"Device profile"**;

![](https://media-hub.inhand.com/edge_computers/EC300_EN/de370a7bf5e8439b.png)

DO status can be controlled by using **echo 1 > "Device Profile" or echo 0 > "Device Profile"** as root user

![](https://media-hub.inhand.com/edge_computers/EC300_EN/47505c0ad9f292f3.png)

## 4.6 AIN Debugging 

Refer to Section 2.3.6 for wiring definitions and Section 2.3.15 for hardware interface definitions.

| Port number | Device description file |
| ----------- | ----------------------- |
| AIN1        | /dev/ain1               |
| AIN2        | /dev/ain2               |

To read the AIN current value, you can use **cat "device description file".**



![img](https://media-hub.inhand.com/edge_computers/EC300_EN/document_image_rId92.png)





The return value indicates the current channel current value in microamperes (uA).

## 4.7 SuperCapacitor

### 4.7.1 Specification

#### 4.7.1.1 Capacitor Specifications

The specifications of the supercapacitor are: 10.8V/5F.

#### 4.7.1.2 Power-Off Retention

The power-off holding module can maintain system operation for 20-30S after power failure depending on the load conditions.



### 4.7.2 Functions

#### 4.7.2.1 Power Failure Alarm 

The EC300 supports the power-down alarm function. When the external power supply is disconnected, the system will send a UDP broadcast message ‘power_down’ to port 9107 of IP address 255.255.255.255.

#### 4.7.2.2 Safe Shutdown

Power failure refers to the continuous disconnection of the external power supply for more than 0.5 seconds. After sending the UDP broadcast message, the system waits for 3 seconds and actively performs a power off.

# **5 Security** 

In this chapter, we will introduce the security mechanism of EC300, an edge computer based on ARM architecture.

## **5.1 Sudo Mechanism** 

In EC300, the root user is banned for better security. Sudo is a program that lets the system administrator allow an approved user to execute some commands as the root user or another user. The most basic rule is to give as few privileges as possible to get the job done. Using sudo is more secure than root session opening for a number of reasons, including:

• Grant privileges to normal users without having to know the root password (sudo will prompt for the current user's password)

• It's easy to run privileged commands via sudo, and the rest of the time, work as an unprivileged user, reducing potential damage due to wrong operations.

## **5.2 Firewalls**

Netfileter/iptables (hereafter referred to as iptables) is an excellent and completely free firewall tool based on packet filtering that comes with the Nuix/Linux system. It is very powerful and flexible to use. It can finely control the data packets flowing into, out of and through the server.

## **5.3 TPM2.0** 

TPM stands for "Trusted Platform Module" and it is a hardware security module designed to provide security and encryption capabilities for computer systems. It is a secure microcontroller that can be embedded in a computer system or sold as a standalone hardware device. It contains a cryptographic coprocessor for storing encryption keys, digital certificates, and other secure data, as well as supporting multiple cryptographic algorithms and security protocols. On EC300, the standard TPM2 protocol stack and TPM2 tools have been integrated for user use.

ARM computers provide TPM2.0 hardware support and are pre-installed with the tpm2-tools tool, which can be used to test and verify TPM2.0.

**Generate random numbers
**

**![](https://media-hub.inhand.com/edge_computers/EC300_EN/99e42861b69d9463.png)
**



NOTE 

For more information on how to use tpm2-tools, please refer to https://tpm2-tools.readthedocs.io/en/latest/


# **6 The System Restores Factory Settings** 

In this chapter, we will describe how EC300, an edge computer based on Arm architecture, restores factory Settings.

This chapter covers the following topics:

## **6.1 Restore Factory Settings** 

There are two ways to restore factory Settings:

1. By typing the command, the system will automatically restart and restore the factory Settings.

![](https://media-hub.inhand.com/edge_computers/EC300_EN/0336f8d8dab8e556.png)

1. Restore factory Settings by pressing:

1. Long press the **Reset** key for 10-20s and see the **WARN** light long on.

   

1. When the **WARN** light has turned on, release the **Reset** key.

   

NOTE:

(1) System reset is an important function of ARM computers. After system reset, the ARM computer will be restored to the default state and all user data and configurations will be lost.

(2) Before resetting your ARM computer system, ensure that critical data has been effectively backed up and transferred to external storage media (such as a removable disk)



# **7 Programming Guidelines**

EC300 provides a JSON format device information description file. Customers who need to operate IO, LED, serial port and other peripherals can obtain the device node information of these peripherals by querying the device description information file.

Device description file path: **/tmp/ieos/etc/system_info.json**, the content is as follows:

```json
{
  "device_info": {
    "model_info": {
      "model": "EC312",
      "pn": "H-LQA3-LC4D",
      "sn": "CL3124050000001",
      "oem": "inhand",
      "features": ";std;cell-LQA3;wlan;"
    },
    "software_info": {
      "boot_loader": "V1.0.2",
      "kernel": "5.10.168",
      "version": "V1.0.1-beta1",
      "os": "Debian GNU/Linux 11 (bullseye)"
    },
    "hardware_info": {
      "arch": "armv8",
      "soc": "AM6231",
      "interface": {
        "eth": [
          {
            "iface_name": "eth1",
            "iface_mac": "00:08:5f:17:04:00"
          },
          {
            "iface_name": "eth2",
            "iface_mac": "00:18:5f:17:04:02"
          }
        ],
        "wlan": [
          {
            "iface_name": "wlan0",
            "iface_mac": "f4:3c:3b:ca:e9:36"
          },
          {
            "iface_name": "wlan1",
            "iface_mac": "f6:3c:3b:ca:e9:36"
          }
        ]
      },
      "gpio": [
        {
          "gpio_name": "cellular_power",
          "dev_node": "/sys/class/gpio/gpio401"
        },
        {
          "gpio_name": "sim_switch",
          "dev_node": "/sys/class/gpio/gpio405"
        }
      ],
      "user_key": [
        {
          "user_key_name": "user1",
          "dev_node": "/dev/input/event2"
        }
      ],
      "uart": [
        {
          "uart_name": "com1",
          "dev_node": "/dev/ttyS4"
        },
        {
          "uart_name": "com2",
          "dev_node": "/dev/ttyS5"
        }
      ],
      "led": [
        {
          "led_name": "user1",
          "dev_node": "/sys/class/leds/user1"
        },
        {
          "led_name": "user2",
          "dev_node": "/sys/class/leds/user2"
        },
        {
          "led_name": "user3",
          "dev_node": "/sys/class/leds/user3"
        },
        {
          "led_name": "user4",
          "dev_node": "/sys/class/leds/user4"
        },
        {
          "led_name": "cell",
          "dev_node": "/sys/class/leds/cell"
        },
        {
          "led_name": "warn",
          "dev_node": "/sys/class/leds/warn"
        },
        {
          "led_name": "status",
          "dev_node": "/sys/class/leds/status"
        }
      ],
      "io": {
        "di": [
          {
            "di_name": "di1",
            "dev_node": "/sys/class/gpio/gpio454"
          },
          {
            "di_name": "di2",
            "dev_node": "/sys/class/gpio/gpio455"
          },
          {
            "di_name": "di3",
            "dev_node": "/sys/class/gpio/gpio456"
          },
          {
            "di_name": "di4",
            "dev_node": "/sys/class/gpio/gpio457"
          }
        ],
         "do": [
                   {
                      "do_name":"do1",     //The name matches the name on the panel
                      "dev_node": "/sys/class/gpio/gpio11"
                   },
                   {
                      "do_name":"do2",
                      "dev_node":"/sys/class/gpio/gpio12"
                   }
                ]
            },
            "ain": [
               {
                    "ain_name": "ain1", 
                    "ain_node": "/dev/ain1"
               },
               {
                    "ain_name": "ain2", 
                    "ain_node": "/dev/ain2"
               }              
            ]
        }
    }
}
```

## 7.1 IO Programming Guide

Currently, there are a total of 8 IO interfaces on the device: for example, there are 4 input pins from DI1 to DI4 on the device panel; DO1~DO4 are 4 output pins.

According to the device description file **/tmp/ieos/etc/system_info.json**, the IO device nodes are:

When you need to program IO interface, directly operate the value under the background device node **(sys/class/gpio/gpioxxx/value)**

Example:

When DO1 needs to output a high level, you can directly write **1** to **sys/class/gpio/gpio323/value**

echo 1 > /sys/class/gpio/gpio323/value

When you need to check the level of DI1, you can also directly check the value of **sys/class/gpio/gpio454/value**

cat /sys/class/gpio/gpio454/value

The full shell script:

```shell
#!/bin/bash

gpio323="/sys/class/gpio/gpio323/value"
gpio453="/sys/class/gpio/gpio453/value"
gpio465="/sys/class/gpio/gpio465/value"
gpio461="/sys/class/gpio/gpio461/value"
# When DO1 needs to output a high level, you can directly write 1 to sys/class/gpio/gpio323/value.
if [ -f "$gpio323" ]; then
    echo 1 > /sys/class/gpio/gpio323/value
else
    echo "no file exit "$gpio323
fi

# When DO1 needs to output a low level, you can directly write 0 to sys/class/gpio/gpio323/value.

if [ -f "$gpio323" ]; then
    echo 0 > $gpio323
else
    echo "no file exit "$gpio323
fi

gpio454="/sys/class/gpio/gpio454/value"
gpio455="/sys/class/gpio/gpio455/value"
gpio456="/sys/class/gpio/gpio456/value"
gpio457="/sys/class/gpio/gpio457/value"
# To check the level of DI1, you can directly read the value of sys/class/gpio/gpio454/value.
if [ -f "$gpio454" ]; then
    cat $gpio454
else
    echo "no file exit "$gpio454
fi
```

## 7.2 Led Programming Guide

The user can use the four lights USER1, USER2, USER3 and USER4 on the device for status prompts, please check the light label to confirm the position of the light.

According to the device description information file **/tmp/ieos/etc/system_info.json**, the device node corresponding to LED can be obtained as follows:

user1: **/sys/class/leds/user1**

user2: **/sys/class/leds/user2**

user3: **/sys/class/leds/user3**

user4: **/sys/class/leds/user4**

There are some control files in **/sys/class/leds/user1** to control the attributes and status of LEDs:

**/sys/class/leds/user1/brightness**: this file is used to control the user1 lights on or off. Write 1 to always on, write 0 to always off.

**/sys/class/leds/user1/trigger**: The trigger of the LED light can be written as timer to indicate timer triggering, and write none to cancel the trigger.

**/sys/class/leds/user1/delay_on**: This file indicates the time the LED light is on, in ms.

**/sys/class/leds/user1/delay_off**: This file indicates the time the LED light is off, in ms.

If trigger is configured for timing, the value in the brightness will no longer take effect and will automatically change to 0.

Replace user1 with user2 in the file path to control the operation of the USER2 light, this mechanism works the same for USER3 and USER4.

Example:

Write 1 to the brightness file when you need the USER1 light to be on

```shell
echo 1 > /sys/class/leds/user1/brightness
```

When the USER1 light is needed to flash, the timer is written to the trigger file, and the light and off times are controlled by delay_on and delay_off

```shell
\# start timer
 echo timer > /sys/class/leds/user1/trigger
\# echo on 1 second
 echo 1000> /sys/class/leds/user1/delay_on
\# echo out 1 second
 echo 1000 > /sys/class/leds/user1/delay_off
```

Full shell script:

```shell
#!/bin/bash

USER1_BRIGTHNESS="/sys/class/leds/user1/brightness"
USER1_TRIGGER="/sys/class/leds/user1/trigger"
USER1_DELAY_ON="/sys/class/leds/user1/delay_on"
USER1_DELAY_OFF="/sys/class/leds/user1/delay_off"

# Light the USER1 LED
if [ -f "$USER1_BRIGTHNESS" ]; then
    echo 1 > $USER1_BRIGTHNESS
else
    echo "no file exit "$USER1_BRIGTHNESS
fi

# Set the USER1 LED to flash
if [ -f "$USER1_TRIGGER" ]; then
    echo timer > $USER1_TRIGGER
else
    echo "no file exit "$USER1_TRIGGER
fi

# Set the USER1 LED on for 1000ms
if [ -f "$USER1_DELAY_ON" ]; then
    echo 1000 > $USER1_DELAY_ON
else
    echo "no file exit "$USER1_DELAY_ON
fi

# Set the USER1 LED off for 1000ms
if [ -f "$USER1_DELAY_OFF" ]; then
    echo 1000 > $USER1_DELAY_OFF
else
    echo "no file exit "$USER1_DELAY_OFF
fi

# Turn off USER1 blinking
if [ -f "$USER1_TRIGGER" ]; then
    echo none > $USER1_TRIGGER
else
    echo "no file exit "$USER1_TRIGGER
fi
```

## 7.3 Cross-compiling

A user's own C/ C++ program can be cross-compiled by using the cross-compilation toolchain on the development machine, and then the object file is uploaded to the EC300 device for execution.

Cross-compilation tool zip package: gcc-linaro-6.3.1-2017.05-x86_64_aarch64-linux-gnu.tar.gz

Here's how to configure the environment variables for the cross-compilation toolchain:

1. Unzip **gcc-linaro-6.3.1-2017.05-x86_64_aarch64-linux-gnu.tar.gz** to /opt on your development machine (you can also unzip it to any other PATH, adjust the path environment variable in step 2)
2. Edit the **~/.bashrc** file and add a line **PATH=$PATH:/opt/gcc-linaro-6.3.1-2017.05-x86_64_aarch64-linux-gnu/bin** at the end of the file
3. Execute source **~/.bashrc** to make the environment variables work in the current terminal; The newly opened terminal will take effect automatically.

Using the classic hello world program as an example, create the following directories and files

```shell
mkdir ~/example
touch ~/example/hello.c
touch ~/example/Makefile
```

The contents of the **~/example/hello.c** file are as follows:

```shell
mkdir ~/example 
touch ~/example/hello.c 
touch ~/example/Makefile
```

The contents of the ~/example/hello.c file are as follows:

```C
\#include <stdio.h>

int main(void) 
{ 
    printf("hello, world! \n"); 
    return 0;  
}
```

The contents of the ~/example/Makefile are as follows:

```Makefile
\# Define TARGET and source filenames 
target := hellworld 
DIRS := $(shell find.-maxdepth 3-type d)  
SRCS := $(foreach dir,$(DIRS),$(wildcard $(dir)/*.c)) 
OBJS := $(SRCS:.c=.o) 


CC=aarch64-linux-gnu-gcc 

\# Define compiler and compile options  
CFLAGS := -Wall-Wextra -g-wno-unused-parameters 

\# define default TARGET  
all: $(TARGET)

\# define target file dependencies and compile commands  
$(TARGET): $(OBJS)  
$(CC) $(CFLAGS) $(LIBS) $^ -o $@  

\# Define the command to compile the source file to the target file 
%.o: %.c 
$(CC) $(CFLAGS) $(LIBS) -C $< -o $@

\# Define command to clear temporary files 
clean: 
rm -f $(TARGET) $(OBJS)

\# declare pseudo target ".PHONY" 
.PHONY: all clean
```

Run make in the ~/example directory to generate the object file helloworld



## **7.4 Watchdog P**rogramming

- There is an external hardware watchdog on the device, and the device will restart if the dog is not fed for 60 seconds
- You can disable the system watchdog program, in your own program to implement feed the dog, so that the program can restart the device when the exception
- Shut down the system watchdog with this command：`systemctl stop watchdog`
- Example watchdog program：

```C
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>

static int fd = 0;

/* Signal processing functions */
void signal_handler(int signal)
{
    /* Shut down the watchdog. The device will restart after 60 seconds if the dog is not fed */
    write(fd, "V", 1);
    close(fd);
    exit(0);
}

int main(int argc, char **argv)
{
    /* open the watchdog by opening */
    fd = open("/dev/watchdog0", O_WRONLY);

    /* Registering Kill signals */
    signal(SIGTERM, signal_handler);
    
    while (1) {
        /* Feed the dog by writing */
        write(fd, "\0", 1); 

        /* Feed the dog every 10 seconds */
        sleep(10);
    }
}
```