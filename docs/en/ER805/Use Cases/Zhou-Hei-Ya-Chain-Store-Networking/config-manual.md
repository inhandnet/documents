# Configuration Guide Manual

## I. Document Information

- Document name: Configuration Manual
- Product model: **ER805**
- Firmware version: **V2.0.1**
- Applicable scenarios: Equipment networking
- Writing date: March 25, 2026

## II. Gateway Overview

### 2.1 Product Introduction

ER805 is a multi-functional edge access router supporting 5G/4G cellular and wired broadband access, equipped with gigabit network ports and gigabit Wi-Fi, capable of supporting network access for various digital terminals to meet the networking needs of various commercial stores and corporate offices, ensuring uninterrupted digital store operations and productivity. ER805's multi-link switching policy and dual SIM design can achieve multi-link backup to ensure network interruption, with excellent network performance and high availability.
The solution also provides Xiaoxing Cloud Manager SaaS platform to help you achieve centralized network configuration, remote equipment upgrades, remote fault diagnosis, and one-stop dynamic management of terminals and applications, online insight into network visualization, keeping store and office networks under control.

### 2.2 Main Functions

- 4/5G internet access
- Remote configuration, remote diagnosis, remote upgrade
- Wide temperature industrial-grade design

### 2.3 Typical Application Topology

POS machine/Cash register equipment → Ethernet → ER805→ 4/5G → Cloud platform/Server

## III. Hardware Description

### 3.1 Appearance and Interfaces

- Power interface: DC 9–36V
- Network ports: LAN ×4 + 1WAN
- Wireless: 4G
- Indicator lights: PWR, Network, WIFI
- Reset button: Restore factory settings

### 3.2 Wiring Instructions

#### 3.2.1 Power Wiring

- Positive: V+
- Negative: V-
- Note: Reverse polarity protection, lightning protection, grounding

#### 3.2.2 Ethernet Wiring

Direct/crossover adaptive, recommends Cat5e or higher network cables.

## IV. Factory Default Parameters

- Default IP: 192.168.10.1
- Subnet mask: 255.255.255.0
- Web username: **adm**
- Web password: 123456

## V. Preliminary Preparation

- Set computer to same network segment IP as gateway
- Connect computer to gateway LAN port with network cable
- Power on router, wait for RUN light to illuminate steadily
- Enter device IP in browser to access configuration page

## VI. Network Configuration

### 6.1 **Local Network Configuration**

![text](images/image_rId7.webp)

### 6.2 4G Wireless Network Configuration

- Insert 5G SIM card
- Enable mobile network
- APN: Automatic
- View signal strength

## VII. Enable Xiaoxing Cloud Platform

![text](images/image_rId8.png)

## VIII. Configuration Backup and Recovery

- Export configuration file
- Restore factory configuration

## IX. Status Monitoring and Diagnosis

### 9.1 Operating Status

- Device online status
- Network traffic, signal strength

![text](images/image_rId10.png)

### 9.2 Log Viewing

- System logs

## X. Common Problems and Troubleshooting

- Cannot open Web
  - Check network segment, network cable, IP conflicts
  - Reset gateway and retry

## XI. Safety Precautions

- Reliable grounding at industrial site
- LAN port address needs to be modified to the gateway of the local subnet
- Backup after configuration is complete
- Change remote password regularly
- Prohibit operation by unauthorized personnel
