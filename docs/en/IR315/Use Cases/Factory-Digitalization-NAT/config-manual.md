# Factory Digitalization NAT Router Configuration Manual

## I. Document Information

- **Document Name**: Industrial Digitalization NAT Router Configuration Manual
- **Product Model**: IR315-EN00
- **Firmware Version**: V1.0.111 (IR315)
- **Applicable Scenarios**: IP address translation, NAT networking, network isolation
- **Writing Date**: April 7, 2026

![alt text](images/image.webp)

## II. Gateway Overview

### 2.1 Product Introduction

In this scenario, the router product is mainly used for **NAT network address translation** for production equipment networking in factories and **achieving isolation between production control network and office network**.

### 2.2 Main Functions

- Provide network address translation functionality for production equipment

- Achieve isolation between production control network and office network

- Wide temperature industrial-grade design

### 2.3 Typical Application Topology

![alt text](images/image-1.webp)

## III. Hardware Description

## 3.1 Appearance and Interfaces

- Power interface: 9-48V (IR315)
- Network ports: LAN×4 WAN×1
- Indicator lights: PWR, RUN
- Reset button: Restore factory settings

## 3.2 Wiring Instructions

![alt text](images/image-2.webp)

### 3.2.1 Power Wiring

- Positive: V+
- Negative: V-
- Note: Reverse polarity protection, lightning protection, grounding

#### 3.2.2 Ethernet Wiring

Direct/crossover adaptive, recommends Cat5e or higher network cables.

## IV. Factory Default Parameters

- Default IP: 192.168.2.1
- Subnet mask: 255.255.255.0
- Web username: adm
- Web password: Random password, refer to corresponding equipment nameplate

## V. Preliminary Preparation

1. Set computer to same network segment IP as gateway
2. Connect computer to gateway LAN port with network cable
3. Power on gateway, wait for RUN light to illuminate steadily
4. Enter gateway IP in browser to access configuration page

## VI. Network Configuration

### 6.1 IR315 LAN Configuration

#### 6.1.1. Set Interface Address

Network - WAN port
Set the WAN interface to the network segment of the upstream connection or where the MES is located. In this example, it is the 192.168.1.X segment. Set to 192.168.1.100
![alt text](images/image-8.webp)
Network - VLAN interface
The downstream PLC address is 192.168.2.100. Set the VLAN interface to 192.168.2.1
![alt text](images/image-5.webp)

#### 6.1.2. Set NAT

1. NAT Interface
Find Firewall - NAT Interface
![alt text](images/image-6.webp)

2. DNAT Setting
DNAT setting is equivalent to mapping the internal network IP address to the external network IP address, achieving NAT networking functionality
![alt text](images/image-7.webp)

3. Set SNAT
This setting is equivalent to replacing the source address of incoming external traffic with the internal LAN port address, achieving the function where downstream equipment can be accessed even without writing a gateway.
![alt text](images/image-9.webp)

4. After setting, click Add, then click the Apply button behind it to apply the configuration to take effect
![alt text](images/image-10.webp)

## VII. Import/Export Router Configuration

### 7.1 Export Configuration File

System - Configuration Management - Export Configuration File
![alt text](images/image-3.webp)

### 7.2 Import Configuration File

System - Configuration Management - Import Configuration File. After importing the configuration file, it will prompt for restart to take effect
![alt text](images/image-4.webp)
Configuration files are in the config directory. The configuration file username is adm, password is inhand@123
