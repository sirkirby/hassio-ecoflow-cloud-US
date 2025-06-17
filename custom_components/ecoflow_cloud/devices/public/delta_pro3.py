from custom_components.ecoflow_cloud.api import EcoflowApiClient
from custom_components.ecoflow_cloud.devices import const
from custom_components.ecoflow_cloud.entities import BaseSensorEntity, BaseNumberEntity, BaseSwitchEntity, \
    BaseSelectEntity
from custom_components.ecoflow_cloud.number import ChargingPowerEntity, MaxBatteryLevelEntity, MinBatteryLevelEntity, \
    MinGenStartLevelEntity, \
    MaxGenStopLevelEntity
from custom_components.ecoflow_cloud.select import DictSelectEntity, TimeoutDictSelectEntity
from custom_components.ecoflow_cloud.sensor import LevelSensorEntity, WattsSensorEntity, RemainSensorEntity, \
    TempSensorEntity, InWattsSensorEntity, OutWattsSensorEntity, OutWattsDcSensorEntity, InWattsSolarSensorEntity, \
    CapacitySensorEntity, QuotaStatusSensorEntity
from custom_components.ecoflow_cloud.switch import BeeperEntity, EnabledEntity

# Import from internal version for implementation sharing
from ..internal.delta_pro3 import DeltaPro3 as InternalDeltaPro3


class DeltaPro3(InternalDeltaPro3):
    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [
            # Main Battery - Using official Delta Pro 3 field names from DP3_IoT_Developer.md
            LevelSensorEntity(client, self, "cmsBattSoc", const.MAIN_BATTERY_LEVEL),  # Overall SOC (float)
            LevelSensorEntity(client, self, "bmsBattSoc", const.MAIN_BATTERY_LEVEL_F32, False),  # Main battery SOC (float)
            CapacitySensorEntity(client, self, "bmsDesignCap", const.MAIN_DESIGN_CAPACITY, False),  # Battery capacity (mAh)
            
            # Combined battery level (for systems with multiple batteries)
            LevelSensorEntity(client, self, "cmsBattSoc", const.COMBINED_BATTERY_LEVEL),

            # === CRITICAL POWER FIELDS (Official API) ===
            WattsSensorEntity(client, self, "powInSumW", const.TOTAL_IN_POWER),  # Total input power (W)
            WattsSensorEntity(client, self, "powOutSumW", const.TOTAL_OUT_POWER),  # Total output power (W)

            # AC Input/Output - Official field names
            InWattsSensorEntity(client, self, "powGetAcIn", const.AC_IN_POWER),  # Real-time AC input power (W)
            OutWattsSensorEntity(client, self, "powGetAc", const.AC_OUT_POWER),  # Real-time AC power (W)
            OutWattsSensorEntity(client, self, "powGetAcHvOut", "HV AC Output Power"),  # Real-time grid power (W)
            OutWattsSensorEntity(client, self, "powGetAcLvOut", "LV AC Output Power"),  # Real-time LV AC output (W)

            # Solar Input - Official field names
            InWattsSolarSensorEntity(client, self, "powGetPvH", const.SOLAR_1_IN_POWER),  # Real-time HV PV power (W)
            InWattsSolarSensorEntity(client, self, "powGetPvL", const.SOLAR_2_IN_POWER),  # Real-time LV PV power (W)

            # DC Output - Official field names
            OutWattsDcSensorEntity(client, self, "powGet12v", const.DC_OUT_POWER),  # Real-time 12V power (W)
            OutWattsSensorEntity(client, self, "powGet24v", "24V Output Power"),  # Real-time 24V power (W)

            # Type-C Output - Official field names
            OutWattsSensorEntity(client, self, "powGetTypec1", const.TYPEC_1_OUT_POWER),  # Real-time Type-C 1 power (W)
            OutWattsSensorEntity(client, self, "powGetTypec2", const.TYPEC_2_OUT_POWER),  # Real-time Type-C 2 power (W)

            # USB Output - Official field names
            OutWattsSensorEntity(client, self, "powGetQcusb1", const.USB_QC_1_OUT_POWER),  # Real-time USB 1 power (W)
            OutWattsSensorEntity(client, self, "powGetQcusb2", const.USB_QC_2_OUT_POWER),  # Real-time USB 2 power (W)

            # Power In/Out port - Official field names
            OutWattsSensorEntity(client, self, "powGet5p8", "Power In/Out Port Power"),  # Real-time Power In/Out port (W)

            # Extra Battery ports - Official field names  
            OutWattsSensorEntity(client, self, "powGet4p81", "Extra Battery Port 1 Power"),  # Real-time Extra Battery Port 1 (W)
            OutWattsSensorEntity(client, self, "powGet4p82", "Extra Battery Port 2 Power"),  # Real-time Extra Battery Port 2 (W)

            # Time & Status - Official field names
            RemainSensorEntity(client, self, "cmsChgRemTime", const.CHARGE_REMAINING_TIME),  # Remaining charging time (min)
            RemainSensorEntity(client, self, "cmsDsgRemTime", const.DISCHARGE_REMAINING_TIME),  # Remaining discharging time (min)
            RemainSensorEntity(client, self, "bmsChgRemTime", "Main Battery Charge Time", False),  # Main battery charging time (min)
            RemainSensorEntity(client, self, "bmsDsgRemTime", "Main Battery Discharge Time", False),  # Main battery discharge time (min)

            # Temperature - Official field names
            TempSensorEntity(client, self, "bmsMaxCellTemp", const.MAX_CELL_TEMP),  # Max temperature (°C)
            TempSensorEntity(client, self, "bmsMinCellTemp", const.MIN_CELL_TEMP),  # Min temperature (°C)

            # Status indicators
            LevelSensorEntity(client, self, "cmsChgDsgState", "Charging Status", False),  # Charging/Discharging status
            LevelSensorEntity(client, self, "cmsBmsRunState", "System Status", False),  # On/Off status
            LevelSensorEntity(client, self, "bmsChgDsgState", "Main Battery Status", False),  # Main battery charge/discharge status

            # Configuration and limits
            LevelSensorEntity(client, self, "cmsMaxChgSoc", const.MAX_CHARGE_LEVEL, False),  # Charge limit
            LevelSensorEntity(client, self, "cmsMinDsgSoc", const.MIN_DISCHARGE_LEVEL, False),  # Discharge limit

            # Generator control
            LevelSensorEntity(client, self, "cmsOilOnSoc", const.GEN_AUTO_START_LEVEL, False),  # SOC for starting generator
            LevelSensorEntity(client, self, "cmsOilOffSoc", const.GEN_AUTO_STOP_LEVEL, False),  # SOC for stopping generator

            # Advanced configuration
            LevelSensorEntity(client, self, "energyBackupStartSoc", const.BACKUP_RESERVE_LEVEL, False),  # Backup reserve level
            LevelSensorEntity(client, self, "lcdLight", "Screen Brightness", False),  # Screen brightness
            LevelSensorEntity(client, self, "screenOffTime", "Screen Timeout", False),  # Screen timeout (s)
            LevelSensorEntity(client, self, "acOutFreq", "AC Output Frequency", False),  # AC output frequency

            # Switch status indicators (flow info)
            LevelSensorEntity(client, self, "flowInfoPvH", "HV PV Switch Status", False),  # HV PV switch status
            LevelSensorEntity(client, self, "flowInfoPvL", "LV PV Switch Status", False),  # LV PV switch status
            LevelSensorEntity(client, self, "flowInfoAcHvOut", "HV AC Output Status", False),  # HV AC output switch
            LevelSensorEntity(client, self, "flowInfoAcLvOut", "LV AC Output Status", False),  # LV AC output switch
            LevelSensorEntity(client, self, "flowInfo12v", "12V Output Status", False),  # 12V output switch
            LevelSensorEntity(client, self, "flowInfo24v", "24V Output Status", False),  # 24V output switch
            LevelSensorEntity(client, self, "flowInfoTypec1", "Type-C 1 Status", False),  # Type-C 1 switch
            LevelSensorEntity(client, self, "flowInfoTypec2", "Type-C 2 Status", False),  # Type-C 2 switch
            LevelSensorEntity(client, self, "flowInfoQcusb1", "USB 1 Status", False),  # USB 1 switch
            LevelSensorEntity(client, self, "flowInfoQcusb2", "USB 2 Status", False),  # USB 2 switch

            # Configuration switches and flags
            LevelSensorEntity(client, self, "enBeep", const.BEEPER, False),  # Beeper on/off
            LevelSensorEntity(client, self, "xboostEn", const.XBOOST_ENABLED, False),  # X-Boost switch
            LevelSensorEntity(client, self, "llcGFCIFlag", "GFCI Switch", False),  # GFCI switch
            LevelSensorEntity(client, self, "acEnergySavingOpen", "AC Energy Saving", False),  # AC energy-saving mode
            LevelSensorEntity(client, self, "energyBackupEn", "Backup Reserve Enabled", False),  # Backup reserve function
            LevelSensorEntity(client, self, "cmsOilSelfStart", "Generator Auto Start", False),  # Smart Generator auto start/stop
            LevelSensorEntity(client, self, "generatorPvHybridModeOpen", "Generator Hybrid Mode", False),  # Generator solar hybrid
            LevelSensorEntity(client, self, "generatorCareModeOpen", "Night Care Mode", False),  # Night care mode

            QuotaStatusSensorEntity(client, self)
        ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return [
            MaxBatteryLevelEntity(client, self, "cmsMaxChgSoc", const.MAX_CHARGE_LEVEL, 50, 100,
                                  lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 49, "maxChgSoc": value}}),
            MinBatteryLevelEntity(client, self, "cmsMinDsgSoc", const.MIN_DISCHARGE_LEVEL, 0, 30,
                                  lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 51, "minDsgSoc": value}}),
            MaxBatteryLevelEntity(client, self, "pd.bppowerSoc", const.BACKUP_RESERVE_LEVEL, 5, 100,
                                  lambda value: {"operateType": "TCP",
                                                 "params": {"cmdSet": 32, "isConfig": 1, "bpPowerSoc": int(value), "minDsgSoc": 0,
                                                            "maxChgSoc": 0, "id": 94}}),
            MinGenStartLevelEntity(client, self, "cmsMinOpenOilEbSoc", const.GEN_AUTO_START_LEVEL, 0, 30,
                                   lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "openOilSoc": value, "id": 52}}),

            MaxGenStopLevelEntity(client, self, "cmsMaxCloseOilEbSoc", const.GEN_AUTO_STOP_LEVEL, 50, 100,
                                  lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "closeOilSoc": value, "id": 53}}),

            ChargingPowerEntity(client, self, "cfgSlowChgWatts", const.AC_CHARGING_POWER, 200, 3600,
                                lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "slowChgPower": value, "id": 69}}),

        ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return [
            BeeperEntity(client, self, "enBeep", const.BEEPER,
                         lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 38, "enabled": value}}),
            EnabledEntity(client, self, "flowInfo12v", const.DC_ENABLED,
                          lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 81, "enabled": value}}),
            EnabledEntity(client, self, "flowInfoAcHvOut", const.AC_ENABLED,
                          lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 66, "enabled": value}}),

            EnabledEntity(client, self, "xboostEn", const.XBOOST_ENABLED,
                          lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 66, "xboost": value}}),
            EnabledEntity(client, self, "acautooutConfig", const.AC_ALWAYS_ENABLED,
                          lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 95, "acautooutConfig": value}}),
            EnabledEntity(client, self, "watthisconfig", const.BP_ENABLED,
                          lambda value, params: {"operateType": "TCP",
                                                 "params": {"cmdSet": 32, "id": 94, "isConfig": value,
                                                            "bpPowerSoc": value * 50,
                                                            "minDsgSoc": 0,
                                                            "maxChgSoc": 0}}),
        ]

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return [
            DictSelectEntity(client, self, "mppt.cfgDcChgCurrent", const.DC_CHARGE_CURRENT, const.DC_CHARGE_CURRENT_OPTIONS,
                             lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "currMa": value, "id": 71}}),

            TimeoutDictSelectEntity(client, self, "pd.lcdOffSec", const.SCREEN_TIMEOUT, const.SCREEN_TIMEOUT_OPTIONS,
                                    lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "lcdTime": value, "id": 39}}),

            TimeoutDictSelectEntity(client, self, "pd.standByMode", const.UNIT_TIMEOUT, const.UNIT_TIMEOUT_OPTIONS_LIMITED,
                                    lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "standByMode": value, "id": 33}}),

            TimeoutDictSelectEntity(client, self, "inv.cfgStandbyMin", const.AC_TIMEOUT, const.AC_TIMEOUT_OPTIONS,
                                    lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "standByMins": value, "id": 153}}),

        ]

    def _prepare_data(self, raw_data) -> dict[str, any]:
        """
        Enhanced Delta Pro 3 public API data parsing with comprehensive field analysis.
        """
        import logging
        from homeassistant.util import utcnow
        _LOGGER = logging.getLogger(__name__)
        
        # Add diagnostic logging for data flow  
        _LOGGER.info("=== DELTA PRO 3 PUBLIC API DATA PROCESSING START ===")
        _LOGGER.info("Raw data length: %d bytes", len(raw_data) if raw_data else 0)
        _LOGGER.info("Raw data hex preview: %s", raw_data[:50].hex() if raw_data and len(raw_data) > 0 else "No data")

        from ..internal.proto import ecopacket_pb2 as ecopacket, delta_pro3_pb2 as delta_pro3
        raw = {"params": {}}

        try:
            payload = raw_data
            packet = ecopacket.SendHeaderMsg()
            packet.ParseFromString(payload)

            _LOGGER.debug("Delta Pro 3 (Public) cmd id %u payload \"%s\"", packet.msg.cmd_id, payload.hex())

            if packet.msg.cmd_id not in [1, 2, 21, 22, 50]:
                _LOGGER.info("Delta Pro 3 (Public) unsupported EcoPacket cmd id %u", packet.msg.cmd_id)
            else:
                pdata = packet.msg.pdata
                _LOGGER.debug("Delta Pro 3 (Public) cmd_id %u pdata length: %u bytes", packet.msg.cmd_id, len(pdata))
                
                if packet.msg.cmd_id == 50:
                    # cmd_id 50: Large status message - use DeltaPro3Status
                    try:
                        status = delta_pro3.DeltaPro3Status()
                        status.ParseFromString(pdata)
                        
                        # Enhanced field mapping with comprehensive power analysis
                        field_mapping = {
                            'soc': 'bmsMaster.soc',
                            'voltage': 'bmsMaster.vol', 
                            'current': 'bmsMaster.amp',
                            'temp': 'bmsMaster.temp',
                            'cycles': 'bmsMaster.cycles',
                            'input_watts': 'pd.wattsInSum',
                            'output_watts': 'pd.wattsOutSum',
                            'ac_in_vol': 'inv.acInVol',
                            'ac_out_vol': 'inv.invOutVol',
                            'ac_in_watts': 'inv.inputWatts',
                            'ac_out_watts': 'inv.outputWatts',
                            'solar_lv_watts_basic': 'mppt.lvInWatts',
                            'solar_lv_vol_raw': 'mppt.lvInVol',
                            'solar_lv_cur_raw': 'mppt.lvInAmp',
                            'solar_hv_watts_raw': 'mppt.hvInWatts',
                            'solar_hv_vol_raw': 'mppt.hvInVol',
                            'solar_hv_cur_raw': 'mppt.hvInAmp',
                            'dc_out_watts': 'mppt.outWatts',
                            'car_out_watts': 'mppt.carOutWatts',
                            'anderson_watts': 'mppt.dcdc12vWatts',
                            'usb1_watts': 'pd.usb1Watts',
                            'usb2_watts': 'pd.usb2Watts',
                            'typec1_watts': 'pd.typec1Watts',
                            'typec2_watts': 'pd.typec2Watts',
                            'qc_usb1_watts': 'pd.qcUsb1Watts',
                            'qc_usb2_watts': 'pd.qcUsb2Watts',
                            'charge_time': 'ems.chgRemainTime',
                            'discharge_time': 'ems.dsgRemainTime',
                            'remain_cap': 'bmsMaster.remainCap',
                            'full_cap': 'bmsMaster.fullCap',
                            'design_cap': 'bmsMaster.designCap',
                            'soh': 'bmsMaster.soh',
                            'min_cell_vol': 'bmsMaster.minCellVol',
                            'max_cell_vol': 'bmsMaster.maxCellVol',
                            'min_cell_temp': 'bmsMaster.minCellTemp',
                            'max_cell_temp': 'bmsMaster.maxCellTemp',
                            'combined_soc': 'ems.lcdShowSoc',
                            'combined_soc_f32': 'ems.f32LcdShowSoc',
                            # Energy fields
                            'charge_ac_energy': 'pd.chgPowerAc',
                            'charge_dc_energy': 'pd.chgPowerDc', 
                            'discharge_ac_energy': 'pd.dsgPowerAc',
                            'discharge_dc_energy': 'pd.dsgPowerDc',
                            'solar_in_energy': 'pd.chgSunPower'
                        }

                        # Log ALL available power-related fields to identify correct ones
                        _LOGGER.info("=== DELTA PRO 3 PUBLIC API COMPLETE FIELD ANALYSIS ===")
                        power_fields = [
                            'input_watts', 'output_watts', 'ac_in_watts', 'ac_out_watts',
                            'dc_out_watts', 'car_out_watts', 'anderson_watts',
                            'usb1_watts', 'usb2_watts', 'typec1_watts', 'typec2_watts',
                            'qc_usb1_watts', 'qc_usb2_watts',
                            'solar_lv_watts_basic', 'solar_hv_watts_raw', 'solar_lv_watts_raw2',
                            # New alternative power field candidates
                            'primary_input_watts', 'primary_output_watts', 'total_in_power', 'total_out_power',
                            'main_input_watts', 'main_output_watts'
                        ]
                        
                        for field in power_fields:
                            if hasattr(status, field):
                                value = getattr(status, field)
                                _LOGGER.info("Public API Field %s: %d", field, value)
                        
                        # Check unknown fields that might contain correct power values
                        unknown_fields = []
                        potential_power_fields = []
                        for i in range(1, 123):  # Extended to cover all new fields
                            field_name = f'unknown{i}'
                            if hasattr(status, field_name):
                                value = getattr(status, field_name)
                                if value > 10000:  # Look for large values
                                    unknown_fields.append(f"{field_name}={value}")
                                    # Look for values that might be correct power readings (1.52kW = 1520000mW)
                                    if 1000000 <= value <= 2000000:  # 1000W-2000W range in mW
                                        potential_power_fields.append(f"{field_name}={value}({value/1000:.1f}W)")
                                    elif 1000 <= value <= 2000:  # 1000W-2000W range in W
                                        potential_power_fields.append(f"{field_name}={value}(direct_W)")
                        
                        if unknown_fields:
                            _LOGGER.info("Large unknown fields: %s", ", ".join(unknown_fields))
                        
                        if potential_power_fields:
                            _LOGGER.info("POTENTIAL CORRECT POWER FIELDS (1.5kW range): %s", ", ".join(potential_power_fields))

                        # Process field mapping with enhanced scaling
                        parsed_fields = 0
                        for descriptor in status.DESCRIPTOR.fields:
                            value = getattr(status, descriptor.name, 0)
                            
                            # Process ALL power fields regardless of value, other fields only if non-zero
                            if value or 'watts' in descriptor.name or descriptor.name in ['soc', 'combined_soc']:
                                sensor_name = field_mapping.get(descriptor.name, descriptor.name)
                                
                                # Handle data type conversions and scaling for specific fields
                                converted_value = value
                                if descriptor.name in ['current', 'amp'] and value > 2147483647:
                                    # Handle signed 32-bit integer overflow (battery current can be negative)
                                    converted_value = value - 4294967296
                                    _LOGGER.info("Delta Pro 3 (Public) converted signed int: %s = %d -> %d", descriptor.name, value, converted_value)
                                elif descriptor.name == 'input_watts':
                                    # Enhanced scaling analysis - try multiple scaling factors
                                    scale_400 = round(value / 400, 1) if value > 0 else 0
                                    scale_1000 = round(value / 1000, 1) if value > 0 else 0
                                    _LOGGER.info("Delta Pro 3 input_watts scaling: raw=%d, ÷400=%0.1fW, ÷1000=%0.1fW", value, scale_400, scale_1000)
                                    converted_value = scale_400  # Use ÷400 scaling
                                elif descriptor.name == 'output_watts':
                                    # Enhanced scaling analysis - try multiple scaling factors  
                                    scale_53 = round(value / 53.4, 1) if value > 0 else 0
                                    scale_1000 = round(value / 1000, 1) if value > 0 else 0
                                    _LOGGER.info("Delta Pro 3 output_watts scaling: raw=%d, ÷53.4=%0.1fW, ÷1000=%0.1fW", value, scale_53, scale_1000)
                                    converted_value = scale_53  # Use ÷53.4 scaling
                                elif descriptor.name.endswith('_watts') and 'solar' in descriptor.name:
                                    # Solar power fields - use minimal scaling for now
                                    converted_value = round(value / 100, 1) if value > 0 else 0
                                elif descriptor.name.endswith('_watts'):
                                    # Other power fields - use standard scaling
                                    converted_value = round(value / 100, 1) if value > 0 else 0
                                elif descriptor.name in ['charge_ac_energy', 'charge_dc_energy', 'discharge_ac_energy', 'discharge_dc_energy', 'solar_in_energy']:
                                    # Energy fields for Home Assistant energy dashboard
                                    converted_value = int(value / 100) if value > 0 else 0
                                    _LOGGER.info("Delta Pro 3 (Public) Energy field %s: raw=%d, scaled=%d", descriptor.name, value, converted_value)
                                
                                raw["params"][sensor_name] = converted_value
                                parsed_fields += 1

                        # Ensure critical fields are always available
                        if hasattr(status, 'soc'):
                            raw["params"]["bmsMaster.soc"] = getattr(status, 'soc')
                        if hasattr(status, 'combined_soc'):
                            raw["params"]["ems.lcdShowSoc"] = getattr(status, 'combined_soc')
                        elif hasattr(status, 'soc'):
                            raw["params"]["ems.lcdShowSoc"] = getattr(status, 'soc')

                        # Solar data processing with comprehensive logging
                        hv_raw_power = getattr(status, 'solar_hv_watts_raw', 0) if hasattr(status, 'solar_hv_watts_raw') else 0
                        lv_raw_power = getattr(status, 'solar_lv_watts_raw2', 0) if hasattr(status, 'solar_lv_watts_raw2') else 0
                        lv_basic_power = getattr(status, 'solar_lv_watts_basic', 0) if hasattr(status, 'solar_lv_watts_basic') else 0
                        
                        _LOGGER.info("Delta Pro 3 (Public) Solar Analysis: HV=%d, LV_raw=%d, LV_basic=%d", hv_raw_power, lv_raw_power, lv_basic_power)

                        # Use best available solar field mapping
                        if lv_basic_power > 0:
                            raw["params"]["mppt.lvInWatts"] = lv_basic_power // 100
                        elif lv_raw_power > 0:
                            raw["params"]["mppt.lvInWatts"] = lv_raw_power // 100
                            
                        if hv_raw_power > 0:
                            raw["params"]["mppt.hvInWatts"] = hv_raw_power // 100

                        _LOGGER.info("Delta Pro 3 (Public) parsed %d fields successfully", parsed_fields)
                        _LOGGER.info("=== END PUBLIC API FIELD ANALYSIS ===")

                    except Exception as e:
                        _LOGGER.warning("Delta Pro 3 (Public) cmd_id 50: Failed to parse as DeltaPro3Status: %s", e)
                        # Store raw data for analysis
                        raw["params"]["cmd_50_raw_hex"] = pdata.hex()
                        raw["params"]["cmd_50_length"] = len(pdata)

                raw["timestamp"] = utcnow()

        except Exception as error:
            _LOGGER.warning("Delta Pro 3 (Public) parsing error: %s", error)
            _LOGGER.debug("Delta Pro 3 (Public) raw data: %s", raw_data.hex() if raw_data else "None")

        return raw 