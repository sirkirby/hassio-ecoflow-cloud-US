from custom_components.ecoflow_cloud.api import EcoflowApiClient
from custom_components.ecoflow_cloud.devices import const, BaseDevice
from custom_components.ecoflow_cloud.entities import BaseSensorEntity, BaseNumberEntity, BaseSwitchEntity, \
    BaseSelectEntity
from custom_components.ecoflow_cloud.number import ChargingPowerEntity, MaxBatteryLevelEntity, MinBatteryLevelEntity, \
    MinGenStartLevelEntity, \
    MaxGenStopLevelEntity
from custom_components.ecoflow_cloud.select import TimeoutDictSelectEntity
from custom_components.ecoflow_cloud.sensor import LevelSensorEntity, RemainSensorEntity, \
    TempSensorEntity, \
    InWattsSensorEntity, OutWattsSensorEntity, OutWattsDcSensorEntity, InWattsSolarSensorEntity, \
    CapacitySensorEntity, QuotaStatusSensorEntity
from custom_components.ecoflow_cloud.switch import BeeperEntity, EnabledEntity


class DeltaPro3(BaseDevice):
    # --- Local helper sensor entity classes for DP3 integer-scaled values ---

    class _LevelKSensorEntity(LevelSensorEntity):
        """Battery level or percentage sensor – raw value is x1000."""

        def _update_value(self, val):  # type: ignore[override]
            try:
                return super()._update_value(int(val) / 1000)
            except Exception:
                return False

    class _InKWattsSensorEntity(InWattsSensorEntity):
        """Input power sensors where raw integer value is x1000 W."""

        def _update_value(self, val):  # type: ignore[override]
            try:
                return super()._update_value(int(val) / 1000)
            except Exception:
                return False

    class _OutKWattsSensorEntity(OutWattsSensorEntity):
        """Output power sensors where raw integer value is x1000 W."""

        def _update_value(self, val):  # type: ignore[override]
            try:
                return super()._update_value(int(val) / 1000)
            except Exception:
                return False

    class _OutKWattsDcSensorEntity(OutWattsDcSensorEntity):
        """DC output power sensors where raw integer value is x1000 W."""

        def _update_value(self, val):  # type: ignore[override]
            try:
                return super()._update_value(int(val) / 1000)
            except Exception:
                return False

    class _InDeciWattsSensorEntity(InWattsSensorEntity):
        """Input power sensors where raw integer value is x10 (0.1 W resolution)."""

        def _update_value(self, val):  # type: ignore[override]
            try:
                return super()._update_value(int(val) / 10)
            except Exception:
                return False

    class _OutDeciWattsSensorEntity(OutWattsSensorEntity):
        """Output power sensors where raw integer value is x10 (0.1 W resolution)."""

        def _update_value(self, val):  # type: ignore[override]
            try:
                return super()._update_value(int(val) / 10)
            except Exception:
                return False

    class _InCentiWattsSensorEntity(InWattsSensorEntity):
        """Input power sensor where raw integer value is x100 (0.01 kW = 0.1 W resolution)."""

        def _update_value(self, val):  # type: ignore[override]
            try:
                return super()._update_value(int(val) / 100)
            except Exception:
                return False

    # -----------------------------------------------------------------------
    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [
            # Main Battery - Using official Delta Pro 3 field names from documentation
            self._LevelKSensorEntity(client, self, "cmsBattSoc", const.MAIN_BATTERY_LEVEL),  # Overall SOC
            self._LevelKSensorEntity(client, self, "bmsBattSoc", const.MAIN_BATTERY_LEVEL_F32, False),  # Main battery SOC
            CapacitySensorEntity(client, self, "bmsDesignCap", const.MAIN_DESIGN_CAPACITY, False),  # Battery capacity (mAh)
            
            # Combined battery level (for systems with multiple batteries)
            self._LevelKSensorEntity(client, self, "cmsBattSoc", const.COMBINED_BATTERY_LEVEL),

            # === CRITICAL POWER FIELDS (Official API) ===
            self._InKWattsSensorEntity(client, self, "powInSumW", const.TOTAL_IN_POWER),  # Total input power
            OutWattsSensorEntity(client, self, "powOutSumW", const.TOTAL_OUT_POWER),  # Total output power (W)

            # AC Input/Output - Official field names (raw x1000 ints)
            self._InKWattsSensorEntity(client, self, "powGetAcIn", const.AC_IN_POWER),  # Real-time AC input power
            self._OutKWattsSensorEntity(client, self, "powGetAc", const.AC_OUT_POWER),  # Real-time AC power
            self._OutKWattsSensorEntity(client, self, "powGetAcHvOut", "HV AC Output Power"),  # Grid
            self._OutKWattsSensorEntity(client, self, "powGetAcLvOut", "LV AC Output Power"),  # LV AC

            # --- Solar Input (clean) ---
            # HV string reports in powGetPvH (value ×100)
            self._InCentiWattsSensorEntity(client, self, "powGetPvH", const.SOLAR_1_IN_POWER),  # Solar HV
            # LV string reports in powGetPvL (value ×100)
            self._InCentiWattsSensorEntity(client, self, "powGetPvL", const.SOLAR_2_IN_POWER),  # Solar LV

            # DC Output - Official field names
            self._OutKWattsDcSensorEntity(client, self, "powGet12v", const.DC_OUT_POWER),  # 12V power
            self._OutKWattsSensorEntity(client, self, "powGet24v", "24V Output Power"),  # 24V power

            # Type-C Output - Official field names
            self._OutKWattsSensorEntity(client, self, "powGetTypec1", const.TYPEC_1_OUT_POWER),  # Type-C 1
            self._OutKWattsSensorEntity(client, self, "powGetTypec2", const.TYPEC_2_OUT_POWER),  # Type-C 2

            # USB Output - Official field names
            self._OutKWattsSensorEntity(client, self, "powGetQcusb1", const.USB_QC_1_OUT_POWER),  # USB 1
            self._OutKWattsSensorEntity(client, self, "powGetQcusb2", const.USB_QC_2_OUT_POWER),  # Real-time USB 2 power (W)

            # Extra Battery ports - Official field names  
            self._OutKWattsSensorEntity(client, self, "powGet4p81", "Extra Battery Port 1 Power"),
            self._OutKWattsSensorEntity(client, self, "powGet4p82", "Extra Battery Port 2 Power"),

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
            self._LevelKSensorEntity(client, self, "cmsMinDsgSoc", const.MIN_DISCHARGE_LEVEL, False),  # Discharge limit

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
                                  lambda value: {"moduleType": 0, "operateType": "TCP",
                                                 "params": {"cfgMaxChgSoc": value}}),
            MinBatteryLevelEntity(client, self, "cmsMinDsgSoc", const.MIN_DISCHARGE_LEVEL, 0, 30,
                                  lambda value: {"moduleType": 0, "operateType": "TCP",
                                                 "params": {"cfgMinDsgSoc": value}}),
            MaxBatteryLevelEntity(client, self, "energyBackupStartSoc", const.BACKUP_RESERVE_LEVEL, 5, 100,
                                  lambda value: {"moduleType": 0, "operateType": "TCP",
                                                 "params": {"cfgEnergyBackup": {"energyBackupStartSoc": int(value), "energyBackupEn": True}}}),
            MinGenStartLevelEntity(client, self, "cmsOilOnSoc", const.GEN_AUTO_START_LEVEL, 0, 30,
                                   lambda value: {"moduleType": 0, "operateType": "TCP",
                                                  "params": {"cfgCmsOilOnSoc": value}}),

            MaxGenStopLevelEntity(client, self, "cmsOilOffSoc", const.GEN_AUTO_STOP_LEVEL, 50, 100,
                                  lambda value: {"moduleType": 0, "operateType": "TCP",
                                                 "params": {"cfgCmsOilOffSoc": value}}),

            ChargingPowerEntity(client, self, "plugInInfoAcInChgPowMax", const.AC_CHARGING_POWER, 200, 3600,
                                lambda value: {"moduleType": 0, "operateType": "TCP",
                                               "params": {"cfgPlugInInfoAcInChgPowMax": value}}),

        ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return [
            BeeperEntity(client, self, "enBeep", const.BEEPER,
                         lambda value: {"moduleType": 0, "operateType": "TCP", "params": {"cfgBeepEn": value}}),
            EnabledEntity(client, self, "flowInfo12v", const.DC_ENABLED,
                          lambda value: {"moduleType": 0, "operateType": "TCP",
                                         "params": {"cfgDc12vOutOpen": value}}),
            EnabledEntity(client, self, "flowInfoAcHvOut", const.AC_ENABLED,
                          lambda value: {"moduleType": 0, "operateType": "TCP",
                                         "params": {"cfgHvAcOutOpen": value}}),

            EnabledEntity(client, self, "xboostEn", const.XBOOST_ENABLED,
                          lambda value: {"moduleType": 0, "operateType": "TCP", "params": {"cfgXboostEn": value}}),
            EnabledEntity(client, self, "acHvAlwaysOn", const.AC_ALWAYS_ENABLED,
                          lambda value: {"moduleType": 0, "operateType": "TCP",
                                         "params": {"cfgAcHvAlwaysOn": value}}),
            EnabledEntity(client, self, "energyBackupEn", const.BP_ENABLED,
                          lambda value, params: {"moduleType": 0, "operateType": "TCP",
                                                 "params": {"cfgEnergyBackup": {"energyBackupEn": value,
                                                            "energyBackupStartSoc": value * 50}}}),
        ]

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return [
            TimeoutDictSelectEntity(client, self, "screenOffTime", const.SCREEN_TIMEOUT, const.SCREEN_TIMEOUT_OPTIONS,
                                    lambda value: {"moduleType": 0, "operateType": "TCP",
                                                   "params": {"cfgScreenOffTime": value}}),
            TimeoutDictSelectEntity(client, self, "devStandbyTime", const.UNIT_TIMEOUT, const.UNIT_TIMEOUT_OPTIONS,
                                    lambda value: {"moduleType": 0, "operateType": "TCP",
                                                   "params": {"cfgDevStandbyTime": value}}),
            TimeoutDictSelectEntity(client, self, "acStandbyTime", const.AC_TIMEOUT, const.AC_TIMEOUT_OPTIONS,
                                    lambda value: {"moduleType": 0, "operateType": "TCP",
                                                   "params": {"cfgAcStandbyTime": value}}),
            TimeoutDictSelectEntity(client, self, "dcStandbyTime", const.DC_TIMEOUT, const.DC_TIMEOUT_OPTIONS,
                                    lambda value: {"moduleType": 0, "operateType": "TCP",
                                                   "params": {"cfgDcStandbyTime": value}}),
        ]

    def flat_json(self) -> bool:
        """Return False so JSONPath expressions can use array indexes like livePower[0]."""
        return False

    def _prepare_data(self, raw_data) -> dict[str, any]:
        """
        Delta Pro 3 protobuf data parsing using official field names from DP3_IoT_Developer.md
        
        This follows the official EcoFlow Delta Pro 3 API documentation and uses the exact
        field names specified in the documentation for reliable integration.
        """
        import logging
        from homeassistant.util import utcnow
        _LOGGER = logging.getLogger(__name__)
        
        # Initialize data structure
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
                    break

                if packet.msg.cmd_id not in [1, 2, 19, 20, 21, 22, 50]:
                    _LOGGER.debug("Delta Pro 3 unsupported EcoPacket cmd id %u", packet.msg.cmd_id)
                else:
                    pdata = packet.msg.pdata
                    
                    if packet.msg.cmd_id == 50:
                        # cmd_id 50: Main status message - official field mapping
                        _LOGGER.debug("Delta Pro 3 cmd_id 50 pdata length: %d bytes", len(pdata))
                        
                        try:
                            status = delta_pro3.DeltaPro3Status()
                            status.ParseFromString(pdata)
                            
                            # === OFFICIAL FIELD MAPPING FROM DP3_IoT_Developer.md ===
                            
                            # Device status and error info
                            if hasattr(status, 'errcode'):
                                data["params"]["errcode"] = status.errcode
                            if hasattr(status, 'devSleepState'):
                                data["params"]["devSleepState"] = status.devSleepState
                            if hasattr(status, 'devStandbyTime'):
                                data["params"]["devStandbyTime"] = status.devStandbyTime
                            if hasattr(status, 'dcStandbyTime'):
                                data["params"]["dcStandbyTime"] = status.dcStandbyTime
                            if hasattr(status, 'bleStandbyTime'):
                                data["params"]["bleStandbyTime"] = status.bleStandbyTime
                            if hasattr(status, 'acStandbyTime'):
                                data["params"]["acStandbyTime"] = status.acStandbyTime

                            # Battery Management System (BMS) - Official fields
                            if hasattr(status, 'cmsMinDsgSoc'):
                                data["params"]["cmsMinDsgSoc"] = status.cmsMinDsgSoc
                            if hasattr(status, 'cmsChgDsgState'):
                                data["params"]["cmsChgDsgState"] = status.cmsChgDsgState
                            if hasattr(status, 'cmsBmsRunState'):
                                data["params"]["cmsBmsRunState"] = status.cmsBmsRunState
                            if hasattr(status, 'cmsBattSoc'):
                                data["params"]["cmsBattSoc"] = status.cmsBattSoc
                            if hasattr(status, 'cmsMaxChgSoc'):
                                data["params"]["cmsMaxChgSoc"] = status.cmsMaxChgSoc
                            if hasattr(status, 'cmsChgRemTime'):
                                data["params"]["cmsChgRemTime"] = status.cmsChgRemTime
                            if hasattr(status, 'cmsOilSelfStart'):
                                data["params"]["cmsOilSelfStart"] = status.cmsOilSelfStart
                            if hasattr(status, 'cmsOilOffSoc'):
                                data["params"]["cmsOilOffSoc"] = status.cmsOilOffSoc
                            if hasattr(status, 'cmsDsgRemTime'):
                                data["params"]["cmsDsgRemTime"] = status.cmsDsgRemTime
                            if hasattr(status, 'cmsOilOnSoc'):
                                data["params"]["cmsOilOnSoc"] = status.cmsOilOnSoc

                            # Main battery specific data - Official fields
                            if hasattr(status, 'bmsChgRemTime'):
                                data["params"]["bmsChgRemTime"] = status.bmsChgRemTime
                            if hasattr(status, 'bmsDesignCap'):
                                data["params"]["bmsDesignCap"] = status.bmsDesignCap
                            if hasattr(status, 'bmsMaxCellTemp'):
                                data["params"]["bmsMaxCellTemp"] = status.bmsMaxCellTemp
                            if hasattr(status, 'bmsBattSoc'):
                                data["params"]["bmsBattSoc"] = status.bmsBattSoc
                            if hasattr(status, 'bmsChgDsgState'):
                                data["params"]["bmsChgDsgState"] = status.bmsChgDsgState
                            if hasattr(status, 'bmsMinCellTemp'):
                                data["params"]["bmsMinCellTemp"] = status.bmsMinCellTemp
                            if hasattr(status, 'bmsDsgRemTime'):
                                data["params"]["bmsDsgRemTime"] = status.bmsDsgRemTime

                            # === CRITICAL POWER FIELDS (Official API) ===
                            if hasattr(status, 'powInSumW'):
                                data["params"]["powInSumW"] = status.powInSumW
                            if hasattr(status, 'powOutSumW'):
                                data["params"]["powOutSumW"] = status.powOutSumW
                            if hasattr(status, 'powGetAcHvOut'):
                                data["params"]["powGetAcHvOut"] = status.powGetAcHvOut
                            if hasattr(status, 'powGetAc'):
                                data["params"]["powGetAc"] = status.powGetAc
                            if hasattr(status, 'powGetTypec1'):
                                data["params"]["powGetTypec1"] = status.powGetTypec1
                            if hasattr(status, 'powGetTypec2'):
                                data["params"]["powGetTypec2"] = status.powGetTypec2
                            if hasattr(status, 'powGet12v'):
                                data["params"]["powGet12v"] = status.powGet12v
                            if hasattr(status, 'powGet24v'):
                                data["params"]["powGet24v"] = status.powGet24v
                            if hasattr(status, 'powGetAcLvOut'):
                                data["params"]["powGetAcLvOut"] = status.powGetAcLvOut
                            if hasattr(status, 'powGet5p8'):
                                data["params"]["powGet5p8"] = status.powGet5p8
                            if hasattr(status, 'powGetQcusb1'):
                                data["params"]["powGetQcusb1"] = status.powGetQcusb1
                            if hasattr(status, 'powGetQcusb2'):
                                data["params"]["powGetQcusb2"] = status.powGetQcusb2
                            if hasattr(status, 'powGet4p81'):
                                data["params"]["powGet4p81"] = status.powGet4p81
                            if hasattr(status, 'powGet4p82'):
                                data["params"]["powGet4p82"] = status.powGet4p82
                            if hasattr(status, 'powGetAcLvTt30Out'):
                                data["params"]["powGetAcLvTt30Out"] = status.powGetAcLvTt30Out
                            if hasattr(status, 'powGetPvH'):
                                data["params"]["powGetPvH"] = status.powGetPvH
                            if hasattr(status, 'powGetAcIn'):
                                data["params"]["powGetAcIn"] = status.powGetAcIn
                            if hasattr(status, 'powGetPvL'):
                                data["params"]["powGetPvL"] = status.powGetPvL

                            # Flow/Switch status information - Official fields
                            if hasattr(status, 'flowInfoPvL'):
                                data["params"]["flowInfoPvL"] = status.flowInfoPvL
                            if hasattr(status, 'flowInfoPvH'):
                                data["params"]["flowInfoPvH"] = status.flowInfoPvH
                            if hasattr(status, 'flowInfoTypec1'):
                                data["params"]["flowInfoTypec1"] = status.flowInfoTypec1
                            if hasattr(status, 'flowInfoTypec2'):
                                data["params"]["flowInfoTypec2"] = status.flowInfoTypec2
                            if hasattr(status, 'flowInfoAcLvOut'):
                                data["params"]["flowInfoAcLvOut"] = status.flowInfoAcLvOut
                            if hasattr(status, 'flowInfo4p82Out'):
                                data["params"]["flowInfo4p82Out"] = status.flowInfo4p82Out
                            if hasattr(status, 'flowInfoAcIn'):
                                data["params"]["flowInfoAcIn"] = status.flowInfoAcIn
                            if hasattr(status, 'flowInfoAcHvOut'):
                                data["params"]["flowInfoAcHvOut"] = status.flowInfoAcHvOut
                            if hasattr(status, 'flowInfo12v'):
                                data["params"]["flowInfo12v"] = status.flowInfo12v
                            if hasattr(status, 'flowInfo24v'):
                                data["params"]["flowInfo24v"] = status.flowInfo24v
                            if hasattr(status, 'flowInfo4p81In'):
                                data["params"]["flowInfo4p81In"] = status.flowInfo4p81In
                            if hasattr(status, 'flowInfoQcusb1'):
                                data["params"]["flowInfoQcusb1"] = status.flowInfoQcusb1
                            if hasattr(status, 'flowInfoQcusb2'):
                                data["params"]["flowInfoQcusb2"] = status.flowInfoQcusb2
                            if hasattr(status, 'flowInfo4p82In'):
                                data["params"]["flowInfo4p82In"] = status.flowInfo4p82In
                            if hasattr(status, 'flowInfo5p8In'):
                                data["params"]["flowInfo5p8In"] = status.flowInfo5p8In
                            if hasattr(status, 'flowInfo4p81Out'):
                                data["params"]["flowInfo4p81Out"] = status.flowInfo4p81Out
                            if hasattr(status, 'flowInfo5p8Out'):
                                data["params"]["flowInfo5p8Out"] = status.flowInfo5p8Out

                            # Configuration and settings - Official fields
                            if hasattr(status, 'acEnergySavingOpen'):
                                data["params"]["acEnergySavingOpen"] = status.acEnergySavingOpen
                            if hasattr(status, 'multiBpChgDsgMode'):
                                data["params"]["multiBpChgDsgMode"] = status.multiBpChgDsgMode
                            if hasattr(status, 'fastChargeSwitch'):
                                data["params"]["fastChargeSwitch"] = status.fastChargeSwitch
                            if hasattr(status, 'lcdLight'):
                                data["params"]["lcdLight"] = status.lcdLight
                            if hasattr(status, 'energyBackupEn'):
                                data["params"]["energyBackupEn"] = status.energyBackupEn
                            if hasattr(status, 'acOutFreq'):
                                data["params"]["acOutFreq"] = status.acOutFreq
                            if hasattr(status, 'xboostEn'):
                                data["params"]["xboostEn"] = status.xboostEn
                            if hasattr(status, 'llcHvLvFlag'):
                                data["params"]["llcHvLvFlag"] = status.llcHvLvFlag
                            if hasattr(status, 'llcGFCIFlag'):
                                data["params"]["llcGFCIFlag"] = status.llcGFCIFlag
                            if hasattr(status, 'acLvAlwaysOn'):
                                data["params"]["acLvAlwaysOn"] = status.acLvAlwaysOn
                            if hasattr(status, 'screenOffTime'):
                                data["params"]["screenOffTime"] = status.screenOffTime
                            if hasattr(status, 'energyBackupStartSoc'):
                                data["params"]["energyBackupStartSoc"] = status.energyBackupStartSoc
                            if hasattr(status, 'acHvAlwaysOn'):
                                data["params"]["acHvAlwaysOn"] = status.acHvAlwaysOn
                            if hasattr(status, 'acAlwaysOnMiniSoc'):
                                data["params"]["acAlwaysOnMiniSoc"] = status.acAlwaysOnMiniSoc
                            if hasattr(status, 'enBeep'):
                                data["params"]["enBeep"] = status.enBeep
                            if hasattr(status, 'generatorPvHybridModeOpen'):
                                data["params"]["generatorPvHybridModeOpen"] = status.generatorPvHybridModeOpen
                            if hasattr(status, 'generatorCareModeOpen'):
                                data["params"]["generatorCareModeOpen"] = status.generatorCareModeOpen
                            if hasattr(status, 'generatorPvHybridModeSocMax'):
                                data["params"]["generatorPvHybridModeSocMax"] = status.generatorPvHybridModeSocMax

                            if hasattr(status, 'livePower') and len(status.livePower) > 0:
                                words = []
                                for v in status.livePower:
                                    words.extend((v & 0xFFFF, v >> 16))
                                data["params"]["livePowerWords"] = words

                                _LOGGER.debug("DP3 livePowerWords first 12: %s", words[:12])

                            if _LOGGER.isEnabledFor(logging.DEBUG):
                                try:
                                    from google.protobuf.json_format import MessageToDict
                                    from google.protobuf import text_format
                                    _LOGGER.debug("Delta Pro 3 full status (dict) %s", MessageToDict(status, preserving_proto_field_name=True))
                                    _LOGGER.debug("Delta Pro 3 full status (text)\n%s", text_format.MessageToString(status, print_unknown_fields=True))

                                    # --- debug marker to verify runtime path & unknown-field exposure ---
                                    _LOGGER.debug("DP3 DEBUG MARKER reached. _unknown_fields present=%s", hasattr(status, "_unknown_fields"))

                                    # Dump using UnknownFields() API (protobuf C-extension)
                                    try:
                                        for uf in status.UnknownFields():
                                            if uf.wire_type == 2:  # length-delimited, usually bytes
                                                _LOGGER.debug("DP3 unknown(C) tag=%d wt=2 len=%d hex=%s", uf.field_number, len(uf.data), uf.data.hex())
                                            else:
                                                _LOGGER.debug("DP3 unknown(C) tag=%d wt=%d value=%s", uf.field_number, uf.wire_type, uf.data)
                                    except Exception as ce:
                                        _LOGGER.debug("UnknownFields API not available: %s", ce)

                                except Exception as dump_error:
                                    _LOGGER.debug("Unable to dump DP3 status: %s", dump_error)
                                
                        except Exception as e:
                            _LOGGER.error("Delta Pro 3 cmd_id 50 parsing failed: %s", e)
                            data["params"]["parse_error"] = str(e)
                    
                    elif packet.msg.cmd_id == 21:
                        # Heartbeat - just acknowledge
                        _LOGGER.debug("Delta Pro 3 heartbeat received (%d bytes)", len(pdata))
                    
                    elif packet.msg.cmd_id in [19, 20]:
                        # Switch commands
                        _LOGGER.debug("Delta Pro 3 switch command (cmd_id %d, %d bytes)", packet.msg.cmd_id, len(pdata))
                    
                    data["timestamp"] = utcnow()

                # Handle multi-frame payloads
                try:
                    if packet.ByteSize() >= len(payload):
                        break
                    packet_length = len(payload) - packet.ByteSize()
                    payload = payload[:packet_length]
                except Exception:
                    break

        except Exception as error:
            _LOGGER.error("Delta Pro 3 parsing error: %s", error)
            if not data.get("params"):
                data["params"]["parse_error"] = str(error)

        return data 