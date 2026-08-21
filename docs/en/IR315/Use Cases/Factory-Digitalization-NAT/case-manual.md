# Factory Digitalization NAT Networking Case

## I. Solution Overview

### 1.1 Project Background

With the acceleration of digitalization, factory digitalization has become increasingly important. Various problems need to be solved during the digitalization process. Old equipment is no longer under warranty and does not support IP address modification, and most equipment has the same IP address. The most complex problem is the networking problem. This solution is specifically designed to solve the networking problem.

### 1.2 Construction Objectives

- Access data from all equipment into the local SCADA platform
- Simple architecture, easy to maintain
- Data security, equipment not allowed to access the internet
- Equipment installation must comply with industrial design, with high stability

### 1.3 Applicable Scenarios

- Digitalization engineering network transformation
- Single equipment connecting to multiple platforms scenarios
- Solving flexible networking problems

## II. Requirements Analysis

### 2.1 Current Equipment Status

- Equipment types: Production lines, machine tools, industrial robots and other production equipment
- Communication interfaces: RJ45 Ethernet interface
- Communication protocols: ModbusTCP, Siemens S7, Ethernet/IP and various PLC protocols
- Deployment environment: Factory workshop

### 2.2 Core Requirements

1. **Networking Requirements**:

   - A single PLC needs to be able to access multiple network systems
   - Multiple PLCs with the same address cannot join the network

2. **Equipment Requirements**:

   - Router (IR315)

## III. Overall Architecture Design

![alt text](images/2026-04-01-15-15-59-image.webp)

Factory digitalization networking:

- **Production Equipment Side**: Because production equipment has only one fixed address that cannot be modified or is extremely difficult to modify, the IR315 industrial router's NAT function is used here to achieve network address translation functionality.

- **Central System**: Uses locally deployed platform software, where the server completes data acquisition parsing and screen display. This solution has high network dependency, so requires a highly stable network.

## IV. Data Flow

Field equipment → Equipment control network → IR315 industrial router → Internal network → Internal network SCADA software

## V. IR Router Functional Requirements

- Supports free NAT settings, can individually set SNAT and DNAT
- Supports multiple network ports and supports VLAN division
- Supports static routing, ACL, NAT and other settings
- Industrial design, can be installed on industrial rails

## VI. Solution Highlights Summary

1. **Industrial-grade Reliability**: Uses industrial-grade NAT routers with high stability, high environmental adaptability, and low failure rate

2. **Lower Deployment and O&M Costs**: Installing a NAT router eliminates the need to replace production line equipment controllers or modify original production programs. It is convenient, fast, and lower cost.

3. **Terminal Block Design**: Uses terminal block wiring, effectively solving the impact of high and low temperatures on equipment, avoiding poor contact problems after oxidation of circular plugs

4. **Three-Level Security Guarantee**:

   Does not connect to the internet at all, eliminating external unsafe factors. The control network of industrial equipment is isolated from the factory intranet using NAT, which also helps ensure safe equipment operation.
