# VT310/320 User Manual Rewrite Checklist

## Document Information

| Item | Content |
|------|---------|
| Original manual | en/device-dsa/VT300/VehicleTelematicsVT310_320UserManual.md |
| New manual | en/device-dsa/VT300/VehicleTelematicsVT310_320UserManual_rewritten.md |
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
| Image path retention | Original image paths preserved (./img/JTyXJeajJoIDZj8-/) | ☑ |
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
| Chapter I 1.2 Packing List | 1.2 Packing List |
| Chapter I 1.3 Product Appearance | 1.3 Product Appearance |
| Chapter I 2. SIM and Cable Installation | 1.4 SIM and Cable Installation |
| Chapter I 2.3 Cable Introduction | 1.5 Cable Connection |
| Chapter I 2.4 VT310 Connect to I/O, 26PIN Definition | 1.6–1.7 Interface Definition and Details |
| Chapter I 3. Start the VT300/200, 3.1–3.2 Indicators | 1.8 LED Indicators, 2.1 Start |
| Chapter II Install Configuration Tool | 2.2 Install Configuration Tool |
| Chapter II Search COM, Login | 2.3 Search COM Port and Login |
| Chapter II Status | 4.1 Status |
| Chapter II System Settings | 4.2 System Settings |
| Chapter II Configure Cellular | 4.3 Cellular Network, 3.1 Cellular Configuration |
| Chapter II Interface (CAN, RS232, J1708, RS485, I/O, ELD) | 4.4–4.5 Interface |
| Chapter II Cloud | 4.6 Cloud, 3.2 Cloud Platform Connection |
| Chapter II Features | 4.7 Features |
| Chapter II 1-Wire | 4.8 1-Wire |
| Chapter II Notice | 4.9 Notice |
| Chapter II Maintenance | 4.10 Maintenance |
| Chapter II Restoration of Default | 1.9 Restore Default Account and Password |
| Chapter II How to Get Device Log | Appendix C Get Device Log |

---

## Notes

1. **VT310 vs VT320:** VT310 uses 26PIN with P1/P14/P15 for power/IGT; VT320 uses different pin layout (VIN+/VIN-, IGT). Both use USB to serial port for config tool connection.
2. **CLI activation:** VT310/320 use "+++" to activate CLI mode before entering username/password (different from VT200 which sends credentials directly).
3. **Original typo:** "Auther", "Descripition", "smatfleet.cloud" (should be smartfleet.cloud), "Emport" (should be Export). Left as-is in source; not present in rewritten summary.
4. **Config tool:** VT310 and VT320 share the same config tool and configuration methods.
5. **GEOTAB:** Added in later versions; included in cloud platform section.
6. **1-Wire sensor:** Original mentions "less02b" for VT310; DS18B20 for water temperature detection. Both retained in context.
