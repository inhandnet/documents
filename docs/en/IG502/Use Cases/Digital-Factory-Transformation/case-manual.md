# Digital Factory Project Solution

# I. Solution Overview

## 1.1 Project Background

With the advancement of smart factories, there are a large number of sensor and meter equipment on site for temperature, humidity, water immersion, electricity meters, etc. Equipment is scattered and data is isolated, making it impossible to remotely monitor relevant data, resulting in high operation and maintenance costs.

## 1.2 Construction Objectives

- Full equipment networking, unified access management

- Real-time data acquisition, standardization, cloud upload / platform integration

- Support remote configuration, remote diagnosis, remote upgrade

- Achieve alarms, linkage, visualization, and report analysis

- Improve operation and maintenance efficiency, reduce manual inspection costs

- Secure, stable, easy to expand, easy to maintain

## 1.3 Applicable Scenarios

- Meter / Sensor networking (electricity meters, water meters, gas meters, temperature and humidity)
- Smart campus

# II. Requirements Analysis

## 2.1 Current Equipment Status

- Equipment types: 2 types (meters / sensors)
- Communication interfaces: RS485
- Communication protocols: Modbus RTU/TCP, HTTP
- Deployment environment: Indoor / Outdoor

# III. Overall Architecture Design

## 3.1 Four-Layer Architecture

1. Perception Layer: Sensors, meters

2. Network Layer: Edge gateway, 4G/5G

3. Platform Layer: IoT platform (HTTP/ cloud platform), data storage, edge computing

4. Application Layer: Monitoring large screen, Web management backend, APP, alarm system

## 3.2 Data Flow

Device → Edge gateway → Protocol parsing → Edge computing / Local caching → Cloud platform → Application display / Control issuance

## 3.3 Solution Topology

![Jiaxibella.jpg](images/c46d82e325347f8bb66aba460f154d699b699c70.webp)

# IV. Network and Access Solution

## 4.1 Networking Method Selection

Cellular

## 4.2 Edge Gateway Selection Points

- Supports multiple protocols (Modbus, DLT, etc.)

- Multiple serial ports (RS485/RS232), network ports, 4G/5G

- Edge computing, local caching, data continuation after network interruption

- Industrial-grade wide temperature, dustproof, anti-interference

- Remote management, remote upgrade, remote configuration

# V. Protocol and Data Acquisition Solution

## 5.1 Southbound Protocols to Support

- Industrial protocols: Modbus RTU/TCP

- Meter protocols: DL/T645

## 5.2 Northbound Protocols to Support

- HTTP

- Gateway side needs to parse HTTP message format

# VI. Solution Highlights Summary

1. One-stop: Access + Network + Platform + Application full-stack solution

2. High compatibility: Multi-device, multi-protocol, multi-network unified access

3. High reliability: Edge caching, data continuation after network interruption, dual-link backup

4. Easy expansion: Support batch expansion, secondary development, API integration

5. Low cost: Reduce manual inspections, improve operation and maintenance efficiency

6. Security and compliance: Transmission encryption, permission management, operation audit
