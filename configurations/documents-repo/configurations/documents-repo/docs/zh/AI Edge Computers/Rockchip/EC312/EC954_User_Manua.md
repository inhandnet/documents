**Edge Computer EC950 Series**

**User's Manual**

**(Compatible with Debian 11, IEOS V2.0.0 and above versions)**

Version 2.0, January 2024

[www.inhandnetworks.com](http://www.inhandnetworks.com/) 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/f881f36ded0963c4.png)

The software described in this manual is according to the license agreement, can only be used in accordance with the terms of the agreement.

**Copyright Notice** 

© 2024 InHand Networks All rights reserved.

**Trademarks** 

The InHand logo is a registered trademark of InHand Networks.

All other trademarks or registered trademarks in this manual belong to their respective manufacturers.

**Disclaimer** 

The company reserves the right to change this manual, and the products are subject to subsequent changes without prior notice.We shall not be responsible for any direct, indirect, intentional or unintentional damage or hidden trouble caused by improper installation or use.

# **1 Introduction** 

This user manual is applicable to the Edge Computer EC954 series based on Arm architecture, and covers a complete set of instructions applicable to all supported models. Before referring to these chapters, please confirm if the hardware specifications of your computer model support the features/settings covered.

# **2 Hardware installation instructions** 

In this chapter, we will introduce the hardware installation instructions of the edge computer EC954 series based on Arm structure. 

## **2.1 Introduction** 

The following chapter takes the EC954 series as an example to describe the application of external connectors and pin assignments in the EC954 series. 

## **2.2 EC954 Panel** 

Top panel

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/c8f4e9629e910bff.png)

Front panel 


![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/20f6b92eabf1b528.png)

## **2.3 EC954 External Connector** 

### **2.3.1 Ethernet** 

These are four RJ45 connectors for Ethernet connection 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/ab7a5b73703e41a9.png)

EC954 has four RJ45 Ethernet ports and supports 10M/100M/1000M adaptive rates. 

Green light: The LINK indicator light is on for a long time when the peer device has a 1000M interface, and off for a long time when the peer device has a 10/100M interface.

Yellow light: ACT light, flashing when there is data 

### **2.3.2 Serial port** 

EC954 supports 8 serial ports, with the first 4 channels supporting RS-232, RS-485, or RS-422 communication. The software is configurable, and the last 4 channels are fixed to RS-485 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/4e4feb0047f7c08a.png)

| **RJ45 pin number** | **RS-232** | **RS-422** | **RS-485** |
| ------------------- | ---------- | ---------- |------------|
| one                 | DSR        | -          | -          |
| two                 | RTS        | TxD+       | -          |
| three               | GND        | GND        | GND        |
| four                | TxD        | TxD-       | -          |
| five                | RxD        | RxD+       | Data+      |
| six                 | DCD        | RxD-       | Data-      |
| seven               | CTS        | -          | -          |
| eight               | DTR        | -          | -          |

### **2.3.3 CAN** 

EC954 has a 2-way CAN bus interface and supports the CAN 2.0A/B standard, and can reach a maximum speed of 5Mbps. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/4e4feb0047f7c08a.png)

| **RJ45 pin number** | **RS-232** | **RS-422** | **RS-485** |
| ------------------- | ---------- | ---------- |------------|
| one                 | DSR        | -          | -          |
| two                 | RTS        | TxD+       | -          |
| three               | GND        | GND        | GND        |
| four                | TxD        | TxD-       | -          |
| five                | RxD        | RxD+       | Data+      |
| six                 | DCD        | RxD-       | Data-      |
| seven               | CTS        | -          | -          |
| eight               | DTR        | -          | -          |

### **2.3.4 Digital Input Interface** 

| **Interface identification** | **Function**                 | **Describe** |
| ---------------------------- | ---------------------------- | ------------ |
| COM                          | DI Common Port               |              |
| DI0                          | Digital input interface 0    |              |
| DI1                          | Digital input interface No.1 |              |
| DI2                          | Digital input interface No.2 |              |
| DI3                          | Digital input interface No.3 |              |

**Prompt**

4-way digital input DI,

Dry contact status：

​     "1": Closed dry contact status 

​     "0": Open

Isolation 3000VDC；

### **2.3.5 Digital Output Interface** 

| **Interface identification** | **function**                  | **describe** |
| ---------------------------- | ----------------------------- | ------------ |
| GND                          | DO grounding terminal         |              |
| DO0                          | Digital output interface 0    |              |
| DO1                          | Digital output interface No.1 |              |
| DO2                          | Digital output interface No.2 |              |
| DO3                          | Digital output interface No.3 |              |

**Prompt**

4-channel digital output DO,

Isolation 3000VDC

### **2.3.6 USB** 

EC954 provides two USB 2.0 Host interfaces. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/b4a1e7f991a8348f.png)

### **2.3.7 LED**

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/11de6be28f315eff.png)

EC954 has 12 LED lights that respectively indicate the power supply and system operation status. 

| **Identification** | **Name**                                              | **Definition**                                               |
| ------------------ | ----------------------------------------------------- | ------------------------------------------------------------ |
| PWR                | Power indicator light                                 | Always on when powered on                                    |
| STAT               | System operation status indicator light               | When the system starts up normally, the STATUS flashes. If there is an abnormality during the system startup phase that causes the system to fail to start; When the factory operation is not yet completed, the STATUS will be turned off for a long time. |
| WARN               | Warning indicator light                               | When a warning exception occurs in the system and the system upgrade or factory restoration is not yet completed, the WARN light flashes. |
| ERR                | Error indicator light                                 | When a serious error occurs in the system and the system upgrade or factory recovery is not yet completed, the Error light flashes. |
| SIM1               | SIM1 card indicator light,                            | When selecting SIM card 1 for dialing, it always lights up. When selecting SIM card 2 for dialing or turning off dialing, it stays off. |
| SIM2               | SIM1 card indicator light, if selected, it remains on | When selecting SIM card 2 for dialing, it always lights up. When selecting SIM card 1 for dialing or turning off dialing, it stays off. |
| USER1              | User programmable indicator light 1                   | Default off, can be programmed and controlled by the user    |
| USER2              | User programmable indicator light 2                   | Default off, can be programmed and controlled by the user    |
| 4G/5G              | Cellular network connection status indicator light    | Always on after successful dialing                           |
| L1                 | Cellular network signal strength                      | See instructions for cellular network signal strength indicator lights |
| L2                 | Cellular network signal strength                      | See instructions for cellular network signal strength indicator lights |
| L3                 | Cellular network signal strength                      | See instructions for cellular network signal strength indicator lights |

Cellular network signal strength indicator light 

| **LED** | **No signal** | **Weak signal (RSSI<-90)** | **Signal medium (-90<=RSSI<-70)** | **Signal strength (RSSI>=-70)** |
| ------- | ------------- | -------------------------- | --------------------------------- | ------------------------------- |
| L1      | Extinction    | bright                     | bright                            | bright                          |
| L2      | Extinction    | Extinction                 | bright                            | bright                          |
| L3      | Extinction    | Extinction                 | Extinction                        | bright                          |

In addition to the combination of L1, L2, and L3 signal lights to indicate cellular signal strength, there is also a set of LED combinations to indicate the process of factory restoration. 

| **LED** | **state**  |
| ------- | ---------- |
| WARN    | flicker    |
| Error   | flicker    |
| STATUS  | Extinguish |

After restoring the factory settings, the system will undergo a restart. After the restart is completed, the factory reset is not complete. At this time, the WARN light and ERROR flash, and the STATUS goes out. In this state, the device cannot be powered off, otherwise it may cause some files to be lost and affect system functions. This state will last for 30 seconds. After the factory is restored, WARN and ERROR will turn off, and STATUS will flash. 

### **2.3.8 User programmable buttons** 

EC954 provides an API interface, which users can call to detect the status of programmable buttons and then implement their own button logic.

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/f71d71d9c11f0059.png)

### **2.3.9 DC Input** 

EC954 supports 12-48V DC input 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/15ca55fda03eb1cc.png)

### **2.3.10 SIM card slot** 

EC954 supports 2 SIM card slots. SIM cards need to be installed in a power-off state. Simply press and insert the SIM card into the slot. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/2358de96fd4f2386.png)

### **2.3.11 MicroSD card slot**

EC954 has a MircoSD card slot, and SD does not support hot swapping. It needs to be plugged and unplugged in the event of a power outage. After inserting the SD card and powering on the device, the system will automatically mount all partitions. 

### **2.3.12 Factory Reset Button** 

There is a reset button for restoring the system to factory settings. Refer to ["Restore Factory Settings"](#**6. System restoration to factory settings and updates** )for operation. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/77f24942a6975dc6.png)

### **2.3.13 On/Off button**

EC954 is equipped with an on/off button for power on/off. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/bbd5e7fc3b893695.png)

### **2.3.14 Antenna interface** 

EC954 has a total of 7 antenna interfaces, and the number of antennas standard for different models varies. The antennas are screwed into the corresponding antenna interfaces to complete antenna installation. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/7122c8f427d55d09.png)

| **Identification** | **Name**                                      |
| ------------------ | --------------------------------------------- |
| ANT1               | 4G LTE main antenna/5G antenna                |
| ANT2               | 4G LTE diversity receiving antenna/5G antenna |
| GNSS               | GNSS antenna                                  |
| ANT3               | 5G antenna                                    |
| ANT4               | 5G antenna                                    |
| WiFi1              | WiFi antenna                                  |
| WiFi2              | WiFi antenna                                  |

### **2.3.15 mSATA hard drive interface**

EC954 supports mSata hard drives, which are not included by default at the factory. If users have high-capacity storage needs and need to purchase their own mSata hard drives, they can also consult InHand to purchase mSATA. 

# **3 Introduction** 

In this chapter, we will introduce the basic configuration of the Edge Computer EC900 based on the Arm structure.

## **3.1 Connecting to EC900** 

You need a computer to connect to EC900 and log in to the command line interface. It can be connected through an Ethernet cable. 

Factory default username and password: 

**Username: edge** 

**Password: security@edge**

EC900 devices default to creating root at the factory, but login is disabled. If you need to use the root user, please manually modify the system configuration and enter sudo - s to switch to the root user. The user edge is in the sudo group, so you can use sudo to execute system level commands under the edge user. For other details, please refer to the sudo mechanism section in Chapter 5. 

**Prompt**

When the **command** **not** **found** appears, enter sudo - s to switch to the root user or use the sudo command to operate. 

**Take care** 

For security reasons, we recommend that you disable the default user account and create your own user account.

### **3.1.1 Connecting through SSH Console** 

EC900 supports SSH connection through Ethernet. Connect to EC900 using the following default IP address. 

| **Port** | **Default IP** |
| -------- | -------------- |
| ETH 1    | 192.168.1.100  |
| ETH 2    | 192.168.1.100  |
| ETH 3    | 192.168.5.100  |
| ETH 4    | 192.168.6.100  |

##### **3.1.1.1 Linux users** 

Prompt

These steps apply to connecting to EC900 on a Linux PC. Please do not apply these steps to the EC900 device itself. Before running the ssh command, make sure to configure the Ethernet port IP address of the PC within a specific range. ETH1: 192.168.1.0/24, ETH2: 192.168.4.0/24, ETH3: 192.168.5.0/24, ETH4: 192.168.6.0/24. 

Use the ssh command on a Linux PC to access the ETH1 port of EC900.

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/e03e6cb2554f7c96.png)

Enter **yes** to continue connecting.

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/31a1696354ad1c80.png)

When the interface displays the terminal prompt `edge@edge-computer:~$`, indicating that shell commands can be entered, the connection is successful.

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/7652a9a58990a057.png)

##### **3.1.1.2 Windows users** 

**Prompt**

These steps apply to connecting EC900 on a Windows PC. Please do not apply these steps to the EC900 device itself. 

Please take the following steps on your Windows PC 

Click on the link [http://www.chiark.greenend.org.uk/ ](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)[~Sgtatham/putty/download.html](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html), download PuTTY (free software), and establish the connection with the edge computer EC900 in the way of SSH command in the Windows environment. The following figure is an example of using SSH connection:

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/0937f9a8e07979e5.png)

## **3.2 User Account Management** 

### **3.2.1 Switch to root user** 

You can use the command sudo - s to switch to the root user. For security reasons, do not operate all commands under root privileges. 

**Prompt** 

Click on the link to get more information about the **sudo** command. 

[https://wiki.debian.org/sudo](https://wiki.debian.org/sudo /h)

**Take care**

You may receive a permission denied prompt when using certain pipes or redirection behaviors without root privileges. In this case, you must use 'sudo su - c' instead of commands such as'>','<','>>','<<',' etc ', and include single quotes for the complete command.

### **3.2.2 Creating and deleting user accounts** 

You can use the **useradd** and **userdel** commands to create and delete user accounts. Please make sure to use these commands on the main interface to set the relevant access permissions for this account. Here is an example of how to create test1 in the sudo group (the default login environment for test1 users is bash, and their home directory is/home/test1) 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/b4752b719477036e.png)

Change the password for test1, use the passwd command, enter the new password, and then repeat the process to confirm the change

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/afd9feb118794f96.png)

If you want to delete user test1, use the command userdel 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/16292e070b876fad.png)

### **3.2.3 Disable default user accounts** 

**Take care** 

Before disabling the default account, you should first create a user account 

Use the passwd command to lock the default user account and prevent edge users from logging in 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/d77c18e200f7a6dd.png)

Unlocking edge users

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/cda1e99f7b06bdb3.png)

## **3.3 Network and System Management**

EC954 is based on the Debian 11 system, so it can use native Linux commands for network and system management; In order to facilitate user configuration, InHand has developed an IEOS system program that provides a web interface, allowing users to easily manage networks and systems through the web. However, it should be noted that when the IEOS function is enabled, IEOS will take over network and system management. At this time, using Linux native commands for network and system management may become ineffective; IEOS is enabled by default at the factory of the device. If users need to perform network and system management based on Linux native command lines, they need to first disable IEOS.

### **3.3.1 Web management based on IEOS**

IEOS is a network management and system management program developed by InHand that runs on Linux systems. IEOS provides a web interface, allowing users to configure Ethernet IP addresses, cellular dialing, Wi Fi Station, DHCP Client/Server, static routing, firewalls, and other network configurations through the web; You can also perform operations on system time, time zone, firmware upgrades, and system restarts; In addition, IEOS also supports integration with InHand's device management platform DeviceLive, allowing users to remotely monitor and manage EC954 devices through the DeviceLive platform.

IEOS adopts a design scheme that separates state and configuration, divided into three functional modules: network management, system management, and state. Only network and system related configurations can be performed under the network management menu and system management menu, and status information needs to be viewed uniformly on the status page. 

Important note: When using the IEOS program to manage network and system configurations, if Linux native commands are used at the same time, the two may affect each other, leading to abnormal running states. It is recommended that the configurations supported by IEOS be managed through the IEOS web. For configurations not supported by IEOS, such as VPN, the configuration goals can be achieved by combining native Linux commands.

#### **3.3.1.1 Logging into the web** 

Considering that the user's program may require the use of HTTP/HTTPS standard port number 80/443, IEOS uses port number 9100 as the port for HTTPS connection and does not support access through HTTP; When users access the web using HTTP, they will automatically redirect to using HTTPS. This document takes the default address 192.168.4100 through eth2 as an example for explanation. After entering 192.168.4100:9100 in the browser, the user will be redirected to the login page

Important note: When the IEOS program is enabled, some port numbers will be reserved for internal communication, with a reserved port number range of 9100 to 9200. After enabling IEOS, customer programs should avoid using these port numbers, otherwise conflicts may occur and functional abnormalities may occur. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/8c452fb93cfeb884.png)

#### **3.3.1.2 Network Management** 

##### **3.3.1.2.1 Configure Ethernet interface** 

Configure static IP addresses for the eth1 interface 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/63f010f26534deef.png)

Configure DHCP Client for eth1 interface

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/7e750e3bc024038e.png)

Start the dhcp server function on the eth1 interface and assign addresses to the underlying devices of eth1 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/6323b90960d474f4.png)

DHCP Server configuration parameter description:

**Enable DHCP** **Server**: Switch for DHCP Server functionality

**Starting** **Address**: The starting base address of the DHCP Server address pool, where network segment+starting address=the starting IP address of the address pool. In the screenshot, the network segment of eth1 is 192.168.1.0/24, and the base address is 1, so the starting address of the address pool is 192.168.1.1/24

**Max Address** **Number**: The maximum number of addresses in the address pool



**Lease** **period**: Lease period

##### **3.3.1.2.2 Configure cellular dialing** 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/a6605d00e5629aed.png)

Cellular network parameter description: 

**Enable**: switch for cellular function; The default is the enabled state.

**APN Profiles**: A set of dialing parameters used to configure APN, username, password, and authentication method information when dialing with a dedicated network card. If it is not a dedicated network card, there is usually no need to modify the configuration here. The dialing parameter set can add up to 10 records. 

**Network Mode**: The cellular network format, which can choose from 3G, 4G and other related network formats, such as LTE, WCDMA, etc. If it is unclear which network standard to choose, choose automatic; The program will automatically select the most suitable network format. The default value is automatic.

**Enable Default Route**: Enable the add default route function. When enabled, a default route for the cellular port will be added after successful dialing. It is enabled by default. 

**Metric**: The metric value of the default routing for cellular ports. When default routing is configured for cellular, Wi Fi, and Ethernet ports, the metric with the smallest value takes effect.

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/cff0830253230923.png)

**Dual SIM enabled**: enables the dual SIM feature. EC954 supports dual card single dial to improve network reliability. Two SIM cards need to be inserted into the device. After enabling this function, if the SIM card 1 fails to dial due to arrears, it will automatically switch to the SIM card 2 for dialing. The default is off. 

**Main SIM**: The main SIM card will prioritize the selected SIM card for dialing. When dialing fails a certain number of times, it will switch to another SIM card for dialing. By default, sim1 will be used for dialing first.

**Max Number of Dials**: After enabling the dual SIM single dial function, if the current SIM card reaches the specified number of dials, switch to another SIM card for dialing. 

**APN Profile**: The dialing parameter set selected by the SIM card, with the default value being automatic. Usually, a dedicated network card needs to configure a dial-up parameter set and select the Index of the dial-up parameter set here.

**PIN** **Code**: The PIN code of the SIM card. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/9b3b35a1f543ad21.png)

Wireless cellular networks are quite complex, and sometimes there may be false dial-up connections, where the dial-up status is successful but the target address cannot be pinged; When these situations occur, dialing again can restore normal operation. IEOS cellular dialing supports ICMP detection to detect fake connections. It is recommended that customers using cellular networking enable ICMP detection, so that when false connections occur, they can quickly recover.

ICMP detection parameters: 

**ICMP Detection Server Probes**: ICMP detection address; Two detection addresses can be configured, and as long as one address is successfully detected, it indicates that there is no false connection in the cell. When both addresses are not configured, the ICMP detection function is turned off. 

**Detection** **Interval**: How often should ICMP detection be conducted.

**Detection** **Timeout**: The ICMP detection timeout period. If no detection response message is received after waiting for a long time, it is considered that the detection has failed 

**Detection Max** **Retries**: Maximum number of detections; When the detection fails and reaches this value, trigger a redial. Value range [1,5]

**Detection Strict**: Whether strict detection is enabled. When strict detection is turned off, the detection program will detect whether the messages received by the cellular interface have changed during each detection cycle. If there are changes, it indicates that the cellular network is connected, and ICMP messages will not be sent for detection, which can save some traffic; If detection is enabled, ICMP detection messages will be periodically sent regardless of whether the number of messages received by the cellular interface has changed. The default is off. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/30fcb6a18612f551.png)

In advanced configuration, there are some uncommon setting options.

**Debug Mode enabled**: Whether to enable the debug function. After enabling it, some dial-up related debugging information will be added to the log, which is disabled by default. 

**Enable Infinitely Redial**: Enable infinite redial. In some cases, dialing may be in an abnormal state and can be restored to normal by restarting the system; The default infinite redial is turned off. After a certain number of failed dials, the system will restart to try to recover. Due to dialing being enabled by default, some customers may fail to dial without inserting a SIM card, and the system may restart. In this case, unlimited redial can be enabled; This way, no matter how many times the dialing fails, the system will not restart.

**Dial Interval**: Dialing interval; But the time to wait before proceeding to the next dial when a dial fails. 

**Signal Query Interval**: Signal query interval. When the signal is poor, false connections may occur; At this point, there is a certain probability that redialing can solve the problem of fake connections. The dial-up program will regularly check the signal strength, and the signal detection cycle is configured here. 

##### **3.3.1.2.3** **Configure Wi Fi Station**



![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/55e05dbda4e4eded.png)



**Enable** **Wi Fi**: enable switch; Default Off 

**Client** **SSID**: The ssid that needs to be connected, which can be manually entered; You can also obtain nearby accessible ssids by scanning the button

**Enable Default** **Route**: Whether to enable the add default route function. When enabled, a default route for the WLAN port will be added after a successful WiFi connection. It is enabled by default. 

**Metric**: The metric value of the default routing for WiFi ports. When default routing is configured for cellular, Wi Fi, and Ethernet ports, the metric with the smallest value takes effect. 

**Auth Method**: Authentication method, supports no authentication, WPA-PSK, WPA2-PSK, WPA-PSK/WPA2-PSK Mixed

**Encrypt** **Mode**: encryption method; Supports CCMP, TKIP, TKIP, and CCMP 

**WPA/WPA2 PSK Key**: Key information 

##### **3.3.1.2.4 Configure static routing**

The configuration here is for static routing of Ethernet. When default routing of Ethernet, cellular, and WiFi is configured simultaneously, the default routing with the lowest metric value takes effect. It is necessary to ensure that the metric value of the default route is different. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/9290b53ac5475971.png)

Static routing configuration parameters: 

**Interface**: The outbound interface for static routing 

**Target**: Target network

**Netmask**: Target Netmask 

**Gateway**: Next hop address 

**Metric**: The metric value of static routing 

##### **3.3.1.2.5** **Configure firewall** 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/76dc4595fe549aee.png)

Currently, only the iptables command is supported for configuration.

##### **3.3.1.2.6** **Configure DNS** 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/888a085d232d8d9c.png)

**DNS** **servers**: DNS server addresses, supporting up to 4 configurations 

**Domain name** **hijacking:** Domain name hijacking function, which can achieve binding between IP addresses and domain names. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/f959063ee1cc26db.png)

##### **3.3.1.2.7** **Network Diagnostics**

Network diagnosis supports ping, traceroute, and nslookup functions. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/c3a592fcda297433.png)

#### **3.3.1.3 System Management** 

##### **3.3.1.3.1 Basic Configuration** 

**Cloud management**

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/17381afbd701ad31.png)

**Enabled**: an enable switch for docking with the DeviceLive platform; DeviceLive is a remote monitoring and management platform for InHand devices; 

**Cloud Server**: DeviceLive platform has 2 addresses; One is the address of the domestic platform, and the other is the address of the overseas platform; Choose which platform to connect to here. 

**Time zone and NTP** **client**

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/3ec4bdfad40aab0c.png)

Up to 10 NTP server addresses can be configured, and the program periodically sends synchronization requests to each server address in sequence. After successful synchronization, the system time is written to the RTC and synchronization requests are no longer sent to subsequent NTP servers. 

In addition to using NTP to synchronize time, there is a synchronization button on the Device Info status page that allows for manual synchronization of time. However, this synchronization button is only displayed when the device time and local time (the time of accessing the computer used by the device) differ by more than 3 seconds. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/497a108631397f48.png)

Here, configuration import, export, and factory recovery are supported.

##### **3.3.1.3.2 Firmware Upgrade** 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/13f3ae4346d49866.png) 

The automatic restart option is disabled by default. After upgrading the firmware, the system needs to be manually restarted to take effect; After enabling the automatic restart option, the system will automatically restart after a successful firmware upgrade. 

##### **3.3.1.3.3 Others**

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/57aafcc91ce48bfc.png)

This page has two functions: system restart and system reset. Resetting the system requires careful use. Resetting the system function will restore the configuration and file system status of the system to be consistent with the factory settings, which means that the software installed by the user will also be cleared. 

#### **3.3.1.4 Status** 

##### **3.3.1.4.1 Equipment information** 

The device information status page displays the host name, device model, serial number, firmware version, kernel version, file system version, as well as an overview of CPU, memory, and disk space usage.



![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/137f58d148c98701.png)



##### **3.3.1.4.2 Cellular dialing status information** 

The cellular dialing status page displays the SIM card, IMEI, IMSI, ICCID, signal strength, as well as the IP address, DNS, and other information obtained during dialing. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/1f1cded8f5ccf498.png)

##### **3.3.1.4.3 Wi-Fi Station Status Information** 

The Wi-Fi status page displays the IP address, gateway, and DNS information obtained after a successful Wi Fi connection.

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/42b7ab3495fc8e4e.png)

##### **3.3.1.4.4 DHCP Server status information** 

The DHCP Server status page displays the IP address, client host name, client host MAC, and expiration time assigned to the device as a DHCP Server. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/b57e23ae4cdb157f.png)

##### **3.3.1.4.5 Routing status information** 

The routing status page displays information such as IPv4 direct routing, static routing, and routing neighbors.

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/e797fba46eb3db1c.png)

##### **3.3.1.4.6 Firewall status information** 

The firewall status information displays filtering rules, IP address mapping rules, and other information. 



![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/ffd5b95c2d4aca24.png)



##### **3.3.1.4.7 Log information** 

The log page can view system logs, user logs, and set the level of logs to be viewed, including Error, Info, Debug, and other levels. Logs can also be downloaded locally. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/f468dfdf21108666.png)

### **3.3.2 Linux based command line management**

When using the Linux command line for network and system configuration, the first step is to close the IEOS program. IEOS is managed through system ctl, 

The way to close IEOS is as follows: 

Systemctl stop ieos_daemon 

This shutdown only takes effect for this startup. Even after the system restarts, the IEOS program will still start. The way to prevent the IEOS program from starting up is as follows:

Systemctl disable ieos_daemon 

Important note: After disabling IEOS, wireless networking functions such as dial-up and Wi Fi require users to implement them based on native Linux commands, and it is also impossible to remotely manage devices through the DeviceLive platform. 

#### **3.3.2.1 Network Management** 

##### **3.3.2.1.1 Set a static IP address**

If you want to set a static IP address for EC954, modify the corresponding network configuration file by using the commands vim/etc/network/interfaces. d/eth1 or vim/etc/network/interfaces. d/eth2 to set the default gateway, address, network, and subnet mask for the Ethernet interface. Here is an example of setting a static IP for the eth2 port:

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/4ac9822441260610.png)

After modifying the interface IP configuration, execute/etc/init.d/networking restart to restart the network service and make the configuration effective. 

##### **3.3.2.1.2 Set a dynamic IP address**

If you want to set a dynamic IP address for EC954, modify the corresponding network configuration file by using the command vim/etc/network/interfaces. d/eth1 or vim/etc/network/interfaces. d/eth2, and set it to DHCP after inet to automatically obtain the IP address. 

Here is an example of setting a dynamic IP for the eth1 port.

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/7e4f44c55f7326d7.png)

After modifying the interface IP configuration, execute/etc/init.d/networking restart to restart the network service and make the configuration effective. 

#### **3.3.2.2 System management** 

##### **3.3.2.2.1 Querying Firmware Version**

To check the computer firmware version of EC954, please type: 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/57723d60bbec2abe.png)

By adding the - a option, you can see the complete version information: 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/010ba92be613f69f.png)

##### **3.3.2.2.2 Viewing available disk space** 

To determine the amount of available drive space, use the df command with the - h option. The system will return the amount of drive space decomposed by the file system. The available disk partition for users in EC954 product is/dev/mmcblk0p8. Here is an example:

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/a94c5490bffe12c5.png)

##### **3.3.2.2.3 Query product model information** 

The devinfo tool can view product model information 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/e5a24dca80dbafe5.png)

##### **3.3.2.2.4 Adjusting Time** 

EC954 has two time settings. One is the system time, and the other is the RTC (Real Time Clock) time maintained by the hardware of EC954. Use the date command to query the current system time or set a new system time. Use the hwclock command to query the current RTC time or set a new RTC time.

Use the command date MMDDhhmmYYYY to set the system time: 

MM: Month 

DD: Day 

Hh: hour 

Mm: minutes 

YYYY: Year 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/cd64938d67906b6d.png)

The following command can be used to set the RTC time to system time

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/2c5406ff7bfc0516.png)

Click on the following link to obtain more detailed information about dates and times: 

[https://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html ](https://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html)

[https://wiki.debian.org/DateTime ](https://wiki.debian.org/DateTime)

##### **3.3.2.2.5 Setting Time Zone** 

There are two methods to configure the time zone of EC954. One is to use the command tzselect. Another option is to use the/etc/localtime file. 

##### **3.3.2.2.6 Using the tzselect command**

After typing the tzselect command, you will enter the region selection interface. First, select the approximate region (divided by continent or ocean) and enter the number in front of the continent or ocean 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/08b14d3cccd2743a.png)

Choose another country under that continent or ocean 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/0e1b65c1030a0600.png)

Follow the above steps to obtain the Chinese time zone keyword Asia/Shanghai, and execute the following command to set the time zone 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/55b899eef0579c1b.png)

##### **3.3.2.2.7 Using Localtime Files**

The local time zone is stored in/etc/localtime, and if no value is set for the TZ environment variable, it is used by the GNU library for C (glibc). This file is either a copy of/usr/share/zoneinfo/file, or a symbolic link pointing to it. If EC954 cannot find the/usr/share/zoneinfo/file, please download the time zone information file you need from the website（ [https://www.iana.org/time-zones ](https://www.iana.org/time-zones)）And re link to the local time file in EC900. 

**Take care**

After successfully downloading the required time zone information file, decompress it, and then use the zic command to compile and generate the corresponding binary file. The generated time zone file is "/usr/share/zoneinfo/custom time zone file name". 

# **4 Advanced configuration of 4 peripheral interfaces**

In this chapter, we will introduce the advanced configuration of the peripheral interface of the edge computer EC900 based on the Arm structure. 

## **4.1 Serial port** 

EC954 has 8 serial ports, and the first 4 ports support multiple serial port modes including RS-232, RS-422, and RS-485. The default mode is RS-485, and the ih_uard_ctl command can be used to switch the serial port mode. The last four serial ports are fixed in RS-485 mode. 

The device node corresponding to P1 is/dev/ttyCOM1 

The device node corresponding to P2 is/dev/ttyCOM2

The device node corresponding to P3 is/dev/ttyCOM3 

The device node corresponding to P4 is/dev/ttyCOM4 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/e58881f084af4089.png)

### **4.1.1 Changing Serial Port Settings** 

Viewing and Setting Serial Ports with the STTY Command 

View detailed command content by typing sudo stty -- help:

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/4ba1829dc86baa84.png)

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/9cbd168c59582db2.png)

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/55d88ec60104dd2e.png)

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/f2b6219de5244a37.png)

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/4a6b6856aa71b8a5.png)

### **4.1.2 Viewing Serial Port Information:** 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/2126aca5a9882e82.png)

### **4.1.3 Set the baud rate of the** **COM1** **serial port:** 

Sudo stty - F /dev/ttyCOM1 ispeed 9600 ospeed 9600 cs8 

### **4.1.4 Setting the Baud Rate of COM2 Serial Port**

Sudo stty - F /dev/ttyCOM1 ispeed 9600 ospeed 9600 cs8 

### **4.1.5 Setting the Baud Rate of COM3 Serial Port**

Sudo stty - F /dev/ttyCOM3 ispeed 9600 ospeed 9600 cs8 

### **4.1.6 Setting the Baud Rate of COM4 Serial Port**

Sudo stty - F /dev/ttyCOM4 ispeed 9600 ospeed 9600 cs8 

**Take care** 

Detailed information about the stty command can be found at the following link 

[http://www.gnu.org/software/coreutils/manual/coreutils.html](http://www.gnu.org/software/coreutils/manual/coreutils.html)

## **4.2 USB interface** 

EC954 provides two USB 2.0 Host interfaces, mainly used for expanding storage devices, connecting mice and keyboards 

EC954 supports hot swapping of USB storage devices. It will automatically mount all partitions. EC954 will partition all USB storage devices and mount them to the/mnt/path. The naming format for the mounting folder is usb1<node>_<num>. Among them,<node>is the device node name of the partition, and<num>can be a number from 0 to 9.

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/003fa8472809bc6c.png)

**Take care** 

Before disconnecting a USB mass storage device, remember to enter the sync synchronization command to prevent data loss. When you disconnect the storage device, please exit from the/media/* directory. If you stay in/media/USB *, the automatic uninstallation process will fail. If this situation occurs, please type umount/media/USB * to manually uninstall the device

## **4.3 Micro SD** 

EC954 supports micro SD storage cards but does not support hot swapping. It will automatically mount all partitions. EC954 will partition all micro SD storage cards and mount them to the/mnt/path. The naming format for the mounting folder is sd_<node>_<num>. Among them,<node>is the device node name of the partition, and<num>is a number from 0 to 9. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/4f1a15c3fc1e016a.png)

## **4.4 mSATA hard disk** 

(1) Log in to the system, execute sudo fdisk - l, and locate your hard disk partition, as shown in the following image:/dev/sda1 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/060344afd867fccb.png)

(2) Format the partition to the desired file system, such as ext4 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/927fe9aa60e27ce7.png)

(3) Create a mount point, such as/mnt/sda1

(4) Edit the vi/etc/fstab file,

Add/dev/sda1/mnt/sda1 ext4 defaults, nofail, x-system. device timeout=1s 0 0 at the end of the line, as shown in the following figure: 

/Dev/sda1: Device partition, user needs to configure according to actual situation

/Mnt/sda1: Mount point, user needs to configure according to actual situation 

The file system format of the etx4 hard disk partition needs to be configured by the user according to the actual situation 

Default, nofail, x-system. device timeout=1s 0 0 fixed configuration. It is recommended to use this configuration, and users can also modify it according to their needs.

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/f4142b95f5bf0544.png)

## **4.5 CAN bus interface** 

The CAN port of EC954 supports two CAN buses, with CAN1 corresponding to device can0 and CAN2 corresponding to device can1 

### **4.5.1 Configure Connection CAN1 Interface** 

By default, the CAN port will be initialized. If any other configuration is required, please use the IP link command to check the CAN device. To check the status of the CAN device, use the IP link command:

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/4c70c2e132ffb176.png)

To configure CAN devices, please use IP link set can0 down to first shut down the device 

Sudo IP link set can0 down 

Then configure the bit rate (the following is an example of a 125k bit rate):

Sudo IP link set can0 type can bitrate 125000 

Finally, restart the device 

Sudo IP link set can0 up 

### **4.5.2 Configure Connection CAN2 Interface**

By default, the CAN port will be initialized. If any other configuration is required, please use the IP link command to check the CAN device. To check the status of the CAN device, use the IP link command: 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/5a12f98392b53300.png)

To configure CAN devices, please use IP link set can1 down to first shut down the device

Sudo IP link set can1 down 

Then configure the bit rate (the following is an example of a 125k bit rate): 

IP link set can1 type can bitrate 125000 dbitrate 1250000 fd on 

Finally, restart the device

Sudo IP link set can1 up 

## **4.6 IO debugging** 

EC954 supports 4-way DI and 4-way DO. When you want to use the IO port, please type the dio_mgmt command to control the input and output of IO. Usage of dio_mgmt: 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/8095dba7b957259d.png)

When you need to set a certain IO port to high or low, you can type the command dio_mgmt set D<I/O><number><HIGH/LOW>

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/b06accdb461e9c8c.png)

Print the level information of the corresponding IO port by typing dio_mgmt show D<I/O><number>. 

## **4.7 GPS** 

Some EC900 models integrate GPS modules internally, and the data serial port nodes are/dev/ttyS9.

If you want to view detailed GPS information, there are two ways to view it:

1. Set up serial port nodes using STTY, type CAT to directly output source data

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/ec954img001.png)

2. Type the gnss command to directly output parsed information such as time, longitude, and latitude



![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/5fea815be162c691.png)

## **4.8 Power on/off button** 

### **4.8.1 Shutdown of equipment** 

1. Press and hold the power button for 8 seconds to turn off the device
2. You can use Linux commands to shut down all software running on the device and stop the system. However, after running this command, major components such as CPU, RAM, and storage devices will power down. 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/c660942439323c7b.png)

### **4.8.2 Starting the equipment** 

Short press the power on button, and the system will perform the power on operation. 

# **5 Security** 

In this chapter, we will introduce the security mechanism of the edge computer EC900 based on ARM architecture.

### **5.1 Sudo mechanism**

In EC900, for better security, root users are prohibited from using it. Sudo is a program that allows system administrators to allow approved users to execute commands as root or other users. The most basic principle is to give as little privilege as possible to complete the work. Using sudo is safer than opening a session with root identity for many reasons, including:

​     No need to know the root password (sudo will prompt the current user's password), ordinary user privileges can be granted 

​     It is easy to run commands that require privileges through sudo, and for the rest of the time, work as an unprivileged user to reduce the potential damage caused by incorrect operations.

​     Some system level commands cannot be directly used by users, as shown in the following example output: 

![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/a8a7dc5befbe07a6.png)

### **5.2 Firewall**

Netfileter/iptables (hereinafter referred to as iptables) is an excellent and completely free packet filtering firewall tool that comes with the Nuix/Linux system. Its functions are very powerful, and it is very flexible to use. It can finely control the inflow, outflow, and flow of data packets through the server. 

### **5.3 TPM2.0**

TPM stands for Trusted Platform Module, which is a hardware security module designed to provide security and encryption capabilities for computer systems. It is a security microcontroller that can be embedded in computer systems or sold as a standalone hardware device. It includes an encryption coprocessor for storing encryption keys, digital certificates, and other secure data, as well as supporting multiple encryption algorithms and security protocols. On EC954, the standard TPM2.0 protocol stack and TPM2.0 tools have been integrated for users to use.

# **6. System restoration to factory settings and updates** 

In this chapter, we will introduce how to restore the factory settings and update the edge computer EC900 based on the Arm structure. 

### **6.1 Restoring Factory Settings** 

There are two methods to restore factory settings: 

1. By typing a command, the system will automatically restart and restore factory settings.



![](https://media-hub.inhand.com/ai_edge_computers/EC954_EN/0773604bd0160851.png)

2. Restore factory settings through buttons: 

​     (1).Press and hold the factory reset button for 10-20 seconds, and you will see that the warning light is on for a long time. 

​     (2).After the warning light stays on, release the factory reset button. 

​     (3).After releasing the factory reset button, the error light flashes a few times before the system starts to restart and perform factory reset

​     (4).After the system restarts, the warning and error lights flash and the status goes out; After about 30 seconds, when both the warn and error lights stop flashing and the status starts flashing, the system will complete the factory reset. 

## **6.2 System Upgrade**  

Prepare a USB flash drive (micro SD card). If the USB drive (SD card) has multiple partitions, please use the first partition. It is recommended not to create multiple partitions. The partition of the USB drive (SD card) needs to be in FAT32 format. This document takes upgrading EC954-V2.0.0.img as an example for explanation.

​     (1).Create an empty ec900_img directory in the root directory of the USB drive (SD card), and place the EC954-V2.0.0.img file and md5.txt file published by inhand in the ec900_img directory. 

​     (2).Confirm that there is only the MD5 hash value in the EC954-V2.0.0.img line in the md5.txt file. EC954 does not support OTA upgrades for multiple IMG images.

​     (3).Exit the USB drive (SD card) normally on the computer. Be careful not to directly remove the USB drive, and choose the "Exit" or "Eject" operation on the desktop. 

​     (4).Insert the USB flash drive (SD card) into the target EC900 device. The target device will automatically verify the EC954-V2.0.0.img file and perform an OTA upgrade. During the upgrade process, the WARN and ERROR lights will be displayed accordingly. After WARN and ERROR return to normal, the upgrade operation will be completed. Due to the large size of the img file and the long upgrade time, please be patient and wait.

​     (5).After the upgrade is completed, EC900 will write the key information during the upgrade to the log file in the ec900_img directory. Please review the relevant documents. 

# **7 Programming Guide**  

EC900 provides a JSON format device information description file. Customers who need to operate peripherals such as IO, LED, serial port, etc. can obtain the device node information of these peripherals by querying the device description information file.

Device description information file path:/tmp/ieos/etc/systeminfo.json, the content is as follows:

```json
{
   "device_info":{
       "model_info":{
           "model":"EC954",
           "pn":"IO-FQ58",
           "sn":"EC9540000011111",
           "oem":"inhand",
           "features":";io;cell-FQ58;wlan;ble;gps;"
       },
       "software_info":{
           "boot_loader":"1.0.2",
           "kernel":"5.10.160-00001-g406d1811beab-dirty",
           "version":"V2.0.0-beta.1",
           "OS":"Debian GNU/Linux 11 (bullseye)"
       },
       "hardware_info":{
           "arch":"arm64",
           "soc":"rk3568",
           "interface":{
               "eth":[
                   {
                       "iface_name":"eth1",
                       "iface_mac":"00:33:44:11:00:01"
                   },
                   {
                       "iface_name":"eth2",
                       "iface_mac":"00:33:44:11:00:02"
                   },
                   {
                       "iface_name":"eth3",
                       "iface_mac":"00:33:44:11:00:03"
                   },
                   {
                       "iface_name":"eth4",
                       "iface_mac":"00:33:44:11:00:04"
                   }
               ],
               "wlan":[
                   {
                       "iface_name":"wlan0",
                       "iface_mac":"94:A4:08:8A:30:CD"
                   },
                   {
                       "iface_name":"wlan1",
                       "iface_mac":"96:A4:08:8A:30:CD"
                   }
               ],
               "ble":[
               ]
           },
           "gpio":[
               {
                   "gpio_name":"cellular_power",
                   "dev_node":"/sys/class/gpio/gpio0"
               },
               {
                   "gpio_name":"sim_switch",
                   "dev_node":"/sys/class/gpio/gpio19"
               },
               {
                   "gpio_name":"msata_power",
                   "dev_node":"/sys/class/gpio/gpio20"
               },
               {
                   "gpio_name":"gnss_power",
                   "dev_node":"/sys/class/gpio/gpio110"
               },
               {
                   "gpio_name":"ble_power",
                   "dev_node":"/sys/class/gpio/gpio220"
               }
           ],
           "user_key":[
               {
                   "user_key_name":"USER",
                   "dev_node":"/sys/class/gpio/gpio95"
               }
           ],
           "uart":[
               {
                   "uart_name":"P1",
                   "dev_node":"/dev/ttyO1"
               },
               {
                   "uart_name":"P2",
                   "dev_node":"/dev/ttyO2"
               },
               {
                   "uart_name":"P3",
                   "dev_node":"/dev/ttyO3"
               },
               {
                   "uart_name":"P4",
                   "dev_node":"/dev/ttyO4"
               },
               {
                   "uart_name":"P5",
                   "dev_node":"/dev/ttyO5"
               },
               {
                   "uart_name":"P6",
                   "dev_node":"/dev/ttyO6"
               },
               {
                   "uart_name":"P7",
                   "dev_node":"/dev/ttyO7"
               },
               {
                   "uart_name":"P7",
                   "dev_node":"/dev/ttyO8"
               }
           ],
           "io":{
               "di":[
                   {
                       "di_name":"DI1",
                       "dev_node":"/sys/class/gpio/gpio487"
                   },
                   {
                       "di_name":"DI2",
                       "dev_node":"/sys/class/gpio/gpio488"
                   },
                   {
                       "di_name":"DI3",
                       "dev_node":"/sys/class/gpio/gpio489"
                   },
                   {
                       "di_name":"DI4",
                       "dev_node":"/sys/class/gpio/gpio490"
                   }
               ],
               "do":[
                   {
                       "di_name":"DO1",
                       "dev_node":"/sys/class/gpio/gpio491"
                   },
                   {
                       "di_name":"DO2",
                       "dev_node":"/sys/class/gpio/gpio492"
                   },
                   {
                       "di_name":"DO3",
                       "dev_node":"/sys/class/gpio/gpio493"
                   },
                   {
                       "di_name":"DO4",
                       "dev_node":"/sys/class/gpio/gpio494"
                   }
               ]
           },
           "led":[
               {
                   "led_name":"USER1",
                   "dev_node":"/sys/class/leds/user1"
               },
               {
                   "led_name":"USER2",
                   "dev_node":"/sys/class/leds/user2"
               },
               {
                   "led_name":"4G/5G",
                   "dev_node":"/sys/class/leds/cell"
               },
               {
                   "led_name":"SIM1",
                   "dev_node":"/sys/class/leds/sim1"
               },
               {
                   "led_name":"SIM2",
                   "dev_node":"/sys/class/leds/sim2"
               },
               {
                   "led_name":"WARN",
                   "dev_node":"/sys/class/leds/warn"
               },
               {
                   "led_name":"ERROR",
                   "dev_node":"/sys/class/leds/error"
               },
               {
                   "led_name":"STATUS",
                   "dev_node":"/sys/class/leds/status"
               },
               {
                   "led_name":"L1",
                   "dev_node":"/sys/class/leds/level1"
               },
               {
                   "led_name":"L2",
                   "dev_node":"/sys/class/leds/level2"
               },
               {
                   "led_name":"L3",
                   "dev_node":"/sys/class/leds/level3"
               }
           ]
       }
   }
}

```

## **7.1 IO Programming Guide** 

At present, there are a total of 8 IO interfaces on the device: for example, DI0~DI3 on the device panel have 4 input pins; DO0~DO3 have 4 output pins. 

According to the device description information file/tmp/ieos/etc/systeminfo.json, the IO device nodes can be obtained as follows:

DI0~DI3-- **sys/class/gpio/gpio487~sys/class/gpio/gpio490** 

DO0~DO3-- **sys/class/gpio/gpio491~sys/class/gpio/gpio494** 

When you need to program IO interfaces, simply operate on the value value value under the backend device node (**sys/class/gpio/gpioxxx/value**)

**Case:** 

When DO0 needs to output high voltage, it can directly **write 1** to **sys/class/gpio/gpio491/value** 

```shell
echo 1>/sys/class/gpio/gpio491/value
```

When you need to check the level of DI0, you can also directly check the value of **sys/class/gpio/gpio487/value** 

```shell
cat/sys/class/gpio/gpio487/value 
```

Complete shell script:
```shell

\#!/bin/bash

gpio491="/sys/class/gpio/gpio491/value"
gpio492="/sys/class/gpio/gpio492/value"
gpio493="/sys/class/gpio/gpio493/value"
gpio492="/sys/class/gpio/gpio494/value"
\# To output a high level on DO0, you can directly write a '1' to sys/class/gpio/gpio491/value.
if [ -f "$gpio491" ]; then
  echo 1 > /sys/class/gpio/gpio491/value
else
  echo "no file exit "$gpio491
fi

\# To output a low level on DO1, you should write '0' to sys/class/gpio/gpio491/value.
if [ -f "$gpio492" ]; then
  echo 0 > $gpio492
else
  echo "no file exit "$gpio492
fi

gpio487="/sys/class/gpio/gpio487/value"
gpio488="/sys/class/gpio/gpio488/value"
gpio489="/sys/class/gpio/gpio489/value"
gpio490="/sys/class/gpio/gpio490/value"
\# To check the level of DI0, you can also directly view the value of `sys/class/gpio/gpio487/value`.
if [ -f "$gpio487" ]; then
  cat $gpio487
else
  echo "no file exit "$gpio487
fi
```

## **7.2 Led Programming Guide** 

On the device, users can use two lights, USER1 and USER2, for status prompts. Please check the light label to confirm the positions of USER1 and USER2 lights.

According to the device description information file/tmp/ieos/etc/systeminfo.json, it can be obtained that the USER1 and USER2 device nodes are: 

User1:/sys/class/LEDs/user1 

User2:/sys/class/LEDs/user2

There are some control files in the sys/class/leds/user1 directory used to control the properties and status of LEDs: 

/Sys/class/leds/user1/brightness: This file is used to control whether the USER1 light is on or off. Writing 1 means it is always on, and writing 0 means it is always off. 

/Sys/class/leds/user1/trigger: The trigger for the LED light, which can be written as timer to indicate the timer is triggered, and written as none to indicate the cancellation of the trigger.

/Sys/class/leds/user1/delay_on: This file represents the time when the LED light is on, in milliseconds. 

/Sys/class/leds/user1/delayed off: This file represents the time when the LED light went out, in milliseconds. 

If the trigger is configured for timed triggering, the value in brightness will no longer take effect and will automatically become 0.

Replacing user1 with user2 in the file path controls the operation of the USER2 light. 

**case:**

When the USER1 light needs to stay on, write 1 to the brightness file 

```shell
echo 1 > /sys/class/leds/user1/brightness
```

When the USER1 light needs to flash, write the timer to the trigger file and control the on and off times through delay_on and delay_off

```shell
\# Start Timer
echo timer > /sys/class/leds/user1/trigger

\# Light for 1 second
echo 1000 > /sys/class/leds/user1/delay_on

\# Off for 1 second
echo 1000 > /sys/class/leds/user1/delay_off
```



Complete shell script:

```shell
\#!/bin/bash

USER1_BRIGTHNESS="/sys/class/leds/user1/brightness"
USER1_TRIGGER="/sys/class/leds/user1/trigger"
USER1_DELAY_ON="/sys/class/leds/user1/delay_on"
USER1_DELAY_OFF="/sys/class/leds/user1/delay_off"

USER2_BRIGTHNESS="/sys/class/leds/user2/brightness"
USER2_TRIGGER="/sys/class/leds/user2/trigger"
USER2_DELAY_ON="/sys/class/leds/user2/delay_on"
USER2_DELAY_OFF="/sys/class/leds/user2/delay_off"


\# Light Up USER1 LED
if [ -f "$USER1_BRIGTHNESS" ]; then
  echo 1 > $USER1_BRIGTHNESS
else
  echo "no file exit "$USER1_BRIGTHNESS
fi

\# Light Up USER2 LED
if [ -f "$USER2_BRIGTHNESS" ]; then
  echo 1 > $USER2_BRIGTHNESS
else
  echo "no file exit "$USER2_BRIGTHNESS
fi

\# Set USER1 LED to Blink
if [ -f "$USER1_TRIGGER" ]; then
  echo timer > $USER1_TRIGGER
else
  echo "no file exit "$USER1_TRIGGER
fi

\# Set USER2 LED to Blink
if [ -f "$USER2_TRIGGER" ]; then
  echo timer > $USER2_TRIGGER
else
  echo "no file exit "$USER2_TRIGGER
fi

\# Set USER1 LED to Illuminate for 1000ms
if [ -f "$USER1_DELAY_ON" ]; then
  echo 1000 > $USER1_DELAY_ON
else
  echo "no file exit "$USER1_DELAY_ON
fi

\# Set USER1 LED to Turn Off for 1000ms
if [ -f "$USER1_DELAY_OFF" ]; then
  echo 1000 > $USER1_DELAY_OFF
else
  echo "no file exit "$USER1_DELAY_OFF
fi

\# Set USER2 LED to Illuminate for 1000ms
if [ -f "$USER2_DELAY_ON" ]; then
  echo 1000 > $USER2_DELAY_ON
else
  echo "no file exit "$USER2_DELAY_ON
fi

\# Set USER2 LED to Turn Off for 1000ms
if [ -f "$USER2_DELAY_OFF" ]; then
  echo 1000 > $USER2_DELAY_OFF
else
  echo "no file exit "$USER2_DELAY_OFF
fi

\# Disable USER1 LED Blinking
if [ -f "$USER1_TRIGGER" ]; then
  echo none > $USER1_TRIGGER
else
  echo "no file exit "$USER1_TRIGGER
fi

\# 关Disable USER2 LED Blinking
if [ -f "$USER2_TRIGGER" ]; then
  echo none > $USER2_TRIGGER
else
  echo "no file exit "$USER2_TRIGGER
fi
```


## **7.3 Cross compilation** 

The user's own C/C++program can be cross compiled using a cross compilation toolchain on the development machine, and then the target file can be uploaded to the EC954 device for execution. 

Cross compilation tool compressed package: gcc-linaro-6.3.1-2017.05-x86_64-arch64 Linux gnu.tar.gz 

Method for configuring environment variables for cross compilation toolchain:

​     1.Unzip gcc-linaro 6.3.1-2017.05-x86_64-arch64 Linux gnu. tar. gz to/opt path on the development machine (you can also unzip to other paths, make corresponding adjustments when setting the PATH environment variable in step 2) 
​     2.Edit the~/. bashrc file and add a line at the end of the file with PATH=$PATH:/opt/gcc linaro 6.3.1-2017.05-x86_64-arch64 Linux gnu/bin
​     3.Execute source~/. bashrc to make the environment variables effective on the current terminal; The newly opened terminal will automatically take effect. 

Using the classic Hello World program as an example, create the following directory and files

```shell
mkdir ~/example
touch ~/example/hello.c
touch ~/example/Makefile
```

~/The content of the example/hello. c file is as follows:

```C
\#include <stdio.h>

int main(void)
{
    printf("hello, world!\n");
    return 0;
}
```

~/The content of the example/Makefile file is as follows:

```Makefile
\# Define Target Filename and Source Filename
TARGET := hellworld
DIRS  := $(shell find . -maxdepth 3 -type d)
SRCS  := $(foreach dir,$(DIRS),$(wildcard $(dir)/*.c))
OBJS  := $(SRCS:.c=.o)


CC=aarch64-linux-gnu-gcc

\# Define Compiler and Compilation Options
CFLAGS := -Wall -Wextra -g -Wno-unused-parameter

\# Specify Default Target
all: $(TARGET)

\# Declare Dependencies of Target Files and Compilation Commands
$(TARGET): $(OBJS)
    $(CC) $(CFLAGS) $(LIBS) $^ -o $@

\# Formulate the Command to Compile Source Files into Target Files
%.o: %.c
    $(CC) $(CFLAGS) $(LIBS) -c $< -o $@

\# Establish the Command to Remove Temporary Files
clean:
    rm -f $(TARGET) $(OBJS)

\# Declare Pseudo-Target ".PHONY"
.PHONY: all clean
```

Execute make in the~/example directory to generate the target file helloworld