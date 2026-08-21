# Chain Store Facility Networking Solution

## I. Solution Overview

### 1.1 Project Background

With the rapid development of chain businesses, chain stores are spread all over the country. The stability of chain store network business is closely related to the headquarters business. How to build a stable, secure, and standardized business network has become the top priority of chain store IT network construction.

Currently, a chain enterprise has a large number of direct-operated stores and franchised stores. Daily network management has become a key task. Network interruption in store business will affect business transactions, causing profit losses to the enterprise, and even bringing poor shopping experiences to customers. Therefore, maintaining network stability and how to quickly locate and restore problems when failures occur are crucial.

The number of chain stores will expand rapidly with the footsteps of the enterprise's rapid development. The IT team needs to complete the networking deployment of numerous stores in a short time, bringing great challenges to the IT team.

Currently, the geographical distribution of chain branch stores is scattered and numerous. Daily operation and maintenance costs are high. Chain enterprises urgently need to solve how to efficiently and real-time manage numerous store networks.

Therefore, Inhand, combining its own advantages, has launched the Xinghan — Cloud Management Network Solution for the application scenario of a chain enterprise's more than 800 chain stores in Wuhan, consisting of ER805 edge router and Xiaoxing Cloud Manager SaaS service, helping the chain enterprise achieve efficient store network management.

### 1.2 Construction Objectives

- Provide high-speed, secure, reliable uninterrupted network connection to achieve real-time communication
- Achieve stable operation of store networks, quickly locate and restore faults
- Quickly complete networking deployment of numerous stores in a short time
- Achieve efficient and real-time management of numerous store networks
- Reduce the workload of large-scale network equipment management

### 1.3 Applicable Scenarios

- Chain store network construction
- Direct-operated store/franchise store networking
- Digital transformation of retail stores
- Branch network management of commercial institutions
- Enterprise SD-WAN networking

## II. Requirements Analysis

### 2.1 Current Equipment Status

- Equipment types: Store TV systems, barcode scanners, charging systems, POS machines, store cameras, employee/customer computers and mobile phones
- Communication interfaces: Ethernet, Wi-Fi, 4G/5G
- Communication protocols: SD-WAN, VPDN
- Deployment environment: Chain stores (more than 800), scattered distribution
- Scale: Large-scale chain store network

### 2.2 Core Requirements

1. **Network stability requirement**: Provide high-speed, secure, reliable uninterrupted network connection to achieve real-time communication
2. **Redundant backup requirement**: Support dual SIM backup, link backup, load balancing, policy routing and other functions
3. **Data security requirement**: Support VPDN to ensure the security of data interaction
4. **Network performance requirement**: Network channels have high stability, low latency, and high bandwidth characteristics
5. **Deployment convenience requirement**: Simple configuration, no need for professional engineers to debug on-site, store employees can install and configure
6. **SD-WAN requirement**: Support SD-WAN to achieve network interconnection and unified management between headquarters and branch stores
7. **Cloud management requirement**: Support cloud management to reduce the workload of large-scale network equipment management

## III. Overall Architecture Design

This solution includes store TV systems, barcode scanners, charging systems, ER805, Xinghan — Cloud Management Platform, and group data center. ER805 edge router serves as the on-site network carrier equipment, quickly accessing the internet through 4G/5G cellular network, wired network, etc., providing stable and efficient business networks.

ER805 can conveniently build efficient local area networks. TV systems, barcode scanners, charging systems, store cameras, and employee/customer computers, mobile phones and other equipment in the store can simply and conveniently access the business local area network through Ethernet or Wi-Fi. The TV system synchronizes product images, real-time prices, promotional activities and other information from the operation center server in real-time; data from barcode scanners, charging systems, POS machines and other equipment are synchronized to the operation center server in real-time; camera images are synchronized to local NVR and operation center in real-time; at the same time, it can provide high-speed wireless network for customers through 5.8G WiFi, thereby providing customers with efficient and comfortable purchasing and checkout experiences. At the same time, ER805 edge router achieves SD-WAN networking with one click through Xinghan — Cloud Management Platform, easily completing network interconnection and unified management between headquarters and branch stores.

### 3.1 Four-Layer Architecture

![Topology Diagram](./images/320f5d3d.webp)

1. **Perception Layer**: Store TV systems, barcode scanners, charging systems, POS machines, store cameras, employee/customer equipment, etc.
2. **Network Layer**: ER805 edge router, supporting 4G/5G, wired network, Wi-Fi, SD-WAN
3. **Platform Layer**: Xinghan — Cloud Management Platform, Group Data Center/Operation Center Server
4. **Application Layer**: Product information synchronization, transaction data processing, video surveillance, customer Wi-Fi service, centralized management

### 3.2 Data Flow

Store equipment → ER805 router → 4G/5G/wired network → Operation center server/data center

SD-WAN networking: Headquarters ←→ ER805 (Xinghan Cloud Platform) ←→ Various branch stores

## IV. Network and Access Solution

### 4.1 Networking Method Selection

Adopt 4G/5G cellular network, wired network and other multi-link access methods, supporting dual SIM switching, wired/wireless link backup, load balancing, policy routing, etc., to ensure uninterrupted equipment network communication.

### 4.2 Edge Gateway Selection Points

**ER805 Edge Router Features**:

- Supports 4G/5G high-speed cellular network, maximum downlink rate 2Gbps, supports SA and NSA networking
- Redundant link design, supports dual SIM switching, wired/wireless link backup, load balancing, policy routing, etc.
- High reliability design, supports multi-link backup, per-flow load balancing and failover
- Real-time detection of link latency, jitter, packet loss, signal strength and other parameters to ensure important business traffic is always forwarded from the optimal link
- Supports gigabit Wi-Fi network, maximum connection rate 1300Mbps, 2.4G and 5.8G WiFi dual-band concurrent, supports AP/STA mode
- Equipped with gigabit Ethernet interface, supports 1WAN/4LAN or 2WAN/3LAN working mode
- Supports VPDN to ensure the security of data interaction
- Supports firewall, access control functions, can set blacklist/whitelist as needed, allow specified IP networking
- Supports SD-WAN, only need to add the device to SD-WAN network on Xiaoxing Cloud Platform, the device can automatically establish tunnels, quickly build secure and reliable network connections between branches
- Cloud-integrated design makes deployment simpler and more convenient, only need simple operations to complete deployment work
- Supports access to Xinghan-Cloud Network Management Platform to achieve centralized remote management deployment, control the site
- Simple configuration, no need for professional engineers to debug on-site, store employees can install and configure

## V. Protocol and Data Acquisition Solution

### 5.1 Supported Protocols

- **Network protocols**: 4G/5G (SA/NSA), wired broadband, Wi-Fi 2.4G/5.8G
- **Networking protocols**: SD-WAN
- **Security protocols**: VPDN, firewall, access control

### 5.2 Northbound Protocol Support

- Supports access to Xinghan-Cloud Network Management Platform
- Supports SD-WAN automatic tunnel establishment
- Supports centralized remote management deployment

## VI. Solution Highlights Summary

1. **High-speed network access**: Supports 4G/5G high-speed cellular network, maximum downlink rate 2Gbps, supports SA and NSA networking

2. **Multi-link redundancy**:

   - Supports dual SIM switching, wired/wireless link backup
   - Supports load balancing, policy routing, etc.
   - Multi-link backup, per-flow load balancing and failover
   - Real-time detection of link latency, jitter, packet loss, signal strength and other parameters to ensure important business traffic is always forwarded from the optimal link

3. **High-speed Wi-Fi**: Supports gigabit Wi-Fi network, maximum connection rate 1300Mbps, 2.4G and 5.8G WiFi dual-band concurrent, supports AP/STA mode, providing high-speed wireless network for customers

4. **SD-WAN networking**: Supports SD-WAN, only need to add the device to SD-WAN network on Xiaoxing Cloud Platform, the device can automatically establish tunnels, quickly build secure and reliable network connections between branches, greatly reducing the difficulty of business inter-access and unified management between enterprise branches

5. **Simple deployment**: Cloud-integrated design makes deployment simpler and more convenient, only need simple operations to complete deployment work. Simple configuration, no need for professional engineers to debug on-site, store employees can install and configure

6. **Cloud management capability**: Supports access to Xinghan-Cloud Network Management Platform to achieve centralized remote management deployment, control the site

7. **Data security guarantee**: Supports VPDN to ensure the security of data interaction. Supports firewall, access control functions, can set blacklist/whitelist as needed

8. **Rich interfaces**: Equipped with gigabit Ethernet interface, supports 1WAN/4LAN or 2WAN/3LAN working mode
