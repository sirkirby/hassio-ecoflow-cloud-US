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

# Import from internal version for implementation sharing
from ..internal.delta_pro3 import DeltaPro3 as InternalDeltaPro3
from .data_bridge import to_plain


class DeltaPro3(InternalDeltaPro3):
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

            # Solar Input
            InWattsSolarSensorEntity(client, self, "mppt.inWatts", const.SOLAR_IN_POWER),
            InVoltSolarSensorEntity(client, self, "mppt.inVol", const.SOLAR_IN_VOLTAGE),
            InAmpSolarSensorEntity(client, self, "mppt.inAmp", const.SOLAR_IN_CURRENT),

            # DC Output
            OutWattsDcSensorEntity(client, self, "mppt.outWatts", const.DC_OUT_POWER),
            OutVoltDcSensorEntity(client, self, "mppt.outVol", const.DC_OUT_VOLTAGE),
            OutWattsSensorEntity(client, self, "mppt.carOutWatts", const.DC_CAR_OUT_POWER),
            OutWattsSensorEntity(client, self, "mppt.dcdc12vWatts", const.DC_ANDERSON_OUT_POWER),

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
            QuotaStatusSensorEntity(client, self)
        ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return [
            MaxBatteryLevelEntity(client, self, "ems.maxChargeSoc", const.MAX_CHARGE_LEVEL, 50, 100,
                                  lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 49, "maxChgSoc": value}}),
            MinBatteryLevelEntity(client, self, "ems.minDsgSoc", const.MIN_DISCHARGE_LEVEL, 0, 30,
                                  lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 51, "minDsgSoc": value}}),
            MaxBatteryLevelEntity(client, self, "pd.bppowerSoc", const.BACKUP_RESERVE_LEVEL, 5, 100,
                                  lambda value: {"operateType": "TCP",
                                                 "params": {"cmdSet": 32, "isConfig": 1, "bpPowerSoc": int(value), "minDsgSoc": 0,
                                                            "maxChgSoc": 0, "id": 94}}),
            MinGenStartLevelEntity(client, self, "ems.minOpenOilEbSoc", const.GEN_AUTO_START_LEVEL, 0, 30,
                                   lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "openOilSoc": value, "id": 52}}),

            MaxGenStopLevelEntity(client, self, "ems.maxCloseOilEbSoc", const.GEN_AUTO_STOP_LEVEL, 50, 100,
                                  lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "closeOilSoc": value, "id": 53}}),

            # Adjusted AC charging power range for Delta Pro 3 (assuming higher capacity)
            ChargingPowerEntity(client, self, "inv.cfgSlowChgWatts", const.AC_CHARGING_POWER, 200, 3600,
                                lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "slowChgPower": value, "id": 69}}),

        ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return [
            BeeperEntity(client, self, "pd.beepState", const.BEEPER,
                         lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 38, "enabled": value}}),
            EnabledEntity(client, self, "mppt.carState", const.DC_ENABLED,
                          lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 81, "enabled": value}}),
            EnabledEntity(client, self, "inv.cfgAcEnabled", const.AC_ENABLED,
                          lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 66, "enabled": value}}),

            EnabledEntity(client, self, "inv.cfgAcXboost", const.XBOOST_ENABLED,
                          lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 66, "xboost": value}}),
            EnabledEntity(client, self, "pd.acautooutConfig", const.AC_ALWAYS_ENABLED,
                          lambda value: {"operateType": "TCP", "params": {"cmdSet": 32, "id": 95, "acautooutConfig": value}}),
            EnabledEntity(client, self, "pd.watthisconfig", const.BP_ENABLED,
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
        Parses Delta Pro 3 protobuf data.
        Uses Delta Pro 3 specific protobuf structure.
        """
        import logging
        from homeassistant.util import utcnow
        _LOGGER = logging.getLogger(__name__)
        
        raw = {"params": {}}
        from ..internal.proto import ecopacket_pb2 as ecopacket, delta_pro3_pb2 as delta_pro3

        try:
            payload = raw_data
            
            while True:
                try:
                    packet = ecopacket.SendHeaderMsg()
                    packet.ParseFromString(payload)
                except Exception as parse_error:
                    _LOGGER.debug("Delta Pro 3 (Public): Invalid ecopacket format, skipping: %s", parse_error)
                    # If we can't parse as ecopacket, skip this message
                    break

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
                            
                            # Extract fields with proper mapping to sensor names
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
                                'solar_in_watts': 'mppt.inWatts',
                                'solar_in_vol': 'mppt.inVol',
                                'solar_in_cur': 'mppt.inAmp',
                                'dc_out_watts': 'mppt.outWatts',
                                'car_out_watts': 'mppt.carOutWatts',
                                'anderson_watts': 'mppt.dcdc12vWatts',
                                'usb1_watts': 'pd.usb1Watts',
                                'usb2_watts': 'pd.usb2Watts',
                                'typec1_watts': 'pd.typec1Watts',
                                'typec2_watts': 'pd.typec2Watts',
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
                                'ac_enabled': 'inv.cfgAcEnabled',
                                'dc_enabled': 'mppt.carState',
                                'beeper_enabled': 'pd.beepState',
                                'error_code': 'error_code',
                                'warning_code': 'warning_code'
                            }
                            
                            # Extract all available fields safely
                            parsed_fields = 0
                            
                            for descriptor in status.DESCRIPTOR.fields:
                                try:
                                    # Check if field exists and has a value
                                    if hasattr(status, descriptor.name):
                                        value = getattr(status, descriptor.name)
                                        
                                        # Process ALL power fields regardless of value, other fields only if non-zero
                                        if value or 'watts' in descriptor.name:
                                            sensor_name = field_mapping.get(descriptor.name, descriptor.name)
                                            
                                            # Handle data type conversions and scaling for specific fields
                                            converted_value = value
                                            if descriptor.name in ['current', 'amp'] and value > 2147483647:
                                                # Handle signed 32-bit integer overflow (battery current can be negative)
                                                converted_value = value - 4294967296
                                                _LOGGER.info("Delta Pro 3 (Public) converted signed int: %s = %d -> %d", descriptor.name, value, converted_value)
                                            elif descriptor.name == 'input_watts':
                                                # Apply scaling to match EcoFlow app total input power
                                                converted_value = round(value / 400, 1) if value > 0 else 0
                                            elif descriptor.name == 'output_watts':
                                                # Apply scaling to match EcoFlow app total output power
                                                converted_value = round(value / 53.4, 1) if value > 0 else 0
                                            
                                            raw["params"][sensor_name] = converted_value
                                            parsed_fields += 1
                                except Exception as field_error:
                                    _LOGGER.debug("Delta Pro 3 (Public) cmd_id 50: Error extracting field %s: %s", descriptor.name, field_error)
                            
                            if parsed_fields > 0:
                                _LOGGER.info("Delta Pro 3 (Public) cmd_id 50: Parsed %u fields from DeltaPro3Status", parsed_fields)
                            else:
                                _LOGGER.debug("Delta Pro 3 (Public) cmd_id 50: No fields extracted, logging raw data")
                                raw["params"]["cmd_50_raw_hex"] = pdata.hex()
                            
                        except Exception as e:
                            _LOGGER.debug("Delta Pro 3 (Public) cmd_id 50: Failed to parse as DeltaPro3Status: %s", e)
                            # Continue logging raw data for analysis
                            raw["params"]["cmd_50_raw_hex"] = pdata.hex()
                            raw["params"]["cmd_50_length"] = len(pdata)
                    
                    elif packet.msg.cmd_id == 21:
                        # cmd_id 21: Heartbeat - appears to be encrypted/encoded data
                        # Variable length (56-92 bytes), no clear pattern found
                        # For now, just log for future analysis when we understand the encoding
                        _LOGGER.debug("Delta Pro 3 (Public) cmd_id 21: Encrypted/encoded heartbeat data (%u bytes) - logging for analysis", len(pdata))
                        raw["params"]["cmd_21_raw_hex"] = pdata.hex()
                        raw["params"]["cmd_21_length"] = len(pdata)
                    
                    else:
                        # cmd_id 2, 22: Still analyzing - keep raw data
                        _LOGGER.debug("Delta Pro 3 (Public) cmd_id %u pdata hex: %s", packet.msg.cmd_id, pdata.hex())
                        raw["params"][f"cmd_{packet.msg.cmd_id}_raw_hex"] = pdata.hex()
                        raw["params"][f"cmd_{packet.msg.cmd_id}_length"] = len(pdata)
                    
                    raw["timestamp"] = utcnow()

                # Check if we've processed the entire payload
                try:
                    if packet.ByteSize() >= len(payload):
                        break

                    _LOGGER.debug("Delta Pro 3 (Public): Found another frame in payload")
                    packet_length = len(payload) - packet.ByteSize()
                    payload = payload[:packet_length]
                except Exception as frame_error:
                    _LOGGER.debug("Delta Pro 3 (Public): Error processing frame: %s", frame_error)
                    break

        except Exception as error:
            _LOGGER.debug("Delta Pro 3 (Public) parsing error: %s", error)
            _LOGGER.debug("Delta Pro 3 (Public) raw data: %s", raw_data.hex() if raw_data else "None")
            # Don't fail completely - return what we have
            if not raw.get("params"):
                raw["params"]["parse_error"] = str(error)
                raw["params"]["raw_data_hex"] = raw_data.hex() if raw_data else "None"

        return raw 