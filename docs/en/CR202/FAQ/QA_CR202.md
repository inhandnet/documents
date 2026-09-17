# QA — CR202 Portable Router (EN samples)

---

## Q1. CR202 won't power on — what should I check?

The CR202 requires a deliberate button press to power on:

1. Press and **hold** the power button for **3 seconds** until the LEDs light up.
2. A brief tap will not power the device on — it must be held for at least 3 seconds.
3. If no LEDs appear after holding the button, check:
   - Is the battery charged? Connect via USB-C and try again.
   - Is the USB-C cable and charger working? Try a different cable and charger (use a standard 5V/2A USB-C charger — not a laptop charger with proprietary voltages).
4. If the battery LED flashes red immediately, the battery is critically low. Continue charging before powering on.

---

## Q2. How do I configure or change the Wi-Fi name (SSID) and password on the CR202?

1. Log in to the CR202 web GUI at `http://192.168.2.1`.
2. Go to **Network > WLAN**.
3. Edit the **SSID** field to change the Wi-Fi name.
4. Change the **Security** type (recommend WPA2-PSK) and update the **Password**.
5. Click **Apply**. Wi-Fi clients will need to reconnect using the new credentials.

---

## Q3. What are the differences between the CR202, CR202-Pro, and CR202-Lite?

The CR202 family has three SKUs: **CR202**, **CR202-Pro**, and **CR202-Lite**. CR202 and CR202-Pro are nearly identical and share the same feature set; the CR202-Lite is a lightweight variant.

Feature summary:

| Capability | CR202 / CR202-Pro | CR202-Lite |
| Battery | Built-in, non-removable | **Removable** |
| Weight | Baseline | ~30 g / 1 oz lighter |
| **VPN (IPsec / OpenVPN / WireGuard / ZeroTier)** | **Supported** | **Not supported** |
| **SNMP** | **Supported** | **Not supported** |

**If your use case needs VPN, SNMP, choose the CR202 or CR202-Pro — not the Lite.** If SNMP is the only blocker for the Lite, the IR315 is also an option and has SNMP.

For enterprise requirements beyond the CR202 family (multiple SSIDs, guest SSID, 802.1X Ethernet authentication, per-port VLAN), consider the **ER605** or **ER805** enterprise routers — no CR202 variant supports those features.

---

## Q4. How do I factory-reset a CR202 when I don't know the current credentials?

The CR202 family uses a two-step reset-button sequence, not a single long hold:

1. **Power on the device**, then **immediately press and hold the RESET button**.
2. Keep holding until the **System LED turns yellow**, then **release**. The System LED will start blinking.
3. **Press RESET a second time** and hold.
4. When the **System LED blinks slowly in green**, release. The device reboots to factory defaults.

After the reboot, the login credentials revert to whatever is printed on the label on the back of the unit:
- **Older batches:** standard default (on label)
- **Newer batches:** per-unit password (on label)
