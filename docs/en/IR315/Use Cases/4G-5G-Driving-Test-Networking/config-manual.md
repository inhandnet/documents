# Driving Test Networking Router Configuration Manual

## I. Document Information

- **Document Name**: Driving Test Networking Router Configuration Manual

- **Product Models**: ER815, IR315

- **Firmware Versions**: V2.0.2 (ER815), V1.0.111 (IR315)

- **Applicable Scenarios**: Equipment networking, self-built L2TP-VPN

- **Writing Date**: March 20, 2026

![text](images/2026-03-25-14-51-14-image.webp)

![text](images/2026-03-25-14-51-44-image.webp)

## II. Gateway Overview

### 2.1 Product Introduction

In this scenario, the router product is mainly used for **vehicle driving test equipment networking** and **self-built L2TP-VPN tunnel** in the driving test networking scenario.

### 2.2 Main Functions

- Provide network for vehicle driving test equipment

- Self-built VPN tunnel encrypted transmission between branch end and central end

- Remote configuration, remote diagnosis, remote upgrade

- Wide temperature industrial-grade design

### 2.3 Typical Application Topology

![alt text](images/2026-03-25-15-06-28-6681f1bfabf01d25a4cd896abf967813.webp)

## III. Hardware Description

## 3.1 Appearance and Interfaces

- Power interface: 12V/3A DC (EC815), 9-48V (IR315)
- Network ports: ER815 LAN ×5 (WAN/LAN configurable ×2), IR315 LAN×4 WAN×1
- Wireless: 4G/5G/Wi-Fi (optional)
- Indicator lights: PWR, RUN, NET, signal strength
- Reset button: Restore factory settings

## 3.2 Wiring Instructions

### 3.2.1 Power Wiring

- Positive: V+
- Negative: V-
- Note: Reverse polarity protection, lightning protection, grounding

### 3.2.2 Ethernet Wiring

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
![alt text](images/2026-03-25-15-56-02-image.webp)

## VI. Network Configuration

### 6.1 IR315 Configuration

1. Insert SIM card (supports NB-IoT/4G)
2. Enable mobile network
3. APN: Automatic / Manual entry
4. View signal strength
![alt text](images/203-253-25-16-07-46-image.png)
![alt text](images/2026-03-25-16-07-57-image.webp)

4. Set VLAN address to 192.168.1.1
![alt text](images/2026-03-25-16-13-27-image.webp)
6. Set L2TP-VPN tunnel
L2TP server address, username and password need to be filled in according to actual situation
![alt text](images/2026-03-25-16-14-54-image.webp)
7. VPN connection successful effect is as follows
![alt text](images/2026-03-25-16-19-10-image.webp)

### 6.2 ER815 Configuration

1. Connect wired network to ER815 wan1 port
![alt text](images/2026-03-25-16-21-11-image.webp)
2. Set local VLAN address to 172.16.33.1
![alt text](images/2026-03-25-16-21-45-image.webp)
3. Set L2TP-VPN server
![alt text](images/2026-03-25-16-22-26-image.webp)
4. Peer connection successful effect is as follows
![alt text](images/2026-03-25-16-24-15-image.webp)

## VII. Import Router Configuration

Configuration files are in the config directory
