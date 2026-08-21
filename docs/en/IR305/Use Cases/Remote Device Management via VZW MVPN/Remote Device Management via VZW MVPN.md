# Remote Device Management via VZW MVPN

## Background

In industrial deployments, field devices such as PLCs are distributed across multiple remote sites with no on-site personnel. Each site connects to the Verizon Wireless private network (MVPN / Private APN) through an industrial router (IR305), which is assigned a unique VZW private WAN IP.

Since all routers share the same LAN subnet (e.g., `192.168.2.x`), PLC IP addresses overlap across sites. A central server needs to remotely access each site's PLC for configuration, monitoring, and diagnostics — differentiated by each router's unique WAN IP.

## Objectives

- Enable remote access to field PLCs across all sites without on-site intervention
- Leverage each router's unique VZW WAN IP to traverse NAT and reach PLCs directly
- Support remote configuration, status polling, and fault alerting
- Reduce field inspection costs and eliminate the need for on-site personnel

## Use Cases

- Remote PLC monitoring and management (oil & gas, utilities, water treatment, manufacturing)
- Multi-site deployments with 1 PLC per site, no fixed broadband available
- Central SCADA / HMI platform accessing field devices through cellular NAT
- Reducing field inspection costs with remote diagnostics and configuration

## Network Topology

![Network Topology](./images/topology.jpg)

## Solution: DMZ Configuration

Enable DMZ (Demilitarized Zone) on each IR305 to forward all inbound WAN traffic directly to the LAN-side PLC. Since every router has a unique VZW WAN IP, the central server reaches each site's PLC by targeting the corresponding WAN IP — no per-port mapping needed, and all PLC protocol ports are transparently accessible.

## Configuration

| Parameter | Value |
|-----------|-------|
| Enable DMZ | Enabled |
| DMZ Host | `192.168.2.2` (PLC IP) |
| Source Address Range | Central server IP, e.g. `192.x.x.x/32` |
| Interface | Cellular |

## Traffic Flow

```
Central Server → VZW Private Network → IR305 WAN → DMZ → PLC (192.168.2.2)
```

Access `192.168.11.1` → reaches PLC at Site 1, access `192.168.11.2` → reaches PLC at Site 2, and so on. TCP traffic is supported, and ICMP (ping) is not supported by design.

## Solution Highlights

1. **Zero Field Changes:** No PLC reconfiguration needed — only enable DMZ on the IR305
2. **Simple Deployment:** One rule covers all protocol ports, no per-port mapping required
3. **Private Network Security:** VZW MVPN keeps all traffic off the public internet
4. **Easy to Scale:** Adding a new site only requires deploying an IR305 and enabling DMZ
