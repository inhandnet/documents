# EC312 Quick Start Guide_V1.0

**Edge computer EC300 series**

**Quick** **Start Guide**

Version 1.0 January 2026

[www.inhand.com](http://www.inhand.com/)

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467617878-1430d413-b74d-4a3d-a8ee-4b19b707a331-167522.png)

The software described in this manual is provided under a license agreement and can only be used in accordance with the terms of that agreement.

**Copyright Statement**

© 2024 InHand Network reserves all rights.

**Trademark**

The InHand logo is a registered trademark of InHand Network.

All other trademarks or registered trademarks in this manual belong to their respective manufacturers.

**Disclaimers**

Our company reserves the right to make changes to this manual, and any subsequent changes to the product will not be notified separately. We are not responsible for any direct, indirect, intentional or unintentional damage or hidden dangers caused by improper installation or use.

## **1 Product Introduction**

EC312-LoRaWAN series edge computers are designed for users who develop lightweight edge applications. It has rich interfaces and can expand various functions such as serial port, CAN, analog input, etc. Built in Linux system, providing long-term support to meet industrial automation needs. Support security features such as Secure Boot and TPM2.0 to ensure software and data security. Built in InHand DeviceSupervisor™ Agent services enable easy data collection, processing, and cloud deployment, supporting DeviceLive cloud management.

## **2 Packing list**

| **Number** | **Name** | **Quantity** | **Remarks** |
| :---: | --- | :---: | --- |
| 1 | EC312-LoRaWAN Host | 1 | — |
| 2 | Power Adapter | 1 | Optional Equipment |
| 3 | Wi-Fi Antenna | 1 | Standard Equipment (Depending on the device model) |
| 4 | GPS Antenna | 1 | Standard Equipment (Depending on the device model) |
| 5 | Cellular Antenna | 1 | Standard Equipment (Depending on the device model) |
| 6 | LoRa Antenna | 1 | Standard Equipment (Depending on the device model) |
| 7 | Card Needle | 1 | — |
| 8 | Warranty Card | 1 | — |

## **3 Product Appearance**

The panel layout of EC312-LoRaWAN is as follows:

### **3.1 Front panel**

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467619488-7bcbbf56-e74d-483a-85c6-875c80d4d6c5-239743.png)

### **3.2 Left panel**

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467624890-3588e90b-f042-4788-a17e-e08e2d953b0c-509049.png)

### **3.3 Right panel**

![1768468138132-0e30e04d-870c-4a06-9192-a502b8958c2c.png](./img/ijvHaNEw-bCla3cX/1768468138132-0e30e04d-870c-4a06-9192-a502b8958c2c-343995.png)

## 4 Description of indicator lights

| **Signage** | **Name** | **Definition** |
| --- | --- | --- |
| PWR | Power indicator | Power on and always on |
| STATUS | System operating status indicator light | When the system starts normally, the STATUS flashes. If the system fails to start due to an exception in the system startup phase, or when the factory recovery operation has not been completed, STATUS is solid off. |
| WARN | Warning indicator light | When the system has a warning abnormality, the WARN light flashes. Warning abnormalities include: the factory reset has not been completed; and the dialing abnormality (the cellular function needs to be turned on). |
| NET | Cellular connection status indicator | Keep on after successful dialing |
| User1 | User programmable indicator LED 1 | It is off by default and can be controlled by user programming |
| User2 | User programmable indicator LED 2 | It is off by default and can be controlled by user programming |
| User3 | User programmable indicator LED 3 | It is off by default and can be controlled by user programming |
| User4 | User programmable indicator LED 4 | It is off by default and can be controlled by user programming |

## **5. Install EC312-LoRaWAN**

### **5.1 DIN rail installation**

The installation plate of the DIN rail is attached to the EC312-LoRaWAN rear panel (fixed with M3 × 6MM screws). The installation steps are as follows:

1. Clip the upper hook of the DIN rail installation plate into the top of the DIN rail bracket
2. Slowly push the device forward towards the DIN rail bracket to ensure that the bottom end of the DIN rail clicks into place

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467770322-72f509cb-ce8e-49e4-a5c7-c27f86db2c3f-164089.png)

### **5.2 Wall mounted installation**

EC312-LoRaWAN can be installed using a wall mounted kit, which needs to be purchased separately. Follow the steps below to install

Step 1: Use screws (M3 × 4mm) to secure the wall mounting kit to the back panel of EC312-LoRaWAN

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467764300-e56bd05b-23e9-41d9-86c4-ef581cafb2a3-344458.png)

Step 2: After the wall mounted kit is successfully fixed to EC312-LoRaWAN, use an additional 4 M8 and 2 M3 screws to secure EC312-LoRaWAN to the wall or cabinet

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467766576-cd8c41a4-07a1-493f-843d-aa9ed4bff53e-202712.png)

## **6 Connector Description**

### **6.1 Ethernet interface**

EC300 has 2 RJ45 Ethernet ports and supports 10M/100M adaptive speed. The pin description of RJ45 is as follows:

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467765556-f28c9d5a-7534-4d6d-827d-75df77aec373-079211.png)

**10/100Mbps**

| **Pin** | **Description** |
| --- | --- |
| 1 | TX+ |
| 2 | TX- |
| 3 | RX+ |
| 4 | — |
| 5 | — |
| 6 | RX- |
| 7 | — |
| 8 | — |

### **6.2 Serial port**

EC300 supports up to four serial ports: two standard serial ports and two expandable serial ports.

**Standard serial port:**

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467767755-5aeda55e-b2f3-41db-ad78-ebefb2c9021f-335603.png)

COM1 (standard): RS-232/RS-485 (RX1 TX1/A1 B1), at the same time, you can only choose to connect to RS-232 or RS-485, they cannot be connected to work at the same time.

COM2 (standard): RS-485 (A2 B2)

| **Pin** | **COM1** | **COM2** |  |
| --- | --- | --- | --- |
|  | **RS-232** | **RS-485** | **RS485** |
| A1 | — | A+ | — |
| B1 | — | B- | — |
| RX1 | RX | — | — |
| TX1 | TX | — | — |
| GND | GND | GND | — |
| A2 | — | — | A+ |
| B2 | — | — | B- |
| GND | — | — | GND |

### **6.2 USB interface**

EC300 provides a USB 2.0 Host interface, mainly used for expanding storage devices. Supports hot swapping of USB storage devices.

**Attention:**

**Before disconnecting a USB** **mass storage device, remember to enter the sync** **synchronization command to prevent data loss.** **When you disconnect the storage device, please exit from the mounting directory.**

### **6.3 User programmable button**

EC300 provides an API interface, which users can call to detect the status of programmable buttons and then implement their own button logic.

### **6.4 DC Input**

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467787114-f77489f4-1a67-4494-b217-5817fa8fa878-315180.jpeg)

EC312-LoRaWAN supports 9-48V DC power supply. Insert the adapter terminal into the DC port of EC312-LoRaWAN and connect the power adapter. When the PWR power indicator light remains on, it indicates that the device has been powered on normally.

### **6.5 SIM card**

EC312-LoRaWAN is equipped with a SIM card holder for cellular communication, located below the left panel. Supports 2 NANO SIM cards. The installation steps are as follows:

Step 1: The SIM card of EC312-LoRaWAN needs to be installed in the event of a power outage. Please ensure that the device power has been disconnected before installation

Step 2: Before installation, the SIM card holder needs to be removed using a card reader (included in the factory)

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467787362-d5d3b63a-c11d-48a8-b1c2-7d31c3001138-347186.png)

Step 3: Insert the NANO SIM card, which has two card slots located above and below the drawer style card holder

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467792524-48f0cf4a-3310-42e9-852c-284b8d6b7f2b-084314.png)

### **6.6 MicroSD card**

EC312-LoRaWAN is equipped with an SD card slot for extended storage, located below the front panel. Before use, please open the protective cover and insert the SD card into the SD card slot.

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467797048-0aabda16-5c80-4760-bfa8-39ca912d4fdb-367924.png) ![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467788598-6a5d75a9-9733-4185-baa1-e92cbd851e20-601480.png)

### **6.7 Antenna interface**

The EC300 has five antenna interfaces in total, and the number of standard antennas for different models is different. See the "Ordering Information" section of the EC312-LoRaWAN Series Edge Computer Product Specification for the antenna support for specific models.

| **Identification** | **Name** |
| --- | --- |
| ANT1 | 4G LTE main antenna/5G antenna |
| ANT2 | 4G LTE diversity receive antenna/5G antenna |
| GPS | GPS antenna |
| Wi-Fi | Wi-Fi antenna |
| LoRa | LoRa antenna |

The product model shown below is EC312-H-LQA3-L470, which only supports one 4G antenna interface. Screw the antenna into the corresponding SMA antenna interface to complete the antenna installation.

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467793585-63739e3b-f9ff-484f-af6d-437d4ad72de1-537198.jpeg)

## **7 Power and Environmental requirements**

| **Input voltage** | 9-48 VDC (dual pin terminals, V+, V -) |
| --- | --- |
| **Power consumption** | 6W |
| **Working temperature** | -20-70℃（-4°F-158°F） |
| **Storage temperature** | -40-85℃（-40°F-185°F） |
| **Environmental humidity** | 5-95% (without frost) |

## **8 Accessing EC312-LoRaWAN**

Connect to EC300 using the following default IP address.

| **Port** | **Default** **IP** |
| --- | --- |
| ETH 1 | 192.168.3.100/24 |
| ETH 2 | 192.168.4.100/24 |

**Step** **1:** **Interconnect** **PC** **and** **EC312-LoRaWAN**

As shown in the following figure, plug one end of the network cable into the ethernet port of EC312-LoRaWAN, insert the example in the figure into port 2, and plug the other end into the network port of the computer. At the same time, set the IP address of the computer to the same network segment address as the device interface

![DocsDisplay](./img/ijvHaNEw-bCla3cX/1768467822808-d503ff2c-a258-40e8-8e38-decd8bd93872-370256.png)

**Step 2:** **Manage** **EC312-LoRaWAN**

Method 1: Use native Linux commands for network and system management by
clicking on the link [http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html), download PuTTY (free software), and establish the connection with the edge computer EC312-LoRaWAN in the way of SSH command in the Windows environment. The default username for logging in is on the device's backplane

The following figure is an example of using SSH connection:

![edbsna808eee51598d7a69169d7e3c4d65465da884254b483a1e742b5c6c8c4a5d61affd1d145b017ba5b6a586feb9e585940](./img/ijvHaNEw-bCla3cX/1768467814418-f68147a9-edad-4ee8-9efa-476b9239b926-737788.png)

Method 2: Network and system management through WEB

EC312-LoRaWAN supports IEOS based web interface management. IEOS is a self-developed network management and system management program developed by InHand that runs on Linux systems. IEOS can provide web interface services

IEOS uses port 9100 as the HTTPS connection port and does not support access through HTTP; When users access the web using HTTP, they will automatically redirect to using HTTPS. This document takes the default address 192.168.4100 of eth2 as an example for explanation.

Login address: [https://192.168.4.100:9100](https://192.168.4.100:9100/)

Initial login account: adm

Initial login password: 123456

The following figure is an example of using a web connection:

![edbsnc636c935db541dec027a976fd0a6baff658c85ecd37fbaa838ff37d0576de14ec35a0275f0294bdcddb654c6f4ff0cfd](./img/ijvHaNEw-bCla3cX/1768467813626-028f0958-a7c4-40bb-a9c5-0ba512a8387f-425616.png)

**Remark :  
Not allEC312-LoRaWANmodels support the WEBinterface management function. For specific support, see the "Ordering Guide" section of theEC312-LoRaWAN Series Edge Computer_Prdt Spec.**

## **9 Accessing the built-in LNS**

1）Click [Network] -> [LoRaWAN], then click [Go to the Network Server manage page] on that page, as shown in the image below.

![1767938094675-e5f6f826-47f0-4ec3-987a-10b83269b962.png](./img/ijvHaNEw-bCla3cX/1767938094675-e5f6f826-47f0-4ec3-987a-10b83269b962-509502.png)

1) Log in with your username and password (admin/admin)

![1767165210807-bbc18a74-7b38-4f60-b770-794455dca59d.png](./img/ijvHaNEw-bCla3cX/1767165210807-bbc18a74-7b38-4f60-b770-794455dca59d-913988.png)

![1768301240911-98ca9528-6266-4ba8-be4d-1af4b2b8dd9d.png](./img/ijvHaNEw-bCla3cX/1768301240911-98ca9528-6266-4ba8-be4d-1af4b2b8dd9d-891713.png)
