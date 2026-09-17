# QA — CR202 Portable Router
**InHand Networks | Team C AI Knowledge Base | Tech Support Transformation**

---

## Q1. CR202 won't power on — what should I check?

**Category:** Hardware | **Product:** CR202 | **Screenshot:** No

The CR202 requires a deliberate button press to power on:

1. Press and **hold** the power button for **3 seconds** until the LEDs light up.
2. A brief tap will not power the device on — it must be held for at least 3 seconds.
3. If no LEDs appear after holding the button, check:
   - Is the battery charged? Connect via USB-C and try again.
   - Is the USB-C cable and charger working? Try a different cable and charger (use a standard 5V/2A USB-C charger — not a laptop charger with proprietary voltages).
4. If the battery LED flashes red immediately, the battery is critically low. Continue charging before powering on.

**Tags:** `#CR202` `#powerOn` `#battery` `#hardware` `#setup`

---

## Q2. CR202 battery LED is red or the device won't charge — how do I fix it?

**Category:** Hardware | **Product:** CR202 | **Screenshot:** No

Battery and charging issues on the CR202:

- **Red battery LED while charging:** Usually indicates battery level is below 20%. Continue charging — the LED should turn green once fully charged. 
- **Won't charge / battery won't hold charge:** Try a different USB-C cable or power adapter.
- **Battery LED flashes red and device won't power on:** Battery may be deeply discharged. Leave connected to a charger for 30–60 minutes.

> **Note:** The CR202 uses a standard USB-C port.  View battery status at **Status > Power** in the web GUI.

**Tags:** `#CR202` `#battery` `#charging` `#USB-C` `#hardware`

---

## Q3. How do I access the CR202 web GUI when my laptop has no Ethernet port?

**Category:** Web GUI | **Product:** CR202 | **Screenshot:** No

If your laptop has no Ethernet port:

1. Power on the CR202 — it broadcasts a default Wi-Fi SSID (printed on the device label).
2. Connect your laptop's Wi-Fi to the CR202's Wi-Fi SSID.
3. Open a browser and go to `http://192.168.2.1`.
4. Log in with `adm` and the password on the device label.

**Tags:** `#CR202` `#webGUI` `#WiFi` `#access` `#noEthernet`

---

## Q4. How do I configure or change the Wi-Fi name (SSID) and password on the CR202?

**Category:** Wi-Fi | **Product:** CR202 | **Screenshot:** Yes

1. Log in to the CR202 web GUI at `http://192.168.2.1`.
2. Go to **Network > WLAN**.
3. Edit the **SSID** field to change the Wi-Fi name.
4. Change the **Security** type (recommend WPA2-PSK) and update the **Password**.
5. Click **Apply**. Wi-Fi clients will need to reconnect using the new credentials.


**Tags:** `#CR202` `#WiFi` `#SSID` `#password` `#WPA2`

---

## Q5. CR202 is not connecting to cellular / shows cellular registered but no internet

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

Troubleshoot CR202 cellular connectivity:


1. **Check profile:** Go to **Network > Cellular** and verify **Nano SIM Network Provider** or **eSIM Network Provider**, select the correct carrier based on the SIM
2. If a customized APN is needed for your SIM, edit the APN at **Profiles** section at the bottom of the **Network > Cellular** page. Then select the profile accordingly at **Nano Network Provider** or **eSIM Network Provider**. For example, **Index 1** at **Profile** section is the **Profile 1** at **Nano Network Provider**. **Index 2** at **Profile** section would be the **Profile 2** at **Nano Network Provider**
3. **Nano-SIM vs eSIM:** The CR202 has both a physical nano-SIM slot and a Verizon embedded eSIM. If the nano-SIM is deactivated, switch the **Main SIM** to **eSIM**.
4. Upgrading the FW to the latest Version.
5. The FW download page for **CR202-Lite** https://www.inhand.com/en/resources-center/#/EnterpriseNetwork/InPortableRouter/CR202-Lite
6. The FW download page for **CR202-Pro** https://www.inhand.com/en/resources-center/#/EnterpriseNetwork/InPortableRouter/CR202-Pro


**Tags:** `#CR202` `#cellular` `#noInternet` `#SIM` `#eSIM` `#APN`

---

## Q6. Verizon changed the APN from vzwinternet to V5GA01INTERNET and the CR202 stopped working

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

This is a known issue when Verizon migrates accounts to 5G plans:

1. Log in to the CR202 web GUI.
2. Go to **Network > Cellular**.
3. At **Profiles** section at the bottom, edit **APN** as **V5GA01INTERNET**. 
4. Then select the profile accordingly at **Nano Network Provider** or **eSIM Network Provider**. For example, **Index 1** at **Profile** section is the **Profile 1** at **Nano Network Provider**. **Index 2** at **Profile** section would be the **Profile 2** at **Nano Network Provider**
5. Click **Apply**

**Tags:** `#CR202` `#Verizon` `#APN` `#V5GA01INTERNET` `#5G`

---



## Q7. End devices cannot connect to CR202 via Wi-Fi or Ethernet after a factory reset — what is wrong?

**Category:** Web GUI | **Product:** CR202 | **Screenshot:** No

After a factory reset, the CR202 returns to default settings. If end devices still can't connect:

1. Ensure the device fully completed the reset — all LEDs should cycle and the device should reboot.
2. Reconnect to the default Wi-Fi SSID (listed on the device label or Quick Start guide).
3. Wait 60–90 seconds after boot before trying to connect.
4. If using Ethernet, connect directly to a LAN port (not the WAN port if one is assigned).
5. Default LAN IP: `192.168.2.1`; default DHCP range is `192.168.2.100–200`.

**Tags:** `#CR202` `#factoryReset` `#WiFi` `#Ethernet` `#DHCP` `#default`

---

## Q8. CR202 SIM failure — fixed after a reboot. Is this expected?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

Transient SIM detection errors can occur after firmware updates, power interruptions, or rarely during normal operation. A reboot (`System > Reboot`) typically resolves them by re-initializing the modem.

If SIM failures recur repeatedly:
1. Reseat the SIM card (power off first).
2. Try a different SIM to rule out a faulty card.
3. Check for firmware updates.
4. If recurring after all steps, the SIM slot contacts may be worn — contact InHand support for RMA evaluation.



**Tags:** `#CR202` `#SIM` `#failure` `#reboot` `#cellular` `#modem`

---

## Q9. I tried to log in to my CR202 with the default username and password but it says login failed — what should I check?

**Category:** Web GUI | **Product:** CR202 | **Screenshot:** No

Default credentials depend on which batch of CR202 you received:

1. **Always check the label on the back of the device first.** The login username and password are printed there. This is the authoritative source, not the booklet or packaging.
2. **Newer CR202 batches** ship with a **unique per-unit password** printed on the label. Don't assume a standard default.
3. **Older batches** used a standard default, but even then, the label on the back is still the place to look — it will match.


**Tags:** `#CR202` `#defaultCredentials` `#webGUI` `#login` `#factoryReset`

---

## Q10. The Global icon LED on my CR202 keeps blinking and the device can't reach the internet — what does this mean?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

A blinking Global icon LED indicates the cellular connection has not been established. If it stays blinking instead of going solid, the device is trying to attach to the cellular network but failing. Common causes:

1. **SIM card not active or out of service.** Confirm with your carrier that the SIM is activated and the data plan is current.
2. **Poor cellular signal at the device's location.** Log in at `http://192.168.2.1` and go to **Status > Modem** to check RSRP (Received Power). If RSRP is below -100 dBm, the signal is weak — move the device nearer a window or use an external antenna via the SMA connector.
3. **Incorrect APN.** Confirm the APN with your carrier and set it under **Network > Cellular**. For some carriers the APN needs to be entered manually instead of relying on auto-detection.


**Tags:** `#CR202` `#cellular` `#LED` `#RSRP` `#APN` `#troubleshooting`


---

## Q11. I need to reach an end device behind my CR202 (e.g. 192.168.1.80) from the public internet — how do I set up port forwarding?

**Category:** Port Mapping | **Product:** CR202 | **Screenshot:** No

Port forwarding on the CR202 (called "Port Mapping" in the GUI) exposes a port on an internal LAN device to the public internet. Two prerequisites before this will work:

1. **The CR202 must have a static public IP** on its WAN/cellular interface. Most regular SIM plans hand out **dynamic private IPs** (carrier-grade NAT), which cannot be reached from the public internet at all. You'll need a static public IP plan from your carrier, or use InConnect (ICS) as a VPN service.
2. **The end device must use the CR202 as its gateway** so return traffic flows back through the router.

To configure port mapping:

1. Go to **Firewall > Port Mapping**
2. Click **Add** and fill in:
   - **External Port** — the port that will be exposed on the CR202's WAN IP (e.g. 8001)
   - **Internal IP** — the LAN IP of the end device (e.g. 192.168.1.80)
   - **Internal Port** — the service port on the end device (e.g. 80 for HTTP)
   - **Protocol** — TCP / UDP / Both
3. **Apply** the changes.

From the public internet you would then reach the end device at `http://<CR202 public IP>:8001`. If you're only reaching it from the **local** LAN, use the CR202's WAN IP directly with the configured external port.

> The CR202 GUI does not support port ranges (e.g. 9000–64000) — each external port needs its own mapping entry. For broad port-range control, use **Firewall > Basic** (default policy Block) combined with **Firewall > MAC-IP Binding** and **Firewall > Filtering** allow-rules to shape traffic at the device/IP level instead of the port level.

**Tags:** `#CR202` `#portMapping` `#portForwarding` `#NAT` `#staticIP`

---

## Q12. I want to restrict my CR202 so only specific devices (by MAC address) can use the network — what's the correct approach?

**Category:** Firewall | **Product:** CR202 | **Screenshot:** No

1. Go to **Firewall > MAC-IP Binding** and add each allowed device as a `MAC → static IP` entry. Only devices on this list will be bound to a known IP.
2. Go to **Firewall > Basic** and set the default policy to **Block**. This blocks everything by default.
3. Go to **Firewall > Filtering** and add explicit allow rules for the IPs you bound in step 1 (and for any required outbound services such as DNS, HTTP, HTTPS).

The result: only devices whose MAC appears in the MAC-IP Binding table receive a usable IP, and only those IPs pass the default-block firewall. Any unknown device connecting (even over Wi-Fi) will fail to reach the network.


**Tags:** `#CR202` `#firewall` `#MACFilter` `#MACIPBinding` `#whitelist`

---

## Q13. My CR202 goes offline randomly — how do I investigate the cause?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

Random offline events on the CR202 are usually cellular-related. Investigation steps:

1. **Collect logs immediately after an outage.**
   Log in to `http://192.168.2.1`, go to **Status > Log**, and click **Download Log File**. Also click **Download System Diagnosing Data** on the same page — these two files together give R&D enough information to correlate the outage with modem events.

2. **Enable cellular debug logging** (captures more detail on modem AT-command state):
   Go to **Network > Cellular** and click the **Debug** toggle. Let the device run long enough to capture at least one outage event, then re-download the logs.

3. **Check if offline events correlate with signal gaps.**
   If the signal-strength chart shows a drop at the same timestamp as the outage, the outage is cellular-network instability (carrier-side, tower issue, or coverage). Move the antenna or deploy an external antenna via the SMA connector.

4. **Upgrade firmware.**
   Older firmware on the CR202 has known handling issues around modem re-attach. Upgrade to the latest firmware from the InHand resource center, then re-test. Apply via **System > Upgrade**.


**Tags:** `#CR202` `#cellular` `#outage` `#logs` `#debug` `#firmware`

---

## Q14. End devices connect to the CR202 Wi-Fi and get an IP, but can't reach the internet — what should I check?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

When end devices show a successful Wi-Fi / LAN connection to the CR202 (green LED, IP assigned) but still cannot browse:

1. **Confirm the router itself has internet**, not just the local network.
   - From the CR202 GUI, go to **Tools > PING** and ping `8.8.8.8`. If that fails, the CR202 itself has no upstream — the issue is cellular, not LAN.
2. **Check cellular attach status** at **Status > Modem**. Look for:
   - **RSRP** — values below -100 dBm suggest poor signal; below -110 dBm the link may pass ping but not heavy traffic.
   - **Operator / Cell info** — confirms the modem has actually registered on the cellular network.
3. **Compare behavior with a known-good CR202** at the same site. If a second CR202 with a different SIM reaches the internet, the failing unit's SIM or cellular plan is the issue (SIM not activated, plan suspended, APN mismatch).
4. **Check APN** under **Network > Cellular**. Some carriers require a manual APN; auto-detection doesn't always pick the right one.
5. **Check IP Passthrough** under **Network > IP Passthrough**. If this is enabled unexpectedly, the cellular public IP is being handed to a single target MAC, and other LAN devices get no internet — disable it unless you specifically want passthrough mode.


**Tags:** `#CR202` `#internetDown` `#cellular` `#IPPassthrough` `#troubleshooting`

---

## Q15. My CR202 battery is not holding a charge even with the supplied power adapter — what can be done?

**Category:** Hardware | **Product:** CR202 | **Screenshot:** No

The CR202 family has three variants (CR202, CR202-Pro, CR202-Lite) and the battery replacement process depends on which one you have — check the label on the back of the device to confirm.

First, rule out external causes for all variants. If the device shows a **red battery LED** or shuts off as soon as it's disconnected from power:

1. **Swap the power adapter and cable with a known-good pair.** If another CR202 at the same site charges normally using the same charger, the adapter is fine — the problem is in the device.
2. **Test the cable separately.** A bad USB-C cable can deliver very low current, enough to run the unit but not enough to charge the battery.
3. **Try a different outlet.** Rule out the wall outlet before concluding it's the device.

If steps 1–3 point to a battery fault, the next step depends on the variant:

- **CR202-Lite** has a **removable battery**. You can order a replacement battery and swap it yourself without returning the unit. Contact support with the Serial Number (S/N on the back label) to arrange the replacement battery shipment.
- **CR202 and CR202-Pro** have **non-removable batteries** — in-field battery swap is not possible. The unit needs to be returned via RMA. When opening the RMA, have ready:
  - **Serial Number** (S/N on the back label)
  - **IMEI** (also on the label, and visible at **Status > Modem**)
  - **Approximate purchase date**

  After InHand receives the returned unit, the battery is inspected. If it's repairable we fix and return the original; if not, we ship a replacement.


**Tags:** `#CR202` `#CR202Lite` `#CR202Pro` `#battery` `#hardware` `#RMA` `#charging`

---

## Q16. How do I set up the CR202 to automatically fail over between SIM cards based on signal strength?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No


1. Go to **Network > Cellular**
2. Enable **Dual SIM Enable**
3. Set **Main SIM** to the preferred slot (e.g. eSIM). The router starts on this SIM at power-on and falls back to the alternate SIM when the signal drops below threshold.
4. Set the **CSQ Threshold** — this is a signal-strength reading (from the modem's `AT+CSQ` command, based on RSSI). When the current CSQ value falls below the threshold for several minutes, the router switches to the other SIM.
5. **Apply**.

> **Newer firmware also supports an RSRP threshold** in addition to CSQ. RSRP is a more accurate signal indicator for LTE than CSQ/RSSI. If your use case needs carrier-signal-based failover, request the latest FW .

> **Physical-SIM present-detection caveat:** While the eSIM is the active SIM, CR202 has no visibility into the physical SIM slot — the physical slot is not powered. The router will only discover whether a physical SIM is present after failover is triggered. You cannot configure "only fail over if physical SIM is inserted" — the device fails over based on signal, then discovers the physical SIM state at that point.

**Tags:** `#CR202` `#DualSIM` `#failover` `#CSQ` `#RSRP` `#cellular`

---

## Q17. What APN should I use on the CR202 for Canadian carriers (Rogers, Bell)?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

The CR202's built-in carrier profiles are primarily US-focused. For Canadian carriers you'll typically need to set the APN manually:

- **Rogers:** APN `ltemobile.apn`
- **Bell:** APN `pda.bell.ca`
- **Telus:** APN `sp.telus.com`

Confirm the exact APN with your carrier if you have an enterprise or IoT plan — the defaults above are the common consumer values.

To configure:

1. Log in at `http://192.168.2.1` and go to **Network > Cellular**
2. In the **Profiles** section, set **Index 1** and enter the APN string (e.g. `ltemobile.apn`). Leave username/password blank unless the carrier requires them.
3. Under **Nano SIM Network Provider** (or **eSIM Network Provider** depending on which slot the SIM is in), select **Profile 1** so the manual profile is used instead of auto-detection.
4. **Apply**, then check **Status > Modem** to confirm the modem registered to the network and obtained an IP.

> **End devices can ping but not browse?** If after configuring the APN, LAN devices can ping external addresses (e.g. `8.8.8.8`) but web pages don't load, the issue is DNS. Try manually assigning a DNS server on one end-device (e.g. `8.8.8.8`) — if pages load, either set a DNS under **Services > DNS** on the CR202 or check whether the carrier-assigned DNS is working.


**Tags:** `#CR202` `#APN` `#Rogers` `#Bell` `#Canada` `#DNS`

---

## Q18. What are the differences between the CR202, CR202-Pro, and CR202-Lite?

**Category:** Hardware | **Product:** CR202 | **Screenshot:** No

The CR202 family has three SKUs: **CR202**, **CR202-Pro**, and **CR202-Lite**. CR202 and CR202-Pro are nearly identical and share the same feature set; the CR202-Lite is a lightweight variant.

Feature summary:

| Capability | CR202 / CR202-Pro | CR202-Lite |
| Battery | Built-in, non-removable | **Removable** |
| Weight | Baseline | ~30 g / 1 oz lighter |
| **VPN (IPsec / OpenVPN / WireGuard / ZeroTier)** | **Supported** | **Not supported** |
| **SNMP** | **Supported** | **Not supported** |

**If your use case needs VPN, SNMP, choose the CR202 or CR202-Pro — not the Lite.** If SNMP is the only blocker for the Lite, the IR315 is also an option and has SNMP.

For enterprise requirements beyond the CR202 family (multiple SSIDs, guest SSID, 802.1X Ethernet authentication, per-port VLAN), consider the **ER605** or **ER805** enterprise routers — no CR202 variant supports those features.


**Tags:** `#CR202` `#CR202Pro` `#CR202Lite` `#comparison` `#VPN` `#SNMP`

---

## Q19. My CR202 connects end devices fine over Wi-Fi, but devices connected via an Ethernet switch to the LAN port cannot be reached — what's wrong?

**Category:** Web GUI | **Product:** CR202 | **Screenshot:** No

When Wi-Fi clients work but wired-switch clients do not:

1. **Check the port mode of WAN/LAN1.** By default it may be in WAN mode. For the port to act as LAN for wired clients, go to **Network > WAN/LAN Switch** and set the port to **LAN** mode. **Apply.**
2. **Try LAN2 instead.** LAN2 is always LAN — if LAN2 works while WAN/LAN1 doesn't, confirm step 1 (WAN/LAN1 needs LAN mode).
3. **Check the end device's IP and gateway.** The CR202's default LAN subnet is `192.168.2.0/24` with the router at `192.168.2.1`. If a switched device (like a printer or POS terminal) is configured with a static IP in a different subnet (e.g. `192.168.1.x`) or with a different gateway, it will get link-layer connectivity but won't talk to the CR202's services (DHCP, DNS, routing).
   - Either set the device to **DHCP** so it takes an IP in `192.168.2.x`, or
   - Set its static IP to `192.168.2.x`, subnet `255.255.255.0`, gateway `192.168.2.1`.
4. **Verify LAN IP range** under **Network > LAN** matches your deployment plan. If you migrated from another router that used a different subnet, end devices may still be configured for the old subnet.

**Tags:** `#CR202` `#LAN` `#WAN_LAN_Switch` `#DHCP` `#staticIP` `#switch`

---

## Q20. Why does my CR202 show the wrong time zone, and how do connected devices (e.g. Zebra tablets) get time through it?

**Category:** Web GUI | **Product:** CR202 | **Screenshot:** No

The CR202 has two time sources, configured under **System > Time**:

1. **Cellular modem** — pulls time from the cell tower after registration
2. **NTP server** — a configurable NTP target (default or custom)

**Important:** the CR202 does **not** automatically adjust time zone. You must manually select the correct Time Zone under **System > Time** and apply — otherwise the clock will display UTC+8 regardless of where the device is deployed.

**Connected devices and time:** Wi-Fi-connected clients (laptops, Zebra tablets, etc.) do NOT pull time directly from the CR202 — Wi-Fi 802.11 does not transmit time. Connected devices either:
- Query their own NTP server over the internet connection the CR202 provides, OR
- Pull time from a cellular tower (only if the device has its own SIM — not applicable when they're only on Wi-Fi)

If an end device is showing wrong time while Wi-Fi-connected to the CR202, its own NTP configuration is the issue — the CR202 is just providing internet access, not time. Consult the end device's documentation for the Zebra's NTP/timezone settings.


**Tags:** `#CR202` `#time` `#NTP` `#timezone` 

---

## Q21. My CR202 log shows frequent "Deauth Reason 3" messages and Wi-Fi clients keep disconnecting — is this a bug?

**Category:** Wi-Fi | **Product:** CR202 | **Screenshot:** No

**Deauthentication Reason 3** ("Station leaving (or has left) the BSS") is **normal 802.11 behavior**, not a bug. The CR202 sends this frame to a Wi-Fi client after about **300 seconds of inactivity** to free up the association slot. When the client becomes active again it will re-associate automatically.

Real causes of persistent client-disconnect issues you should investigate:

1. **Cellular signal (if client can't reconnect after DEAUTH).** Check **Status > Modem** for RSRP. Below -100 dBm is cell-edge and unstable; below -110 dBm may not sustain traffic even if the Wi-Fi link is fine. Reposition the device or add an external antenna.
2. **Wi-Fi channel congestion.** Under **Network > WLAN**, try a fixed channel (e.g. channel 1, 6, or 11 on 2.4 GHz) instead of **Auto**.
3. **Force Reboot feature.** Enable **Network > Cellular > Force Reboot** — the CR202 will automatically reboot after a threshold of failed cellular reconnects, which recovers from stuck modem states that prevent Wi-Fi from providing internet even though clients are associated.
4. **Firmware.** Upgrade to the latest CR202 firmware via **System > Upgrade** — some older versions had WiFi stability fixes.

If after these steps clients still can't reconnect after an inactivity-triggered DEAUTH, collect logs (**Status > Log** → **Download Log File** + **Download System Diagnosing Data**) and open a support case.


**Tags:** `#CR202` `#WiFi` `#Deauth` `#RSRP` `#ForceReboot` `#troubleshooting`

---

## Q22. Device Manager cannot push a config to one of my CR202 units — it errors with "Invalid parameter" — how do I work around it?

**Category:** Device Manager | **Product:** CR202 | **Screenshot:** No

Known issue: when the source CR202 has empty Nano SIM / eSIM profiles, the firmware writes an invalid value (e.g. `wan1_ppp_sim2_authen=3`) to the config snapshot that Device Manager captures. Pushing that snapshot to other devices fails because `3` is outside the valid range `0..2` for SIM Authentication Type.

Workaround:

1. On the source / template CR202 (the one you're pushing the config FROM), log in at `http://192.168.2.1`
2. Go to **Network > Cellular**
3. For each SIM slot (eSIM and Nano SIM), make sure the **Authentication Type** is explicitly set to `auto`, `PAP`, or `CHAP` — not left at the blank default. Setting Authentication Type to **auto** (internal value `0`) works for most carriers and avoids the bug.
4. **Apply**, then re-capture / re-push the running config via Device Manager to the target devices.


**Tags:** `#CR202` `#DeviceManager` `#config` `#bug` `#SIMAuthentication`

---

## Q23. Does the CR202 support guest SSID or multiple SSIDs, and can I require Ethernet-port authentication?

**Category:** Wi-Fi | **Product:** CR202 | **Screenshot:** No

No. The CR202 supports only a **single SSID**. It also does **not** require authentication on the Ethernet LAN ports — any device connected via Ethernet with a patch cable gets an IP and internet access immediately.

If your use case requires:
- **Multiple SSIDs** (e.g. separate primary and guest networks)
- **Ethernet 802.1X authentication**
- **Per-port VLAN / access control**

…choose an enterprise-grade device instead. Recommended:
- **ER605 / ER805** — enterprise routers with multiple SSIDs, 802.1X, VLAN support, and richer firewall features.

As a partial workaround on the CR202 (restrict which devices can connect to the single SSID), combine three GUI features:

1. **Firewall > MAC-IP Binding** — bind each allowed device's MAC to a static IP
2. **Firewall > Basic** — set default policy to **Block**
3. **Firewall > Filtering** — add explicit allow rules for the bound IPs

This enforces device-level access control but does not give you a true segmented guest network. For that, use the ER605 or ER805 enterprise routers.

**Tags:** `#CR202` `#WiFi` `#guestSSID` `#multiSSID` `#802.1X` `#ER805`

---

## Q24. Does the CR202 support IPsec VPN tunnels, and why is the VPN menu missing from my GUI?

**Category:** IPSec VPN | **Product:** CR202 | **Screenshot:** No

Yes — the CR202 and CR202-Pro (which are nearly identical SKUs) support IPsec in both server and client modes, plus OpenVPN, WireGuard, and ZeroTier. The CR202-Lite does not have VPN capability at all. The VPN configuration on CR202 / CR202-Pro lives at:

- **VPN > IPSec Settings** — global phase-1/phase-2 proposals, IKE version, DH group
- **VPN > IPSec Tunnels** — per-tunnel config (local/remote subnets, pre-shared key)

If you don't see a **VPN** menu in your CR202 web GUI at all, your firmware is out of date. Earlier CR202 firmware revisions did not expose the VPN menu. To fix:

1. Download the latest firmware from the InHand resource center.
2. Log in at `http://192.168.2.1` and go to **System > Upgrade**.
3. Upload the firmware file and apply. The device will reboot.
4. After the reboot, the **VPN** menu should appear on the left navigation.

Note: IPsec is not available on the CR202-Lite. The Lite has no VPN menu at all regardless of firmware version — it is a more basic consumer variant without VPN capability. If VPN is required, use the CR202 or CR202-Pro.

**Tags:** `#CR202` `#IPsec` `#VPN` `#firmware` `#upgrade`

---

## Q25. On a CR202 with eSIM + Nano SIM, how exactly does the failover between them work?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

The CR202 dual-SIM architecture has one important constraint: **only one SIM slot is powered / visible to the modem at a time.** While the eSIM is active, the CR202 cannot see or power the Nano SIM slot, and vice versa.

Failover behavior:

1. At power-on, the router uses the **Main SIM** (configured under **Network > Cellular > Main SIM** — set this to eSIM or Nano SIM as desired).
2. If the Main SIM fails to register, or signal drops below the configured CSQ / RSRP threshold for several minutes (configured under **Network > Cellular** with **Dual SIM Enable** and **CSQ Threshold** — new firmware also exposes an RSRP threshold), the router switches to the alternate SIM slot.
3. The device will make multiple registration attempts on the Main SIM before failing over. Expect to see brief "airplane mode" / SIM-probing states in the LED during this process — this is normal.
4. Once switched to the alternate SIM, the router continues on that SIM until the next failover threshold triggers in reverse, or until reboot.

**Implications for deployment:**
- You cannot configure "only fail over if a physical SIM is inserted" — because the CR202 cannot detect the physical SIM until it actually switches to it. If you push a dual-SIM-enabled config to a device that has only an eSIM, the device will still attempt the Nano SIM after eSIM failures, find nothing, and return to eSIM.

**Tags:** `#CR202` `#DualSIM` `#eSIM` `#NanoSIM` `#failover`

---

## Q26. I configured one CR202 the way I want it — how do I push that same config to my other CR202 units via Device Manager?

**Category:** Device Manager | **Product:** CR202 | **Screenshot:** No

Device Manager (DM) supports bulk config push across CR202 units. The flow:

1. **Export the config from your reference device.**
   - In the DM portal, open the source device's **Remote Configuration** and **Export** the running config. You'll get a config file.

2. **Upload the config file to DM's Config library.**
   - Go to **Config** in the DM portal
   - Click **Add** and upload the config file

3. **Apply the config to target devices.**
   - After upload, DM prompts you to select which devices to apply it to. Select the target CR202 units.

> **Before pushing, decide whether target devices should keep their own login / Wi-Fi credentials.** If you push the config unedited, all target devices will inherit the source device's login password, SSID, and Wi-Fi password — identical across all units. For most deployments you want each device to keep its own per-unit credentials.


**Tags:** `#CR202` `#DeviceManager` `#bulkConfig` `#deployment`

---

## Q27. How do I factory-reset a CR202 when I don't know the current credentials?

**Category:** Factory Reset | **Product:** CR202 | **Screenshot:** No

The CR202 family uses a two-step reset-button sequence, not a single long hold:

1. **Power on the device**, then **immediately press and hold the RESET button**.
2. Keep holding until the **System LED turns yellow**, then **release**. The System LED will start blinking.
3. **Press RESET a second time** and hold.
4. When the **System LED blinks slowly in green**, release. The device reboots to factory defaults.

After the reboot, the login credentials revert to whatever is printed on the label on the back of the unit:
- **Older batches:** standard default (on label)
- **Newer batches:** per-unit password (on label)

**Tags:** `#CR202` `#factoryReset` `#resetButton` `#credentials`

---

## Q28. My application needs multicast, but it's not working through the CR202 — is multicast blocked?

**Category:** Firewall | **Product:** CR202 | **Screenshot:** No

Yes — the CR202 **blocks multicast traffic by default**. If your application (e.g. mDNS / Bonjour / SSDP / IPTV discovery, industrial multicast protocols) depends on multicast crossing the router, you need to explicitly allow it.

To enable multicast:

1. Log in at `http://192.168.2.1`
2. Go to **Firewall > Basic**
3. **Uncheck** the **Filter Multicast** option
4. **Apply**

After the change, multicast packets will flow between the LAN and other interfaces as expected. No other configuration changes are required.

**Tags:** `#CR202` `#multicast` `#firewall` `#mDNS`

---

## Q29. My CR202 is connecting but the speeds are much slower than Verizon shows I should be getting — what could cause this?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

When throughput is low but the device is online, check three things in order:

1. **QoS / bandwidth limit.** QoS is the only CR202 setting that can cap throughput, and it's **disabled by default**. Confirm this:
   - Go to **QoS > IP BW Limit** and verify no rule is active on the failing device's IP.
   - If you previously enabled QoS for testing, disable it and re-test.

2. **Cellular signal strength.** Check **Status > Modem**:
   - **RSRP below -100 dBm** = **Cell Edge** condition. Even with full Verizon bars on your phone, the CR202's internal antenna may see a weaker signal. A reading of -107 dBm would cap practical throughput around 10 Mbps down / 2 Mbps up regardless of plan.
   - Fix: reposition the device (nearer a window, higher mounting), or connect an **external antenna** via the SMA connector.

3. **Network congestion.** If signal is strong (RSRP better than -90 dBm) and QoS is off but throughput is still low, the cellular sector may be congested — common in dense urban areas at peak hours. There's no router-side fix; confirm by testing in a different location or at an off-peak time.

**Tags:** `#CR202` `#slowSpeed` `#throughput` `#QoS` `#RSRP` `#congestion`

---

## Q30. Are the firmware files for CR202, CR202-Pro, and CR202-Lite interchangeable?

**Category:** Firmware | **Product:** CR202 | **Screenshot:** No

**No — only two of the three share firmware.** Breakdown:

- **CR202 and CR202-Pro:** share the **same firmware image**. The filename typically looks like `CR2XX-V1.0.NN.bin`. On the InHand Resources Center this file may appear under the CR202 listing only (even though it also applies to CR202-Pro) — that's a naming inconsistency on the download site, not a product limitation.
- **CR202-Lite:** has a **separate firmware image**, typically named with a `CR2XXL-` prefix (for example `CR2XXL-V1.0.NN.bin`). The Lite firmware is **not compatible** with the CR202 or CR202-Pro, and vice versa.

How to pick the right firmware:

1. Confirm your exact model on the label on the back of the unit (it will explicitly say `CR202`, `CR202-Pro`, or `CR202-Lite`).
2. Go to the InHand Resources Center and filter or search:
   - For **CR202 / CR202-Pro**: look for the `CR2XX-*.bin` image
   - For **CR202-Lite**: look for the `CR2XXL-*.bin` image
3. If your search returns results for both series, **match the filename prefix to your variant**, not just the model name in the listing title.
4. Upload via **System > Upgrade** in the local web GUI, or via Device Manager's **Upgrade Firmware** flow for batch upgrades.

If you flash the wrong image, the device will either refuse the upgrade (preferred) or become non-functional and need recovery — use the correct prefix.


**Tags:** `#CR202` `#CR202Pro` `#CR202Lite` `#firmware` `#upgrade` `#ResourceCenter`

---

## Q31. My CR202 seems overwhelmed by too many DHCP clients — the lease list keeps growing even after I shortened the lease time. How do I clear it?

**Category:** DHCP | **Product:** CR202 | **Screenshot:** No

Two things going on here, handled separately.

**1. How to clear / shorten the DHCP lease list.**

The CR202 cannot **force-release** a DHCP lease — that decision is owned by the client device. You have two ways to turn the lease table over:

- **Shorten the lease time** under **Services > DHCP Service** (default is 60 minutes; set to 5 minutes during active troubleshooting). New leases and renewals will inherit the shorter time. Existing leases will persist at their original duration until they expire.
- **Reboot the CR202** — this clears the active lease table and forces every client to re-DHCP on reconnect. Go to **System > Reboot**.

**2. Why leases keep piling up even at a short lease time.**

The CR202 is a portable router designed for a **maximum of ~30 simultaneous clients**. When significantly more devices (50+, especially mobile phones aggressively rotating MAC addresses for privacy) try to associate, the CR202's DHCP server issues leases faster than it can track them, end devices experience packet loss, and the lease table stays congested.

Mitigations:

- **Upgrade firmware.** Confirm you're on the latest CR202 firmware (`System > Upgrade`). Several DHCP stability fixes have landed in recent versions; older firmware (e.g. V1.0.29) has known issues under load. After firmware upload, **make sure to click the Reboot prompt** — the upload alone doesn't activate the new firmware.
- **Split the client load.** If the deployment has more than ~30 simultaneous clients, one CR202 is the wrong form factor. Add a second CR202 to split the client pool, or move to an enterprise-grade router (ER605 / ER805) that handles higher client counts.
- **Randomized-MAC devices** (modern Android / iOS) can appear as many distinct "clients" if they rotate MAC per-SSID scan. This is usually tolerable, but contributes to large lease counts — not a CR202 bug.

**Tags:** `#CR202` `#DHCP` `#leaseTable` `#clientCount` `#firmware`

---

## Q32. My customer's CR202(-Lite) will not activate / register on Verizon even though the SIM shows "Active" on the Verizon portal — what to try?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

This is a common pattern: the Verizon portal shows the SIM / eSIM as Active, but the CR202 keeps failing to register on the cellular network (Globe LED blinking, `+CEREG: 0,2` in the modem logs meaning "searching, not registered"). Work through these checks in order:

1. **Manually select the Verizon LTE profile in the GUI.** Auto-APN assignment can fail on older firmware. Log in at `http://192.168.2.1` → **Network > Cellular**:
   - For **eSIM-active units**: set **eSIM Network Provider** to **Verizon LTE** and **Main SIM** to **eSIM**.
   - For **physical-SIM-active units**: set **Nano SIM Network Provider** to **Verizon LTE** and **Main SIM** to **Nano SIM**.
   - Click **Apply** and wait 2–3 minutes for re-registration.

2. **Confirm Main SIM matches the SIM actually in use.** If the device is configured to start on Nano SIM but the customer is trying to activate the eSIM, the router will keep retrying nano first, fail, then switch to eSIM — causing long delays (20+ minutes, sometimes overnight) before activation succeeds. Mismatched Main SIM is the #1 cause of "it eventually activated" reports.

3. **Upgrade firmware.** For persistent registration failures on CR202-Lite units, upgrade to the latest GA firmware which includes a fix for auto-APN assignment failures on eSIM. After upload via **System > Upgrade**, click the Reboot prompt.

**Tags:** `#CR202` `#CR202Lite` `#Verizon` `#eSIM` `#activation` `#registration`

---

## Q33. I want to use a non-mainstream (MVNO / prepaid) SIM in my CR202 — how do I configure the APN?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

The CR202 works with any carrier SIM as long as the carrier uses an LTE band the device supports (CR202 is LTE-only — no 5G). You will usually need to set the APN manually because MVNO and prepaid carriers are rarely in the CR202's built-in profile list.

1. **Get the APN from your carrier.** This is a one-line string provided by the carrier — examples:
   - H2O Wireless → `RESELLER`
   - Rogers (CA) → `ltemobile.apn`
   - Bell (CA) → `pda.bell.ca`
   - Claro (PE) → `claro.pe` (with `claro` / `claro` user/pass)
   - Check the carrier's IoT / APN support page if in doubt.

2. **Enter the APN on the CR202:**
   - Log in at `http://192.168.2.1`
   - Go to **Network > Cellular**
   - In the **Profiles** section, for **Index 1**, enter the APN string. Leave Username/Password blank unless the carrier requires them.
   - Under **Nano SIM Network Provider** (or eSIM Network Provider), select **Profile 1** — this tells the modem to use your manual profile instead of trying to auto-match a built-in carrier.
   - **Apply**.

3. **Verify attach.** Go to **Status > Modem** and check:
   - **Modem is Ready** — yes, modem is up
   - **Operator** — should show the carrier name once attached
   - **RSRP** — signal quality; below -100 dBm is cell edge

If the modem stays in "Searching" for more than 3–5 minutes with a manually-set APN, verify:
- The APN string (typos / case-sensitivity — most APNs are case-insensitive but double-check)
- The SIM is activated and provisioned for data (not voice-only)
- The carrier supports one of the CR202's LTE bands in your area (LTE-FDD: B2, B4, B5, B7, B12, B13, B14, B25, B26, B29, B30, B66, B71; LTE-TDD: B41, B48)

**Tags:** `#CR202` `#APN` `#MVNO` `#H2O` `#prepaid` `#cellular`

---

## Q34. I set up Content Filtering / URL whitelist on my CR202 but non-whitelisted sites (e.g. Facebook) are still accessible — what's wrong?

**Category:** Firewall | **Product:** CR202 | **Screenshot:** No

URL-based filtering on the CR202 has several non-obvious dependencies that all need to be right for the whitelist to actually enforce. Common pitfalls and the correct setup:

**1. Use the right Filtering page for wildcards.**
- If your whitelist uses wildcard domains (e.g. `*.example.com`), edit the list at **Firewall > Filtering**, NOT **Firewall > Content Filtering**. Content Filtering does not handle wildcards the way most users expect.
- When using a wildcard like `*.example.com`, it **only matches subdomains** — the root domain `example.com` is not included. Add BOTH `*.example.com` and `example.com` to the list.

**2. Enable DNS Proxy** so the CR202 can inspect DNS requests:
- Go to **Firewall > Basic** and **enable DNS Proxy**. Without this, the CR202 does not intercept DNS requests, and URL-based filtering has no way to see which domain the client is trying to reach.

**3. Disable IPv6 on the client** (or block IPv6 on CR202):
- IPv6 DNS requests bypass the CR202's filtering engine. If the client has IPv6 enabled and the upstream has IPv6 connectivity, filtered domains may still resolve and load over IPv6.
- Disable IPv6 on the end-device network adapter for testing.

**4. One URL may require many allowed domains.**
- Modern websites load content from CDNs, analytics, fonts, cookie consent providers, and embedded third-party services. A "simple" whitelist of `yourdomain.com` won't render the page if those helpers are blocked.
- Use **Tools > Traffic Analysis**, set **Type** to **Domain Only**, click **Start Analysis**, then visit the target site from a client device. Download the analysis CSV — it lists every domain the browser actually contacted. Add all of them to the whitelist.
- Alternatively, open the site in a browser with dev tools (F12 → Sources) on a non-CR202 network first to see which domains it pulls from.

**Firewall default-policy setup to enforce the whitelist:**

- **Firewall > Basic** → Default Filter Policy: **Block** (so anything not explicitly allowed is dropped).
- **Firewall > Basic** → enable **DNS Proxy**.
- **Firewall > Filtering** → import your whitelist CSV (domains and any required destination IPs/ports).

**Tags:** `#CR202` `#contentFiltering` `#whitelist` `#DNSProxy` `#IPv6` `#firewall`

---

## Q35. How do I enable or disable cellular roaming on the CR202?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

**You can't — roaming is always enabled on the CR202 and there is no toggle in the GUI.** Every variant (CR202, CR202-Pro, CR202-Lite) permits the modem to roam onto available networks without a user-configurable setting.

This differs from the **FWA02**, which exposes a roaming on/off toggle — if the customer specifically needs manual control of roaming (e.g. for cost containment on international trips, or to force a specific home carrier), the CR202 is not the right product for that use case.

**Operational implications:**
- If a CR202 with a Rogers SIM in Canada sees a stronger Bell tower, it may roam onto Bell without any user action. Troubleshooting tip: in the modem logs you'll see the registered operator code shift between carriers — that's expected behavior, not a bug.
- If a customer is seeing unexpected roaming charges, the control is on the **carrier side** (Verizon, Rogers, etc.) — have them ask the carrier to block roaming on the SIM's plan. The CR202 cannot enforce it.

If your deployment plan depends on roaming control, choose the FWA02 (or an InHand enterprise router) instead, or configure the plan with the carrier to restrict roaming at the SIM level.


**Tags:** `#CR202` `#roaming` `#FWA02` `#cellular` `#productComparison`

---

## Q36. When cellular signal gets poor, my CR202's Wi-Fi network drops too — how do I keep the Wi-Fi broadcasting during LTE re-registration?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

This is expected behavior caused by the **Force Reboot** feature, which is enabled by default. When cellular signal deteriorates (e.g. RSRP drops to -112 to -120 dBm), the CR202 goes through this sequence:

1. First, it reboots just the **cellular modem** (keeping the rest of the router up).
2. If the cellular connection continues to fail repeatedly after modem reboots, Force Reboot triggers a **full router reboot** — which takes the Wi-Fi down along with everything else.

The full-router-reboot step is the one that kills local Wi-Fi clients (e.g. scanners talking to a laptop on the CR202 LAN).

**To keep Wi-Fi up during LTE re-registration:**

1. Log in at `http://192.168.2.1`
2. Go to **Network > Cellular**
3. **Disable Force Reboot**
4. **Apply**

After this change, the CR202 will still reboot just the cellular modem when the WAN drops, but the router core and Wi-Fi stay running. End-devices on the LAN keep talking to each other even during periods of no internet connectivity.

**Tradeoff to understand:**
- With Force Reboot ON: better chance of recovering cellular connectivity automatically in "stuck modem" scenarios, at the cost of a brief LAN outage every time the recovery logic triggers.
- With Force Reboot OFF: LAN stays stable through cellular flaps, but if the modem ever enters a genuinely hung state (rare, but possible), you may need to power-cycle the CR202 manually to recover WAN.


**Tags:** `#CR202` `#WiFi` `#ForceReboot` `#cellular` `#LAN` `#stability`

---

## Q37. How do I configure the CR202 for an AT&T SIM?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

AT&T is in the CR202's built-in carrier profile list, so manual APN entry is usually not needed:

1. Log in at `http://192.168.2.1`
2. Go to **Network > Cellular**
3. Under **Nano SIM Network Provider** (for a physical AT&T SIM) or **eSIM Network Provider** (for an eSIM if provisioned for AT&T), select **AT&T** from the dropdown.
4. Set **Main SIM** to match the slot where the AT&T SIM is (Nano SIM or eSIM).
5. **Apply** and wait 2–3 minutes for the modem to register.

Check **Status > Modem** — the Operator field should show "AT&T" or "ATT" once registered successfully.

**If the built-in AT&T profile does not attach**, fall back to manual APN entry:

- Most common AT&T IoT/consumer APNs: `broadband` (consumer) or `m2m.com.attz` (M2M/IoT plans) — confirm with the customer's AT&T account manager which APN their plan uses.
- Enter the APN under **Profiles > Index 1**, then set **Nano SIM Network Provider** to **Profile 1**.

**Tags:** `#CR202` `#APN` `#ATT` `#cellular` `#profile`

---

## Q38. How do I allow FTP while keeping the Firewall default policy set to Block?

**Category:** Firewall | **Product:** CR202 | **Screenshot:** No

To combine a strict default-block policy with functional FTP, the setup depends on whether you're using plain FTP or FTPS (encrypted).

**Plain / unencrypted FTP (port 21 control, dynamic data):**

- Add a single rule at **Firewall > Filtering**: allow **TCP Destination Port 21** to the FTP server's IP (or any IP, if you can't enumerate).
- The CR202 firewall automatically permits the FTP data channel ports that get negotiated on the control channel — you do NOT need to add a separate rule for the dynamic data ports.

**FTPS (FTP over SSL/TLS):**

- Because the control channel is encrypted, the firewall cannot inspect port negotiation and auto-permit data ports. You must manually allow the data port range the FTP server uses.
- At **Firewall > Filtering**, allow:
  - **TCP Destination Port 21** (control, if using explicit FTPS) or **TCP Destination Port 990** (control, if using implicit FTPS)
  - **TCP Destination Port 5000–5100** (or whatever range the FTP server is configured to use for data) — ask the FTP server admin for the data-port range they allow.

**SFTP (SSH File Transfer, port 22):**

- Just allow **TCP Destination Port 22** to the SFTP server. No dynamic data ports, simpler than FTP/FTPS.

**Whitelisting by server IP instead of port:**

- If the customer only needs FTP to a specific known server, the simplest rule is to allow **all traffic to that server's IP** in Firewall > Filtering (no port restriction). The server itself will only accept FTP anyway.

**What the CR202 cannot do:** there is no "protocol-level whitelist override" — you cannot say "allow FTP as a class regardless of port/IP". Each allow-rule is explicit. If the customer connects to hundreds of different FTP servers, the practical approach is the allow-any-port-to-anywhere-on-TCP-21 rule, accepting that the default-block policy still blocks HTTP/HTTPS etc. unless separately whitelisted.


**Tags:** `#CR202` `#FTP` `#FTPS` `#SFTP` `#firewall` `#filtering`

---

## Q39. Is there an HTTP API on the CR202 to query status and change settings programmatically?

**Category:** Web GUI | **Product:** CR202 | **Screenshot:** No

Yes — the CR202 exposes an HTTP API suitable for status queries and parameter changes. Setup:

1. Log in at `http://192.168.2.1`
2. Go to **System > Admin Access**
3. Enable the **HTTP API** port. Default port is **4444**.
4. Set (or confirm) the API username and password — for programmatic access, use the admin credentials on the label or dedicated API credentials if you've added them.
5. **Apply**.

**Example: query the device list** (clients connected to the CR202) from another machine on the LAN:

```
curl -u <username>:<password> <CR202_LAN_IP>:4444/update.cgi \
  -d "exec=devlist" -H "Content-Type:text/plain"
```

Replace `<username>:<password>` with your admin credentials (from the back-label) and `<CR202_LAN_IP>` with the router's LAN IP (default `192.168.2.1`, or whatever you set under **Network > LAN**).

For **info / status queries** use `/getinfo.cgi` with a `-d` parameter naming the info block, e.g.:

```
curl -u <user>:<pass> <CR202_LAN_IP>:4444/getinfo.cgi \
  -d "modem_info" -H "Content-Type:text/plain"
```

Other info blocks follow the same pattern. Additional `exec=` and `getinfo` parameter names are documented in the HTTP API guide — request the latest PDF from InHand support (the guide is not always bundled with the public user manual). Typical exec commands include querying the cellular status, modifying network settings, and triggering reboots.

**Security caveat:**

- The HTTP API listens on whatever interfaces the web GUI is reachable on. If the CR202 is deployed with a public-IP cellular SIM and the web management is exposed to the internet, the API is also exposed. **Restrict management access** at **Firewall > Device Access Filtering** to only trusted source IPs/MACs before enabling the HTTP API on an internet-facing device.
- Consider rotating the admin password if you enable the API — default label credentials should not be used for programmatic access over the internet.

For integration with InHand's own platform (Device Manager), use the Device Manager API instead of the local HTTP API — the DM API offers fleet-level operations across many CR202 units at once.

**Tags:** `#CR202` `#HTTPAPI` `#automation` `#integration`

---

## Q40. How can I see which domains my CR202 whitelist is allowing or blocking?

**Category:** Firewall | **Product:** CR202 | **Screenshot:** No

Two different mechanisms, each showing different things:

**1. Firewall > Filtering log — shows which domains were ACCEPTED.**

Enable the **Log** checkbox on each Filtering rule you care about. After traffic flows, you can view the accepted hits in the system log:

- The log entry shows the destination IP resolved from the domain plus a hit count, e.g.:
  ```
  domain:flexcount-qa.com ===> <dest-IP>, numbers:1
  ```
- This confirms that the CR202 matched a request to `flexcount-qa.com`, resolved it, and allowed it through.

**2. Tools > Traffic Analysis — shows all OUTBOUND domains that reached the network.**

- Go to **Tools > Traffic Analysis**, set **Type** to **Domain Only**, click **Start Analysis**, let clients generate traffic.
- Download the analysis CSV. It lists every domain the clients actually contacted through the CR202 (these are domains that passed the filter).

**Tags:** `#CR202` `#contentFiltering` `#log` `#TrafficAnalysis` `#whitelist`

---

## Q41. The Status-Modem page shows "SIM Failure" for the Nano SIM on my CR202 — what does this mean and how do I diagnose it?

**Category:** Cellular | **Product:** CR202 | **Screenshot:** No

A **SIM Failure** / **UIM Failure** indication at **Status > Modem** for the Nano SIM slot means the CR202 tried to read the physical SIM card and could not — the device is not receiving the expected response from the SIM.

Two possible root causes (firmware cannot distinguish them from logs alone):

- The SIM card itself is faulty (damaged chip contacts, manufacturing defect, or end of life).
- The SIM slot / reader on the CR202 is damaged (bent pins, debris, bad solder joint).

**Diagnostic steps:**

1. **Power off the CR202.** (For CR202-Lite, you can also remove the battery. For CR202 / CR202-Pro, just unplug power.)
2. **Remove and re-insert the SIM.** Make sure it's seated firmly and oriented correctly per the arrow printed on the slot.
3. **Power on** and check **Status > Modem** again. If the SIM now shows an ICCID and IMSI, the reseat fixed it (intermittent contact).
4. **If the failure persists, test with another SIM.** Any LTE-capable Nano SIM will do — just checking whether the slot can read anything.
   - If the second SIM is detected: the original SIM is faulty. Contact the SIM's carrier for a replacement.
   - If the second SIM is also not detected: the CR202's Nano SIM slot is likely damaged. Open an RMA with the device Serial Number (S/N on the back label) and IMEI.
5. **Cross-test the original SIM in another device** (e.g. a phone or another CR202). If it fails there too, it's the SIM. If it works there, it's the CR202 slot.

**Workaround while you wait for replacement hardware:** if the CR202 has an active eSIM profile, you can temporarily rely on the eSIM only by setting **Main SIM** to **eSIM** under **Network > Cellular**. This avoids the SIM Failure error and keeps the unit online until the faulty SIM or the unit itself is swapped.

**Tags:** `#CR202` `#SIMFailure` `#NanoSIM` `#diagnostics` `#RMA`

---

---

*InHand Networks | Team C AI Knowledge Base | Tech Support Transformation*
