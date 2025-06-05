from custom_components.ecoflow_cloud.api import EcoflowApiClient
from custom_components.ecoflow_cloud.devices import const, BaseDevice
from custom_components.ecoflow_cloud.entities import BaseSensorEntity, BaseNumberEntity, BaseSwitchEntity, \
    BaseSelectEntity
from custom_components.ecoflow_cloud.number import ChargingPowerEntity, MaxBatteryLevelEntity, MinBatteryLevelEntity, \
    MinGenStartLevelEntity, \
    MaxGenStopLevelEntity
from custom_components.ecoflow_cloud.select import DictSelectEntity, TimeoutDictSelectEntity
from custom_components.ecoflow_cloud.sensor import LevelSensorEntity, WattsSensorEntity, RemainSensorEntity, \
    TempSensorEntity, \
    CyclesSensorEntity, InWattsSensorEntity, OutWattsSensorEntity, OutWattsDcSensorEntity, InWattsSolarSensorEntity, \
    InVoltSolarSensorEntity, InAmpSolarSensorEntity, OutVoltDcSensorEntity, \
    InEnergySensorEntity, OutEnergySensorEntity, MilliVoltSensorEntity, InMilliVoltSensorEntity, \
    OutMilliVoltSensorEntity, AmpSensorEntity, CapacitySensorEntity, QuotaStatusSensorEntity
from custom_components.ecoflow_cloud.switch import BeeperEntity, EnabledEntity


class DeltaPro3(BaseDevice):
    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [
            # Main Battery
            LevelSensorEntity(client, self, "bmsMaster.soc", const.MAIN_BATTERY_LEVEL)
            .attr("bmsMaster.designCap", const.ATTR_DESIGN_CAPACITY, 0)
            .attr("bmsMaster.fullCap", const.ATTR_FULL_CAPACITY, 0)
            .attr("bmsMaster.remainCap", const.ATTR_REMAIN_CAPACITY, 0),
            LevelSensorEntity(client, self, "bmsMaster.f32ShowSoc", const.MAIN_BATTERY_LEVEL_F32, False)
            .attr("bmsMaster.designCap", const.ATTR_DESIGN_CAPACITY, 0)
            .attr("bmsMaster.fullCap", const.ATTR_FULL_CAPACITY, 0)
            .attr("bmsMaster.remainCap", const.ATTR_REMAIN_CAPACITY, 0),
            CapacitySensorEntity(client, self, "bmsMaster.designCap", const.MAIN_DESIGN_CAPACITY, False),
            CapacitySensorEntity(client, self, "bmsMaster.fullCap", const.MAIN_FULL_CAPACITY, False),
            CapacitySensorEntity(client, self, "bmsMaster.remainCap", const.MAIN_REMAIN_CAPACITY, False),
            LevelSensorEntity(client, self, "bmsMaster.soh", const.SOH),

            # Combined Battery Status
            LevelSensorEntity(client, self, "ems.lcdShowSoc", const.COMBINED_BATTERY_LEVEL),
            LevelSensorEntity(client, self, "ems.f32LcdShowSoc", const.COMBINED_BATTERY_LEVEL_F32, False),
            WattsSensorEntity(client, self, "pd.wattsInSum", const.TOTAL_IN_POWER),
            WattsSensorEntity(client, self, "pd.wattsOutSum", const.TOTAL_OUT_POWER),
            AmpSensorEntity(client, self, "bmsMaster.amp", const.MAIN_BATTERY_CURRENT),

            # AC Input/Output
            InWattsSensorEntity(client, self, "inv.inputWatts", const.AC_IN_POWER),
            OutWattsSensorEntity(client, self, "inv.outputWatts", const.AC_OUT_POWER),
            InMilliVoltSensorEntity(client, self, "inv.acInVol", const.AC_IN_VOLT),
            OutMilliVoltSensorEntity(client, self, "inv.invOutVol", const.AC_OUT_VOLT),

            # Solar Input - Primary (LV Port)
            InWattsSolarSensorEntity(client, self, "mppt.lvInWatts", const.SOLAR_IN_POWER),
            InVoltSolarSensorEntity(client, self, "mppt.lvInVol", const.SOLAR_IN_VOLTAGE),
            InAmpSolarSensorEntity(client, self, "mppt.lvInAmp", const.SOLAR_IN_CURRENT),
            
            # Solar Input - Secondary (HV Port) - New for Delta Pro 3
            InWattsSolarSensorEntity(client, self, "mppt.hvInWatts", const.SOLAR_2_IN_POWER),
            InVoltSolarSensorEntity(client, self, "mppt.hvInVol", const.SOLAR_2_IN_VOLTS),
            InAmpSolarSensorEntity(client, self, "mppt.hvInAmp", const.SOLAR_2_IN_AMPS),

            # DC Output
            OutWattsDcSensorEntity(client, self, "mppt.outWatts", const.DC_OUT_POWER),
            OutVoltDcSensorEntity(client, self, "mppt.outVol", const.DC_OUT_VOLTAGE),
            OutWattsSensorEntity(client, self, "mppt.carOutWatts", const.DC_CAR_OUT_POWER),
            OutWattsSensorEntity(client, self, "mppt.dcdc12vWatts", const.DC_ANDERSON_OUT_POWER),
            
            # Smart Home Panel Output - New for Delta Pro 3
            OutWattsSensorEntity(client, self, "mppt.smartPanelWatts", "Smart Home Panel Out Power", False),

            # USB & Type-C Output
            OutWattsSensorEntity(client, self, "pd.typec1Watts", const.TYPEC_1_OUT_POWER),
            OutWattsSensorEntity(client, self, "pd.typec2Watts", const.TYPEC_2_OUT_POWER),
            OutWattsSensorEntity(client, self, "pd.usb1Watts", const.USB_1_OUT_POWER),
            OutWattsSensorEntity(client, self, "pd.usb2Watts", const.USB_2_OUT_POWER),
            OutWattsSensorEntity(client, self, "pd.qcUsb1Watts", const.USB_QC_1_OUT_POWER),
            OutWattsSensorEntity(client, self, "pd.qcUsb2Watts", const.USB_QC_2_OUT_POWER),

            # Time & Cycles
            RemainSensorEntity(client, self, "ems.chgRemainTime", const.CHARGE_REMAINING_TIME),
            RemainSensorEntity(client, self, "ems.dsgRemainTime", const.DISCHARGE_REMAINING_TIME),
            CyclesSensorEntity(client, self, "bmsMaster.cycles", const.CYCLES),

            # Temperature
            TempSensorEntity(client, self, "bmsMaster.temp", const.BATTERY_TEMP)
            .attr("bmsMaster.minCellTemp", const.ATTR_MIN_CELL_TEMP, 0)
            .attr("bmsMaster.maxCellTemp", const.ATTR_MAX_CELL_TEMP, 0),
            TempSensorEntity(client, self, "bmsMaster.minCellTemp", const.MIN_CELL_TEMP, False),
            TempSensorEntity(client, self, "bmsMaster.maxCellTemp", const.MAX_CELL_TEMP, False),

            # Voltage
            MilliVoltSensorEntity(client, self, "bmsMaster.vol", const.BATTERY_VOLT, False)
            .attr("bmsMaster.minCellVol", const.ATTR_MIN_CELL_VOLT, 0)
            .attr("bmsMaster.maxCellVol", const.ATTR_MAX_CELL_VOLT, 0),
            MilliVoltSensorEntity(client, self, "bmsMaster.minCellVol", const.MIN_CELL_VOLT, False),
            MilliVoltSensorEntity(client, self, "bmsMaster.maxCellVol", const.MAX_CELL_VOLT, False),

            # Energy counters
            InEnergySensorEntity(client, self, "pd.chgSunPower", const.SOLAR_IN_ENERGY),
            InEnergySensorEntity(client, self, "pd.chgPowerAc", const.CHARGE_AC_ENERGY),
            InEnergySensorEntity(client, self, "pd.chgPowerDc", const.CHARGE_DC_ENERGY),
            OutEnergySensorEntity(client, self, "pd.dsgPowerAc", const.DISCHARGE_AC_ENERGY),
            OutEnergySensorEntity(client, self, "pd.dsgPowerDc", const.DISCHARGE_DC_ENERGY),

            # Optional Slave Batteries (same as Delta Pro)
            LevelSensorEntity(client, self, "bmsSlave1.soc", const.SLAVE_N_BATTERY_LEVEL % 1, False, True)
            .attr("bmsSlave1.designCap", const.ATTR_DESIGN_CAPACITY, 0)
            .attr("bmsSlave1.fullCap", const.ATTR_FULL_CAPACITY, 0)
            .attr("bmsSlave1.remainCap", const.ATTR_REMAIN_CAPACITY, 0),
            LevelSensorEntity(client, self, "bmsSlave1.f32ShowSoc", const.SLAVE_N_BATTERY_LEVEL_F32 % 1, False, False)
            .attr("bmsSlave1.designCap", const.ATTR_DESIGN_CAPACITY, 0)
            .attr("bmsSlave1.fullCap", const.ATTR_FULL_CAPACITY, 0)
            .attr("bmsSlave1.remainCap", const.ATTR_REMAIN_CAPACITY, 0),
            CapacitySensorEntity(client, self, "bmsSlave1.designCap", const.SLAVE_N_DESIGN_CAPACITY % 1, False),
            CapacitySensorEntity(client, self, "bmsSlave1.fullCap", const.SLAVE_N_FULL_CAPACITY % 1, False),
            CapacitySensorEntity(client, self, "bmsSlave1.remainCap", const.SLAVE_N_REMAIN_CAPACITY % 1, False),
            LevelSensorEntity(client, self, "bmsSlave1.soh", const.SLAVE_N_SOH % 1),

            TempSensorEntity(client, self, "bmsSlave1.temp", const.SLAVE_N_BATTERY_TEMP % 1, False, True)
            .attr("bmsSlave1.minCellTemp", const.ATTR_MIN_CELL_TEMP, 0)
            .attr("bmsSlave1.maxCellTemp", const.ATTR_MAX_CELL_TEMP, 0),
            WattsSensorEntity(client, self, "bmsSlave1.inputWatts", const.SLAVE_N_IN_POWER % 1, False, True),
            WattsSensorEntity(client, self, "bmsSlave1.outputWatts", const.SLAVE_N_OUT_POWER % 1, False, True),

            LevelSensorEntity(client, self, "bmsSlave2.soc", const.SLAVE_N_BATTERY_LEVEL % 2, False, True)
            .attr("bmsSlave2.designCap", const.ATTR_DESIGN_CAPACITY, 0)
            .attr("bmsSlave2.fullCap", const.ATTR_FULL_CAPACITY, 0)
            .attr("bmsSlave2.remainCap", const.ATTR_REMAIN_CAPACITY, 0),
            LevelSensorEntity(client, self, "bmsSlave2.f32ShowSoc", const.SLAVE_N_BATTERY_LEVEL_F32 % 2, False, False)
            .attr("bmsSlave2.designCap", const.ATTR_DESIGN_CAPACITY, 0)
            .attr("bmsSlave2.fullCap", const.ATTR_FULL_CAPACITY, 0)
            .attr("bmsSlave2.remainCap", const.ATTR_REMAIN_CAPACITY, 0),
            CapacitySensorEntity(client, self, "bmsSlave2.designCap", const.SLAVE_N_DESIGN_CAPACITY % 2, False),
            CapacitySensorEntity(client, self, "bmsSlave2.fullCap", const.SLAVE_N_FULL_CAPACITY % 2, False),
            CapacitySensorEntity(client, self, "bmsSlave2.remainCap", const.SLAVE_N_REMAIN_CAPACITY % 2, False),
            LevelSensorEntity(client, self, "bmsSlave2.soh", const.SLAVE_N_SOH % 2),
            MilliVoltSensorEntity(client, self, "bmsSlave1.vol", const.SLAVE_N_BATTERY_VOLT % 1, False),
            MilliVoltSensorEntity(client, self, "bmsSlave1.minCellVol", const.SLAVE_N_MIN_CELL_VOLT % 1, False),
            MilliVoltSensorEntity(client, self, "bmsSlave1.maxCellVol", const.SLAVE_N_MAX_CELL_VOLT % 1, False),
            AmpSensorEntity(client, self, "bmsSlave1.amp", const.SLAVE_N_BATTERY_CURRENT % 1, False),
            MilliVoltSensorEntity(client, self, "bmsSlave2.vol", const.SLAVE_N_BATTERY_VOLT % 2, False),
            MilliVoltSensorEntity(client, self, "bmsSlave2.minCellVol", const.SLAVE_N_MIN_CELL_VOLT % 2, False),
            MilliVoltSensorEntity(client, self, "bmsSlave2.maxCellVol", const.SLAVE_N_MAX_CELL_VOLT % 2, False),
            AmpSensorEntity(client, self, "bmsSlave2.amp", const.SLAVE_N_BATTERY_CURRENT % 2, False),
            TempSensorEntity(client, self, "bmsSlave2.temp", const.SLAVE_N_BATTERY_TEMP % 2, False, True)
            .attr("bmsSlave2.minCellTemp", const.ATTR_MIN_CELL_TEMP, 0)
            .attr("bmsSlave2.maxCellTemp", const.ATTR_MAX_CELL_TEMP, 0),
            WattsSensorEntity(client, self, "bmsSlave2.inputWatts", const.SLAVE_N_IN_POWER % 2, False, True),
            WattsSensorEntity(client, self, "bmsSlave2.outputWatts", const.SLAVE_N_OUT_POWER % 2, False, True),
            CyclesSensorEntity(client, self, "bmsSlave1.cycles", const.SLAVE_N_CYCLES % 1, False),
            CyclesSensorEntity(client, self, "bmsSlave2.cycles", const.SLAVE_N_CYCLES % 2, False),
            QuotaStatusSensorEntity(client, self),
        ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return [
            MaxBatteryLevelEntity(client, self, "ems.maxChargeSoc", const.MAX_CHARGE_LEVEL, 50, 100,
                                  lambda value: {"moduleType": 0, "operateType": "TCP",
                                                 "params": {"id": 49, "maxChgSoc": value}}),
            MinBatteryLevelEntity(client, self, "ems.minDsgSoc", const.MIN_DISCHARGE_LEVEL, 0, 30,
                                  lambda value: {"moduleType": 0, "operateType": "TCP",
                                                 "params": {"id": 51, "minDsgSoc": value}}),
            MaxBatteryLevelEntity(client, self, "pd.bppowerSoc", const.BACKUP_RESERVE_LEVEL, 5, 100,
                                  lambda value: {"moduleType": 0, "operateType": "TCP",
                                                 "params": {"isConfig": 1, "bpPowerSoc": int(value), "minDsgSoc": 0,
                                                            "maxChgSoc": 0, "id": 94}}),
            MinGenStartLevelEntity(client, self, "ems.minOpenOilEbSoc", const.GEN_AUTO_START_LEVEL, 0, 30,
                                   lambda value: {"moduleType": 0, "operateType": "TCP",
                                                  "params": {"openOilSoc": value, "id": 52}}),

            MaxGenStopLevelEntity(client, self, "ems.maxCloseOilEbSoc", const.GEN_AUTO_STOP_LEVEL, 50, 100,
                                  lambda value: {"moduleType": 0, "operateType": "TCP",
                                                 "params": {"closeOilSoc": value, "id": 53}}),

            # Adjusted AC charging power range for Delta Pro 3 (assuming higher capacity)
            ChargingPowerEntity(client, self, "inv.cfgSlowChgWatts", const.AC_CHARGING_POWER, 200, 3600,
                                lambda value: {"moduleType": 0, "operateType": "TCP",
                                               "params": {"slowChgPower": value, "id": 69}}),

        ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return [
            BeeperEntity(client, self, "pd.beepState", const.BEEPER,
                         lambda value: {"moduleType": 0, "operateType": "TCP", "params": {"id": 38, "enabled": value}}),
            EnabledEntity(client, self, "mppt.carState", const.DC_ENABLED,
                          lambda value: {"moduleType": 0, "operateType": "TCP",
                                         "params": {"id": 81, "enabled": value}}),
            EnabledEntity(client, self, "inv.cfgAcEnabled", const.AC_ENABLED,
                          lambda value: {"moduleType": 0, "operateType": "TCP",
                                         "params": {"id": 66, "enabled": value}}),

            EnabledEntity(client, self, "inv.cfgAcXboost", const.XBOOST_ENABLED,
                          lambda value: {"moduleType": 0, "operateType": "TCP", "params": {"id": 66, "xboost": value}}),
            EnabledEntity(client, self, "pd.acautooutConfig", const.AC_ALWAYS_ENABLED,
                          lambda value: {"moduleType": 0, "operateType": "TCP",
                                         "params": {"id": 95, "acautooutConfig": value}}),
            EnabledEntity(client, self, "pd.watthisconfig", const.BP_ENABLED,
                          lambda value, params: {"moduleType": 0, "operateType": "TCP",
                                                 "params": {"id": 94, "isConfig": value,
                                                            "bpPowerSoc": value * 50,
                                                            "minDsgSoc": 0,
                                                            "maxChgSoc": 0}}),
        ]

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return [
            TimeoutDictSelectEntity(client, self, "pd.lcdOffSec", const.SCREEN_TIMEOUT, const.SCREEN_TIMEOUT_OPTIONS,
                                    lambda value: {"moduleType": 0, "operateType": "TCP",
                                                   "params": {"lcdTime": value}}),
            TimeoutDictSelectEntity(client, self, "pd.standbyMin", const.UNIT_TIMEOUT, const.UNIT_TIMEOUT_OPTIONS,
                                    lambda value: {"moduleType": 0, "operateType": "TCP",
                                                   "params": {"standbyMin": value}}),
            TimeoutDictSelectEntity(client, self, "inv.cfgStandbyMin", const.AC_TIMEOUT, const.AC_TIMEOUT_OPTIONS,
                                    lambda value: {"moduleType": 0, "operateType": "TCP",
                                                   "params": {"standbyMins": value}}),
            TimeoutDictSelectEntity(client, self, "mppt.dcChgCurrent", const.DC_CHARGE_CURRENT,
                                    const.DC_CHARGE_CURRENT_OPTIONS,
                                    lambda value: {"moduleType": 0, "operateType": "TCP",
                                                   "params": {"dcChgCfg": value}}),
        ]

    def _prepare_data(self, raw_data) -> dict[str, any]:
        """
        Parses Delta Pro 3 protobuf data.
        Uses Delta Pro 3 specific protobuf structure.
        """
        import logging
        from homeassistant.util import utcnow
        _LOGGER = logging.getLogger(__name__)
        
        data = {"params": {}}
        from .proto import ecopacket_pb2 as ecopacket, delta_pro3_pb2 as delta_pro3

        try:
            payload = raw_data
            
            while True:
                try:
                    packet = ecopacket.SendHeaderMsg()
                    packet.ParseFromString(payload)
                except Exception as parse_error:
                    _LOGGER.debug("Delta Pro 3: Invalid ecopacket format, skipping: %s", parse_error)
                    # If we can't parse as ecopacket, skip this message
                    break

                _LOGGER.debug("Delta Pro 3 cmd id %u payload \"%s\"", packet.msg.cmd_id, payload.hex())

                if packet.msg.cmd_id not in [1, 2, 21, 22, 50]:
                    _LOGGER.info("Delta Pro 3 unsupported EcoPacket cmd id %u", packet.msg.cmd_id)
                else:
                    pdata = packet.msg.pdata
                    _LOGGER.debug("Delta Pro 3 cmd_id %u pdata length: %u bytes", packet.msg.cmd_id, len(pdata))
                    
                    if packet.msg.cmd_id == 50:
                        # cmd_id 50: Large status message - use DeltaPro3Status
                        try:
                            status = delta_pro3.DeltaPro3Status()
                            status.ParseFromString(pdata)
                            
                            # Restore basic field mapping with corrected scaling factors
                            # IMPORTANT: Exclude solar fields that would conflict with manual injection
                            field_mapping = {
                                # Battery Master fields
                                'soc': 'bmsMaster.soc',
                                'voltage': 'bmsMaster.vol', 
                                'current': 'bmsMaster.amp',
                                'temp': 'bmsMaster.temp',
                                'cycles': 'bmsMaster.cycles',
                                'remain_cap': 'bmsMaster.remainCap',
                                'full_cap': 'bmsMaster.fullCap',
                                'design_cap': 'bmsMaster.designCap',
                                'soh': 'bmsMaster.soh',
                                
                                # Power fields with corrected scaling
                                'input_watts': 'pd.wattsInSum',
                                'output_watts': 'pd.wattsOutSum',
                                'ac_in_watts': 'inv.inputWatts',
                                'ac_out_watts': 'inv.outputWatts',
                                
                                # USB/Type-C Output
                                'usb1_watts': 'pd.usb1Watts',
                                'usb2_watts': 'pd.usb2Watts',
                                'typec1_watts': 'pd.typec1Watts',
                                'typec2_watts': 'pd.typec2Watts',
                                'qc_usb1_watts': 'pd.qcUsb1Watts',
                                'qc_usb2_watts': 'pd.qcUsb2Watts',
                                
                                # DC Output
                                'dc_out_watts': 'mppt.outWatts',
                                'car_out_watts': 'mppt.carOutWatts',
                                'anderson_watts': 'mppt.dcdc12vWatts',
                                
                                # AC Voltage
                                'ac_in_vol': 'inv.acInVol',
                                'ac_out_vol': 'inv.invOutVol',
                                
                                # Time fields
                                'charge_time': 'ems.chgRemainTime',
                                'discharge_time': 'ems.dsgRemainTime',
                                
                                # Combined battery
                                'combined_soc': 'ems.lcdShowSoc',
                                'combined_soc_f32': 'ems.f32LcdShowSoc',

                                # Energy counters (Wh)
                                'solar_in_energy':      'pd.chgSunPower',
                                'charge_ac_energy':     'pd.chgPowerAc',
                                'charge_dc_energy':     'pd.chgPowerDc',
                                'discharge_ac_energy':  'pd.dsgPowerAc',
                                'discharge_dc_energy':  'pd.dsgPowerDc',
                                
                                # NOTE: Excluded solar fields to prevent conflicts with manual extraction:
                                # 'solar_in_watts': would create duplicate sensors
                                # 'solar_in_vol': would create duplicate sensors  
                                # 'solar_in_cur': would create duplicate sensors
                                # 'solar_lv_watts': additional LV power field that would create duplicates
                                # 'solar_lv_cur': additional LV current field that would create duplicates
                                # 'solar_hv_watts_raw': raw HV field used in manual extraction
                                # 'solar_lv_watts_raw': raw LV field  
                                # 'solar_lv_watts_raw2': raw LV field 2 used in manual extraction
                            }

                            for proto_field, ha_field in field_mapping.items():
                                if hasattr(status, proto_field):
                                    raw_value = getattr(status, proto_field)
                                    # Apply corrected scaling based on real data analysis
                                    if proto_field == 'voltage':
                                        mapped_value = raw_value / 1000  # millivolts to volts
                                    elif proto_field == 'current':
                                        if raw_value > 2147483647:
                                            raw_value = raw_value - 4294967296
                                        mapped_value = raw_value / 1000
                                    elif proto_field == 'input_watts':
                                        mapped_value = round(raw_value / 400, 1)
                                    elif proto_field == 'output_watts':
                                        mapped_value = round(raw_value / 53.4, 1)
                                    elif proto_field in ['ac_in_vol', 'ac_out_vol']:
                                        volts = raw_value / 27.9
                                        mapped_value = int(volts * 1000)
                                    elif proto_field.endswith('_watts') and raw_value > 50000:
                                        mapped_value = 0
                                    elif proto_field.endswith('_watts'):
                                        mapped_value = raw_value / 100
                                    elif proto_field in ['solar_in_energy','charge_ac_energy','charge_dc_energy','discharge_ac_energy','discharge_dc_energy']:
                                        mapped_value = int(raw_value / 100)
                                    else:
                                        mapped_value = raw_value
                                    
                                    data["params"][ha_field] = mapped_value
                                    _LOGGER.debug(f"Delta Pro 3 mapped: {proto_field} -> {ha_field} = {mapped_value}")

                            # Extract solar data from protobuf fields
                            experimental_hv_solar = 0
                            experimental_lv_solar = 0  
                            if hasattr(status, 'solar_hv_watts_raw') and getattr(status, 'solar_hv_watts_raw', 0) > 0:
                                raw72 = getattr(status, 'solar_hv_watts_raw', 0)
                                experimental_hv_solar = raw72 / 500  # Corrected scaling to match app (99W from ~49k raw)
                                
                                # Extract HV voltage and current from protobuf fields
                                hv_voltage_raw = getattr(status, 'solar_hv_vol_raw', 0)
                                hv_current_raw = getattr(status, 'solar_hv_cur_raw', 0)
                                
                                # Set HV solar values accounting for sensor entity additional scaling
                                # InWattsSolarSensorEntity applies ÷10, so we multiply by 10
                                # InVoltSolarSensorEntity applies ÷10, so we multiply by 10  
                                # InAmpSolarSensorEntity applies ×10, so we divide by 10
                                data["params"]["mppt.hvInWatts"] = experimental_hv_solar * 10  # Will be ÷10 by sensor → correct value
                                
                                # Calculate HV voltage and current with proper scaling
                                if hv_voltage_raw > 0:
                                    hv_voltage = hv_voltage_raw / 400  # Scale to realistic voltage
                                else:
                                    hv_voltage = 0
                                    
                                if hv_current_raw > 0:
                                    hv_current_a = hv_current_raw / 37000  # Scale to realistic current
                                    hv_current_ma = hv_current_a * 1000
                                else:
                                    hv_current_ma = 0
                                
                                data["params"]["mppt.hvInVol"] = hv_voltage * 10  # Will be ÷10 by sensor → correct V
                                data["params"]["mppt.hvInAmp"] = hv_current_ma / 10  # Will be ×10 by sensor → correct mA
                                    
                            if hasattr(status, 'solar_lv_watts_raw2') and getattr(status, 'solar_lv_watts_raw2', 0) > 0:
                                raw73 = getattr(status, 'solar_lv_watts_raw2', 0)
                                experimental_lv_solar = raw73 / 2374  # Corrected scaling to match app (38W from ~90k raw)
                                
                                # Extract LV voltage and current from protobuf fields
                                lv_voltage_raw = getattr(status, 'solar_lv_vol_raw', 0)    # Field 18
                                lv_current_raw = getattr(status, 'solar_lv_cur_raw', 0)    # Field 19
                                
                                # Set LV solar values accounting for sensor entity additional scaling
                                data["params"]["mppt.lvInWatts"] = experimental_lv_solar * 10  # Will be ÷10 by sensor → correct value
                                
                                # Calculate LV voltage and current with proper scaling
                                if lv_voltage_raw > 0:
                                    lv_voltage = lv_voltage_raw * 2.08  # Scale to panel voltage (~50V)
                                else:
                                    lv_voltage = 0
                                    
                                if lv_current_raw > 0:
                                    lv_current_a = lv_current_raw * 0.036  # Scale to realistic current
                                    lv_current_ma = lv_current_a * 1000
                                else:
                                    lv_current_ma = 0
                                
                                data["params"]["mppt.lvInVol"] = lv_voltage * 10  # Will be ÷10 by sensor → correct V
                                data["params"]["mppt.lvInAmp"] = lv_current_ma / 10  # Will be ×10 by sensor → correct mA
                        except Exception as e:
                            _LOGGER.warning("Delta Pro 3 cmd_id 50: Failed to parse as DeltaPro3Status: %s", e)
                            # Continue logging raw data for analysis
                            data["params"]["cmd_50_raw_hex"] = pdata.hex()
                            data["params"]["cmd_50_length"] = len(pdata)
                    
                    elif packet.msg.cmd_id == 21:
                        # cmd_id 21: Heartbeat - appears to be encrypted/encoded data
                        # Variable length (56-92 bytes), no clear pattern found
                        # For now, just log for future analysis when we understand the encoding
                        _LOGGER.debug("Delta Pro 3 cmd_id 21: Encrypted/encoded heartbeat data (%u bytes) - logging for analysis", len(pdata))
                        data["params"]["cmd_21_raw_hex"] = pdata.hex()
                        data["params"]["cmd_21_length"] = len(pdata)
                    
                    elif packet.msg.cmd_id == 2:
                        # cmd_id 2: Store raw data for future analysis
                        _LOGGER.debug("Delta Pro 3 cmd_id %u pdata hex: %s", packet.msg.cmd_id, pdata.hex())
                        data["params"][f"cmd_{packet.msg.cmd_id}_raw_hex"] = pdata.hex()
                        data["params"][f"cmd_{packet.msg.cmd_id}_length"] = len(pdata)
                    
                    else:
                        # cmd_id 2, 22: Still analyzing - keep raw data
                        _LOGGER.debug("Delta Pro 3 cmd_id %u pdata hex: %s", packet.msg.cmd_id, pdata.hex())
                        data["params"][f"cmd_{packet.msg.cmd_id}_raw_hex"] = pdata.hex()
                        data["params"][f"cmd_{packet.msg.cmd_id}_length"] = len(pdata)
                    
                    data["timestamp"] = utcnow()

                # Check if we've processed the entire payload
                try:
                    if packet.ByteSize() >= len(payload):
                        break

                    _LOGGER.debug("Delta Pro 3: Found another frame in payload")
                    packet_length = len(payload) - packet.ByteSize()
                    payload = payload[:packet_length]
                except Exception as frame_error:
                    _LOGGER.debug("Delta Pro 3: Error processing frame: %s", frame_error)
                    break

        except Exception as error:
            _LOGGER.debug("Delta Pro 3 parsing error: %s", error)
            _LOGGER.debug("Delta Pro 3 raw data: %s", raw_data.hex() if raw_data else "None")
            # Don't fail completely - return what we have
            if not data.get("params"):
                data["params"]["parse_error"] = str(error)
                data["params"]["raw_data_hex"] = raw_data.hex() if raw_data else "None"

        return data 