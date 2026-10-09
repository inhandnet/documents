# EC312 CAN-to-AWS 解决方案

**产品：** InHand EC312 边缘计算网关（Edge Computing Gateway）

**应用场景：** 采集 CAN 总线数据并转发至 AWS IoT Core

---

## 1. 方案概述

### 1.1 背景

随着工业物联网（IIoT，Industrial IoT）、智能工厂（Smart Factory）、智能移动（Smart Mobility）以及智能运维（Smart Operations）的快速发展，大量现场设备（发动机、发电机、车辆、传感器、控制器）通过 **CAN 总线（Controller Area Network，控制器局域网）** 进行通信。这些数据资产通常被困在本地总线中，难以被上层云应用调用。传统网关在现场环境中往往力不从心，原因包括：无法原生解码 CAN 帧、缺乏边缘侧脚本能力，或无法安全地接入 AWS 等公有云。

本方案采用 **InHand EC312 边缘计算网关** 作为“车载计算机”，实现以下功能：

- 从本地 CAN 总线读取原始 CAN 帧；
- 通过 Python 应用程序解码并标准化数据；
- 利用内部 MQTT 消息总线以及内置的 **Device Supervisor（DSA）** 虚拟控制器缓存数据；
- 最终通过 TLS/X.509 安全地将数据发布到 **AWS IoT Core**，以便进行存储、分析和可视化。

### 1.2 目标

- 实时采集现场设备的 CAN 总线数据；
- 在边缘侧解码、结构化并标准化 CAN 帧；
- 以最小延迟和最低蜂窝流量将数据推送至 AWS IoT Core；
- 实现边缘网关的远程配置、远程诊断和远程升级；
- 为客户提供灵活的 Python 运行时，支持自定义协议解析；
- 提供安全、可靠、低运营成本的现场部署。

### 1.3 应用场景

EC312 + DSA + AWS 模式适用于任何需要将 CAN 总线数据接入公有云的项目：

- **商用车辆 / 车队远程信息处理（Telematics）** — 发动机 ECU（Engine Control Unit，电子控制单元）、变速箱、制动系统、燃油系统（J1939、OBD-II）；
- **非公路与工程机械** — 挖掘机、装载机、起重机、农用拖拉机；
- **发电与发电机组** — 带 CAN/J1939 接口的柴油发电机控制器；
- **工业机械** — 基于 CAN 的数控机床（CNC）、压力机、压缩机和水泵等 PLC 驱动设备；
- **电动汽车充电与电池管理** — BMS（Battery Management System，电池管理系统）、充电桩 CAN 报文；
- **船舶与轨道交通车辆的远程信息处理**；
- **售后传感器集成** — 在 CAN 总线上广播数据的差压、振动、温度传感器。

> **本手册参考现场示例：** 某 **差压（DP，Differential Pressure）传感器** 在 CAN ID `0x18FF0155` 上广播压力和温度数据。EC312 通过 `can2` 接口读取，将其转换为 bar / °C，并转发至 AWS IoT。

---

## 2. 需求分析

### 2.1 现场侧情况

| 项目 | 典型值 |
|---|---|
| 设备类型 | 带 CAN 接口的 ECU、传感器、控制器 |
| 通信接口 | CAN 2.0A/B，可选 Modbus/Ethernet |
| 通信协议 | 原始 CAN、J1939、OBD-II、厂商自定义协议 |
| 部署环境 | 车辆 / 户外 / 工业机柜 |
| 供电 | DC 9–36 V（符合 EC312 输入范围） |
| 网络连接 | 4G/LTE 蜂窝为主，以太网为备 |

### 2.2 核心需求

1. **采集** — 实时读取 CAN 帧，不丢失消息。
2. **边缘处理** — 在边缘侧解码物理量（bar、°C、RPM 等），过滤噪声，丢弃冗余帧。
3. **网络** — 4G 为主上行链路，流量消耗低，支持自动重拨。
4. **云集成** — 安全接入 AWS IoT Core，支持 X.509 双向 TLS（mTLS）。
5. **远程运维（O&M，Operation and Maintenance）** — 通过 InHand Device Manager 实现远程配置、远程诊断和远程固件升级。
6. **安全** — 加密传输、基于证书的身份认证、基于角色的本地 Web 访问控制。

---

## 3. 整体架构

### 3.1 逻辑架构（四层）

1. **感知层** — CAN 传感器、ECU、控制器；
2. **边缘层** — EC312，运行 Python 应用 + Device Supervisor（虚拟控制器 + AWS IoT 北向接口）；
3. **网络层** — 4G/LTE 蜂窝（主链路）和以太网（备份链路）；
4. **云/应用层** — AWS IoT Core、AWS Rules Engine，以及下游服务（Timestream / S3 / Lambda / QuickSight 等）。

### 3.2 方案拓扑

![方案拓扑 — EC312 内部数据流](images/image1.png)

```
CAN 传感器 (0x18FF0155)
        │  CAN 2.0B (can2)
        ▼
┌───────────────────────── EC312 (边缘) ─────────────────────────┐
│                                                                │
│   Python 应用  ──►  内部 MQTT 代理  ──►  虚拟控制器            │
│   (python-can)     127.0.0.1 : 9105        (DSA)             │
│                                                                │
└──────────────────────────────┬─────────────────────────────────┘
                               │ MQTT over TLS（北向）
                               ▼
                        AWS IoT Core（云端）
                               │
                               ▼
              Rules Engine ► Timestream / S3 / Lambda / 仪表盘
```

### 3.3 数据流（南 → 北）

1. 现场 CAN 传感器在总线上广播一帧 CAN 数据；
2. EC312 的 `can2` 套接字接收该帧，Python 应用按 `arbitration_id` 进行过滤；
3. Python 应用解码有效载荷（例如压力 / 温度），并转换为物理单位；
4. Python 应用将 JSON 负载发布到 Device Supervisor 的内部 MQTT 代理主题 `ds2/eventbus/south/read/{driverServiceId}`；
5. **虚拟控制器（Virtual Controller）** 接收该测量值并存储为标签（例如 `pressure`）；
6. DSA 的 **AWS IoT 北向接口** 通过 TLS 将标签值发布到已配置的 AWS IoT 主题；
7. AWS IoT Core 将消息转发给订阅者 / Rules Engine，以进行存储和可视化。

---

## 4. 网络与连接设计

### 4.1 上行链路选择

| 选项 | 推荐使用场景 |
|---|---|
| 4G/LTE | 车辆、移动资产、偏远站点 — **本方案首选** |
| 以太网（WAN） | 具备有线互联网的固定安装 — 备份或替代方案 |
| Wi-Fi | 本地调试、工厂 Wi-Fi |
| 双 SIM（视型号而定） | 需要运营商冗余的关键任务车队 |

### 4.2 选择 EC312 的理由

- **原生 CAN 支持** — 内置 CAN 接口（本案例使用 `can2`），可通过 Linux 的 `socketcan` 直接访问。
- **开放的 Linux 边缘操作系统** — root SSH、`apt`、Python 3，完整支持 `python-can` / `paho-mqtt`。
- **Device Supervisor（DSA）** — 内置工业协议与云连接器框架（Modbus、OPC UA、MQTT、AWS IoT、Azure IoT 等）。
- **工业级设计** — DC 9–36 V 宽电压、宽温、车载级。
- **远程运维** — 通过 InHand Device Manager 云端实现大规模车队配置和 OTA（Over-The-Air）升级。

---

## 5. 数据采集与协议

### 5.1 南向（现场 → 边缘）

- CAN 2.0A / 2.0B（本案例：扩展 ID `0x18FF0155`）
- Modbus RTU / TCP、OPC UA、自定义串口 — 可通过 DSA 驱动或自定义 Python 应用支持
- 标准汽车 / 工业协议：J1939、OBD-II、NMEA 2000

### 5.2 北向（边缘 → 云端）

- **AWS IoT Core**（本案例） — MQTT + X.509 双向 TLS
- DSA 支持的其他云平台：Azure IoT Hub、阿里云物联网平台、通用 MQTT 代理、HTTP REST
- 自定义应用内部接口：**MQTT 消息总线** 位于 `127.0.0.1:9105`（用户名 `inhand` / `inhand`）

### 5.3 解码后的示例负载

```json
{
  "controllers": [
    {
      "name": "con1",
      "version": "d3b0c5fc05cb72e7759c95f346e29f8d",
      "health": 1,
      "timestamp": 1747800000,
      "measures": [
        {
          "name": "pressure",
          "health": 1,
          "timestamp": 1747800000,
          "timestampMsec": 1747800000123,
          "value": 3.27
        }
      ]
    }
  ]
}
```

---

## 6. 安全

- EC312 与 AWS IoT Core 之间采用 TLS 1.2 + X.509 双向认证（mTLS）
- AWS IoT 策略（Policy）将设备限制在其专属 MQTT 主题内
- 本地 Web 管理通过用户名 / 密码保护（默认 `adm` / `123456` — **必须修改**）
- SSH 访问仅限制在边缘侧 LAN 端口
- 通过网关的 `Services → Configuration Management` 进行配置备份 / 恢复
- 通过 InHand Device Manager 实现远程升级与审计

---

## 7. 方案亮点

1. **CAN 原生边缘** — 直接基于内核级 CAN 套接字，无需额外 USB 适配器。
2. **边缘 Python 运行** — 完整 Linux + Python 3 + `python-can` + `paho-mqtt`；客户可部署自己的解码器。
3. **解耦架构** — Python 应用 ⇄ 内部 MQTT ⇄ 虚拟控制器；任何客户能用 Python 解析的协议都可复用该流程。
4. **一键上云** — Device Supervisor 内置 AWS IoT 北向接口：只需粘贴端点 + X.509 证书，无需额外胶合代码。
5. **车队就绪** — 通过 InHand Device Manager 为成百上千台 EC312 提供远程运维。
6. **车载级** — 宽电压、宽温，适用于车载和户外机柜环境。

---

## 8. 物料清单（每站点）

| # | 项目 | 说明 |
|---|---|---|
| 1 | InHand EC312 边缘计算网关 | 带 CAN、4G/LTE、Linux |
| 2 | SIM 卡 | 按区域选择运营商；按需配置 APN |
| 3 | 4G 天线 | 主天线（及适用时的辅助天线） |
| 4 | 电源 | DC 9–36 V |
| 5 | CAN 线束 | DB9 或端子接线至 CAN 总线 |
| 6 | AWS IoT Core 账户 | 端点、Thing、X.509 证书、策略 |

---
