<div style="width: 100%;height: 100%;background: url(四图/EC300-lorawan.jpg); background-size: 100% 100%;">
  <div style="height:75%;">
    <div style="width:35%; padding: 40px 40px">
      <img src="images/logo.png" alt="logo" />
    </div>
    <div style="font-size: 28px; font-weight: bold; color:#000;text-align: center; margin-bottom: 60px;">
      高安全、高性能、云管理的 LoRaWAN 边缘网关
    </div>
  </div>
  <div style="padding-left: 40px;">
    <div style="font-size: 40px; font-weight: bold; color:#000;margin-bottom: 30px;">
      EC312 系列 LoRaWAN 边缘网关
    </div>
    <div style="text-align: center;">
      <div style="display: flex; flex-wrap: wrap; gap: 16px; ">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· 多链路</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· LoRaWAN</div>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 16px;margin-top:16px">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· 可编程</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px; ">· MQTT</div>
      </div>
    </div>
  </div>
</div>

<div style="page-break-after: always;"></div>

# <span style="color: green;">1. 产品概述</span>

**EC312 是面向工业物联网的工业级 LoRaWAN 可编程边缘网关，支持大规模节点接入与多链路冗余通信。**


**产品特点：**
- **LoRa高容量:** 基于 SX1302，最高支持约 2000 节点接入
- **远距覆盖:** 视距最远可达 15km，支持城区 NLOS 覆盖
- **链路冗余:** 以太网/蜂窝/Wi-Fi 互备，支持双 SIM 故障切换
- **安全可靠:** 支持 Secure Boot、TPM2.0、TrustZone、看门狗与掉电保护
- **开放易集成:** Debian 11 + Docker + 多协议，兼容主流 IoT 云平台

## <span style="color: green;">核心技术指标</span>

|技术指标|规格|
|---|---|
|蜂窝网络|LTE Cat1（按型号支持不同频段）|
|LoRaWAN|支持 LoRaWAN 网关功能，最高约 2000 节点接入|
|云管理|支持 InHand DeviceLive / 公有云接入|
|网络特性|APN、VPDN、CHAP/PAP，支持 Web/Telnet/SSH 配置|
|二次开发|Debian 11 + Docker，支持 Python 应用开发|
|工业/电力协议|DLT645-2007、IEC104|
|尺寸（W × D × H）|145 × 106 × 36 mm|
|重量|339 g|
|接口|2 × FE，Nano SIM ×2，USB2.0，BLE 4.2|
|供电|9~48V DC|
|工作温度|-20 ~ 70 ℃|
|防护等级|IP30|

# <span style="color: green;">2. 产品尺寸</span>

<div style="display: flex; align-items: end; flex-wrap: wrap; justify-content: space-between;row-gap: 16px; ">
  <div style="width: 33%;">
    <img src="images/prod_1.png" alt="正视图" />
    <div style="width: 100%; text-align: center; font-size: 12px;">正视图</div>
  </div>
  <div style="width: 33%;">
    <img src="images/prod_3.png" alt="侧视图" style="width: 55%; display: block; margin: 0 auto;" />
    <div style="width: 100%; text-align: center; font-size: 12px;">侧视图</div>
  </div>
    <div style="width: 33%;">
    <img src="images/prod_2.png" alt="接口图" />
    <div style="width: 100%; text-align: center; font-size: 12px;">接口图</div>
  </div>
  <div style="width: 80%;">
    <div>注意：</div><div>1.所有尺寸单位为毫米（mm）。</div><div>2.所有尺寸均为近似值，<span style="font-weight: bold;">仅供参考</span>。</div><div>3.图示尺寸<span style="font-weight: bold;">不得用于生产加工</span>。</div><div>4.尺寸需符合零件及制造公差要求。</div><div>5.尺寸如有变更，恕不另行通知。</div>
  </div>
</div>

# <span style="color: green;">3. 硬件规格</span>

| 类别/参数 | 规格 |
|--------------------------|------|
| <span style="color: green;">**硬件平台**</span> | |
| CPU | ARM Cortex-A53 @ 1.4GHz |
| RAM | 1GB DDR4（1GB SDRAM / DDR4） |
| FLASH | 8GB eMMC |
| <span style="color: green;">**LoRaWAN**</span> | |
| 基带芯片 | Semtech SX1302 |
| 通道 | 8，半双工 |
| 频段 | RU864 / IN865 / EU868 / US915 / AU915 / KR920 / AS923 / CN470 |
| 最大发射功率 | 27 dBm |
| 接收灵敏度 | -140 dBm（125KHz / SF12） |
| 接入节点 | 2000 |
| 通信距离 | 城区 2 km NLOS 覆盖，视距 LOS 15 km（视环境与天线安装方式） |
| <span style="color: green;">**连接与接口**</span> | |
| 以太网端口 | 2 × 10/100M 以太网 |
| 串口 | 1 × RS-232/485 + 1 × RS-485（带隔离） |
| 按键 | 针孔式复位按键 × 1，可编程按键 × 1 |
| SIM卡座 | Nano SIM × 2 |
| 天线接头 | LTE: SMA × 1，Wi-Fi: SMA × 1，GPS: SMA × 1，LoRaWAN: SMA × 1（北美产品型号 LTE 天线接口：SMA × 1） |
| LED指示灯 | PWR, STATUS, WARN, NET, USER * 4 |
| USB | USB2.0 Type-A |
| TF | 支持 MicroSD，最高可扩展 32GB |
| WiFi | Wi-Fi STA，802.11ac/a/b/g/n，2.4G/5G |
| 蓝牙 | BLE 4.2 |
| GNSS | 卫星定位GPS |
| <span style="color: green;">**电源与功耗**</span> | |
| 输入电压 | 9~48V DC |
| 典型值（OS 空闲态） | 平均功耗 2.5W |
| 掉电保护 | 断电后保持 20s（安全关机） |
| 掉电告警 | 掉电后可发送掉电告警 |
| <span style="color: green;">**机械规格**</span> | |
| 产品尺寸 | 145 × 106 × 36 mm |
| 产品重量 | 339 g |
| 安装方式 | 挂耳、导轨 |
| 防护等级 | IP30 |
| 外壳与散热 | 金属+塑料外壳，无风扇散热 |
| RTC | 支持（纽扣电池备份） |
| 硬件看门狗 | 支持 |
| TPM | 内置 TPM 芯片，TPM v2.0 |
| <span style="color: green;">**环境与认证**</span> | |
| 存储温度 | -40 ~ 85 ℃ |
| 工作温度 | -20 ~ 70 ℃ |
| 环境湿度 | 5~95%（无凝露） |
| 物理特性 | 防震 IEC60068-2-27<br/>振动 IEC60068-2-6<br/>跌落 IEC60068-2-32 |
| EMC指标 | EN61000-4-2，level 3，静电<br/>EN61000-4-3，level 3，辐射电场<br/>EN61000-4-4，level 3，脉冲电场<br/>EN61000-4-5，level 3，浪涌<br/>EN61000-4-6，level 3，传导骚扰抗扰度<br/>EN61000-4-8，&gt;level 2，工频磁场抗扰度，水平方向/垂直方向 400A/m<br/>EN61000-4-12，level 3，震荡波抗扰度 |
| 认证 | CE, FCC, IC, PTCRB |

# <span style="color: green;">4. 软件规格</span>

| 类别/参数 | 规格 |
|--------------------------|------|
| <span style="color: green;">**操作系统**</span> | |
| 操作系统 | Debian 11（Kernel 5.10.168） |
| <span style="color: green;">**LoRaWAN**</span> | |
| LoRaWAN LNS | 内置 LoRaWAN 网络服务器，兼容主流网络服务器（The ThingsStack、ChirpStack 等） |
| LoRaWAN 协议 | LoRaWAN 1.0 / 1.0.2，Class A/B/C |
| <span style="color: green;">**网络特性**</span> | |
| 网络接入 | APN、VPDN |
| 接入认证 | CHAP/PAP |
| 网络制式 | LTE CAT 1 |
| WAN协议 | 静态 IP、DHCP |
| LAN协议 | ARP、Ethernet |
| IP应用 | ICMP、DNS、TCP/UDP、TCP Server、DHCP |
| IP路由 | 静态路由 |
| <span style="color: green;">**安全**</span> | |
| Secure Boot | 支持 |
| Trust Zone | 支持 |
| 网络安全 | 支持防火墙功能 |
| 用户管理 | 支持多级用户权限管理 |
| 数据安全 | 支持防火墙功能 |
| 其他技术 | OpenVPN、IPSec、TPM2.0 |
| <span style="color: green;">**可靠性**</span> | |
| 链路探测 | 心跳检测与自动重连 |
| 内置看门狗 | 设备运行自检技术，设备运行故障自修复 |
| 备份机制 | 链路冗余（有线、蜂窝、Wi-Fi 互为备份） |
| 双卡切换 | 支持双 SIM 链路切换 |
| <span style="color: green;">**数据采集协议（DSA）**</span> | |
| Python二次开发 | 多编程语言开发平台 |
| 工业协议 | Modbus RTU Master/Slave，Modbus TCP Master/Slave，EtherNet/IP，ISO on TCP，OPC UA Client/Server，Mitsubishi MC 3C/3E/3C Over TCP，Mitsubishi CPU Port，FINSUDP，HostLink，PPI |
| Docker | 集成 Docker，支持应用容器化管理 |
| <span style="color: green;">**网络管理**</span> | |
| 配置方式 | Web、Telnet、SSH |
| 升级方式 | Web、FOTA、DFOTA |
| 日志功能 | 支持本地系统日志、远程日志，重要日志掉电保存 |
| 配置备份 | 支持配置文件导入和导出 |
| 远程管理 | 支持 InHand DeviceLive 或 HTTP、HTTPS、Telnet、SSH 等 |
| 平台功能 | 支持基于云的参数配置、容器管理、应用和固件管理 |

# <span style="color: green;">5. 订购信息</span>

## <span style="color: green;">型号规则</span>

**Model code:** EC312-H-\<WMNN\>-\<Lxxx\>

\<WMNN\>: 无线通讯类型 & 模块  
\<Lxxx\>: LoRaWAN 频段版本（如 L868/L915/L470）

## <span style="color: green;">产品型号</span>

<table style="width:100%; table-layout:fixed;">
  <colgroup>
    <col style="width:29%;">
    <col style="width:16%;">
    <col style="width:40%;">
    <col style="width:15%;">
  </colgroup>
  <tr><th>型号</th><th>区域</th><th>&lt;WMNN&gt;: 无线通讯类型 &amp; 模块</th><th>&lt;Lxxx&gt;</th></tr>
  <tr><td style="white-space: nowrap;">EC312-H-FQ53-L868</td><td style="white-space: nowrap;">EMEA</td><td>CAT1<br/>FDD: B1/B3/B7/B8/B20/B28<br/>TDD: B38/B40/B41<br/>GSM: B2/B3/B5/B8</td><td>EU868</td></tr>
  <tr><td style="white-space: nowrap;">EC312-H-FQ33-L915</td><td style="white-space: nowrap;">North <br/>America</td><td>CAT1<br/>FDD: B2/B4/B5/B12/B13/B25/B26<br/>WCDMA: B2/B4/B5</td><td>US915/AS923</td></tr>
  <tr><td style="white-space: nowrap;">EC312-H-FQ53-L915</td><td style="white-space: nowrap;">EMEA</td><td>CAT1<br/>FDD: B1/B3/B7/B8/B20/B28<br/>TDD: B38/B40/B41<br/>GSM: B2/B3/B5/B8</td><td>US915/AS923</td></tr>
  <tr><td style="white-space: nowrap;">EC312-H-LQA3-L470</td><td style="white-space: nowrap;">China</td><td>CAT1<br/>LTE-FDD: B1/B3/B5/B8<br/>LTE-TDD: B34/B38/B39/B40/B41</td><td>CN470</td></tr>
</table>

# <span style="color: green;">6. 联系我们</span>

- **官网：** [映翰通官网](https://www.inhand.com.cn)
- **版权声明：** ©映翰通网络 保留所有权利
