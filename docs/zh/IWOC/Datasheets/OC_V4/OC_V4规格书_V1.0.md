<div style="width: 100%;height: 100%;background: url(images/OC_V4.jpg); background-size: 100% 100%;">
  <div style="height:75%;">
    <div style="width:35%; padding: 40px 40px">
      <img src="images/logo.png" alt="logo" />
    </div>
    <div style="font-size: 28px; font-weight: bold; color:#000;text-align: center; margin-bottom: 60px;">
      智慧配网，状态感知，为供电可靠性赋能
    </div>
  </div>
  <div style="padding-left: 40px;">
    <div style="font-size: 40px; font-weight: bold; color:#000;margin-bottom: 30px;">
     暂态录波型故障指示器——汇集单元(太阳能取电型)
    </div>
    <div style="text-align: center;">
      <div style="display: flex; flex-wrap: wrap; gap: 16px; ">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">高可靠主备电源系统</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">高精度广域对时</div>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 16px;margin-top:16px">
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px;">太阳能取电</div>
        <div style="width: 200px;background-color: #4CAF50; color: white; padding: 8px 8px; border-radius: 6px; font-size: 18px; ">远程维护</div>
      </div>
    </div>
  </div>
</div>

<div style="page-break-after: always;"></div>

# <span style="color: green;">1. 产品概述</span>

智能化配电网线路状态监测系统用于配电线路的实时监测，具备检测线路故障、记录故障波形、故障区段定位、线路隐患预警、电能质量分析等功能，提升了配电系统的可视性，帮助电力公司缩短停电时间、减少停电次数、提高资产寿命，并实现数据驱动的运营决策。该系统由采集单元、汇集单元、智能分析平台和AI算法模块构成，汇集单元是采集单元与智能分析平台交互的桥梁，借助短距无线和远程无线混合组网技术，实现对线路状态的远程监测，高可靠的电源系统与链路保活设计，确保通讯稳定可靠。

# <span style="color: green;">2. 解决方案</span>
智能化配电网线路状态监测系统由三部分构成：**采集单元（端侧）+ 汇集单元（边缘侧）+ 智能分析平台（主站侧）**。采集单元安装于配电线路各监测点，负责采集线路电流、电场等原始数据；汇集单元部署于电杆或塔杆，通过短距无线汇聚多组采集单元数据，经边缘预处理后通过蜂窝网络上送至智能分析平台；ADAIA算法模块对故障录波数据进行深度分析，实现故障反演与溯源。

<div style="text-align: center;">
  <img src="images/image.png" alt="汇集单元方案拓扑" />
  <div style="width: 100%; text-align: center; font-size: 12px;">智能化配电网线路状态监测系统</div>
</div>

<div style="page-break-before: always;"></div>

## <span style="color: green;">特性和优势</span>

### <span style="color: green;">通信稳定可靠，数据传输安全</span>

具备通道监视、通道切换和故障报警功能，支持通道诊断和自愈功能；支持通信中断恢复后数据续传，防止数据丢失；支持电网行业主流加密通讯方式。

### <span style="color: green;">超低功耗</span> 

采用低功耗设计，采用特殊的编程技术，实现了汇集单元与智能分析平台之间，汇集单元与采集单元之间，以极低功耗实时双向通信。

### <span style="color: green;">BDS高精度授时</span>  

内置北斗授时模块实现广域时间同步，再使用短距无线给采集单元进行授时，可为遥信、遥测和录波数据提供精确绝对时标。

### <span style="color: green;">安全便利的免维护设计</span>

* 具备远程维护与升级功能，支持对多个终端批量、逐个的自动维护或升级，操作安全简便；支持手机App进行安装诊断；
* 机箱坚固防锈，配合密封圈、防水接头，实现IP55防尘防水等级，确保在户外长时间安全稳定运行；

### <span style="color: green;">三相合成零序电流、电场信号，接地故障就地精准检测、定位</span>

通过三相合成获取暂态零序电流、电场信号，可实现接地故障就地精准检测、定位，同时将故障演变过程中的录波数据上传至主站系统，用于线路故障分析、反演及溯源。

### <span style="color: green;">高可靠电源系统</span>

采用太阳能电源板作为主电源，同时采用免维护长寿命可充电蓄电池作为备用电源。在有太阳能供电的情况下，优先使用太阳能电源板供电；在没有太阳能的情况下，使用备用电源供电，备用电源可以支持汇集单元连续工作15天（与选择的备用电池容量相关）。采用弱光性太阳能电池，并结合最大功率追踪算法，保证在弱光照条件下的也能获取能量。

<div style="page-break-before: always;"></div>

# <span style="color: green;">3. 产品尺寸</span>

<div style="display: flex; align-items: end; flex-wrap: wrap; justify-content: space-between;row-gap: 16px;">
  <div style="width: 45%;">
    <img src="images/image-3.png" alt="产品尺寸图" />
    <div style="width: 100%; text-align: center; font-size: 12px;">尺寸（长x宽x高）：400mm x 406mm x 420m</div>
  </div>
  <div style="width: 45%;">
    <div>注意：</div><div>1.所有尺寸单位为毫米（mm）。</div><div>2.所有尺寸均为近似值，<span style="font-weight: bold;">仅供参考</span>。</div><div>3.图示尺寸<span style="font-weight: bold;">不得用于生产加工</span>。</div><div>4.尺寸需符合零件及制造公差要求。</div><div>5.尺寸如有变更，恕不另行通知。</div>
  </div>
</div>

# <span style="color: green;">4. 技术指标</span>

| 规格 | 参数 | 
| :--- | :--- |
|**适用的电力系统**| |
|额定功率| 50Hz|
|额定电压|6~35KV|
|**蜂窝通信指标**|  |
|网络接入|支持无线DDN（APN）/VPDN专网|
|网络认证|支持CHAP、PAP认证|
|网络制式|⽀持FDD LTE：Band 1/3/8<br>⽀持TDD LTE：Band 38/39/40/41<br>⽀持DC-HSPA+/HSPA+/HSPA/WCDMA：Band 1/5/8/9<br>⽀持TD-SCDMA：Band 34/39<br>⽀持GSM/GPRS/EDGE：1800 MHz/900 MHz|
|UIM/SIM卡|3V，翻盖式卡座安装|
|**BDS授时**|  |
|首次启动时间|35s|
|再次启动时间|1s|
|授时精度|1μs|
|天线增益|26dB~28dB|
|**通讯与安全**|  |
|通讯规约|⽀持 DL／T634.5 101-2002、DL／T634.5 104-2002 、DNP3<br>支持映翰通OVDP远程维护协议|
|通讯安全|支持电力行业主流安全通讯方式|
|设备管理安全|支持密码+硬件Key的登录验证<br>支持角色分类和权限控制：管理员，维护员|
|本地运维通讯方式|串口、蓝牙|
|**短距通信指标**|  |
|工作频率|470~510MHz|
|通信距离|≤50m|
|发射功率|≤20mW（13dBm）|
|通信速率|250kbps|
|网络拓扑|星形|
|接收灵敏度|≥-100dBm
|方向性|全向|
|**取能与功耗**|  |
|主电源|太阳能电池板供电|
|电池|免维护长寿命可充电蓄电池|
|平均休眠功耗（离线、系统休眠）|≤ 1mA@12V|
|平均待机功耗（在线、无通信）|≤15mA@12V|
|平均运行功耗（在线、定期通信）|≤20mA@12V|
|最大运行功耗（在线、持续通信）|≤100mA@12V|
|设计寿命|＞8年|
|**结构参数**|  |
|尺寸|406mmx420mmx400mm|
|重量|≤10kg|
|机械强度|振动1级、倾斜跌落1米|
|防护等级|IP55|
|**环境适应性**|  |
|工作温度|-40~+70°C|
|存储温度|-40~+85°C|
|环境相对湿度|5%~95%（无凝露）|
|海拔|≤4000m|
|阻尼振荡磁场抗扰度|5级|
|静电放电抗扰度|4级|
|射频电磁场辐射抗扰度|4级|
|快速瞬变脉冲群抗扰度|4级|
|浪涌冲击抗扰度|4级|
|脉冲磁场抗扰|5级|
|工频磁场抗扰度|5级|
|临近干扰试验|100mm|

# <span style="color: green;">5. 订购信息</span>

## <span style="color: green;">型号规则</span>

**Model code:** JYL-FF 系列型号编码由 **类型标识代码 + 厂商代码 + 特性代码** 三部分组成

<table style="width:100%; table-layout:fixed; font-size:11px;">
  <tr><th>型号</th><th>类型</th><th>供电/安装</th><th>网络/频率</th><th>电池</th><th>取电</th><th>加密</th><th>启动</th><th>匹配采集单元</th></tr>
  <tr><td style="white-space: nowrap;">JYL-FF</td><td>H：汇集单元</td><td>D：电杆安装/太阳能</td><td>O：CAT1/50Hz/470MHz<br/>L：CAT4/50Hz/470MHz<br/>B：CAT4/50Hz/470MHz/BDS</td><td>A：7.2 Ah 铅酸<br/>B：12 Ah 铅酸<br/>C：40 Ah 磷酸铁锂<br/>D：40 Ah 胶体<br/>E：12 Ah 磷酸铁锂</td><td>2：20 W<br/>3：30 W<br/>N：无太阳能<br/>X：20 W+AC220V</td><td>S：国网标准<br/>N：无加密<br/>V：南网 VPN<br/>H：湖南<br/>Z：浙江</td><td>F：电场启动<br/>V：零序电压启动<br/>L：本地研判</td><td>A：AI/LT<br/>M：MT<br/>S：SE<br/>CS：CSP</td></tr>
</table>

**订购示例**：`JYL-IH-HD-LB2SFA`
> 映翰通版汇集单元，电杆安装/太阳能取电，LTE CAT4 通信，适用 50 Hz 的 10 kV 线路，短距频率 470 MHz，配 12 Ah 铅酸电池，20 W 太阳能板，含标准版加密芯片，支持电场启动，匹配 AI/LT 版高精度采集单元。

<div style="page-break-before: always;"></div>

# <span style="color: green;">6. 联系我们</span>

- **官网：** [映翰通官网](https://www.inhand.com.cn)
- **版权声明：** ©映翰通网络 保留所有权利

---
