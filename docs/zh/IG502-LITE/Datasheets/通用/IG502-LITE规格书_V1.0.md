<div style="width: 100%;height: 100%;background: url(images/product_new.png); background-size: 100% 100%;">
  <div style="height:75%;">
    <div style="width:35%; padding: 40px 40px">
      <img src="images/logo.png" alt="logo" />
    </div>
    <div style="font-size: 28px; font-weight: bold; color:#000;text-align: center; margin-bottom: 60px;">
      极简型边缘网关，超高性价比，助力工业数字化
    </div>
  </div>
  <div style="padding-left: 40px;">
    <div style="font-size: 40px; font-weight: bold; color:#000;margin-bottom: 30px;">
      IG502-LITE 系列边缘网关
    </div>
    <div style="text-align: center;">
      <div style="display: flex; flex-wrap: wrap; gap: 16px; ">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· 多网络接入</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· 云管理</div>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 16px;margin-top:16px">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">· 内置DSA</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px; "></div>
      </div>
    </div>
  </div>
</div>

<div style="page-break-after: always;"></div>

# <span style="color: green;">1. 产品概述</span>

**IG502-LITE 是面向工业物联网推出的极简型边缘网关，支持4G接入、边缘数据处理和云端管理。**


**产品特点：**
- **高性价比接入:** 提供4G与有线接入能力，满足基础工业联网需求
- **可靠在线:** 多级链路检测 + 软硬件看门狗，保障通信连续性
- **边缘处理能力:** 支持 Python 二次开发，支持 DSA 零代码/低代码部署
- **协议集成丰富:** 支持 80+ 工业协议，快速实现采集、处理与上云
- **云端统一管理:** 支持 DeviceLive、InConnect、iSCADA 远程管理

## <span style="color: green;">核心技术指标</span>

|技术指标|规格|
|---|---|
|蜂窝网络|LTE Cat1|
|网络接入|APN、VPDN|
|接入认证|CHAP/PAP|
|数据安全|防火墙、OpenVPN、IPSec VPN|
|边缘开发|支持 Python 二次开发|
|云端运维|DeviceLive、InConnect、iSCADA|
|CPU|ARM Cortex-A8 @300MHz|
|内存与存储|512MB RAM，8GB eMMC|
|以太网接口|2 × 10/100Mbps|
|供电与功耗|12~48V DC（防反接），230mA@12V|
|工作温度|-20 ~ 70 ℃|
|防护等级|IP30|

# <span style="color: green;">2. 产品尺寸 & 端子定义</span>

<div style="display: flex; align-items: end; flex-wrap: wrap; justify-content: space-between;row-gap: 16px;">
  <div style="width: 35%;">
    <img src="images/prod_1.png" alt="正视图" />
    <div style="width: 100%; text-align: center; font-size: 12px;">正视图</div>
  </div>
  <div style="width: 15%;">
    <img src="images/prod_3.png" alt="侧视图" />
    <div style="width: 100%; text-align: center; font-size: 12px;">侧视图</div>
  </div>
  <div style="width: 22%;">
    <img src="images/prod_2.png" alt="接口图" />
    <div style="width: 100%; text-align: center; font-size: 12px;">接口图</div>
  </div>
  
  <div style="width: 45%;">
    <div>注意：</div><div>1.所有尺寸单位为毫米（mm）。</div><div>2.所有尺寸均为近似值，<span style="font-weight: bold;">仅供参考</span>。</div><div>3.图示尺寸<span style="font-weight: bold;">不得用于生产加工</span>。</div><div>4.尺寸需符合零件及制造公差要求。</div><div>5.尺寸如有变更，恕不另行通知。</div>
  </div>
</div>


## 7pin 端子定义

<table style="width:78%;">
  <colgroup>
    <col style="width:15%;">
    <col style="width:23%;">
    <col style="width:62%;">
  </colgroup>
  <tr><th align="center">引脚</th><th align="center">定义</th><th align="left">说明</th></tr>
  <tr><td align="center">1</td><td align="center">V+</td><td>电源正极</td></tr>
  <tr><td align="center">2</td><td align="center">V-</td><td>电源负极</td></tr>
  <tr><td align="center">3</td><td align="center">TXD或1A</td><td>串口RS232发送或第一路RS485+</td></tr>
  <tr><td align="center">4</td><td align="center">RXD或1B</td><td>串口RS232接收或第一路RS485-</td></tr>
  <tr><td align="center">5</td><td align="center">GND</td><td>串口RS232信号地</td></tr>
  <tr><td align="center">6</td><td align="center">2A</td><td>第二路RS485+</td></tr>
  <tr><td align="center">7</td><td align="center">2B</td><td>第二路RS485-</td></tr>
</table>

# <span style="color: green;">3. 硬件规格</span>

| 类别/参数 | 规格 |
|--------------------------|------|
| <span style="color: green;">**CPU与存储**</span> | |
| CPU | ARM Cortex-A8 @300MHz |
| RAM | 512MB |
| FLASH | 8GB eMMC |
| <span style="color: green;">**连接与接口**</span> | |
| 以太网端口 | 2 × 10/100Mbps |
| 串口 | RS485×1 + RS232×1，或 RS485×2（见订购信息） |
| 复位按键 | 针孔式复位按键 ×1 |
| SIM卡座 | 标准 SIM x1，单卡 |
| 天线接头 | 4G: SMA×1 |
| LED指示灯 | PWR、STATUS、WARN、ERR、信号强度（3颗）、LTE |
| <span style="color: green;">**电源与功耗**</span> | |
| 输入电压 | 12~48V DC（防反接） |
| 电源接口 | 工业端子 |
| 工作功耗 | 230mA@12V |
| <span style="color: green;">**机械规格**</span> | |
| 产品尺寸 | 110 × 127 × 35 mm |
| 产品重量 | 390 g |
| 安装方式 | 挂耳、导轨 |
| 防护等级 | IP30 |
| 外壳与散热 | 金属，无风扇散热 |
| RTC | 支持（纽扣电池备份） |
| 硬件看门狗 | 支持 |
| <span style="color: green;">**环境与认证**</span> | |
| 存储温度 | -40 ~ 85 ℃ |
| 工作温度 | -20 ~ 70 ℃ |
| 环境湿度 | 5~95%（无凝霜） |
| 物理特性 | 防震 IEC60068-2-27<br/> 振动 IEC60068-2-6<br/> 跌落 IEC60068-2-32 |
| EMC指标 | EN61000-4-2，level 3，静电 <br/> EN61000-4-3，level 3，辐射电场<br/>EN61000-4-4，level 3，脉冲电场<br/>EN61000-4-5，level 3，浪涌<br/>EN61000-4-6，level 3，传导骚扰抗扰度<br/>EN61000-4-8，>level 2，工频磁场抗扰度，水平方向/垂直方向 400A/m<br/>EN61000-4-12，level 3，震荡波抗绕度 |

# <span style="color: green;">4. 软件规格</span>

| 类别/参数 | 规格 |
|--------------------------|------|
| <span style="color: green;">**操作系统**</span> | |
| 操作系统 | 定制版 Linux |
| <span style="color: green;">**网络特性**</span> | |
| 网络接入 | APN、VPDN |
| 接入认证 | CHAP/PAP |
| 网络制式 | LTE Cat1 |
| WAN协议 | 静态IP、DHCP |
| LAN协议 | ARP、Ethernet |
| IP应用 | ICMP、DNS、TCP/UDP、TCPServer、DHCP |
| IP路由 | 静态路由 |
| <span style="color: green;">**安全性**</span> | |
| 用户管理 | 支持多级管理权限 |
| 网络安全 | 防火墙 |
| 数据安全 | OpenVPN、IPSec VPN |
| <span style="color: green;">**可靠性**</span> | |
| 链路探测 | 心跳检测与断线自动连接 |
| 内置看门狗 | 支持设备故障自恢复 |
| <span style="color: green;">**开放式平台与数据采集协议（DSA）**</span> | |
| Python二次开发 | 支持 Python |
| 接入云平台 | 支持AWS、Azure、阿里等云平台 |
| 工业协议 | Modbus RTU/TCP、EtherNet/IP、OPC UA、Mitsubishi MC/CPU、FINS、HostLink、PPI 等 |
| 电力协议 | DLT645-2007、IEC101/104、DNP3.0 |
| 其他协议 | BACnet、CNC 等 |
| 最大采集点数 | 500 |
| <span style="color: green;">**网络管理**</span> | |
| 配置方式 | Web 配置页面 |
| 升级方式 | Web 升级、DM 平台远程升级 |
| 日志功能 | 本地/远程日志，重要日志掉电保存 |
| 配置备份 | 配置导入与导出 |
| 远程管理 | DeviceLive、InConnect |

# <span style="color: green;">5. 订购信息</span>

## <span style="color: green;">型号规则</span>

**Model code:** IG502-LITE-\<WMNN\>-\<D485/NA\>

\<WMNN\>: 无线通讯类型 & 模块

## <span style="color: green;">产品型号</span>

| 型号 | 区域 | 无线制式 | 网口 | 串口 |
|------|------|---------|------|------|
| IG502-LITE-LQA3 | 中国 | LTE-FDD B1/B3/B5/B8；LTE-TDD B34/B38/B39/B40/B41 | 2 × 10/100Mbps | RS232 ×1 + RS485 ×1 |
| IG502-LITE-LQA3-D485 | 中国 | LTE-FDD B1/B3/B5/B8；LTE-TDD B34/B38/B39/B40/B41 | 2 × 10/100Mbps | RS485 ×2 |

# <span style="color: green;">6. 联系我们</span>

- **官网：** [映翰通官网](https://www.inhand.com.cn)
- **版权声明：** ©映翰通网络 保留所有权利
