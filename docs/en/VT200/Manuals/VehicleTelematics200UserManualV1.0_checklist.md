# VT200 User Manual Rewrite Checklist

## Document Information

| Item | Content |
|------|---------|
| Original manual | en/device-dsa/VT200/VehicleTelematics200UserManualV1.0.md |
| New manual | en/device-dsa/VT200/VehicleTelematics200UserManualV1.0_rewritten.md |
| Rewrite date | 2025-03-13 |

---

## Self-Check Items

| Check Item | Requirement | Status |
|------------|-------------|--------|
| Content basis | No content not in original; no assumptions/inferences | ☑ |
| Wiki style consistency | Third-person, objective; no "you/please" | ☑ |
| Terminology explanation | First occurrence of terms has "can be understood as:" | ☑ |
| Conventions table | Front matter includes symbol meanings | ☑ |
| How to use this manual | Role-based routing, task quick jump, estimated time | ☑ |
| New chapter image placeholders | New chapters have image placeholders where needed | ☐ N/A (original has images) |
| Image path retention | Original image paths preserved (./img/tdkhaYR-toANRd6e/) | ☑ |
| Estimated time | Each scenario has estimated time | ☑ |
| Troubleshooting appendix | By symptom; each item links to relevant section | ☑ |
| Figure numbering | Format "Fig. X-Y" | ☑ |
| Cross-references | Body and appendix form knowledge loop | ☑ |

---

## Images to Supplement

**List of image positions in new chapters that need figures (where original had none).**

| Fig. No. | Chapter | Location | Description | Status |
|----------|---------|----------|-------------|--------|
| — | 5. Typical Applications | Chapter | Application topology | ☐ To be supplemented (original not specified) |

**Note:**
- **To be supplemented:** Not in original; needs new image
- **Retained:** In original; copied to new document

---

## Content Mapping (Original → New)

| Original Chapter | New Section |
|------------------|-------------|
| Chapter I 1. Introduction | 1.1 Overview |
| Chapter I 2. Start to use VT200 (accessories, interface) | 1.2 Accessories, 1.3–1.4 Interface |
| Chapter I 2.2.x RS232, DI, DO, AI, 1-Wire, IGT | 1.4 Interface Details |
| Chapter I 3. Start the VT200 | 2.1 Start the VT200 |
| Chapter I 3.2–3.3 GNSS/Cellular Status Light | 1.5 LED Indicators |
| Chapter II 1. Install Configuration Tool | 2.2 Install Configuration Tool |
| Chapter II 1.2–1.3 Search COM, Login | 2.3 Search COM Port and Login |
| Chapter II 2. Inquire Status | 4.1 Status Information |
| Chapter II 3. System Settings (Sleep, Account) | 4.2 System Settings |
| Chapter II 4. Configure Cellular | 4.3 Cellular Network, 3.1 Cellular Configuration |
| Chapter II 5. OBD | 4.4 OBD Interface |
| Chapter II 6. Cloud Platform (SmartFleet, Wialon, Azure, AWS, Aliyun, MQTT) | 4.5 Cloud Platform, 3.2 Cloud Platform Connection |
| Chapter II 7. Maintenance | 4.6 Maintenance |
| Chapter II 8. Restoration of Default | 1.6 Restore Default Account and Password |
| Chapter II 9. How to Get Device Log | Appendix C Get Device Log |

---

## Notes

1. **VT200 vs Web-based gateways:** VT200 uses a PC configuration tool (VT310/VT3_Installer), not a Web interface. "Installation and First Use" is adapted to config tool installation and USB connection.
2. **Original typo:** "Auther" and "Descripition" in Revision History; "colelcted" in Wialon section; "congifuration" in Maintenance. Left as-is in source; not present in rewritten summary.
3. **Config tool name:** Original refers to "VT310 configuration tool" and "VT3_Installer"; VT200 uses the same tool family.
4. **No standalone FAQ/Safety:** Original has no dedicated FAQ or Safety chapter; troubleshooting and safety items were derived from Cautions/Notes in the body.
5. **Appendix C:** CLI log retrieval is optional advanced reference; placed in Appendix C per framework.
