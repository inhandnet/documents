# Retail Store Connectivity Solution

## 1. Solution Overview

### 1.1 Project Background

As chain retailers expand nationwide, network reliability directly impacts core in-store operations — POS transactions, video surveillance, and real-time data synchronization. A single-link wired WAN failure can disrupt checkout experiences and cause revenue loss. This solution addresses two critical challenges: keeping every retail store **always online** through automatic WAN + 5G Cellular failover, and enabling headquarters IT teams to **remotely manage** hundreds of stores from a single platform.

### 1.2 Objectives

- Seamless WAN + 5G Cellular failover with zero business interruption
- Plug-and-play deployment — store staff can install without on-site engineers
- Centralized remote management via InCloud Manager for real-time visibility
- Secure data transmission with VPN encryption and multi-layer firewall

### 1.3 Use Cases

- Chain retail stores / convenience stores / supermarkets
- Franchised and directly-operated store network standardization
- Distributed store centralized O&M management

---

## 2. Requirements Analysis

### 2.1 Current Device Landscape

| Item | Description |
|------|-------------|
| Device Types | POS terminals, barcode scanners, payment systems, digital signage, IP cameras, staff/customer devices |
| Interfaces | Ethernet, Wi-Fi, 4G/5G |
| Deployment | Indoor retail stores, geographically distributed |
| Scale | Large-scale (hundreds to thousands of stores) |

### 2.2 Core Requirements

1. **Always-on Connectivity** — Auto-failover to 5G Cellular when wired WAN degrades or fails; auto-failback when restored
2. **Easy Deployment** — Store staff self-installation; zero-touch provisioning via cloud
3. **Centralized Management** — HQ IT monitors all stores in real time; remote troubleshooting without site visits
4. **Data Security** — VPN tunnels and firewall policies to protect transaction data
5. **High-Performance Wi-Fi** — Stable wireless access for staff terminals and customer devices

---

## 3. Architecture Design

### 3.1 Four-Layer Architecture

| Layer | Components |
|-------|------------|
| **Perception** | POS terminals, barcode scanners, payment systems, digital signage, IP cameras, staff/customer devices |
| **Network** | FWA02 (Wired WAN primary + 5G Cellular backup, Wi-Fi 6) |
| **Platform** | InCloud Manager SaaS, HQ Data Center / Operations Center |
| **Application** | Transaction processing, product info sync, video surveillance, guest Wi-Fi, centralized O&M |

### 3.2 Data Flow

```
In-Store Devices
   └→ FWA02
         ├─ Primary : Wired WAN (Broadband) ──────────┐
         └─ Backup  : 5G Cellular (Auto Failover) ─────┴→ HQ Data Center / Ops Server
                                                                    ↕
                                                        InCloud Manager (Cloud)
                                                                    ↕
                                                          HQ IT Management Console
```

**Failover Logic:** FWA02 continuously monitors WAN link quality (latency, jitter, packet loss). Upon detecting degradation or failure, it automatically switches to 5G Cellular. Once the wired link recovers, it fails back automatically — no manual intervention required.

---

## 4. Network & Access Solution

### 4.1 Connectivity Design

**Primary Link — Wired WAN:** 2.5 GbE broadband connection delivering high bandwidth and low latency for all daily store operations.

**Backup Link — 5G Cellular:** 5G SA/NSA with up to 4.76 Gbps downlink / 1.25 Gbps uplink, with automatic fallback to 4G LTE Cat 19 (1.6 Gbps DL). Dual Nano SIM + eSIM support enables flexible carrier switching for maximum backup reliability.

### 4.2 FWA02 Device Specifications

| Category | Specification |
|----------|---------------|
| **Ethernet** | 2 × 2.5 GbE RJ45, WAN/LAN switchable |
| **5G Speed** | DL 4.76 Gbps / UL 1.25 Gbps (SA & NSA) |
| **4G Fallback** | LTE Cat 19, DL 1.6 Gbps / UL 200 Mbps |
| **SIM** | 1 × eSIM + 2 × Nano SIM (hot-plug) |
| **Wi-Fi** | Wi-Fi 6 (802.11ax), 2.4G + 5.8G dual-band, up to 3600 Mbps |
| **Max Users** | 220 devices (128 Wi-Fi) |
| **Firewall Throughput** | 2 Gbps |
| **Link Monitoring** | Real-time latency, jitter, packet loss detection |
| **VPN** | IPSec VPN, L2TP VPN |
| **Firewall** | MAC / IP / port / protocol filtering, access control, port mapping |
| **Working Temp.** | -10°C to 50°C |
| **Certifications** | FCC, IC, PTCRB, Verizon, T-Mobile, CE |
| **Warranty** | 3 years |

---

## 5. Cloud Management — InCloud Manager

FWA02 natively integrates with **InHand InCloud Manager**, a SaaS platform for centralized management of distributed retail store networks.

| Feature | Description |
|---------|-------------|
| **Centralized Dashboard** | Single-pane view of all store devices, interface status, and traffic |
| **Zero-Touch Deployment** | Devices auto-register to the cloud upon power-on — no on-site configuration needed |
| **Real-Time Monitoring** | Link latency, jitter, packet loss, throughput, and cellular signal (RSSI / RSRP / RSRQ / SINR) |
| **Alerting** | Email alerts for device offline, link switchover, and abnormal events |
| **Remote O&M** | Web UI / CLI remote access; Ping / Traceroute / packet capture for remote diagnostics |
| **Batch Management** | Bulk firmware upgrade and configuration push across hundreds of stores |
| **Config Backup** | Import / export configuration templates for rapid store rollout replication |

---

## 6. Security

| Security Capability | Implementation |
|---------------------|----------------|
| Encrypted Transmission | IPSec / L2TP VPN tunnels between stores and HQ data center |
| Access Control | Multi-dimensional firewall filtering by MAC, IP, port, and protocol |
| Wi-Fi Security | Enhanced Wi-Fi security; staff and guest networks logically isolated |
| Self-Recovery | Built-in software and hardware watchdog for autonomous fault recovery |

---

## 7. Solution Highlights

| # | Highlight | Description |
|---|-----------|-------------|
| 1 | **Always-On Connectivity** | Wired WAN + 5G Cellular dual-link failover; zero-perception switchover for business continuity |
| 2 | **Plug-and-Play** | Store staff self-install; zero-touch cloud onboarding — no engineer site visits |
| 3 | **High-Speed 5G Backup** | Up to 4.76 Gbps downlink backup ensures video, POS, and sync are unaffected during failover |
| 4 | **Wi-Fi 6 Coverage** | Dual-band 3600 Mbps; staff and guest traffic served concurrently without interference |
| 5 | **InCloud Centralized Management** | Real-time monitoring, zero-touch deployment, and batch O&M for large-scale store networks |
| 6 | **Comprehensive Security** | VPN encryption + multi-layer firewall + network isolation protects all transaction data |
| 7 | **Broad Carrier Certification** | FCC / IC / PTCRB / Verizon / T-Mobile / CE certified for global carrier compatibility |
