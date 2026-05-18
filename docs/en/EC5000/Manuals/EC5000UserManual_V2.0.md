# EC5000 User Manual_V2.0

**EC5000 Series AI Edge Computer**

**User Manual**

Version 1.0, September 2024

[www.inhand.com](http://www.inhand.com)

![1725334179414-aa8a79b0-f4dc-4847-a1ee-a6768aeca285.png](./img/sHmqyKbSIhNYMmOI/1725334179414-aa8a79b0-f4dc-4847-a1ee-a6768aeca285-077331.png)

The software described in this manual is according to the license agreement, can only be used in accordance with the terms of the agreement.

**Copyright Notice**

© 2024 InHand Networks All rights reserved.

**Trademarks**

The InHand logo is a registered trademark of InHand Networks.

All other trademarks or registered trademarks in this manual belong to their respective manufacturers.

**Disclaimer**

The company reserves the right to change this manual, and the products are subject to subsequent changes without prior notice. 9. We shall not be responsible for any direct, indirect, intentional or unintentional damage or hidden trouble caused by improper installation or use.

## 1 General Introduction  

### 1.1 Introduction  

The EC5000 comes pre-integrated with NVIDIA® Jetson Orin NX™ or Orin Nano™, making it ideal for industrial AI applications.The EC5000 design includes 2 Gigabit LAN ports, 1 HDMI video display, 6 external USB 3.2 ports, 2xRS-232/RS- 422/RS-485, 1 power indicator, 1 system status light, 2 GMSL video interfaces, 4 DI, 4 DO, 1 CAN FD, 2 SIM card slots, 1 USB Type C for system burn-in, 1 TF card slot, 1 reboot (hardware watchdog enable) button, 1 restore mode button, and 1 linear output connector and microphone connector.

### 1.2 Product Features

### 1.2.1 Key Features

#### 1.2.1.1 Processor

| **Table 1： Processor** | | | |
| --- | --- | --- | --- |
|  | **On-Module memory** | **Orin NX** | **Orin Nano** |
| **CPU** | 4G | - | ARM Cortex-A78AE CPU (6 cores), (TDP up to 10 W, 1.5 GHz) |
| | 8G | ARM Cortex-A78AE CPU (6 cores), (TDP up to 20 W, 2 GHz) | ARM Cortex-A78AE CPU (6 cores), (TDP up to 15 W, 1.5 GHz) |
| | 16G | 16GB (ONX 16GB) - ARM Cortex-A78AE CPU (8 cores),(TDP up to 25 W, 2 GHz) | - |
| **GPU** | 4G | - | 512-core NVIDIA Ampere GPU with 16 <br/>Tensor Cores (Max frequency up to 625 MHz) |
| | 8G | 1024-core NVIDIA Ampere GPU with 32 Tensor Cores (Max frequency up to 765 MHz) | 1024-core NVIDIA Ampere GPU with 32 <br/>Tensor Cores (Max frequency up to 625 MHz) |
| | 16G | 1024-core NVIDIA Ampere GPU with 32 Tensor Cores (Max frequency up to <br/>918 MHz) | - |

#### 1.2.1.2 Ethernet  

2 x 10 / 100 / 1000 Mbps

#### 1.2.1.3  Peripheral & I/O

2 x RS-232/422/485 switchable serial interfaces with DB9 connectors

4 x DI, Optocoupler isolation, supporting dry and wet nodes.

4 x DO, Optocoupler isolation, supporting 60 VDC sink voltage, 1.3 A max sink current

2 x USB 3.2 with ≤15W drive capacity each

4 x USB 3.2 with ≤4.5W drive capacity each

1 x USB 2.0, Type-C for system restore only

1 x HDMI 2.0 with maximum resolution of 3840 x 2160 @60Hz

2 x SIM card slots, supporting 1.8/3V SIM/UIM cards, built-in 15KV ESD protection, uses standard SIM cards

7 x SMA antennas, 4 for cellular modules, 2 for Wi-Fi modules, 1 for GNSS

2 x LEDs, 1 for power indication, 1 for system status indication

1 x Micro-SD card slot for Micro-SD card expansion

1 x CAN FD up to 5Mbps

2 x flick switch buttons, 1 for reboot (enable/disable hardware watchdog), 1 for system restore

2 x GMSL 2.0 FAKRA connectors

1 x MIC, 3.5mm microphone audio jack

1 x Audio, 3.5mm line-out

#### 1.2.1.4 Internal System Interfaces

1 x Trusted Platform Module, TPM 2.0

1 x NVME SSD

1 x Wi-Fi, supporting Wi-Fi 5/6

1 x Cellular module with 4G/5G support

1 x RTC, powered by a button cell battery

### 1.3 Mechanical Specifications

**Standard Size:**180.0 x 160.0 x 60.0 mm

**Reference Weight:** 1.65 kg (excluding package and power adapter)

![1725344513241-fa9b5685-b4f2-4d2f-8150-621172a729de.png](./img/sHmqyKbSIhNYMmOI/1725344513241-fa9b5685-b4f2-4d2f-8150-621172a729de-800638.png)

### 1.4 Electrical Specifications  

**Power Type:** AT

**Power Input:** DC 9-36 V, 15-5.6 A

### 1.5  Environmental Specifications  

**Oprerating temperature:** -20 ~ 60°C

**Operating humidity:** 95%@40°C (non-condensing)

**Storage temperature:** -40 ~ 85°C

## 2. System Interface Information

### 2.1 System Interface Overview

![1725258538413-762983db-9fc2-4764-960a-931406c10ae7.png](./img/sHmqyKbSIhNYMmOI/1725258538413-762983db-9fc2-4764-960a-931406c10ae7-401751.png)

### 2.2 Interfaces

### 2.2.1. Power Indicator

The front panel is equipped with a power on/off indicator (red LED), which indicates the system power-on status. When the LED is on, it means the system is in the power-on state, and when the LED is off, it means the system is in the power-off state.

![1725261673648-2a789e6e-fd12-43cc-9bb3-ddfe99202e56.png](./img/sHmqyKbSIhNYMmOI/1725261673648-2a789e6e-fd12-43cc-9bb3-ddfe99202e56-499855.webp)

### 2.2.2 System Status LED

The front panel is equipped with a system status light (green LED), which indicates the system operation status. When the LED flashes (frequency 1Hz), it means that the system is operating normally, and the LED is off, which means that the system is not operating.

![1725262100917-abcb4cf6-c97e-45b4-99b1-ba842e898cca.png](./img/sHmqyKbSIhNYMmOI/1725262100917-abcb4cf6-c97e-45b4-99b1-ba842e898cca-024475.png)

### 2.2.3 Serial Port

The device provides 2 RS-232/422/485 serial ports, the function definition is described in the following table.

![1725263915562-cace9aaf-880e-4164-96a6-b0137f17edea.png](./img/sHmqyKbSIhNYMmOI/1725263915562-cace9aaf-880e-4164-96a6-b0137f17edea-397321.png)

| **Table 2：Serial Interface** | | | |
| --- | --- | --- | --- |
| **DB9-F** | **RS-232** | **RS-422** | **RS-485** |
| 1 | | | |
| 2 | RXD | RX+ | |
| 3 | TXD | TX- | Data- |
| 4 | | | |
| 5 | Ground | | |
| 6 | | | |
| 7 | | TX+ | Data+ |
| 8 | | RX- | |
| 9 | | | |

### 2.2.4 USB 3.2 Gen2

The device provides 2 USB3.2 Gen 2 with maximum power 15W and 4 USB3.2 Gen 2 with maximum power 4.5W. When multiple USBs are working at full load, please choose 12V (or above)/120W (or above) power adapter to use according to the total load.

![1725264899197-36869667-3bf4-4b7c-9f89-ad3f5f04083a.png](./img/sHmqyKbSIhNYMmOI/1725264899197-36869667-3bf4-4b7c-9f89-ad3f5f04083a-363632.png)

### 2.2.5 HDMI 2.0

The device provides a Type-A HDMI 2.0 connector on the front panel for external screens. The maximum resolution is 3840 x 2160 @60Hz.

![1725266486896-166b5cf2-d71a-400b-933a-9a2a9e0db80d.png](./img/sHmqyKbSIhNYMmOI/1725266486896-166b5cf2-d71a-400b-933a-9a2a9e0db80d-112258.png)

### 2.2.6  Ethernet(WAN/LAN)

The device provides two network interfaces on the front panel, each with two LEDs above it. The green LED indicates the network connection rate, the green LED lights up when the network is Link up at a rate of 1000Mbps, otherwise the green LED is off; the orange LED indicates the network communication situation, if there is a data communication when the network is Link up, the orange LED blinks, otherwise the orange LED is off.

![1725266655851-5803bf51-d8ea-4e5d-9a2f-b626af7c9042.png](./img/sHmqyKbSIhNYMmOI/1725266655851-5803bf51-d8ea-4e5d-9a2f-b626af7c9042-377323.png)

| **Table 3: Networks** | | |
| :--- | --- | --- |
| **Green LED** | | |
| OFF | ON | Blinking |
| 1. No connection<br/>2. Speed 10Mbps<br/>3. Speed 100Mbps | Speed 1000Mbps | - |
| **Orange LED** | | |
| OFF | ON | Blinking |
| 1. No connection<br/>2. No activity on this port | - | Activity on this port |

### 2.2.7 SMA

The front panel of the device provides up to seven SMA connectors. Different models are equipped with different types and numbers of 4G/5G/Wi-Fi/GNSS antennas. Users can select equipment according to their own needs. For the support status of antennas of specific models, please refer to the "Ordering Guide" section in the "EC5000 Series Edge AI Computer Product Specification".

![1725267135755-eb7ccff3-8c00-4cb6-abef-d6fc2979fd12.png](./img/sHmqyKbSIhNYMmOI/1725267135755-eb7ccff3-8c00-4cb6-abef-d6fc2979fd12-824034.png)

### 2.2.8 Grounding Connection  

There is 1 system grounding screw on the right panel of the equipment, please use a green-yellow grounding wire (16AWG) and ground it with the system grounding screw.

![1725267388567-cf29e192-f32b-4901-a005-89ac7aa25cd1.png](./img/sHmqyKbSIhNYMmOI/1725267388567-cf29e192-f32b-4901-a005-89ac7aa25cd1-866237.png)

### 2.2.9  DC-IN Connector  

When conducting DC connector wiring you should follow the below instructions:

1. Must be installed by a skilled person.
2. Use copper conductors only.
3. Choose appropriate wire diameter.
4. The voltage for the system is 9 VDC to 36 VDC.
5. The current for the system is 15 A to 5.6 A.

![1725267506238-aa3ad93e-404d-4e58-9f88-f59049c806d7.png](./img/sHmqyKbSIhNYMmOI/1725267506238-aa3ad93e-404d-4e58-9f88-f59049c806d7-335342.png)

### 2.2.10 Recovery Button

The device has a Recovery touch-switch button under the removable baffle on the right panel. When the system is running normally, press and hold Recovery for 10 seconds and wait for the system status light to change from blinking to always on and release it, the device will enter the system reset state (restoring the system to the factory state); press and hold the Recovery button and reboot the system(press Reset, reboot, or power-down reboot) before the system is powered on or during the system running, then the system will enter the burn-in mode.

![1725267937189-814a188e-42f2-44eb-afb7-9abb173c3908.png](./img/sHmqyKbSIhNYMmOI/1725267937189-814a188e-42f2-44eb-afb7-9abb173c3908-582826.png)

### 2.2.11 Reset Button

The device has a Recovery touch-switch button under the removable baffle on the right panel, press and hold Reset for 3 seconds and release it during normal system operation, then the system will reboot and enable the hardware watchdog; press and hold Reset for 3 seconds and then release it during normal system operation, then the system will reboot and disable the hardware watchdog, please disable the hardware watchdog before the system is burned in, to prevent the hardware watchdog from restarting the system and leading to the failure of the burn-in process.

![1725268762552-e4cb9422-4da9-41e1-992b-70d432283009.png](./img/sHmqyKbSIhNYMmOI/1725268762552-e4cb9422-4da9-41e1-992b-70d432283009-635803.png)

### 2.2.12 USB 2.0 Type-C

The equipment has a USB 2.0 Type-C connector under the emovable baffle on the right panel for connecting to a host burning system in burn-in mode.

![1725269208625-31718dad-50cf-43dc-89c4-fb10c5d8a15f.png](./img/sHmqyKbSIhNYMmOI/1725269208625-31718dad-50cf-43dc-89c4-fb10c5d8a15f-015520.png)

### 2.2.13 TF Card

The device has a TF card slot under the removable baffle on the right panel, which supports Micro SD memory cards. When there is a need for additional storage space, please insert a Micro SD card with a capacity of at least 8GB into this card slot for subsequent use.

![1725269366090-d52c2f86-9d3a-46e2-b54a-9ec8db45242f.png](./img/sHmqyKbSIhNYMmOI/1725269366090-d52c2f86-9d3a-46e2-b54a-9ec8db45242f-644663.png)

### 2.2.14 SIM Card Slot

The device has 2 SIM card slots (SIM1/SIM2) on the right panel to support standard SIM cards, please insert at least 1 available SIM when using the cellular function.

![1725269574191-f0d3420d-3cb8-4eec-8645-049dd2c3ad33.png](./img/sHmqyKbSIhNYMmOI/1725269574191-f0d3420d-3cb8-4eec-8645-049dd2c3ad33-265781.png)

### 2.2.15 CAN FD

The device has 1 CAN FD interface (on-board 120Ω resistor) on the right panel, supporting a maximum communication rate of 5Mbps.

![1725270217533-2736a53c-8e54-4a1c-ba01-2c7946544643.png](./img/sHmqyKbSIhNYMmOI/1725270217533-2736a53c-8e54-4a1c-ba01-2c7946544643-674972.png)

### 2.2.16 Digital Outputs

The device has four isolated digital output connectors on the right panel in open-drain output mode.

![1725270410679-8a9e96a5-6257-45e6-8213-eaff25766093.png](./img/sHmqyKbSIhNYMmOI/1725270410679-8a9e96a5-6257-45e6-8213-eaff25766093-877810.png)

The wiring method is as follows:

![1725334185802-eb686246-84e8-4693-9e62-c6863199bfa7.png](./img/sHmqyKbSIhNYMmOI/1725334185802-eb686246-84e8-4693-9e62-c6863199bfa7-750944.png)

| **Table 4: Isolated Digital Outputs** | |
| --- | --- |
| Number of Output Channels | 4 |
| Optical Isolation | 1414 VDC |
| Supply Voltage | Sink 60 VDC |
| Sink Current | 1.3 A max./Channel |

### 2.2.17 Digital Inputs

The device has four isolated digital inputs on the right panel that support wet and dry contacts.

![1725271256363-c99f61f4-4d83-4060-b643-9ef010b36afd.png](./img/sHmqyKbSIhNYMmOI/1725271256363-c99f61f4-4d83-4060-b643-9ef010b36afd-434445.png)

The wiring method is as follows:

![1725334186340-8c9ba95c-52d7-4c4d-9866-a9389180ec6c.png](./img/sHmqyKbSIhNYMmOI/1725334186340-8c9ba95c-52d7-4c4d-9866-a9389180ec6c-407196.png)

| **Table 5: Isolated Digital Inputs** | |
| :--- | --- |
| Number of Input Channels | 4 |
| Optical Isolation | 3750 VDC |
| Input Voltage | Dry contact.<br/>Logic 1: Open<br/>Logic 0: Close to ground  |
| | Wet contact.<br/>VIH(max.) = 60 VDC<br/>VIH(min.) = 5 VDC<br/>VIL(max.) = 2 VDC |

### 2.2.18 RS-485 Pull-up/down Dip Switches

The device has 1 RS-485 pull-up and pull-down dip switches on the right panel to control the pull-up and pull-down resistors of the RS-485 bus (corresponding to COM1/COM2).

![1725273032079-21a75e67-52c5-4099-b962-2b48bf2765de.png](./img/sHmqyKbSIhNYMmOI/1725273032079-21a75e67-52c5-4099-b962-2b48bf2765de-644020.png)

| **Table 6: RS-485 Pull-up/down** | |
| :--- | --- |
| PU | ON: Enable pull-up<br/>OFF: Disable pull-up |
| PD | ON: Enable pull-down<br/>OFF: Disable pull-down |
| T | ON: Enable termination matching resistor<br/>OFF: Disable termination matching resistor |

### 2.2.19 GMSL 2.0

The device has 2 GMSL 2.0 ports on the right panel, supporting docking of 2 GMSL cameras.

![1725273687602-6a012b97-5154-44bd-8594-7ac774f5ea78.png](./img/sHmqyKbSIhNYMmOI/1725273687602-6a012b97-5154-44bd-8594-7ac774f5ea78-133217.png)

### 2.2.20 Lineout

The device has 1 Line-out connector on the right panel, which supports 3.5mm standard audio output.

![1725273854344-70b7866a-bf14-46d6-b27a-aca13f7327f6.png](./img/sHmqyKbSIhNYMmOI/1725273854344-70b7866a-bf14-46d6-b27a-aca13f7327f6-095099.png)

### 2.2.21 Microphone

The device has 1 microphone connector on the right panel and supports 3.5mm standard audio input.

![1725273981849-a5234507-f50e-4d2a-9267-a80fb929a294.png](./img/sHmqyKbSIhNYMmOI/1725273981849-a5234507-f50e-4d2a-9267-a80fb929a294-841877.png)

## 3 Installation

### 3.1 Rail Mounting Installation

![1725275590454-0a44d85e-9697-432f-86ae-5778f0b7dd78.png](./img/sHmqyKbSIhNYMmOI/1725275590454-0a44d85e-9697-432f-86ae-5778f0b7dd78-722780.png)

### 3.2 Wall-mounted Installation

![1725275646904-570d7113-af2b-4281-bf67-07ad65cc1e8b.png](./img/sHmqyKbSIhNYMmOI/1725275646904-570d7113-af2b-4281-bf67-07ad65cc1e8b-293547.png)

## 4 Getting Started

### 4.1 Connecting to Equipment

### 4.1.1 Connecting Device via HDMI

#### 4.1.1.1 Connecting HDMI and Peripherals

Connect the device to the monitor via the HDMI 2.0 port, plug the keyboard and mouse into the USB 3.2 port of the device, power up the device and wait for the device to finish booting. Check the nameplate on the bottom of the device to find the default system username and password.

![1725413310081-4dca03f0-5901-4b67-843a-14ad0b088059.png](./img/sHmqyKbSIhNYMmOI/1725413310081-4dca03f0-5901-4b67-843a-14ad0b088059-197084.png)

#### 4.1.1.2 Logging Equipment

On the login screen, select the user that corresponds to System User, enter the password, and log in.

![1725342890143-ea95a961-841d-44fa-bedb-e79334972a9c.png](./img/sHmqyKbSIhNYMmOI/1725342890143-ea95a961-841d-44fa-bedb-e79334972a9c-377780.png)

![1725345211806-cdb5434f-d599-44c4-9bad-f8bba6bf6d96.png](./img/sHmqyKbSIhNYMmOI/1725345211806-cdb5434f-d599-44c4-9bad-f8bba6bf6d96-601945.png)

### 4.1.2 Connecting via SSH

#### 4.1.2.1 Connecting to the Network

Connecting to the device using SSH requires ensuring that the device network is accessible. Check the nameplate on the bottom of the device to find the system default Ethernet address and configure the host and device to be on the same network segment.

![1725427385386-44b243ed-d82d-4c71-878f-8c1354e545f1.png](./img/sHmqyKbSIhNYMmOI/1725427385386-44b243ed-d82d-4c71-878f-8c1354e545f1-820222.png)

#### 4.1.2.2 Access to Equipment

Open the SSH terminal tool (Mobaxterm for example), enter the device address and click Connect.

![1725345810237-fa8e7147-66de-4bfc-bebf-84577e99c6a9.png](./img/sHmqyKbSIhNYMmOI/1725345810237-fa8e7147-66de-4bfc-bebf-84577e99c6a9-829857.png)

Follow the prompts and enter the default user and password.

![1725427512036-06b2508d-df93-4bca-aed0-c6d9c4e46625.png](./img/sHmqyKbSIhNYMmOI/1725427512036-06b2508d-df93-4bca-aed0-c6d9c4e46625-732955.png)

![1725427636737-fd46dbfe-deb4-4aa2-a589-81165abdccba.png](./img/sHmqyKbSIhNYMmOI/1725427636737-fd46dbfe-deb4-4aa2-a589-81165abdccba-571619.png)

### 4.2 Version Query

Open Terminal on the desktop or right-click and select "Open in Terminal" and enter the following command.

Version Query：

```json
## Query version number only
sudo ecversion 
## Query detailed version information
sudo ecversion -all
```

![1725346276701-c66f489d-1d18-441f-ab17-4726d7f3afe2.png](./img/sHmqyKbSIhNYMmOI/1725346276701-c66f489d-1d18-441f-ab17-4726d7f3afe2-726820.png)

![1725427814108-fd48d524-1226-4984-a3fc-0e0ad52768a2.png](./img/sHmqyKbSIhNYMmOI/1725427814108-fd48d524-1226-4984-a3fc-0e0ad52768a2-594118.png)

### 4.3 User Management

### 4.3.1 Creating Users

Open the desktop Terminal or right-click and select "Open in Terminal", and enter the following commands, according to the prompts to enter the password and user information, before creating the user, please make sure that the user exists, for the user that already exists, to create again will be prompted by The user 'username' already exists.

```json
## check if the test user exists 
id test 
## create test user
sudo adduser test
```

![1725362223173-5c9134a9-319d-4926-80b4-23538cfbef31.png](./img/sHmqyKbSIhNYMmOI/1725362223173-5c9134a9-319d-4926-80b4-23538cfbef31-232784.png)

### 4.3.2 Delete Users

Open the desktop Terminal or right-click and click "Open in Terminal", and enter the following command to delete the user, before deleting the user, please make sure the user exists, if you delete the user does not exist will prompt The user 'username' does not exist.

```json
## Check if the test user exists 
id test 
## Delete the test user
sudo deluser test
```

![1725438456220-31f9a143-d551-4190-b13f-b1a6adeff534.png](./img/sHmqyKbSIhNYMmOI/1725438456220-31f9a143-d551-4190-b13f-b1a6adeff534-584328.png)

### 4.3.3 Disable and Enable Users

Open the desktop Terminal or right-click and click "Open in Terminal", and enter the following command to disable/enable the user, disable/enable the user before please make sure that the user exists, if the user does not exist, it will be prompted The user 'username' does not exist.

```json
## Check if the test user exists 
id test 
## Disable the test user
sudo passwd -l test 
## Enable test user
sudo passwd -u test 
## Query the status of the test user (L disabled/P enabled)
sudo passwd -S test
```

![1725438533754-8c10146b-6ec4-409b-9970-0b3bbd42ae54.png](./img/sHmqyKbSIhNYMmOI/1725438533754-8c10146b-6ec4-409b-9970-0b3bbd42ae54-467285.png)

### 4.3.4 Advanced Extension of User Management

Reference:

1. [Ubuntu Manpage: adduser, addgroup - add a user or group to the system](https://manpages.ubuntu.com/manpages/xenial/en/man8/adduser.8.html?_gl=1*1jz4dhl*_gcl_au*MTkwNTc0MDUwMC4xNzI1MzQ3ODI1&_ga=2.97338463.1940871822.1725347824-1111823313.1715413709)
2. [Ubuntu Manpage: deluser, delgroup - remove a user or group from the system](https://manpages.ubuntu.com/manpages/focal/en/man8/deluser.8.html?_gl=1*2hnawf*_gcl_au*MTkwNTc0MDUwMC4xNzI1MzQ3ODI1&_ga=2.165044991.1940871822.1725347824-1111823313.1715413709)
3. [Ubuntu Manpage: passwd - change user password](https://manpages.ubuntu.com/manpages/bionic/man1/passwd.1.html?_gl=1*1rjws9d*_gcl_au*MTkwNTc0MDUwMC4xNzI1MzQ3ODI1&_ga=2.211133397.1940871822.1725347824-1111823313.1715413709)
4. [Ubuntu Manpage: usermod - modify a user account](https://manpages.ubuntu.com/manpages/trusty/en/man8/usermod.8.html?_gl=1*2hnawf*_gcl_au*MTkwNTc0MDUwMC4xNzI1MzQ3ODI1&_ga=2.165044991.1940871822.1725347824-1111823313.1715413709)

### 4.4 Network Settings

### 4.4.1 Ethernet Settings

#### 4.4.1.1 Settings Management

Click the network icon on the top right corner of the desktop, select Ethernet ->Wired Settings or click Show Applications->Settings->Network->Ethernet on the bottom left corner of the desktop, please choose to set eth1/eth2 according to the actual situation.

![1725428529882-ce3a4a69-02ac-470b-98a1-792ccd7d9b1d.png](./img/sHmqyKbSIhNYMmOI/1725428529882-ce3a4a69-02ac-470b-98a1-792ccd7d9b1d-377919.png)

![1725428623356-31c21d24-590c-40b1-a285-058f183b6192.png](./img/sHmqyKbSIhNYMmOI/1725428623356-31c21d24-590c-40b1-a285-058f183b6192-707823.png)

#### 4.4.1.2 On/Off Management

Click Turn On/Turn Off or slide the button in the Ethernet settings to turn the network off or on.

![1725429121289-de5e07e1-d3c3-4b00-8ca1-7b175c23f843.png](./img/sHmqyKbSIhNYMmOI/1725429121289-de5e07e1-d3c3-4b00-8ca1-7b175c23f843-765005.png)

![1725428659620-9b17ac18-b86c-49b8-8cd5-148ef3a50696.png](./img/sHmqyKbSIhNYMmOI/1725428659620-9b17ac18-b86c-49b8-8cd5-148ef3a50696-565116.png)

#### 4.4.1.3 Static Configuration

Click Setup button, select IPv4/IPv6, select Manual for Method, fill in Address, Netmask, Gateway, DNS and Routes according to the network conditions, and click Apply to save. Click Apply to save. After saving, please re-switch the network to make the configuration take effect.

![1725428761352-f159cf0b-1407-4e02-8387-929bc29e2e26.png](./img/sHmqyKbSIhNYMmOI/1725428761352-f159cf0b-1407-4e02-8387-929bc29e2e26-865215.png)

#### 4.4.1.4. Dynamic Configuration

Click the Setup button, select IPv4/IPv6, select Automaitc(DHCP) for Method, and click Apply to save. After saving, please re-switch the network to make the configuration take effect.

![1725428880104-4f0c7741-4c20-4b86-ae0a-20bb5c04a926.png](./img/sHmqyKbSIhNYMmOI/1725428880104-4f0c7741-4c20-4b86-ae0a-20bb5c04a926-449910.png)

### 4.4.2 Wi-Fi Settings

#### 4.4.2.1 Settings Management

Click the network icon on the top right corner of your desktop and select Wi-Fi -> Wi-Fi Settings or click Show Applications -> Settings -> Wi-Fi on the bottom left corner of your desktop.

![1725428957787-b447b035-810b-4c59-a0fd-9d85ad8360b7.png](./img/sHmqyKbSIhNYMmOI/1725428957787-b447b035-810b-4c59-a0fd-9d85ad8360b7-122104.png)

![1725429018386-b1e46f89-48eb-422c-96de-f19c75ca6e4f.png](./img/sHmqyKbSIhNYMmOI/1725429018386-b1e46f89-48eb-422c-96de-f19c75ca6e4f-908444.png)

#### 4.4.2.2 On/Off Management

Tap Turn On/Turn Off or slide the button in the Wi-Fi settings to turn the network off or on.

![1725429179602-47cbe6f4-2a78-42a9-99a4-883e00e9e997.png](./img/sHmqyKbSIhNYMmOI/1725429179602-47cbe6f4-2a78-42a9-99a4-883e00e9e997-436667.png)

![1725429211254-00a4142a-4056-4a13-91ff-5c5e57b67c4a.png](./img/sHmqyKbSIhNYMmOI/1725429211254-00a4142a-4056-4a13-91ff-5c5e57b67c4a-992891.png)

#### 4.4.2.3 Scanning

Scanning can be turned on via Wi-Fi -> Select Network, or the Wi-Fi Setting feature will automatically scan for visible Wi-Fi SSIDs in the neighbourhood when turned on.

![1725429779060-836be2aa-a278-45fa-a21b-16cee41fa0e6.png](./img/sHmqyKbSIhNYMmOI/1725429779060-836be2aa-a278-45fa-a21b-16cee41fa0e6-703124.png)

![1725429842707-0c2357cf-59a8-4a26-86d5-5e65d0ac05b2.png](./img/sHmqyKbSIhNYMmOI/1725429842707-0c2357cf-59a8-4a26-86d5-5e65d0ac05b2-680969.png)

![1725429484290-08d8c3ce-22e4-42e4-b866-d46aad3b7b84.png](./img/sHmqyKbSIhNYMmOI/1725429484290-08d8c3ce-22e4-42e4-b866-d46aad3b7b84-344379.png)

#### 4.4.2.4 Connection

Tap the Settings button on the right side of the Wi-Fi network, enter the password and tap Connect to connect to the network.

![1725430053125-73f3fdc1-d251-44f5-9e42-06cc3cddd97b.png](./img/sHmqyKbSIhNYMmOI/1725430053125-73f3fdc1-d251-44f5-9e42-06cc3cddd97b-437581.png)

### 4.4.3 Cellular Network Settings

#### 4.4.3.1 Configuring Cellular ECM Mode

Insert the SIM card into SIM1/SIM2, access the cellular antenna, open Terminal and enter the following commands in order.

Cellular Network Settings:

```json
## Access cellular AT command interface using 115200 baud rate
sudo sdebug /dev/ttyUSB2 115200 
## Configure cellular ECM mode 
AT+QCFG="usbnet",1 
## Save and reboot cellular module 
AT+CFUN=1,1
```

![1725430168767-73f4222c-ed3a-402b-b647-524a4c34e538.png](./img/sHmqyKbSIhNYMmOI/1725430168767-73f4222c-ed3a-402b-b647-524a4c34e538-080307.png)

#### 4.4.3.2 Switching SIM Card

Open Terminal and enter the following command to switch the SIM card.

Switching SIM Card:

```json
## Switch to root
sudo -s 
## Switch to SIM1 
echo 0 > /sys/class/gpio/PG.06/value 
## Switch to SIM2 
echo 1 > /sys/class/gpio/PG.06/value
```

![1725430252579-51416f1f-e9cb-48d9-95cd-58d32e3c487c.png](./img/sHmqyKbSIhNYMmOI/1725430252579-51416f1f-e9cb-48d9-95cd-58d32e3c487c-888876.png)

### 4.4.4 CAN FD Settings

Open Terminal and enter the following command to configure the CAN interface.

Configure CAN FD:

```json
## Link up CAN interface
sudo ip link set can0 up type can bitrate 1000000 dbitrate 5000000 restart-ms 1000 fd on
```

![1725430339502-d407015a-bf6a-4243-98e4-7391dab2f35b.png](./img/sHmqyKbSIhNYMmOI/1725430339502-d407015a-bf6a-4243-98e4-7391dab2f35b-921628.png)

### 4.4.5 Bluetooth Settings

#### 4.4.5.1 Settings Management

Click the network icon on the top right corner of the desktop and select Bluetooth -> Bluetooth Settings or click Show Applications->Settings->Bluetooth on the bottom left corner of the desktop.

![1725430415128-4f985f5b-064a-4fa3-a5d4-72f7e8e7c839.png](./img/sHmqyKbSIhNYMmOI/1725430415128-4f985f5b-064a-4fa3-a5d4-72f7e8e7c839-036447.png)

![1725430459388-936568fe-67d1-4d18-9169-ac95565691a0.png](./img/sHmqyKbSIhNYMmOI/1725430459388-936568fe-67d1-4d18-9169-ac95565691a0-318194.png)

#### 4.4.5.2 On/Off Management

Tap Turn On/Turn Off or slide the button in Bluetooth settings to turn Bluetooth off or on.

![1725430495328-1c78492d-3a71-42cd-a015-ea8cd94f0a3f.png](./img/sHmqyKbSIhNYMmOI/1725430495328-1c78492d-3a71-42cd-a015-ea8cd94f0a3f-949671.png)

![1725430520685-2cb4814e-db12-41c1-becf-dd41e0016674.png](./img/sHmqyKbSIhNYMmOI/1725430520685-2cb4814e-db12-41c1-becf-dd41e0016674-264324.png)

#### 4.4.5.3 Bluetooth Connection

After switching on the Bluetooth switch, it will automatically scan the neighbouring Bluetooth devices，click on the Bluetooth device name to connect (for Bluetooth devices that require a PIN code, please enter the PIN code).

![1725430620038-11dcce0a-7c9a-40ca-9182-e42317d2b472.png](./img/sHmqyKbSIhNYMmOI/1725430620038-11dcce0a-7c9a-40ca-9182-e42317d2b472-948440.png)

### 4.4.6 Network Settings Advanced Extensions

Reference:

1. [Network Manager | Ubuntu](https://ubuntu.com/core/docs/networkmanager)
2. [Bluez Prerequisites | Ubuntu](https://ubuntu.com/core/docs/bluez/check-installation)

### 4.5 Time Settings

Click Show Applications->Settings->Data & Time at the bottom left corner of the desktop.

![1725430667148-b418509a-55d5-48b2-89f9-25d8c8447492.png](./img/sHmqyKbSIhNYMmOI/1725430667148-b418509a-55d5-48b2-89f9-25d8c8447492-436875.png)

### 4.5.1 Setting the Time Zone

Select or enter the system time zone by clicking Time Zone on the Settings page.

![1725430709699-f6a5a8fc-490e-4254-90c1-9d1f9929b71e.png](./img/sHmqyKbSIhNYMmOI/1725430709699-f6a5a8fc-490e-4254-90c1-9d1f9929b71e-049379.png)

### 4.5.2 Adjusting the Time

By default, the system will automatically set the time when the device is connected to the network, if you need to set the time manually, please turn off Automatic Date & Time and set Date & Time manually.

![1725430813516-29a80334-7d77-4b12-af9e-4981712ff863.png](./img/sHmqyKbSIhNYMmOI/1725430813516-29a80334-7d77-4b12-af9e-4981712ff863-217964.png)

### 4.6 Peripheral Configuration

### 4.6.1 Serial Port Management

The device supports two RS-232/422/485 optional serial ports, corresponding to the device nodes /dev/ttyCOM1 and /dev/ttyCOM2 respectively. Open Terminal and use the uart_mode command to switch the serial port operating mode.

| **Table 7：Serial Port Mapping** | |
| --- | --- |
| COM1 | /dev/ttyCOM1 |
| COM2 | /dev/ttyCOM2 |

| **Table 8：Serial port operating mode switching** | | |
| --- | --- | --- |
| uart_mode | COM1 | 485<br/>422<br/>232 |
| | COM2 | 485<br/>422<br/>232 |

For example, to configure COM1 to operate in RS-485 mode, enter the following command.

```json
sudo uart_mode COM1 485
```

![1725430899148-091507bc-58a1-4e5b-b2e0-ad3df3c42f53.png](./img/sHmqyKbSIhNYMmOI/1725430899148-091507bc-58a1-4e5b-b2e0-ad3df3c42f53-588266.png)

### 4.6.2 Digital input/output Management

The device supports 4 isolated digital inputs and 4 isolated digital outputs.

| **Table 9：Digital Inputs/Outputs** | | |
| --- | --- | --- |
| DI | DI0 | /sys/class/gpio/gpio308 |
| | DI1 | /sys/class/gpio/gpio309 |
| | DI2 | /sys/class/gpio/gpio310 |
| | DI3 | /sys/class/gpio/gpio311 |
| | | |
| DO | DO0 | /sys/class/gpio/gpio312 |
| | DO1 | /sys/class/gpio/gpio313 |
| | DO2 | /sys/class/gpio/gpio314 |
| | DO3 | /sys/class/gpio/gpio315 |

## 5. Advanced

### 5.1 System Updates

Copy the system upgrade image to removable storage media or transfer it to the device via network, enter the following command to perform the system update operation, please be patient as the system update takes a long time.

```json
sudo update ota <update file>
```

![1725366527696-0d11e33b-f2a4-4512-8aec-57e1af5de669.png](./img/sHmqyKbSIhNYMmOI/1725366527696-0d11e33b-f2a4-4512-8aec-57e1af5de669-903182.png)

### 5.2 System Reset

### 5.2.1 Recovery flick switch reset

The device has a Recovery flick switch button under the detachable bezel on the right panel, press and hold Recovery for 10 seconds during normal system operation and wait for the system status light to change from blinking to normally lit and release it, the device will enter the system reset state (restoring the system to the factory state), please refer to part 2.2.10 for detailed descriptions of the buttons;

### 5.2.2 Command Reset

Open Terminal and use the update command to perform a system reset.

```json
sudo update reset
```

![1725366527658-f96bcf40-f901-411a-8341-53cc348d7cb5.png](./img/sHmqyKbSIhNYMmOI/1725366527658-f96bcf40-f901-411a-8341-53cc348d7cb5-247802.png)

## 6. Security (TPM2.0)

The device supports Trusted Platform Module 2.0 (TPM2.0) and is pre-installed with the tpm2-tools tool. You can directly use instructions to operate the TPM2.0 module to achieve security functions.

**Reference：**

1. [tpm2-tools](https://tpm2-tools.readthedocs.io/en/latest/)
2. [tpm2-tools/man at master · tpm2-software/tpm2-tools (github.com)](https://github.com/tpm2-software/tpm2-tools/tree/master/man)

## 7. Programming Guide

**Reference：**

1. [Jetson - Embedded AI Computing Platform | NVIDIA Developer](https://developer.nvidia.com/embedded-computing)
2. [Jetson Software | NVIDIA Developer](https://developer.nvidia.com/embedded/develop/software)
3. [Jetson Software Getting Started | NVIDIA Developer](https://developer.nvidia.com/embedded/learn/getting-started-jetson)
4. [NVIDIA Developer Forums - NVIDIA Developer Forums](https://forums.developer.nvidia.com/)
