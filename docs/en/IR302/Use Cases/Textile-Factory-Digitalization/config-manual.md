# Medical Device Networking Case Configuration Guide Manual

## I. Document Information

- Product Model: IR302-EN00-WLAN
- Firmware Version: V3.5.107
- Applicable Scenarios: Industrial equipment networking, medical equipment networking, biochemical culture equipment networking
- Writing Date: March 31, 2026

![alt text](images/image1.webp)

## II. Router Overview

### 2.1 Product Introduction

InRouter302 (IR302 for short) series products are IoT wireless routers that integrate 4G network, Wi-Fi, virtual private networks, and other technologies, providing simple, reliable, and secure Internet connections. The product design considers the communication requirements of unattended sites, adopting software and hardware watchdogs and multi-level link detection mechanisms to ensure communication stability and reliability. At the same time, the IR302 series supports Inhand's Device Manager "Device Cloud" management platform, enabling users to achieve remote intelligent device management. The IR302 series is suitable for various industrial and commercial IoT applications, providing efficient and reliable solutions for digital IoT.

### 2.2 Main Functions

- Supports providing network connections for network and serial devices
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

![alt text](images/image-101.webp)

1. Log in to the router, select [Network] → [WLAN Mode Switch] → [Change mode to STA mode] → [Apply] (Note: takes effect after restart)
   ![alt text](images/image-102.webp)
2. Enter [Network] → [WLAN Client]
   ![alt text](images/image-103.webp)
3. Configure WLAN client, enter SSID and password, or scan the network and select the network to connect to
   ![alt text](images/image-4.webp)
4. Enter [Network] → [WLAN (STA)], disabled by default, set to static IP and configure the correct IP address, subnet mask, and gateway address
   ![alt text](images/image-5.webp)
5. Configure port mapping for network devices, map port 502 of WAN (STA) to 192.168.20.100:502, used for Modbus data collection. (Specific port number is set according to the port used by the PLC protocol)
   ![alt text](images/image-6.webp)
6. Configure DTU function for serial devices, [Service] → [DTU Function], enable DTU function, protocol set to Modbus bridge function.

## VII. Router User Management Configuration

### 7.1 Changing Username and Password

1. Enter [System Settings] → [Management Control]
2. Enter username, old password, new password
3. Select Apply, save configuration

### 7.2 Configuration Backup and Recovery

#### Backup Configuration

![alt text](images/image-11.webp)

1. Enter [Service] → [Configuration Management]
2. Click Backup Configuration in router configuration
![alt text](images/image-12.webp)

#### Import Configuration

1. Enter [Service] → [Configuration Management]
2. Click Import Configuration in router configuration
3. Restart after importing configuration for it to take effect (LAN port address in the configuration file in the attachment is 192.168.20.1)
![alt text](images/image-13.webp)

## X. Common Problems and Troubleshooting

1. Cannot open Web interface
   - Check network segment, network cable, IP conflicts
   - Restore gateway to factory settings and retry

2. Cannot find WiFi signal
   - Check if antenna is installed correctly
   - Check if AP is working properly
   - Check if WiFi frequency band is supported by the router (2.4GHz)

3. Cannot connect to WiFi normally
   - Check if WiFi password is correct
   - Confirm if router supports the WiFi authentication method
   - Check if router has access whitelist/blacklist restrictions

## XI. Safety Precautions

- Reliable grounding at industrial site
- Avoid hot-plugging serial ports with power on
- Backup after configuration is complete
- Change remote password regularly
- Prohibit operation by unauthorized personnel
