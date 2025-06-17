# DELTA Pro 3

**Status**: ✅ **Fully Functional** - Dual solar inputs (HV/LV), comprehensive power monitoring, and Home Assistant Energy Dashboard integration

## Key Features

- **Dual Solar Inputs**: Separate monitoring for HV (High Voltage) and LV (Low Voltage) solar inputs
- **Energy Dashboard Integration**: Individual and combined solar energy tracking for Home Assistant Energy Dashboard
- **Comprehensive Power Monitoring**: Input/output power across all ports
- **Battery Management**: Multi-battery support with individual slave battery monitoring

## Energy Dashboard Integration

The Delta Pro 3 provides comprehensive energy data for Home Assistant's Energy Dashboard:

- **Solar Energy**: Total solar input plus separate HV/LV tracking
- **Battery Energy**: Charge/discharge tracking for AC and DC
- **Real-time Power**: Live power monitoring for all inputs/outputs

## Sensors

| Sensor | Key | Notes |
| ------ | --- | ----- |
| **Main Battery** |  |  |
| Main Battery Level | `bmsMaster.soc` | Primary battery percentage |
| Main Battery Level (Precise) | `bmsMaster.f32ShowSoc` | High precision battery level |
| Main Design Capacity | `bmsMaster.designCap` | |
| Main Full Capacity | `bmsMaster.fullCap` | |
| Main Remain Capacity | `bmsMaster.remainCap` | |
| State of Health | `bmsMaster.soh` | |
| **System Battery** |  |  |
| Battery Level | `ems.lcdShowSoc` | Combined system battery level |
| Battery Level (Precise) | `ems.f32LcdShowSoc` | High precision combined level |
| **System Power** |  |  |
| Total In Power | `pd.wattsInSum` | Total system input power |
| Total Out Power | `pd.wattsOutSum` | Total system output power |
| Main Battery Current | `bmsMaster.amp` | Battery charge/discharge current |
| **AC Input/Output** |  |  |
| AC In Power | `inv.inputWatts` | AC input power |
| AC Out Power | `inv.outputWatts` | AC output power |
| AC In Volts | `inv.acInVol` | AC input voltage |
| AC Out Volts | `inv.invOutVol` | AC output voltage |
| **Solar Input - LV Port** |  |  |
| Solar (1) LV In Power | `mppt.lvInWatts` | Low voltage solar input power |
| Solar (1) LV In Voltage | `mppt.lvInVol` | Low voltage solar input voltage |
| Solar (1) LV In Current | `mppt.lvInAmp` | Low voltage solar input current |
| **Solar Input - HV Port** |  |  |
| Solar (2) HV In Power | `mppt.hvInWatts` | High voltage solar input power |
| Solar (2) HV In Volts | `mppt.hvInVol` | High voltage solar input voltage |
| Solar (2) HV In Amps | `mppt.hvInAmp` | High voltage solar input current |
| **Energy Sensors** |  |  |
| Solar In Energy | `pd.chgSunPower` | Total solar energy input |
| Solar (LV) In Energy | `mppt.lvSolarEnergy` | LV solar energy (estimated) |
| Solar (HV) In Energy | `mppt.hvSolarEnergy` | HV solar energy (estimated) |
| Battery Charge Energy from AC | `pd.chgPowerAc` | AC charging energy |
| Battery Charge Energy from DC | `pd.chgPowerDc` | DC charging energy |
| Battery Discharge Energy to AC | `pd.dsgPowerAc` | AC discharge energy |
| Battery Discharge Energy to DC | `pd.dsgPowerDc` | DC discharge energy |
| **DC Output** |  |  |
| DC Out Power | `mppt.outWatts` | Main DC output power |
| DC Car Out Power | `mppt.carOutWatts` | Car port output power |
| DC Anderson Out Power | `mppt.dcdc12vWatts` | Anderson port output power |
| **USB & Type-C Output** |  |  |
| Type-C (1) Out Power | `pd.typec1Watts` | Type-C port 1 output |
| Type-C (2) Out Power | `pd.typec2Watts` | Type-C port 2 output |
| USB (1) Out Power | `pd.usb1Watts` | USB port 1 output |
| USB (2) Out Power | `pd.usb2Watts` | USB port 2 output |
| USB QC (1) Out Power | `pd.qcUsb1Watts` | USB QC port 1 output |
| USB QC (2) Out Power | `pd.qcUsb2Watts` | USB QC port 2 output |
| **System Information** |  |  |
| Charge Remaining Time | `ems.chgRemainTime` | Time to full charge |
| Discharge Remaining Time | `ems.dsgRemainTime` | Time to empty |
| Cycles | `bmsMaster.cycles` | Battery charge cycles |
| Battery Temperature | `bmsMaster.temp` | Battery temperature |
| Min Cell Temperature | `bmsMaster.minCellTemp` | |
| Max Cell Temperature | `bmsMaster.maxCellTemp` | |
| Battery Volts | `bmsMaster.vol` | |
| Min Cell Volts | `bmsMaster.minCellVol` | |
| Max Cell Volts | `bmsMaster.maxCellVol` | |
| **Slave Battery 1** |  |  |
| Slave 1 Battery Level | `bmsSlave1.soc` | |
| Slave 1 Battery Level (Precise) | `bmsSlave1.f32ShowSoc` | |
| Slave 1 Design Capacity | `bmsSlave1.designCap` | |
| Slave 1 Full Capacity | `bmsSlave1.fullCap` | |
| Slave 1 Remain Capacity | `bmsSlave1.remainCap` | |
| Slave 1 State of Health | `bmsSlave1.soh` | |
| Slave 1 Battery Temperature | `bmsSlave1.temp` | |
| Slave 1 Min Cell Temperature | `bmsSlave1.minCellTemp` | |
| Slave 1 Max Cell Temperature | `bmsSlave1.maxCellTemp` | |
| Slave 1 Battery Volts | `bmsSlave1.vol` | |
| Slave 1 Min Cell Volts | `bmsSlave1.minCellVol` | |
| Slave 1 Max Cell Volts | `bmsSlave1.maxCellVol` | |
| Slave 1 Battery Current | `bmsSlave1.amp` | |
| Slave 1 In Power | `bmsSlave1.inputWatts` | |
| Slave 1 Out Power | `bmsSlave1.outputWatts` | |
| Slave 1 Cycles | `bmsSlave1.cycles` | |
| **Slave Battery 2** |  |  |
| Slave 2 Battery Level | `bmsSlave2.soc` | |
| Slave 2 Battery Level (Precise) | `bmsSlave2.f32ShowSoc` | |
| Slave 2 Design Capacity | `bmsSlave2.designCap` | |
| Slave 2 Full Capacity | `bmsSlave2.fullCap` | |
| Slave 2 Remain Capacity | `bmsSlave2.remainCap` | |
| Slave 2 State of Health | `bmsSlave2.soh` | |
| Slave 2 Battery Temperature | `bmsSlave2.temp` | |
| Slave 2 Min Cell Temperature | `bmsSlave2.minCellTemp` | |
| Slave 2 Max Cell Temperature | `bmsSlave2.maxCellTemp` | |
| Slave 2 Battery Volts | `bmsSlave2.vol` | |
| Slave 2 Min Cell Volts | `bmsSlave2.minCellVol` | |
| Slave 2 Max Cell Volts | `bmsSlave2.maxCellVol` | |
| Slave 2 Battery Current | `bmsSlave2.amp` | |
| Slave 2 In Power | `bmsSlave2.inputWatts` | |
| Slave 2 Out Power | `bmsSlave2.outputWatts` | |
| Slave 2 Cycles | `bmsSlave2.cycles` | |

## Switches

| Switch | Key | Commands |
| ------ | --- | -------- |
| Beeper | `pd.beepState` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 38, "enabled": VALUE}}` |
| DC (12V) Output | `mppt.carState` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 81, "enabled": VALUE}}` |
| AC Output | `inv.cfgAcEnabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 66, "enabled": VALUE}}` |
| X-Boost | `inv.cfgAcXboost` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 66, "xboost": VALUE}}` |
| AC Always On | `pd.acautooutConfig` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 95, "acautooutConfig": VALUE}}` |
| Backup Reserve Enabled | `pd.watthisconfig` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 94, "isConfig": VALUE, "bpPowerSoc": -3333300, "minDsgSoc": 0, "maxChgSoc": 0}}` |
| AC Enabled | `inv.cfgAcEnabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"enabled": VALUE, "id": 66}}` |
| AC Out Power | `inv.cfgAcOutVol` | `{"moduleType": 0, "operateType": "TCP", "params": {"out_vol": VALUE, "id": 69}}` |
| AC Out Freq | `inv.cfgAcOutFreq` | `{"moduleType": 0, "operateType": "TCP", "params": {"out_freq": VALUE, "id": 70}}` |
| AC Charging Speed | `inv.cfgFastChgWatts` | `{"moduleType": 0, "operateType": "TCP", "params": {"fastChgWatts": VALUE, "id": 73}}` | Range: 200-2875 |
| AC Slow Charging Speed | `inv.cfgSlowChgWatts` | `{"moduleType": 0, "operateType": "TCP", "params": {"slowChgWatts": VALUE, "id": 74}}` | Range: 200-400 |
| DC (12V) Enabled | `mppt.cfgDcChgCurrent` | `{"moduleType": 0, "operateType": "TCP", "params": {"enabled": VALUE, "id": 81}}` | `{0: "Off", 1: "On"}` |
| DC (12V) Charge Current | `mppt.cfgDcChgCurrent` | `{"moduleType": 0, "operateType": "TCP", "params": {"currMa": VALUE, "id": 71}}` | `{"4A": 4000, "6A": 6000, "8A": 8000}` |
| Screen Timeout | `pd.lcdOffSec` | `{"moduleType": 0, "operateType": "TCP", "params": {"lcdTime": VALUE, "id": 39}}` | `{"Never": 0, "10 sec": 10, "30 sec": 30, "1 min": 60, "5 min": 300, "30 min": 1800}` |
| Unit Timeout | `pd.standByMode` | `{"moduleType": 0, "operateType": "TCP", "params": {"standByMode": VALUE, "id": 33}}` | `{"Never": 0, "30 min": 30, "1 hr": 60, "2 hr": 120, "6 hr": 360, "12 hr": 720}` |
| AC Timeout | `inv.cfgStandbyMin` | `{"moduleType": 0, "operateType": "TCP", "params": {"standByMins": VALUE, "id": 153}}` | `{"Never": 0, "30 min": 30, "1 hr": 60, "2 hr": 120, "4 hr": 240, "6 hr": 360, "12 hr": 720, "24 hr": 1440}` |

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

## Technical Notes

- **Power Scaling**: Primary power sensors use milliwatt (mW) scaling from protobuf
- **Solar Inputs**: Supports both standard and experimental field mapping for maximum compatibility  
- **Energy Calculation**: HV/LV energy sensors estimate individual contributions based on power ratios
- **Current Accuracy**: Solar current sensors properly scaled to display actual mA values
- **Field Mapping**: Uses `ems.lcdShowSoc` for combined battery level and individual BMS sensors for detailed battery monitoring