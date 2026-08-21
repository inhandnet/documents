# IG502 - IEC 60870-5-101 to IEC 60870-5-104 Protocol Conversion

**Product Model:** IG502 (InGateway 502)

## 1. Executive Summary

In power utilities, smart grid, water / gas pipelines and other industrial control environments, a very large installed base of RTUs (Remote Terminal Units), protection relays, IEDs and metering devices still communicates over **IEC 60870-5-101** — a serial, byte-oriented telecontrol protocol designed for low-bandwidth links (RS-232 / RS-485 / fiber modems).

Modern SCADA / DMS / EMS master stations and cloud-based monitoring platforms, however, expect **IEC 60870-5-104** — the IP-based variant of the same telecontrol standard, transported over TCP/IP (port 2404).

The InHand **IG502 Edge Gateway** bridges these two worlds. Acting as an IEC 101 master on the serial side and an IEC 104 server on the Ethernet / cellular side, it converts traffic transparently — preserving Type IDs, Information Object Addresses (IOA), Cause of Transmission (COT) and ASDU addressing — so existing legacy devices can be integrated into modern IP-based SCADA systems **without replacing any field equipment**.

This document describes the application scenarios, system architecture and value the IG502 delivers in such projects.

![Reference Topology — IEC101 to IEC104 Conversion](images/image1.png)

## 2. Background & Pain Points

### 2.1 The Legacy Reality

Field assets such as substation RTUs, feeder terminal units (FTUs), distribution transformer terminal units (TTUs), pole-mounted reclosers and older protection IEDs were installed years — sometimes decades — ago. They typically expose:

- **RS-232 / RS-485 / RS-422** serial ports
- **IEC 60870-5-101** as the application protocol (balanced or unbalanced mode)
- 1200 / 2400 / 9600 / 19200 bps speeds
- Proprietary cabling and short-range fiber modems

Replacing these devices to gain native IEC 104 connectivity is rarely feasible — both because of CAPEX and because of the operational risk of touching critical primary equipment.

### 2.2 The Modern Requirement

At the same time, control centers are being modernized:

- Master stations move from dedicated serial fan-out cabinets to **IP-based SCADA / DMS** platforms
- Centralized telemetry is required for **fault location, isolation and service restoration (FLISR)**
- **Cyber-security** standards (IEC 62351, NERC CIP and similar) require network segmentation, authentication and audit trails — natural for IP, painful for raw serial
- **Cellular (4G / 5G) backhaul** is used to reach unmanned, geographically dispersed sites
- **Cloud / edge analytics** require a uniform northbound data plane

### 2.3 The Gap

The protocol-conversion gap between IEC 101 and IEC 104 is the single largest barrier to integrating brownfield assets into greenfield SCADA infrastructure. A purpose-built protocol-conversion gateway resolves this gap.

---

## 3. Solution Overview

### 3.1 Role of the IG502

The IG502 sits at the field edge and performs three roles simultaneously:

1. **IEC 101 master** on the RS-232 / RS-485 serial port, polling one or more downstream IEC 101 outstations.
2. **IEC 104 server** on the Ethernet (or cellular WAN) port, accepting connections from upstream SCADA masters on TCP/2404.
3. **Edge router** providing 4G / 5G / wired uplinks, VPN, firewall and remote management.

Because the IG502 keeps the IEC 101 / 104 data model identical (Type ID, IOA, COT and ASDU address are preserved one-for-one), the SCADA master station sees the legacy device **as if it were natively IEC 104**.

### 3.2 Reference Architecture

```
┌──────────────────────┐     RS-485       ┌──────────────┐     Ethernet / 4G      ┌──────────────────┐
│  IEC 101 Outstations │ ───────────────► │   IG502      │ ─────────────────────► │  IEC 104 SCADA   │
│  (RTU / IED / FTU)   │   IEC 60870-5-101│   Gateway    │  IEC 60870-5-104 (2404)│  Master Station  │
└──────────────────────┘                  └──────────────┘                        └──────────────────┘
                                          │   Protocol   │
                                          │   conversion │
                                          │ + edge router│
```

A four-layer model:

| Layer | Components | Role |
|-------|-----------|------|
| Field / Sensing | RTU, IED, FTU, TTU, recloser, meter | Generate telemetry / accept controls (IEC 101) |
| Edge / Gateway | **IG502** | Polls IEC 101, exposes IEC 104, buffers, secures, routes |
| Transport | Wired Ethernet, 4G / 5G, optional VPN | Carries IEC 104 traffic to the control center |
| Application | SCADA / DMS / EMS / cloud HMI | Consumes IEC 104, drives dashboards and controls |

### 3.3 IEC 101 vs IEC 104 — Standards at a Glance

| Aspect | IEC 60870-5-101 (serial) | IEC 60870-5-104 (TCP/IP) |
|--------|--------------------------|--------------------------|
| Physical layer | RS-232 / RS-485 | Ethernet / 4G / 5G |
| Link layer | FT 1.2 frame, balanced / unbalanced | TCP, APCI (start / stop / test) |
| ASDU | Type IDs identical (M_SP_NA_1, M_DP_NA_1, M_ME_NC_1, C_SC_NA_1, …) | Type IDs identical |
| Application data | Preserved end-to-end through the gateway | Preserved end-to-end through the gateway |
| Typical TCP port | n/a | 2404 |

The IG502 bridges the link-layer and physical-layer differences while keeping the application-layer data model untouched — this is what allows a SCADA point list developed for IEC 104 to remain valid against legacy IEC 101 devices.

---

## 4. Application Scenarios

### 4.1 Smart Grid — Distribution Automation

**Pain:** Hundreds of pole-top FTUs and TTUs across a feeder still speak IEC 101 over serial. The new distribution master station only supports IEC 104.

**Solution:** Mount one IG502 per site (or per ring main unit). Serial side connects to the FTU; cellular side reports to the master via APN-private 4G. Existing FTUs are kept in service for their full economic life.

**Benefit:** No primary-equipment replacement, single-digit minutes per site for commissioning, fault data reaches dispatchers in real time.

### 4.2 Substation Retrofit

**Pain:** Indoor / outdoor substations with legacy protection IEDs aggregated by an IEC 101 bay controller. The utility wants centralized monitoring without rewiring the bay.

**Solution:** Place an IG502 in the substation telecom cabinet. Wire RS-485 to the bay controller; uplink via fiber Ethernet (or 4G backup) to the regional control center on IEC 104.

**Benefit:** Drop-in modernization; the substation appears as a native IEC 104 RTU; redundant WAN (wired + 4G) improves availability.

### 4.3 Renewable Generation — Solar / Wind Farms

**Pain:** Inverters, combiner boxes and weather stations expose IEC 101; the SCADA / energy management system at the regional operations center is IEC 104 only.

**Solution:** IG502 per inverter zone or per substation skid; converts IEC 101 telemetry (active power, reactive power, faults, switches) into IEC 104; uplink to operator's cloud SCADA.

**Benefit:** Plant-wide observability over standardized IP transport; ready for cyber-security hardening (VPN, firewall, role-based access).

### 4.4 Water, Gas and District Heating

**Pain:** Pumping stations, valve chambers and pressure regulators use serial IEC 101; the utility's IP network and SCADA expect IEC 104.

**Solution:** Pole-mounted or cabinet-mounted IG502s convert protocols and provide cellular backhaul where wired networks are not available.

**Benefit:** Single multi-purpose device (router + protocol gateway + edge compute) reduces BoM and footprint inside small cabinets.

### 4.5 Railway and Industrial Energy Systems

**Pain:** Traction substations and large industrial sites operate IEC 101 RTUs purchased a decade ago; new EMS platforms standardize on IEC 104.

**Solution:** IG502 sits between the RTU and the IT / OT boundary, exposing IEC 104 northbound and (optionally) MQTT for IT analytics.

**Benefit:** OT data is freed for digitalization initiatives without disturbing the safety-critical control loop.

---

## 5. Solution Highlights

1. **Drop-in conversion** — same Type IDs, COT and IOA on both sides; no SCADA point-list rework required.
2. **Industrial-grade hardware** — wide-temperature, fanless, DIN-rail; designed for substations and outdoor cabinets.
3. **Multiple uplinks** — Gigabit Ethernet, 4G / 5G, with link backup and seamless failover.
4. **Edge compute & buffering** — Python / Docker container, local caching, store-and-forward during WAN outages.
5. **Secure by design** — IPsec / OpenVPN / L2TP, firewall, RBAC, signed firmware, optional IEC 62351 compatible TLS deployments.
6. **Remote management** — InHand Device Manager Cloud for batch configuration, monitoring, firmware updates and remote troubleshooting.
7. **Verified interoperability** — validated against widely-used IEC 101 and IEC 104 master / outstation systems.

---

## 6. Why InHand IG502

| Requirement | What the IG502 delivers |
|-------------|-------------------------|
| Protocol conversion IEC 101 ↔ IEC 104 | Native — no scripting required |
| Other industrial protocols | Modbus RTU/TCP, OPC UA, DLT/645, MQTT, transparent TCP — coexisting with IEC stack |
| Connectivity | 2× GbE, RS-232, RS-485, 4G / 5G, Wi-Fi (model dependent) |
| Edge compute | Python SDK, Docker, local rules, store-and-forward |
| Security | VPN, firewall, RBAC, signed firmware |
| Remote O&M | InHand Device Manager Cloud |
| Environmental | -40 °C to +75 °C, fanless, DIN-rail, surge protection |
| Certifications | FCC, CE, RoHS (regional models — confirm with InHand sales) |

---

## 7. Deployment Outline

1. **Survey** the field site: identify RTUs / IEDs, serial parameters, IEC 101 framing details.
2. **Select uplink**: wired Ethernet, 4G , or both with link backup.
3. **Validate** end-to-end with the customer's SCADA master station.
4. **Onboard** the gateway to InHand Device Manager Cloud for long-term operations.

