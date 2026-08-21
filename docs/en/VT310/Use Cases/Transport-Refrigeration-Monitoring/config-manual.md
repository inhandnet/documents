# Vehicle Refrigeration Monitoring

## I. Document Information

- **Document Name**: Vehicle Refrigeration Monitoring Configuration Manual
- **Product Model**: VT310
- **Firmware Version**: V1.1.64
- **Applicable Scenarios**: Logistics, commercial vehicle networking, government vehicles, construction machinery
- **Writing Date**: April 15, 2026

## II. VT310 Vehicle Refrigeration Monitoring Overview

### 2.1 Product Introduction

VT310 is a reliable, durable, feature-rich, and high-performance vehicle tracker. VT310 has IP66 high-level protection and a unique low-power design, allowing it to work stably in harsh environments and operate for a long time after the vehicle is turned off. This tracker integrates LTE, GNSS, gyroscope, and inertial sensors, with strong processing and computing capabilities and a multi-threaded operating system. It provides real-time precise positioning of vehicle location, statistics of vehicle mileage, real-time monitoring of emergency braking, acceleration, collisions, and other emergencies, maintaining transport cargo safety, and recording and analyzing driver behavior. Rich I/O interfaces can remotely monitor various vehicle peripherals, such as: alarms, sensors, switches, ignition status, controllers, etc. Supports standard OBD-II, J1939, J1708 and other vehicle diagnostic protocols, tracking vehicle operating status, achieving preventive maintenance.

### 2.2 Main Functions

- VT310 supports LTE CAT M1, CAT 1, and CAT 4
- Built-in GNSS module
- Supports Docker container technology
- Integrated inertial navigation system
- Integrated gyroscope

### 2.3 Typical Application Topology

![alt text](images/image-1.webp)

## III. Hardware Description

## 3.1 Appearance and Interfaces

![alt text](images/image.webp)

## 3.2 Wiring Instructions

Interface number position
![alt text](images/image-2.webp)
Interface pin definition
![alt text](images/image-3.webp)

### 3.2.1 Power Wiring

- Positive: V+
- Negative: V-
- IGT: Ignition signal

Ignition line IGT (Ignition sense, hereafter referred to as IGT, also known as ACC): IGT is used to connect to the vehicle's ignition switch. VT310 can detect whether the connected vehicle has started ignition. When using the 20PIN cable for testing, connect the IGT line and V+ line to the DC power supply.

***Note: If the ignition signal line is not connected, the device cannot start***

## IV. Factory Default Parameters

- Baud rate: 115200bps
- Username: admin
- Password: 123456, if random password, refer to corresponding equipment nameplate
![alt text](images/image-6.webp)

## V. Preliminary Preparation

1. Computer installs VT310 configuration tool
![alt text](images/image-5.webp)
2. Connect computer to VT310 with serial cable
3. Power on VT310, wait for device to operate normally
4. Open software, select the computer's corresponding serial port, enter correct parameters and click connect device.

## VI. Parameter Configuration

### 6.1 Platform Parameter Settings

Platform type: MQTT Broker
Domain: XXXX.XXX.com
Port: 1883
Username: XXXX
Password: XXX
![alt text](images/image-4.webp)

## VII. Import/Export Configuration Files

![alt text](images/image-7.webp)

### 7.1 Export Configuration File

Select Maintenance - Import/Export Configuration File - Export Configuration
![alt text](images/image-8.webp)

### 7.2 Import Configuration File

Select Maintenance - Import Configuration File - Import File, select import configuration, save and restart to take effect
![alt text](images/image-9.webp)
