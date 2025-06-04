# Smart Home Panel 2

## Sensors

| Sensor | Key |
| ------ | --- |
| Grid Input Power | `grid.inputWatts` |
| Grid Input Voltage | `grid.inputVolt` |
| Grid Input Current | `grid.inputAmp` |
| Grid Input Energy | `grid.inputEnergy` |
| EPS Battery Level | `eps.batteryLevel` |
| EPS Input Power | `eps.inputWatts` |
| EPS Output Power | `eps.outputWatts` |
| Circuit 1 Power | `load.circuit1Watts` |
| Circuit 2 Power | `load.circuit2Watts` |
| Circuit 3 Power | `load.circuit3Watts` |
| Circuit 4 Power | `load.circuit4Watts` |
| Circuit 5 Power | `load.circuit5Watts` |
| Circuit 6 Power | `load.circuit6Watts` |
| Circuit 7 Power | `load.circuit7Watts` |
| Circuit 8 Power | `load.circuit8Watts` |
| Circuit 9 Power | `load.circuit9Watts` |
| Circuit 10 Power | `load.circuit10Watts` |
| Total Load Power | `load.totalWatts` |
| Circuit 1 Energy | `load.circuit1Energy` |
| Circuit 2 Energy | `load.circuit2Energy` |
| Circuit 3 Energy | `load.circuit3Energy` |
| Circuit 4 Energy | `load.circuit4Energy` |
| Circuit 5 Energy | `load.circuit5Energy` |
| Circuit 6 Energy | `load.circuit6Energy` |
| Circuit 7 Energy | `load.circuit7Energy` |
| Circuit 8 Energy | `load.circuit8Energy` |
| Circuit 9 Energy | `load.circuit9Energy` |
| Circuit 10 Energy | `load.circuit10Energy` |
| Grid Status | `sys.gridStatus` |
| EPS Status | `sys.epsStatus` |

## Switches

| Switch | Key | Commands |
| ------ | --- | -------- |
| EPS Enabled | `sys.epsEnabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 1, "enabled": VALUE}}` |
| Grid Charging Enabled | `sys.gridChargeEnabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 2, "enabled": VALUE}}` |
| Circuit 1 Breaker | `load.circuit1Enabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 11, "enabled": VALUE, "circuit": 1}}` |
| Circuit 2 Breaker | `load.circuit2Enabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 12, "enabled": VALUE, "circuit": 2}}` |
| Circuit 3 Breaker | `load.circuit3Enabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 13, "enabled": VALUE, "circuit": 3}}` |
| Circuit 4 Breaker | `load.circuit4Enabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 14, "enabled": VALUE, "circuit": 4}}` |
| Circuit 5 Breaker | `load.circuit5Enabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 15, "enabled": VALUE, "circuit": 5}}` |
| Circuit 6 Breaker | `load.circuit6Enabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 16, "enabled": VALUE, "circuit": 6}}` |
| Circuit 7 Breaker | `load.circuit7Enabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 17, "enabled": VALUE, "circuit": 7}}` |
| Circuit 8 Breaker | `load.circuit8Enabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 18, "enabled": VALUE, "circuit": 8}}` |
| Circuit 9 Breaker | `load.circuit9Enabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 19, "enabled": VALUE, "circuit": 9}}` |
| Circuit 10 Breaker | `load.circuit10Enabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 20, "enabled": VALUE, "circuit": 10}}` |
| Load Shedding Enabled | `eps.loadSheddingEnabled` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 30, "enabled": VALUE}}` |

## Sliders

| Slider | Key | Commands | Min | Max |
| ------ | --- | -------- | --- | --- |
| Circuit 1 Priority | `load.circuit1Priority` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 101, "priority": VALUE, "circuit": 1}}` | 1 | 10 |
| Circuit 2 Priority | `load.circuit2Priority` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 102, "priority": VALUE, "circuit": 2}}` | 1 | 10 |
| Circuit 3 Priority | `load.circuit3Priority` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 103, "priority": VALUE, "circuit": 3}}` | 1 | 10 |
| Circuit 4 Priority | `load.circuit4Priority` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 104, "priority": VALUE, "circuit": 4}}` | 1 | 10 |
| Circuit 5 Priority | `load.circuit5Priority` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 105, "priority": VALUE, "circuit": 5}}` | 1 | 10 |
| Circuit 6 Priority | `load.circuit6Priority` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 106, "priority": VALUE, "circuit": 6}}` | 1 | 10 |
| Circuit 7 Priority | `load.circuit7Priority` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 107, "priority": VALUE, "circuit": 7}}` | 1 | 10 |
| Circuit 8 Priority | `load.circuit8Priority` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 108, "priority": VALUE, "circuit": 8}}` | 1 | 10 |
| Circuit 9 Priority | `load.circuit9Priority` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 109, "priority": VALUE, "circuit": 9}}` | 1 | 10 |
| Circuit 10 Priority | `load.circuit10Priority` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 110, "priority": VALUE, "circuit": 10}}` | 1 | 10 |
| Grid Backup Transition Delay (ms) | `eps.transitionDelay` | `{"moduleType": 0, "operateType": "TCP", "params": {"id": 200, "transitionDelay": VALUE}}` | 0 | 20 |

## Selects

| Select | Key | Commands | Options |
| ------ | --- | -------- | ------- |
| Backup Mode Timeout | `eps.backupTimeout` | `{"moduleType": 0, "operateType": "TCP", "params": {"backupTimeout": VALUE, "id": 40}}` | `{"Never": 0, "30 min": 30, "1 hr": 60, "2 hr": 120, "4 hr": 240, "6 hr": 360, "12 hr": 720, "24 hr": 1440}` | 