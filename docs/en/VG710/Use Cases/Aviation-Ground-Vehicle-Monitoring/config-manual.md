# Aviation Ground Vehicle VG710 Vehicle Gateway Configuration Manual

## I. Document Information

- **Document Name**: Aviation Ground Vehicle VG710 Vehicle Gateway Configuration Manual
- **Product Model**: VG710
- **Firmware Version**: V1.2.5
- **Applicable Scenarios**: Smart apron, commercial vehicle networking, government vehicles, medical ambulances
- **Writing Date**: April 14, 2026

![alt text](images/image.webp)

## II. VG710 Vehicle Gateway Overview

### 2.1 Product Introduction

InVehicle G710 vehicle gateway is a new generation vehicle gateway launched for the Internet of Vehicles field. This product provides high-speed and secure networks for automotive and transportation services, meeting the needs of special vehicles, law enforcement, emergency, engineering, rescue, and mobile asset management. Combined with a cloud-based remote fleet management platform, it provides ubiquitous networks and uninterrupted operational supervision for logistics management, asset tracking, mobile office, and government security work.

### 2.2 Main Functions

- Integrated vehicle OBD-II/J1939 diagnostic interface
- Supports Python secondary development
- Supports Docker container technology
- Industrial-grade chips, communication modules, and electronic components
- Wide temperature industrial-grade design
- Integrated inertial navigation system
- Integrated 3D accelerometer and gyroscope

### 2.3 Typical Application Topology

![alt text](images/image-1.webp)

## III. Hardware Description

## 3.1 Appearance and Interfaces

- Power interface: 9-48V (IR315)
- Network ports: LAN×4 WAN×1
- Indicator lights: PWR, RUN
- Reset button: Restore factory settings

4G version:
![alt text](images/image-2.webp)
![alt text](images/image-4.webp)
5G version:
![alt text](images/image-3.webp)
![alt text](images/image-5.webp)

## 3.2 Wiring Instructions

![alt text](images/image-7.webp)

### 3.2.1 Power Wiring

- Positive: V+
- Negative: V-
- Ignition sense: Ignition signal
![alt text](images/image-6.webp)
Power input range: DC 9~36V, recommended power 18W. Power sourcing methods:
● Vehicle battery;
● Storage battery;
● Cigarette lighter;
● Power adapter (indoor use)

Normal engineering environment: Connect power V+, GND and ignition line (Ignition sense) separately. The ignition signal line is connected to the vehicle's ignition line as shown in Figure 1;
Test status wiring: Ignition line and positive terminal are connected together as shown in Figure 2

***Note: If the ignition signal line is not connected, the device cannot start***

#### 3.2.2 Ethernet Wiring

Direct/crossover adaptive, recommends Cat5e or higher network cables.

## IV. Factory Default Parameters

- Default IP: 192.168.2.1
- Subnet mask: 255.255.255.0
- Web username: adm
- Web password: 123456, if random password, refer to corresponding equipment nameplate

## V. Preliminary Preparation

1. Set computer to same network segment IP as VG710
2. Connect computer to VG710 LAN port with network cable
3. Power on VG710, wait for device to operate normally
4. Enter VG710 IP in browser to access configuration page

## VI. Network Configuration

### 6.1 VG710 LAN Configuration

#### 6.1.1. Set Interface Address

Network - Bridge interface
The downstream device address is 192.168.2.100. Set the bridge interface to 192.168.2.1
![alt text](images/image-8.webp)
If there is no initial address in the bridge interface, or there is no bridge interface, select the VLAN interface setting below.

#### 6.1.2. Set Diagnostic Protocol

1. Find Service - Vehicle Diagnosis
![alt text](images/image-9.webp)
2. Set vehicle diagnosis on the corresponding interface
![alt text](images/image-10.webp)
3. Install the customer's custom-developed APP for reporting vehicle status and diagnostic information to the cloud platform.
APP - APP Management - Import APP
![alt text](images/image-11.webp)
The APP part belongs to the customer's private equipment and does not provide a download link. Customers need to develop corresponding APPs according to their needs.

## VII. Import/Export Router Configuration

### 7.1 Export Configuration File

Management - Configuration Management - Backup startup-config
![alt text](images/image-13.webp)

### 7.2 Import Configuration File

Management - Configuration Management - Import Configuration File. After importing the configuration file, it will prompt for restart to take effect
![alt text](images/image-12.webp)
