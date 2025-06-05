# DELTA Pro 3

## Sensors

| Sensor | Key |
| ------ | --- |
| Main Battery Level | `bmsMaster.soc` |
| Main Battery Level (Precise) | `bmsMaster.f32ShowSoc` |
| Main Design Capacity | `bmsMaster.designCap` |
| Main Full Capacity | `bmsMaster.fullCap` |
| Main Remain Capacity | `bmsMaster.remainCap` |
| State of Health | `bmsMaster.soh` |
| Battery Level | `ems.lcdShowSoc` |
| Battery Level (Precise) | `ems.f32LcdShowSoc` |
| Total In Power | `pd.wattsInSum` |
| Total Out Power | `pd.wattsOutSum` |
| Main Battery Current | `bmsMaster.amp` |
| AC In Power | `inv.inputWatts` |
| AC Out Power | `inv.outputWatts` |
| AC In Volts | `inv.acInVol` |
| AC Out Volts | `inv.invOutVol` |
| Solar In Power | `mppt.inWatts` |
| Solar In Voltage | `mppt.inVol` |
| Solar In Current | `mppt.inAmp` |
| DC Out Power | `mppt.outWatts` |
| DC Out Voltage | `mppt.outVol` |
| DC Car Out Power | `mppt.carOutWatts` |
| DC Anderson Out Power | `mppt.dcdc12vWatts` |
| Type-C (1) Out Power | `pd.typec1Watts` |
| Type-C (2) Out Power | `pd.typec2Watts` |
| USB (1) Out Power | `pd.usb1Watts` |
| USB (2) Out Power | `pd.usb2Watts` |
| USB QC (1) Out Power | `pd.qcUsb1Watts` |
| USB QC (2) Out Power | `pd.qcUsb2Watts` |
| Charge Remaining Time | `ems.chgRemainTime` |
| Discharge Remaining Time | `ems.dsgRemainTime` |
| Cycles | `bmsMaster.cycles` |
| Battery Temperature | `bmsMaster.temp` |
| Min Cell Temperature | `bmsMaster.minCellTemp` |
| Max Cell Temperature | `bmsMaster.maxCellTemp` |
| Battery Volts | `bmsMaster.vol` |
| Min Cell Volts | `bmsMaster.minCellVol` |
| Max Cell Volts | `bmsMaster.maxCellVol` |
| Solar In Energy | `pd.chgSunPower` |
| Battery Charge Energy from AC | `pd.chgPowerAc` |
| Battery Charge Energy from DC | `pd.chgPowerDc` |
| Battery Discharge Energy to AC | `pd.dsgPowerAc` |
| Battery Discharge Energy to DC | `pd.dsgPowerDc` |
| Slave 1 Battery Level | `bmsSlave1.soc` |
| Slave 1 Battery Temperature | `bmsSlave1.temp` |
| Slave 1 In Power | `bmsSlave1.inputWatts` |
| Slave 1 Out Power | `bmsSlave1.outputWatts` |
| Slave 2 Battery Level | `bmsSlave2.soc` |
| Slave 2 Battery Temperature | `bmsSlave2.temp` |
| Slave 2 In Power | `bmsSlave2.inputWatts` |
| Slave 2 Out Power | `bmsSlave2.outputWatts` |

## Switches

| Switch | Key | Commands |
| ------ | --- | -------- |
| Beeper | `pd.beepState` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 38, "enabled": VALUE}}` |
| DC (12V) Enabled | `mppt.carState` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 81, "enabled": VALUE}}` |
| AC Enabled | `inv.cfgAcEnabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 66, "enabled": VALUE}}` |
| X-Boost Enabled | `inv.cfgAcXboost` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 66, "xboost": VALUE}}` |
| AC Always On | `pd.acautooutConfig` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 95, "acautooutConfig": VALUE}}` |
| Backup Reserve Enabled | `pd.watthisconfig` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 94, "isConfig": VALUE, "bpPowerSoc": VALUE * 50, "minDsgSoc": 0, "maxChgSoc": 0}}` |

## Sliders

| Slider | Key | Commands | Min | Max |
| ------ | --- | -------- | --- | --- |
| Max Charge Level | `ems.maxChargeSoc` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 49, "maxChgSoc": VALUE}}` | 50 | 100 |
| Min Discharge Level | `ems.minDsgSoc` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 51, "minDsgSoc": VALUE}}` | 0 | 30 |
| Backup Reserve Level | `pd.bppowerSoc` | `{"moduleType": 0, "operateType": "TCP", "params": {"isConfig": 1, "bpPowerSoc": VALUE, "minDsgSoc": 0, "maxChgSoc": 0, "id": 94}}` | 5 | 100 |
| Generator Auto Start Level | `ems.minOpenOilEbSoc` | `{"moduleType": 0, "operateType": "TCP", "params": {"openOilSoc": VALUE, "id": 52}}` | 0 | 30 |
| Generator Auto Stop Level | `ems.maxCloseOilEbSoc` | `{"moduleType": 0, "operateType": "TCP", "params": {"closeOilSoc": VALUE, "id": 53}}` | 50 | 100 |
| AC Charging Power | `inv.cfgSlowChgWatts` | `{"moduleType": 0, "operateType": "TCP", "params": {"slowChgPower": VALUE, "id": 69}}` | 200 | 3600 |

## Selects

| Select | Key | Commands | Options |
| ------ | --- | -------- | ------- |
| DC (12V) Charge Current | `mppt.cfgDcChgCurrent` | `{"moduleType": 0, "operateType": "TCP", "params": {"currMa": VALUE, "id": 71}}` | `{"4A": 4000, "6A": 6000, "8A": 8000}` |
| Screen Timeout | `pd.lcdOffSec` | `{"moduleType": 0, "operateType": "TCP", "params": {"lcdTime": VALUE, "id": 39}}` | `{"Never": 0, "10 sec": 10, "30 sec": 30, "1 min": 60, "5 min": 300, "30 min": 1800}` |
| Unit Timeout | `pd.standByMode` | `{"moduleType": 0, "operateType": "TCP", "params": {"standByMode": VALUE, "id": 33}}` | `{"Never": 0, "30 min": 30, "1 hr": 60, "2 hr": 120, "6 hr": 360, "12 hr": 720}` |
| AC Timeout | `inv.cfgStandbyMin` | `{"moduleType": 0, "operateType": "TCP", "params": {"standByMins": VALUE, "id": 153}}` | `{"Never": 0, "30 min": 30, "1 hr": 60, "2 hr": 120, "4 hr": 240, "6 hr": 360, "12 hr": 720, "24 hr": 1440}` | 