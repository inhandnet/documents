# Textile Factory Digitalization Networking Case

## I. Solution Overview

### 1.1 Project Background

With the maturity of industrial digitalization, many factories plan for digitalization directly from the initial construction. A large textile factory has many old production lines that now need digital transformation. The goal is to minimize production stoppages, reduce wiring, and complete digital transformation through local HMI display.

### 1.2 Objectives

- Provide network connections for textile equipment at various stages of the factory
- Use WiFi wireless method to avoid production shutdown
- Requires stability, unattended operation
- Can display production data of the entire factory on a large screen

### 1.3 Applicable Scenarios

- Digital transformation of old production lines
- Biochemical culture equipment, intelligent networking
- WiFi wireless solution for new digital production lines

## II. Requirements Analysis

### 2.1 Current Equipment Status

- Equipment types: Textile machinery (PLC)
- Communication interfaces: Ethernet/RS485
- Communication protocols: TCP
- Deployment environment: Indoor

### 2.2 Core Requirements

1. Access requirement: Ethernet port, RS485
2. Data requirement: Host computer actively collects data
3. Network requirement: WiFi, stable automatic reconnection
4. Security requirement: EMC, isolation from external network

## III. Overall Architecture Design

### 3.1 Architecture

![alt text](images/image.webp)
1. Device layer: Textile equipment
2. Network layer: Industrial router IR302
3. Platform layer: Local Scada system

### 3.2 Data Flow

Device → Industrial router IR302 → WiFi → Local Scada system

## IV. Network and Access Solution

### 4.1 Networking Method Selection

This project uses WiFi wireless network. Needs to support Ethernet port and serial port.

### 4.2 Router Selection Points

- Supports WiFi client mode
- Supports Modbus gateway functionality
- Industrial-grade wide temperature, dustproof, anti-interference
- Software and hardware security needs testing

## V. Solution Highlights Summary

1. One-stop: Access + Network + Platform + Application full-stack solution
2. High compatibility: Multi-device, multi-protocol, multi-network unified access
3. High reliability: Edge caching, data continuation after network interruption, dual-link backup
4. Easy expansion: Support batch expansion, secondary development, API integration
5. Low cost: Reduce manual inspections, improve operation and maintenance efficiency
6. Security and compliance: Transmission encryption, permission management, operation audit
