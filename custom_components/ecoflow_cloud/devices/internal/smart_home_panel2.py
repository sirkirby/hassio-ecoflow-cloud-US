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
            # Grid Input
            InWattsSensorEntity(client, self, "grid.inputWatts", "Grid Input Power"),
            InMilliVoltSensorEntity(client, self, "grid.inputVolt", "Grid Input Voltage"),
            AmpSensorEntity(client, self, "grid.inputAmp", "Grid Input Current"),
            InEnergySensorEntity(client, self, "grid.inputEnergy", "Grid Input Energy"),
            
            # EPS System
            LevelSensorEntity(client, self, "eps.batteryLevel", "EPS Battery Level"),
            InWattsSensorEntity(client, self, "eps.inputWatts", "EPS Input Power"),
            OutWattsSensorEntity(client, self, "eps.outputWatts", "EPS Output Power"),
            
            # Load Circuits (1-10)
            WattsSensorEntity(client, self, "load.circuit1Watts", "Circuit 1 Power"),
            WattsSensorEntity(client, self, "load.circuit2Watts", "Circuit 2 Power"),
            WattsSensorEntity(client, self, "load.circuit3Watts", "Circuit 3 Power"),
            WattsSensorEntity(client, self, "load.circuit4Watts", "Circuit 4 Power"),
            WattsSensorEntity(client, self, "load.circuit5Watts", "Circuit 5 Power"),
            WattsSensorEntity(client, self, "load.circuit6Watts", "Circuit 6 Power"),
            WattsSensorEntity(client, self, "load.circuit7Watts", "Circuit 7 Power"),
            WattsSensorEntity(client, self, "load.circuit8Watts", "Circuit 8 Power"),
            WattsSensorEntity(client, self, "load.circuit9Watts", "Circuit 9 Power"),
            WattsSensorEntity(client, self, "load.circuit10Watts", "Circuit 10 Power"),
            WattsSensorEntity(client, self, "load.totalWatts", "Total Load Power"),
            
            # Circuit Energy Monitoring
            InEnergySensorEntity(client, self, "load.circuit1Energy", "Circuit 1 Energy"),
            InEnergySensorEntity(client, self, "load.circuit2Energy", "Circuit 2 Energy"),
            InEnergySensorEntity(client, self, "load.circuit3Energy", "Circuit 3 Energy"),
            InEnergySensorEntity(client, self, "load.circuit4Energy", "Circuit 4 Energy"),
            InEnergySensorEntity(client, self, "load.circuit5Energy", "Circuit 5 Energy"),
            InEnergySensorEntity(client, self, "load.circuit6Energy", "Circuit 6 Energy"),
            InEnergySensorEntity(client, self, "load.circuit7Energy", "Circuit 7 Energy"),
            InEnergySensorEntity(client, self, "load.circuit8Energy", "Circuit 8 Energy"),
            InEnergySensorEntity(client, self, "load.circuit9Energy", "Circuit 9 Energy"),
            InEnergySensorEntity(client, self, "load.circuit10Energy", "Circuit 10 Energy"),
            
            # Status
            StatusSensorEntity(client, self, "sys.gridStatus", "Grid Status"),
            StatusSensorEntity(client, self, "sys.epsMode", "EPS Mode"),
            
            # Status sensors
            QuotaStatusSensorEntity(client, self)
        ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return [
            # EPS Settings
            MaxBatteryLevelEntity(client, self, "eps.maxBatteryLevel", "EPS Max Battery Level", 50, 100, 
                                 lambda value: {"moduleType": 0, "operateType": "epsMaxBatteryLevel", "params": {"level": value}}),
            
            # Circuit Priority Settings
            ValueUpdateEntity(client, self, "load.circuit1Priority", "Circuit 1 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 1, "priority": value}}),
            ValueUpdateEntity(client, self, "load.circuit2Priority", "Circuit 2 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 2, "priority": value}}),
            ValueUpdateEntity(client, self, "load.circuit3Priority", "Circuit 3 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 3, "priority": value}}),
            ValueUpdateEntity(client, self, "load.circuit4Priority", "Circuit 4 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 4, "priority": value}}),
            ValueUpdateEntity(client, self, "load.circuit5Priority", "Circuit 5 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 5, "priority": value}}),
            ValueUpdateEntity(client, self, "load.circuit6Priority", "Circuit 6 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 6, "priority": value}}),
            ValueUpdateEntity(client, self, "load.circuit7Priority", "Circuit 7 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 7, "priority": value}}),
            ValueUpdateEntity(client, self, "load.circuit8Priority", "Circuit 8 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 8, "priority": value}}),
            ValueUpdateEntity(client, self, "load.circuit9Priority", "Circuit 9 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 9, "priority": value}}),
            ValueUpdateEntity(client, self, "load.circuit10Priority", "Circuit 10 Priority", 1, 10,
                             lambda value: {"moduleType": 0, "operateType": "loadPriority", "params": {"circuit": 10, "priority": value}}),
        ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return [
            # Main Controls
            EnabledEntity(client, self, "sys.gridConnected", "Grid Connected", 
                         lambda value: {"moduleType": 0, "operateType": "gridConnection", "params": {"enable": value}}),
            EnabledEntity(client, self, "eps.enabled", "EPS Enabled",
                         lambda value: {"moduleType": 0, "operateType": "epsControl", "params": {"enable": value}}),
            
            # Circuit Switches
            EnabledEntity(client, self, "load.circuit1Enabled", "Circuit 1 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 1, "enable": value}}),
            EnabledEntity(client, self, "load.circuit2Enabled", "Circuit 2 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 2, "enable": value}}),
            EnabledEntity(client, self, "load.circuit3Enabled", "Circuit 3 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 3, "enable": value}}),
            EnabledEntity(client, self, "load.circuit4Enabled", "Circuit 4 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 4, "enable": value}}),
            EnabledEntity(client, self, "load.circuit5Enabled", "Circuit 5 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 5, "enable": value}}),
            EnabledEntity(client, self, "load.circuit6Enabled", "Circuit 6 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 6, "enable": value}}),
            EnabledEntity(client, self, "load.circuit7Enabled", "Circuit 7 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 7, "enable": value}}),
            EnabledEntity(client, self, "load.circuit8Enabled", "Circuit 8 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 8, "enable": value}}),
            EnabledEntity(client, self, "load.circuit9Enabled", "Circuit 9 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 9, "enable": value}}),
            EnabledEntity(client, self, "load.circuit10Enabled", "Circuit 10 Enabled",
                         lambda value: {"moduleType": 0, "operateType": "circuitControl", "params": {"circuit": 10, "enable": value}}),
        ]

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return [
            TimeoutDictSelectEntity(client, self, "sys.transferTime", "Transfer Time", const.TRANSFER_TIME_OPTIONS,
                                   lambda value: {"moduleType": 0, "operateType": "transferTime", "params": {"time": value}}),
        ] 