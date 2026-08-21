# Medical Device Networking Case Configuration Guide Manual

## I. Document Information

- Product Model: IR302
- Firmware Version: V3.5.107
- Applicable Scenarios: Industrial equipment networking, medical equipment networking, self-service terminal networking, cash register networking, etc.
- Writing Date: March 30, 2026

![alt text](images/image.webp)

## II. Router Overview

### 2.1 Product Introduction

InRouter302 (IR302 for short) series products are IoT wireless routers that integrate 4G network, Wi-Fi, virtual private networks, and other technologies, providing simple, reliable, and secure Internet connections. The product design considers the communication requirements of unattended sites, adopting software and hardware watchdogs and multi-level link detection mechanisms to ensure communication stability and reliability. At the same time, the IR302 series supports Inhand's Device Manager "Device Cloud" management platform, enabling users to achieve remote intelligent device management. The IR302 series is suitable for various industrial and commercial IoT applications, providing efficient and reliable solutions for digital IoT.

### 2.2 Main Functions

- Supports providing Internet connections for network and serial devices
- Supports multiple connection methods such as 4G network, Wi-Fi, wired network
- Supports multiple VPN protocols such as OpenVPN, IpSec, L2TP, etc.
- Supports remote configuration, remote diagnosis, remote upgrade
- Industrial-grade design

### 2.3 Typical Application Topology

Medical devices → IR302 router → 4G → Medical device cloud platform

## III. Hardware Description

### 3.1 Appearance and Interfaces

- Power interface: DC 9–36V, reverse polarity protection, overcurrent protection
- Serial port: 1 × RS232 (optional)
- Network ports: RJ45 ×2, WAN/LAN
- Wireless: 4G/Wi-Fi (optional)
- Indicator lights: Power, Status, cellular, Signal, Wi-Fi
- Reset button: Restore factory settings

### 3.2 Interface Description

![alt text](images/image-2.webp)

- Positive: V+
- Negative: V-
- Note: Reverse polarity protection, lightning protection, grounding
- MAIN → 4G antenna
- WiFi → WiFi antenna
- AUX → 4G enhanced antenna (North American models only)
- WAN/LAN → Ethernet port (can be set to WAN mode)
- LAN2 → Ethernet LAN interface
- Ground wire: Grounding, used to prevent static electricity and noise interference

## IV. Factory Default Parameters

- Default IP: 192.168.2.1
- Subnet mask: 255.255.255.0
- Web username: adm
- Web password: 123456 (some batches have random passwords. Refer to the password on the nameplate)

## V. Preliminary Preparation

1. Set the computer to an IP address on the same network segment as the gateway LAN port. The gateway LAN port is: 192.168.2.1.
2. Connect the computer to the gateway LAN port with a network cable
3. Power on the gateway and wait for the Status light to illuminate
4. Ensure the computer has a properly functioning browser installed

## VI. Network Configuration

### 6.1 LAN Port Configuration (Static)

![alt text](images/image-1.webp)

1. Enter [Network Settings] → [LAN]
2. Configure an appropriate IP address. Generally, it needs to be on the same network segment as the device address and serves as the gateway address for the device.
3. Select Apply
4. After application, you need to use the newly set address to log in to the device
![alt text](images/image-3.webp)

### 6.2 4G Wireless Network Configuration

1. Insert SIM card (note that the SIM card must be installed while powered off)
2. Enter [Network] → [cellular]
![alt text](images/image-5.webp)
3. If using a dedicated card or customized card, you need to configure the APN (this case uses a standard IoT card, no APN setting required)
![alt text](images/image-6.webp)
4. View the Signal indicator on the panel. Red - poor (signal value 0~10), Yellow - medium (signal value 11~20), Green - good (signal value 21~30)
![alt text](images/image-4.webp)

## VII. Router User Management Configuration

### 7.1 Changing Username and Password

![alt text](images/image-7.webp)

1. Enter [System Settings] → [Management Control]
2. Enter username, old password, new password
3. Select Apply, save configuration

### 7.3 Changing Management Method

1. Enter [System Settings] → [Management Control]
2. In management functions, select service type, port parameters, remote management, local management, etc.
3. Select Apply, save configuration
![alt text](images/image-8.webp)

### 7.4 Enabling Remote Management Platform

![alt text](images/image-9.webp)

1. Enter [Service] → [Device Remote Management Platform]
2. Check Enable
3. Select Device Management for service type
4. Select domestic or international server based on project requirements
5. Register account - enter the account you registered on this platform
![alt text](images/image-10.webp)

### 7.5 Configuration Backup and Recovery

#### Backup Configuration

![alt text](images/image-11.webp)

1. Enter [Service] → [Configuration Management]
2. Click Backup Configuration in router configuration
![alt text](images/image-12.webp)

#### Import Configuration

1. Enter [Service] → [Configuration Management]
2. Click Import Configuration in router configuration
3. Restart after importing configuration for it to take effect
![alt text](images/image-13.webp)

## X. Common Problems and Troubleshooting

1. Cannot open Web interface
   - Check network segment, network cable, IP conflicts
   - Restore gateway to factory settings and retry

2. Cellular network cannot dial normally
   - Check if SIM card is working properly
   - Check if APN is correct
   - Check if 4G network is working properly (recommended signal value 21~30)

3. Signal dialing is normal but cannot access server
   - Check if downlink device is set with correct IP address
   - Check if gateway address is correct
   - Check if DNS server is set
   - Confirm if this card is a whitelist card and whether the server address is added to the whitelist

## XI. Safety Precautions

- Reliable grounding at industrial site
- Avoid hot-plugging serial ports with power on
- Backup after configuration is complete
- Change remote password regularly
- Prohibit operation by unauthorized personnel
