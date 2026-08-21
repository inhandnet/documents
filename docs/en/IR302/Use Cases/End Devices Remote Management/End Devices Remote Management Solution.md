# End Devices Remote Management

## 1. Solution Overview

### 1.1 Project Background

With the rapid expansion of Industrial IoT, smart parks, smart factories, and intelligent O&M, more and more sensors, meters, PLCs, controllers, kiosks, medical devices, and other terminal equipment are deployed in distributed field sites. These devices are typically:

- Geographically dispersed and hard to reach physically;
- Behind carrier-grade NAT or private networks without public IP addresses;
- Maintained as data silos with no unified channel for remote monitoring or remote service;
- Costly to maintain because every site visit requires on-site labor.

This solution leverages the InHand **InRouter302 (IR302)** industrial 4G router together with the **InHand Connect Service (InConnect / ICS)** cloud platform to build a unified, secure, plug-and-play remote-access infrastructure. It enables centralized device onboarding, real-time data exchange, remote control, status monitoring, alarm handling, and cloud data integration — providing a stable IoT foundation for upper-layer business applications.

### 1.2 Construction Goals

- Bring all field end devices online and manage them under one platform.
- Collect real-time data and forward it to standard cloud / enterprise platforms.
- Support remote configuration, remote diagnostics, and remote firmware upgrade.
- Provide alarming, automation, visualization, and reporting.
- Reduce on-site inspection costs and improve O&M efficiency.
- Deliver a secure, reliable, easily scalable, and easy-to-maintain solution.

### 1.3 Applicable Scenarios

- Industrial equipment networking — CNC machines, fans, pumps, air compressors, production lines.
- Meter / sensor networking — electricity, water, gas, temperature & humidity meters.
- Smart parks, buildings, server rooms, and base stations.
- Smart agriculture, environmental monitoring, energy management.
- Mobile assets, vehicles, and construction machinery networking.
- Medical device networking, self-service kiosks, POS terminals, vending machines.

## 2. Data Flow Topology

The diagram below visualizes how a remote engineer reaches an on-site PLC/HMI through ICS:

![Data Flow Topology](images/image1.png)

Steps shown on the diagram:

1. The IR302 establishes an outbound registration + OpenVPN tunnel to ICS — no public IP, no port forwarding required at the field site.
2. The remote engineer (PC or smartphone) imports the `.ovpn` profile and dials in to ICS.
3. ICS pushes the running configuration and assigns virtual IPs (10.16.0.0/16) to the router and to its downstream devices.
4. The engineer accesses field devices via the assigned virtual IP, with all traffic encrypted by OpenVPN + TLS.
5. ICS forwards the packets through the tunnel to the corresponding IR302.
6. The IR302 NATs the virtual IP to the device's real IP and delivers traffic to the PLC/HMI/medical terminal.

## 3. Network Solution

| Method | Use Case | Notes |
|--------|----------|-------|
| 4G cellular (recommended) | Sites without wired network, mobile assets, temporary deployments | Use IoT SIM cards; signal 21–30 recommended |
| Wired WAN | Sites with stable broadband / fiber | Lowest latency, best throughput |
| Wi-Fi uplink | Offices, retail outlets, kiosks with existing Wi-Fi | IR302 supports Wi-Fi as WAN (model-dependent) |
| Dual-link backup | Mission-critical sites | Cellular as backup for wired WAN |

## 4. Access Modes Provided by InConnect Service

- **Virtual IP access** — ICS auto-maps each downstream device to a virtual IP under 10.16.0.0/16, avoiding any IP conflict.
- **Real IP access** — Preserves the device's original on-site IP, useful when engineering tools have hard-coded targets.
- **Mesh Network** — Isolates multi-tenant or multi-project access; can be enabled per-network.
- **Star Network** — For telecommuting scenarios where staff need to reach corporate intranet servers via ICS.

## 5. Solution Highlights

1. **One-stop offering** — gateway + connectivity + cloud + application in a single stack from one vendor.
2. **High compatibility** — multi-device, multi-protocol, multi-network unified onboarding.
3. **High reliability** — edge cache, store-and-forward during outages, dual-link backup.
4. **Easy to scale** — batch onboarding, REST API, secondary development friendly.
5. **Low operating cost** — drastically reduces on-site inspection and shortens MTTR.
6. **Security & compliance** — TLS-encrypted transport, role-based access, audit logs, no public IP required at field sites.
7. **Zero public IP dependency** — IR302 always initiates outbound connections; works behind CGNAT, behind private LTE APN, and inside locked-down enterprise networks.
