# Mobile Guardian — Electronic Police Remote Monitoring Solution

## I. Solution Overview

### 1.1 Project Background

An intelligent transportation enterprise and a city traffic police department jointly created the "5G+Mobile Guardian" solution to help the traffic police supervision department monitor the surveillance area 24 hours a day. Through remote real-time monitoring, service management levels can be improved, pre-control objectives achieved, and spot inspection plans rationally arranged, making supervision more effective and targeted, promoting various key areas toward "unmanned" and "fewer personnel" operation and management models.

Utilizing 5G network's high bandwidth, low latency, security, and reliability characteristics, front-end images are uploaded in real-time to the monitoring center and mobile devices such as mobile phones, and integrated with existing video surveillance networks to form a unified and coordinated dynamic video command system. As the first line of security defense equipment, surveillance systems have been widely deployed; however, surveillance remote areas often face difficulties in providing power supply and network supply. Complex environmental wiring in locations such as emergency site monitoring and construction site monitoring consumes considerable human and material resources and poses safety hazards.

Therefore, the Mobile Guardian monitoring deployment solution has become the best choice. Built-in batteries plus solar auxiliary power supply can摆脱 many limitations of wired cables, while wireless 5G transmission can be deployed anywhere with operator signal coverage. It is a sentinel in the true sense for traffic police, public security, emergency, security, and stability maintenance fields. Currently, the city traffic police department has deployed 80 5G Mobile Guardians on-site. In the next ten years, with the continuous growth of remote monitoring demand, it is expected that more than 10,000 units will be deployed successively.

### 1.2 Construction Objectives

- Monitor the surveillance area 24 hours a day
- Improve service management levels through remote real-time monitoring
- Achieve pre-control objectives and rationally arrange spot inspection plans
- Make supervision more effective and targeted
- Promote various key areas toward "unmanned" and "fewer personnel" operation and management models
- Upload front-end images to monitoring center and mobile terminals in real-time
- Integrate with existing video surveillance networks to form a unified and coordinated dynamic video command system

### 1.3 Applicable Scenarios

- Electronic police remote monitoring
- Traffic security monitoring
- Emergency site monitoring
- Smart construction site monitoring
- Counter-terrorism, disaster relief site monitoring
- Large event security monitoring
- Oil and natural gas industry monitoring
- Troop training monitoring

## II. Requirements Analysis

### 2.1 Current Equipment Status

- Equipment types: Mobile Guardian integrated equipment (built-in storage battery, solar panels, capture equipment, vehicle model detection, license plate recognition system)
- Communication interfaces: Ethernet, 4G/5G
- Communication protocols: VPDN private network
- Deployment environment: Construction sites, traffic intersections, emergency sites, construction sites, remote monitoring areas, mobile deployment
- Scale: 80 units deployed, expected deployment of more than 10,000 units

### 2.2 Core Requirements

1. **Construction monitoring requirement**: Monitor construction progress and worker safety conditions in real-time through mobile monitoring, quickly issue warnings when abnormalities are detected to ensure life and property safety
2. **Intelligent transportation requirement**: Equipped with new generation information technologies such as vehicle model detection, license plate recognition, and vehicle control to ensure traffic safety, exert traffic infrastructure efficiency, and improve traffic system operation efficiency and management level
3. **Remote maintenance requirement**: Support remote maintenance of equipment, connect with traffic police management platform, providing powerful data support
4. **Network backup requirement**: Support dual SIM card backup to ensure uninterrupted network communication
5. **Scheduled management requirement**: Support scheduled restart function, users can enable as needed
6. **Environmental adaptation requirement**: Equipment complies with full industrial design, capable of stable long-term operation even in harsh environments
7. **Data security requirement**: Support VPDN for seamless integration with traffic departments, ensuring data security
8. **High-speed network requirement**: High bandwidth, low latency, secure, reliable and stable 5G network for real-time fast monitoring of Mobile Guardian operation status

## III. Overall Architecture Design

This solution consists of Mobile Guardian, ER805, and traffic management monitoring center. Mobile Guardians are deployed for real-time monitoring at government law enforcement sites, oil and natural gas industries, traffic security, troop training, counter-terrorism, disaster relief, smart construction sites, large events, and other locations.

The Mobile Guardian connects to ER805 via Ethernet and securely transmits data to the traffic police department platform through the VPDN channel via 4G/5G operator network. Maintenance personnel can directly access on-site routers through the VPDN private network for remote configuration, debugging, and upgrading of the routers.

The Mobile Guardian can provide PC client software, mobile APP, and digital touch screen keyboards for on-site control to grasp real-time traffic information, perform real-time remote monitoring and retrieve video at specified times and locations.

### 3.1 Four-Layer Architecture

![Topology Diagram](./images/40103f00.webp)

1. **Perception Layer**: Mobile Guardian integrated equipment (storage battery, solar panels, capture equipment, vehicle model detection, license plate recognition system)
2. **Network Layer**: Inhand ER805 5G edge router, supporting dual SIM cards, 4G/5G, VPDN private network
3. **Platform Layer**: Traffic management monitoring center, traffic police department platform
4. **Application Layer**: Real-time monitoring, remote configuration debugging upgrading, video retrieval, traffic information grasp, vehicle model detection, license plate recognition

### 3.2 Data Flow

Mobile Guardian (capture/detection) → ER805 router (4G/5G, VPDN encryption) → Traffic police department platform → Monitoring center/mobile APP/PC client

Remote maintenance: Maintenance personnel → VPDN private network → ER805 → Remote configuration/debugging/upgrade

## IV. Network and Access Solution

### 4.1 Networking Method Selection

Adopt 5G/4G high-speed cellular network access, supporting dual SIM card backup, and securely transmit data through VPDN private network channel. Wireless 5G transmission can be deployed anywhere with operator signal coverage.

### 4.2 Edge Gateway Selection Points

**ER805 5G Edge Router Features**:

- Supports dual SIM card backup to ensure uninterrupted network communication
- Supports scheduled restart function, users can enable as needed
- Full industrial design, capable of stable long-term operation even in harsh environments
- Supports VPDN for seamless integration with traffic departments, ensuring data security
- High bandwidth, low latency, secure, reliable and stable 5G network
- 5G high-speed cellular network access, high-speed local area networking
- Supports 5*gigabit ports, can divide VLANs
- Supports gigabit Wi-Fi 1200M, 2.4G and 5G dual-band concurrent
- Industrial design, stable and reliable, providing high availability data transmission services, meeting mobile scenario challenges
- Supports SD-WAN, provides quality data links, achieves load balancing redundancy, link backup, ensuring uninterrupted equipment network communication
- Certified by CE, FCC, IC, PTCRB, AT&T, Verizon, etc., applicable worldwide

## V. Protocol and Data Acquisition Solution

### 5.1 Supported Protocols

- **Network protocols**: 5G, 4G, dual SIM cards, gigabit Ethernet, Wi-Fi 1200M (2.4G and 5G dual-band)
- **Security protocols**: VPDN virtual private network
- **Management protocols**: SD-WAN

### 5.2 Northbound Protocol Support

- Supports VPDN private network access to traffic police department platform
- Supports remote configuration, debugging, and upgrading
- Supports PC client software and mobile APP access

## VI. Solution Highlights Summary

1. **Mobile Guardian functional features**:

   - High intelligent monitoring combat efficiency: Comes with storage battery, solar panels, capture data information supports resumable transfer, achieving 24h uninterrupted monitoring
   - Strong adaptability: Mobile monitoring is not limited by network or power, flexible vehicle body, single person can deploy, more advantageous than wired monitoring for scattered, complex environment areas and environments requiring temporary deployment

2. **High bandwidth low latency**: ER805's high bandwidth, low latency network characteristics provide stable and reliable network channels for Mobile Guardian application scenarios

3. **5G high-speed network**: 5G high-speed cellular network access, high-speed local area networking, supports 5*gigabit ports, can divide VLANs, supports gigabit Wi-Fi 1200M, 2.4G and 5G dual-band concurrent

4. **Dual SIM card backup**: Supports dual SIM card backup to ensure uninterrupted network communication

5. **SD-WAN technology**: Supports SD-WAN, provides quality data links, achieves load balancing redundancy, link backup, ensuring uninterrupted equipment network communication

6. **VPDN security guarantee**: Supports VPDN for seamless integration with traffic departments, ensuring data security

7. **Industrial-grade reliability**: Full industrial design, capable of stable long-term operation even in harsh environments, meeting mobile scenario challenges

8. **Global certification**: Certified by CE, FCC, IC, PTCRB, AT&T, Verizon, etc., applicable worldwide

9. **Flexible deployment**: Built-in battery plus solar auxiliary power supply can摆脱 many limitations of wired cables, while wireless 5G transmission can be deployed anywhere with operator signal coverage

10. **Multi-platform support**: Can provide PC client software, mobile APP, and digital touch screen keyboards for on-site control to grasp real-time traffic information, perform real-time remote monitoring and retrieve video at specified times and locations

---

*Other images:*

![Image 2](./images/831f8c43.jpeg)
![Image 4](./images/39636704.jpeg)
