# VG814 User Manual Rewrite Checklist

## Document Information

| Item | Content |
|------|---------|
| Original manual | en/device-dsa/VG814/InHandVG814User'sManualV1.2.md |
| New manual | en/device-dsa/VG814/InHandVG814User'sManualV1.2_rewritten.md |
| Rewrite date | 2025-03-13 |

---

## Self-Check Items

| Check Item | Requirement | Status |
|------------|-------------|--------|
| Content basis | No content not in original; no assumptions/inferences | ☑ |
| Wiki style consistency | Third-person, objective; no "you/please" | ☑ |
| Terminology explanation | First occurrence of terms has "can be understood as:" | ☑ |
| Conventions table | Front matter includes symbol meanings (> "" >>) | ☑ |
| How to use this manual | Role-based routing, task quick jump, estimated time | ☑ |
| New chapter image placeholders | New chapters have image placeholders where needed | ☐ N/A (original has images) |
| Image path retention | Original image paths preserved (./img/TFRyisVs9_mw-DgG/) | ☑ |
| Estimated time | Each scenario has estimated time | ☑ |
| Troubleshooting appendix | By symptom; each item links to relevant section | ☑ |
| Figure numbering | Format "Fig. X-Y" | ☑ |
| Cross-references | Body and appendix form knowledge loop | ☑ |

---

## Images to Supplement

**List of image positions in new chapters that need figures (where original had none).**

| Fig. No. | Chapter | Location | Description | Status |
|----------|---------|----------|-------------|--------|
| — | 1. Know the Device | Packaging list | Packaging list photo | ☐ To be supplemented (original not specified) |
| — | 5. Typical Applications | Chapter | Application topology | ☐ To be supplemented (original not specified) |

**Note:**
- **To be supplemented:** Not in original; needs new image
- **Retained:** In original; copied to new document

---

## Content Mapping (Original → New)

| Original Chapter | New Section |
|------------------|-------------|
| Overview | 1.1 Overview |
| Hardware (Indicator, Reset, Panel) | 1.3–1.6 |
| Default Settings | 1.5 Default Settings |
| Power ON, Power and FMS | 1.6 Panel Interface |
| Login and Network Access (Dialup/Wi-Fi) | 2. Installation and First Use, 3. Common Scenarios |
| Network (Cellular, Bridge, VLAN, PPPoE, Wi-Fi, Loopback, L2 Switch) | 4.1 Network |
| OBD | 4.2 OBD |
| VPN (IPsec, GRE, L2TP, OpenVPN, Certificate) | 4.3 VPN |
| Services (DHCP, DNS, DDNS, SMS, GPS, QoS, Traffic Control) | 4.4 Services |
| Firewall (ACL, NAT, MAC-IP Binding) | 4.5 Security |
| Routing (Static, RIP, OSPF, BGP) | 4.5 Security |
| Link Backup (SLA, Track, VRRP, Interface Backup) | 4.6 Link Backup |
| Administration (System, User, AAA, SNMP, Alarm, Logs, Upgrade, Reboot) | 4.7 Administration |
| Diagnostic Tools | 4.8 Diagnostic Tools |
| Hardware installation | 2.2 Hardware Installation |
| More reference documents | Note at end of rewritten manual |

---

## Notes

1. **VG814 versions:** Road (Bus) and Rail versions have different antenna connectors (FAKRA vs TNC) and slightly different ETX pin definitions.
2. **Original typo:** "Auther" and "Descripition" in Revision History table; left as-is in rewritten manual (front matter simplified).
3. **No standalone FAQ/Safety:** Original has no dedicated FAQ or Safety chapter; troubleshooting and safety items were derived from Cautions/Notes in the body.
4. **Installation content:** Original includes installation/first-use content and hardware installation; retained in Section 2 per skill rules.
5. **M12 Ethernet definition:** Original includes M12 X-coded pin definition; referenced in note, full table in original document.
