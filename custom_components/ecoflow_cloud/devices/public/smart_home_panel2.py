from custom_components.ecoflow_cloud.api import EcoflowApiClient
from custom_components.ecoflow_cloud.devices import const, BaseDevice
from custom_components.ecoflow_cloud.entities import BaseSensorEntity, BaseNumberEntity, BaseSwitchEntity, \
    BaseSelectEntity
from custom_components.ecoflow_cloud.sensor import LevelSensorEntity, WattsSensorEntity, \
    InWattsSensorEntity, OutWattsSensorEntity, MilliVoltSensorEntity, InMilliVoltSensorEntity, \
    AmpSensorEntity, InEnergySensorEntity, OutEnergySensorEntity, StatusSensorEntity, \
    QuotaStatusSensorEntity
from custom_components.ecoflow_cloud.switch import EnabledEntity
from custom_components.ecoflow_cloud.number import MaxBatteryLevelEntity, ValueUpdateEntity
from custom_components.ecoflow_cloud.select import TimeoutDictSelectEntity


class SmartHomePanel2(BaseDevice):
    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [
            # Grid Input - using prefix "20_1." for consistency with other public API devices
            InWattsSensorEntity(client, self, "20_1.gridInputWatts", "Grid Input Power"),
            InMilliVoltSensorEntity(client, self, "20_1.gridInputVolt", "Grid Input Voltage"),
            AmpSensorEntity(client, self, "20_1.gridInputAmp", "Grid Input Current"),
            InEnergySensorEntity(client, self, "20_1.gridInputEnergy", "Grid Input Energy"),
            
            # EPS System
            LevelSensorEntity(client, self, "20_1.epsBatteryLevel", "EPS Battery Level"),
            InWattsSensorEntity(client, self, "20_1.epsInputWatts", "EPS Input Power"),
            OutWattsSensorEntity(client, self, "20_1.epsOutputWatts", "EPS Output Power"),
            
            # Load Circuits (1-10)
            WattsSensorEntity(client, self, "20_1.loadCircuit1Watts", "Circuit 1 Power"),
            WattsSensorEntity(client, self, "20_1.loadCircuit2Watts", "Circuit 2 Power"),
            WattsSensorEntity(client, self, "20_1.loadCircuit3Watts", "Circuit 3 Power"),
            WattsSensorEntity(client, self, "20_1.loadCircuit4Watts", "Circuit 4 Power"),
            WattsSensorEntity(client, self, "20_1.loadCircuit5Watts", "Circuit 5 Power"),
            WattsSensorEntity(client, self, "20_1.loadCircuit6Watts", "Circuit 6 Power"),
            WattsSensorEntity(client, self, "20_1.loadCircuit7Watts", "Circuit 7 Power"),
            WattsSensorEntity(client, self, "20_1.loadCircuit8Watts", "Circuit 8 Power"),
            WattsSensorEntity(client, self, "20_1.loadCircuit9Watts", "Circuit 9 Power"),
            WattsSensorEntity(client, self, "20_1.loadCircuit10Watts", "Circuit 10 Power"),
            WattsSensorEntity(client, self, "20_1.loadTotalWatts", "Total Load Power"),
            
            # Circuit Energy Monitoring
            InEnergySensorEntity(client, self, "20_1.loadCircuit1Energy", "Circuit 1 Energy"),
            InEnergySensorEntity(client, self, "20_1.loadCircuit2Energy", "Circuit 2 Energy"),
            InEnergySensorEntity(client, self, "20_1.loadCircuit3Energy", "Circuit 3 Energy"),
            InEnergySensorEntity(client, self, "20_1.loadCircuit4Energy", "Circuit 4 Energy"),
            InEnergySensorEntity(client, self, "20_1.loadCircuit5Energy", "Circuit 5 Energy"),
            InEnergySensorEntity(client, self, "20_1.loadCircuit6Energy", "Circuit 6 Energy"),
            InEnergySensorEntity(client, self, "20_1.loadCircuit7Energy", "Circuit 7 Energy"),
            InEnergySensorEntity(client, self, "20_1.loadCircuit8Energy", "Circuit 8 Energy"),
            InEnergySensorEntity(client, self, "20_1.loadCircuit9Energy", "Circuit 9 Energy"),
            InEnergySensorEntity(client, self, "20_1.loadCircuit10Energy", "Circuit 10 Energy"),
            
            # Status
            StatusSensorEntity(client, self, "20_1.sysGridStatus", "Grid Status"),
            StatusSensorEntity(client, self, "20_1.sysEpsMode", "EPS Mode"),
            
            # Status sensors
            QuotaStatusSensorEntity(client, self)
        ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return [
            # EPS Settings
            MaxBatteryLevelEntity(client, self, "20_1.epsMaxBatteryLevel", "EPS Max Battery Level", 50, 100,
                                 lambda value: {"moduleType": 0, "operateType": "epsMaxBatteryLevel", "params": {"level": value}}),
            
            # Circuit Priority Settings
            ValueUpdateEntity(client, self, "20_1.loadCircuit1Priority", "Circuit 1 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 1, "priority": value}}),
            ValueUpdateEntity(client, self, "20_1.loadCircuit2Priority", "Circuit 2 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 2, "priority": value}}),
            ValueUpdateEntity(client, self, "20_1.loadCircuit3Priority", "Circuit 3 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 3, "priority": value}}),
            ValueUpdateEntity(client, self, "20_1.loadCircuit4Priority", "Circuit 4 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 4, "priority": value}}),
            ValueUpdateEntity(client, self, "20_1.loadCircuit5Priority", "Circuit 5 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 5, "priority": value}}),
            ValueUpdateEntity(client, self, "20_1.loadCircuit6Priority", "Circuit 6 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 6, "priority": value}}),
            ValueUpdateEntity(client, self, "20_1.loadCircuit7Priority", "Circuit 7 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 7, "priority": value}}),
            ValueUpdateEntity(client, self, "20_1.loadCircuit8Priority", "Circuit 8 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 8, "priority": value}}),
            ValueUpdateEntity(client, self, "20_1.loadCircuit9Priority", "Circuit 9 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 9, "priority": value}}),
            ValueUpdateEntity(client, self, "20_1.loadCircuit10Priority", "Circuit 10 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 10, "priority": value}}),
        ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return [
            # Main Controls
            EnabledEntity(client, self, "20_1.sysGridConnected", "Grid Connected",
                         lambda value: {"moduleType": 0, "operateType": "gridConnection", "params": {"enable": value}}),
            EnabledEntity(client, self, "20_1.epsEnabled", "EPS Enabled",
                         lambda value: {"moduleType": 0, "operateType": "epsControl", "params": {"enable": value}}),
            
            # Circuit Switches
            EnabledEntity(client, self, "20_1.loadCircuit1Enabled", "Circuit 1 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 1, "enable": value}}),
            EnabledEntity(client, self, "20_1.loadCircuit2Enabled", "Circuit 2 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 2, "enable": value}}),
            EnabledEntity(client, self, "20_1.loadCircuit3Enabled", "Circuit 3 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 3, "enable": value}}),
            EnabledEntity(client, self, "20_1.loadCircuit4Enabled", "Circuit 4 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 4, "enable": value}}),
            EnabledEntity(client, self, "20_1.loadCircuit5Enabled", "Circuit 5 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 5, "enable": value}}),
            EnabledEntity(client, self, "20_1.loadCircuit6Enabled", "Circuit 6 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 6, "enable": value}}),
            EnabledEntity(client, self, "20_1.loadCircuit7Enabled", "Circuit 7 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 7, "enable": value}}),
            EnabledEntity(client, self, "20_1.loadCircuit8Enabled", "Circuit 8 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 8, "enable": value}}),
            EnabledEntity(client, self, "20_1.loadCircuit9Enabled", "Circuit 9 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 9, "enable": value}}),
            EnabledEntity(client, self, "20_1.loadCircuit10Enabled", "Circuit 10 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 10, "enable": value}}),
        ]

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return [
            TimeoutDictSelectEntity(client, self, "20_1.sysTransferTime", "Transfer Time", const.TRANSFER_TIME_OPTIONS,
                                   lambda value: {"moduleType": 0, "operateType": "transferTime", "params": {"time": value}}),
        ] 