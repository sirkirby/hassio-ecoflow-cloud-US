[![GitHub Release](https://img.shields.io/github/release/snell-evan-itt/hassio-ecoflow-cloud-US.svg?style=for-the-badge&color=blue)](https://github.com/snell-evan-itt/hassio-ecoflow-cloud-US/releases)
[![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/snell-evan-itt/hassio-ecoflow-cloud-US/total?style=for-the-badge)](https://github.com/snell-evan-itt/hassio-ecoflow-cloud-US/releases/latest)
[![HACS Default](https://img.shields.io/badge/HACS-default-blue.svg?style=for-the-badge)](https://hacs.xyz) [![Community forum discussion](https://img.shields.io/badge/COMMUNITY-FORUM-success?style=for-the-badge&color=yellow)](https://community.home-assistant.io/t/custom-component-ecoflow-cloud-api-for-us-users/799962)



# EcoFlow Cloud Integration for Home Assistant (en-US)
Inspired by [hassio-ecoflow](https://github.com/vwt12eh8/hassio-ecoflow),  [ecoflow-mqtt-prometheus-exporter](https://github.com/berezhinskiy/ecoflow-mqtt-prometheus-exporter), and [hassio-ecoflow-cloud](https://github.com/tolwi/hassio-ecoflow-cloud) this integration uses EcoFlow MQTT Broker `mqtt.ecoflow.com` to monitor and control the device. I also updated this repo to run United States API Endpoint for Public API as the reference repo was for European API Endpoint.

## Request Ecoflow Public API Key for your Account
Link to Official Documentation: https://developer.ecoflow.com/us/document/introduction

Request API Access to Ecoflow United States:

- Go to https://developer.ecoflow.com/ 
- Click on "Become a Developer" 
- Login with your Ecoflow username and Password 
- Go back to https://developer.ecoflow.com/ 
- Click on "Become a Developer" 
- Wait until the access is approved by Ecoflow Receive email with subject "Approval notice from EcoFlow Developer Platform". May take some time 
- Go to https://developer.ecoflow.com/us/security and create new AccessKey and SecretKey

## Installation

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?category=integration&repository=hassio-ecoflow-cloud-US&owner=snell-evan-itt)

- Click above to install as a custom repository via HACS
- Restart Home Assistant
- Once restart is done, use Add Integration -> Ecoflow Cloud.

## Disclaimers

>[!IMPORTANT]
>Originally developed for personal use without a goal to cover all available device attributes i am updating for my device <b>Delta 2 Max</b>

## Current state
<details><summary> DELTA_2 <i>(sensors: 45, switches: 8, sliders: 6, selects: 5)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Total In Power
- Total Out Power
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar In Power
- DC Out Power
- Type-C (1) Out Power
- Type-C (2) Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB QC (1) Out Power
- USB QC (2) Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Slave Battery Level  _(auto)_
- Slave Design Capacity  _(disabled)_
- Slave Full Capacity  _(disabled)_
- Slave Remain Capacity  _(disabled)_
- Slave State of Health
- Slave Battery Temperature  _(auto)_
- Slave Min Cell Temperature  _(disabled)_
- Slave Max Cell Temperature  _(disabled)_
- Slave Battery Volts  _(disabled)_
- Slave Min Cell Volts  _(disabled)_
- Slave Max Cell Volts  _(disabled)_
- Slave Cycles  _(auto)_
- Slave In Power  _(auto)_
- Slave Out Power  _(auto)_
- Status

*Switches*
- Beeper 
- USB Enabled 
- AC Always On 
- Prio Solar Charging 
- AC Enabled 
- X-Boost Enabled 
- DC (12V) Enabled 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- Backup Reserve Level 
- Generator Auto Start Level 
- Generator Auto Stop Level 
- AC Charging Power 

*Selects*
- DC (12V) Charge Current 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 
- DC (12V) Timeout 

</p></details>

<details><summary> RIVER_2 <i>(sensors: 32, switches: 5, sliders: 4, selects: 5)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Battery Charging State
- Total In Power
- Total Out Power
- Solar In Current
- Solar In Voltage
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Type-C In Power
- Solar In Power
- DC Out Power
- Type-C Out Power
- USB Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Status

*Switches*
- AC Enabled 
- AC Always On 
- X-Boost Enabled 
- DC (12V) Enabled 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- AC Charging Power 
- Backup Reserve Level 

*Selects*
- DC (12V) Charge Current 
- DC Mode 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> RIVER_2_MAX <i>(sensors: 32, switches: 5, sliders: 4, selects: 5)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Battery Charging State
- Total In Power
- Total Out Power
- Solar In Current
- Solar In Voltage
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Type-C In Power
- Solar In Power
- DC Out Power
- Type-C Out Power
- USB Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Status

*Switches*
- AC Enabled 
- AC Always On 
- X-Boost Enabled 
- DC (12V) Enabled 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- AC Charging Power 
- Backup Reserve Level 

*Selects*
- DC (12V) Charge Current 
- DC Mode 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> RIVER_2_PRO <i>(sensors: 30, switches: 3, sliders: 3, selects: 5)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Battery Charging State
- Total In Power
- Total Out Power
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Type-C In Power
- Solar In Power
- DC Out Power
- Type-C Out Power
- USB Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Status

*Switches*
- AC Enabled 
- X-Boost Enabled 
- DC (12V) Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- AC Charging Power 

*Selects*
- DC (12V) Charge Current 
- DC Mode 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> DELTA_PRO <i>(sensors: 71, switches: 6, sliders: 6, selects: 4)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Battery Level (Precise)  _(disabled)_
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Battery Level (Precise)  _(disabled)_
- Total In Power
- Total Out Power
- Main Battery Current
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar In Power
- Solar In Voltage
- Solar In Current
- DC Out Power
- DC Out Voltage
- DC Car Out Power
- DC Anderson Out Power
- Type-C (1) Out Power
- Type-C (2) Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB QC (1) Out Power
- USB QC (2) Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Solar In Energy
- Battery Charge Energy from AC
- Battery Charge Energy from DC
- Battery Discharge Energy to AC
- Battery Discharge Energy to DC
- Slave 1 Battery Level  _(auto)_
- Slave 1 Battery Level (Precise)  _(disabled)_
- Slave 1 Design Capacity  _(disabled)_
- Slave 1 Full Capacity  _(disabled)_
- Slave 1 Remain Capacity  _(disabled)_
- Slave 1 State of Health
- Slave 1 Battery Temperature  _(auto)_
- Slave 1 In Power  _(auto)_
- Slave 1 Out Power  _(auto)_
- Slave 2 Battery Level  _(auto)_
- Slave 2 Battery Level (Precise)  _(disabled)_
- Slave 2 Design Capacity  _(disabled)_
- Slave 2 Full Capacity  _(disabled)_
- Slave 2 Remain Capacity  _(disabled)_
- Slave 2 State of Health
- Slave 1 Battery Volts  _(disabled)_
- Slave 1 Min Cell Volts  _(disabled)_
- Slave 1 Max Cell Volts  _(disabled)_
- Slave 1 Battery Current  _(disabled)_
- Slave 2 Battery Volts  _(disabled)_
- Slave 2 Min Cell Volts  _(disabled)_
- Slave 2 Max Cell Volts  _(disabled)_
- Slave 2 Battery Current  _(disabled)_
- Slave 2 Battery Temperature  _(auto)_
- Slave 2 In Power  _(auto)_
- Slave 2 Out Power  _(auto)_
- Slave 1 Cycles  _(disabled)_
- Slave 2 Cycles  _(disabled)_
- Status

*Switches*
- Beeper 
- DC (12V) Enabled 
- AC Enabled 
- X-Boost Enabled 
- AC Always On 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- Backup Reserve Level 
- Generator Auto Start Level 
- Generator Auto Stop Level 
- AC Charging Power 

*Selects*
- DC (12V) Charge Current 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> RIVER_MAX <i>(sensors: 40, switches: 5, sliders: 1, selects: 2)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- Total In Power
- Total Out Power
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- DC Out Power
- Type-C Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB (3) Out Power
- Remaining Time
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Solar In Energy
- Battery Charge Energy from AC
- Battery Charge Energy from DC
- Battery Discharge Energy to AC
- Battery Discharge Energy to DC
- Slave Battery Level  _(auto)_
- Slave Design Capacity  _(disabled)_
- Slave Full Capacity  _(disabled)_
- Slave Remain Capacity  _(disabled)_
- Slave Battery Temperature  _(auto)_
- Slave Min Cell Temperature  _(disabled)_
- Slave Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Slave Cycles  _(auto)_
- Status

*Switches*
- Beeper 
- AC Enabled 
- DC (12V) Enabled 
- X-Boost Enabled 
- Auto Fan Speed 

*Sliders (numbers)*
- Max Charge Level  _(read-only)_

*Selects*
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> RIVER_PRO <i>(sensors: 46, switches: 7, sliders: 1, selects: 3)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- Total In Power
- Total Out Power
- Solar In Current
- Solar In Voltage
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- DC Out Power
- Type-C Out Power
- DC Temperature  _(disabled)_
- USB C Temperature  _(disabled)_
- USB (1) Out Power
- USB (2) Out Power
- USB (3) Out Power
- Remaining Time
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Inverter Inside Temperature
- Inverter Outside Temperature
- Solar In Energy
- Battery Charge Energy from AC
- Battery Charge Energy from DC
- Battery Discharge Energy to AC
- Battery Discharge Energy to DC
- Battery Current  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Cycles
- Slave Battery Level  _(auto)_
- Slave Design Capacity  _(disabled)_
- Slave Full Capacity  _(disabled)_
- Slave Remain Capacity  _(disabled)_
- Slave Cycles  _(auto)_
- Slave Battery Temperature  _(auto)_
- Slave Battery Current  _(disabled)_
- Slave Battery Volts  _(disabled)_
- Slave Min Cell Volts  _(disabled)_
- Slave Max Cell Volts  _(disabled)_
- Status

*Switches*
- Beeper 
- AC Always On 
- DC (12V) Enabled 
- AC Enabled 
- X-Boost Enabled 
- AC Slow Charging 
- Auto Fan Speed 

*Sliders (numbers)*
- Max Charge Level 

*Selects*
- Unit Timeout 
- DC (12V) Timeout 
- AC Timeout 

</p></details>

<details><summary> RIVER_MINI <i>(sensors: 17, switches: 2, sliders: 1, selects: 0)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar In Voltage
- Solar In Current
- Inverter Inside Temperature
- Inverter Outside Temperature
- Solar In Energy
- Battery Charge Energy from AC
- Battery Charge Energy from DC
- Battery Discharge Energy to AC
- Battery Discharge Energy to DC
- Total In Power
- Total Out Power
- Cycles

*Switches*
- AC Enabled 
- X-Boost Enabled 

*Sliders (numbers)*
- Max Charge Level 

*Selects*

</p></details>

<details><summary> DELTA_MINI <i>(sensors: 33, switches: 4, sliders: 3, selects: 4)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Total In Power
- Total Out Power
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar In Power
- DC Out Power
- DC Car Out Power
- DC Anderson Out Power
- Type-C (1) Out Power
- Type-C (2) Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB QC (1) Out Power
- USB QC (2) Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Cycles
- Battery Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Solar In Energy
- Battery Charge Energy from AC
- Battery Charge Energy from DC
- Battery Discharge Energy to AC
- Battery Discharge Energy to DC
- Status

*Switches*
- Beeper 
- DC (12V) Enabled 
- AC Enabled 
- X-Boost Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- AC Charging Power 

*Selects*
- DC (12V) Charge Current 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> DELTA_MAX <i>(sensors: 30, switches: 7, sliders: 5, selects: 0)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- Battery Level
- Total In Power
- Total Out Power
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar In Power
- DC Out Power
- Type-C (1) Out Power
- Type-C (2) Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB QC (1) Out Power
- USB QC (2) Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Status

*Switches*
- Beeper 
- USB Enabled 
- AC Always On 
- Prio Solar Charging 
- AC Enabled 
- X-Boost Enabled 
- DC (12V) Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- Generator Auto Start Level 
- Generator Auto Stop Level 
- AC Charging Power 

*Selects*

</p></details>

<details><summary> DELTA_2_MAX <i>(sensors: 67, switches: 7, sliders: 6, selects: 3)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Total In Power
- Total Out Power
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar (1) In Power
- Solar (2) In Power
- Solar (1) In Volts
- Solar (2) In Volts
- Solar (1) In Amps
- Solar (2) In Amps
- DC Out Power
- Type-C (1) Out Power
- Type-C (2) Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB QC (1) Out Power
- USB QC (2) Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Solar In Energy
- Battery Charge Energy from AC
- Battery Charge Energy from DC
- Battery Discharge Energy to AC
- Battery Discharge Energy to DC
- Battery level SOC  _(auto)_
- Slave 1 Battery Level  _(auto)_
- Slave 1 Design Capacity  _(disabled)_
- Slave 1 Full Capacity  _(disabled)_
- Slave 1 Remain Capacity  _(disabled)_
- Slave 1 Battery Temperature  _(auto)_
- Slave 1 Min Cell Temperature  _(disabled)_
- Slave 1 Max Cell Temperature  _(disabled)_
- Slave 1 Battery Volts  _(disabled)_
- Slave 1 Min Cell Volts  _(disabled)_
- Slave 1 Max Cell Volts  _(disabled)_
- Slave 1 Cycles  _(auto)_
- Slave 1 State of Health  _(auto)_
- Slave 1 In Power  _(auto)_
- Slave 1 Out Power  _(auto)_
- Slave 1 Battery level SOC  _(auto)_
- Slave 2 Battery Level  _(auto)_
- Slave 2 Design Capacity  _(disabled)_
- Slave 2 Full Capacity  _(disabled)_
- Slave 2 Remain Capacity  _(disabled)_
- Slave 2 Battery Temperature  _(auto)_
- Slave 2 Min Cell Temperature  _(disabled)_
- Slave 2 Max Cell Temperature  _(disabled)_
- Slave 2 Battery Volts  _(disabled)_
- Slave 2 Min Cell Volts  _(disabled)_
- Slave 2 Max Cell Volts  _(disabled)_
- Slave 2 Cycles  _(auto)_
- Slave 2 State of Health  _(auto)_
- Slave 2 In Power  _(auto)_
- Slave 2 Out Power  _(auto)_
- Slave 2 Battery level SOC  _(auto)_
- Status

*Switches*
- Beeper 
- USB Enabled 
- AC Always On 
- AC Enabled 
- X-Boost Enabled 
- DC (12V) Enabled 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- Backup Reserve Level 
- Generator Auto Start Level 
- Generator Auto Stop Level 
- AC Charging Power 

*Selects*
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> POWERSTREAM <i>(sensors: 57, switches: 0, sliders: 0, selects: 0)</i> </summary>
<p>

*Sensors*
- Solar 1 Watts
- Solar 1 Input Potential
- Solar 1 Op Potential
- Solar 1 Current
- Solar 1 Temperature
- Solar 1 Relay Status
- Solar 1 Error Code  _(disabled)_
- Solar 1 Warning Code  _(disabled)_
- Solar 1 Status  _(disabled)_
- Solar 2 Watts
- Solar 2 Input Potential
- Solar 2 Op Potential
- Solar 2 Current
- Solar 2 Temperature
- Solar 2 Relay Status
- Solar 2 Error Code  _(disabled)_
- Solar 2 Warning Code  _(disabled)_
- Solar 2 Status  _(disabled)_
- Battery Type  _(disabled)_
- Battery Charge
- Battery Input Watts
- Battery Input Potential
- Battery Op Potential
- Battery Input Current
- Battery Temperature
- Charge Time
- Discharge Time
- Battery Error Code  _(disabled)_
- Battery Warning Code  _(disabled)_
- Battery Status  _(disabled)_
- LLC Input Potential  _(disabled)_
- LLC Op Potential  _(disabled)_
- LLC Error Code  _(disabled)_
- LLC Warning Code  _(disabled)_
- LLC Status  _(disabled)_
- Inverter On/Off Status
- Inverter Output Watts
- Inverter Output Potential  _(disabled)_
- Inverter Op Potential
- Inverter Output Current
- Inverter DC Current
- Inverter Frequency
- Inverter Temperature
- Inverter Relay Status
- Inverter Error Code  _(disabled)_
- Inverter Warning Code  _(disabled)_
- Inverter Status  _(disabled)_
- Other Loads
- Smart Plug Loads
- Rated Power
- Lower Battery Limit  _(disabled)_
- Upper Battery Limit  _(disabled)_
- Wireless Error Code  _(disabled)_
- Wireless Warning Code  _(disabled)_
- LED Brightness  _(disabled)_
- Heartbeat Frequency  _(disabled)_
- Status

*Switches*

*Sliders (numbers)*

*Selects*

</p></details>

<details><summary> GLACIER <i>(sensors: 33, switches: 3, sliders: 3, selects: 0)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- Battery Level
- Battery Charging State
- Total In Power
- Total Out Power
- Motor Power
- Charge Remaining Time
- Discharge Remaining Time
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Battery Present
- XT60 State
- Fan Level
- Ambient Temperature
- Exhaust Temperature
- Water Temperature
- Left Temperature
- Right Temperature
- Dual Zone Mode
- Ice Time Remain
- Ice Percentage
- Ice Make Mode
- Ice Alert
- Ice Water Level OK
- Status

*Switches*
- Beeper 
- Eco Mode 
- Power 

*Sliders (numbers)*
- Left Set Temperature 
- Combined Set Temperature 
- Right Set Temperature 

*Selects*

</p></details>

<details><summary> WAVE_2 <i>(sensors: 27, switches: 0, sliders: 1, selects: 4)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Remain Capacity  _(disabled)_
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Charge Remaining Time
- Discharge Remaining Time
- Condensation temperature  _(disabled)_
- Return air temperature in condensation zone  _(disabled)_
- Air outlet temperature  _(disabled)_
- Evaporation temperature  _(disabled)_
- Exhaust temperature  _(disabled)_
- Evaporation zone return air temperature  _(disabled)_
- Air outlet temperature  _(disabled)_
- Ambient temperature  _(disabled)_
- PV input power
- Battery output power
- PV charging power
- AC input power
- Power supply power
- System power
- Battery power
- Motor operating power
- Battery output power
- AC input power
- PV input power
- Status

*Switches*

*Sliders (numbers)*
- Set Temperature 

*Selects*
- Wind speed 
- Main mode 
- Remote startup/shutdown 
- Sub-mode 

</p></details>

<details><summary> DELTA Pro (API) <i>(sensors: 71, switches: 6, sliders: 6, selects: 4)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Battery Level (Precise)  _(disabled)_
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Battery Level (Precise)  _(disabled)_
- Total In Power
- Total Out Power
- Main Battery Current
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar In Power
- Solar In Voltage
- Solar In Current
- DC Out Power
- DC Out Voltage
- DC Car Out Power
- DC Anderson Out Power
- Type-C (1) Out Power
- Type-C (2) Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB QC (1) Out Power
- USB QC (2) Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Solar In Energy
- Battery Charge Energy from AC
- Battery Charge Energy from DC
- Battery Discharge Energy to AC
- Battery Discharge Energy to DC
- Slave 1 Battery Level  _(auto)_
- Slave 1 Battery Level (Precise)  _(disabled)_
- Slave 1 Design Capacity  _(disabled)_
- Slave 1 Full Capacity  _(disabled)_
- Slave 1 Remain Capacity  _(disabled)_
- Slave 1 State of Health
- Slave 1 Battery Temperature  _(auto)_
- Slave 1 In Power  _(auto)_
- Slave 1 Out Power  _(auto)_
- Slave 2 Battery Level  _(auto)_
- Slave 2 Battery Level (Precise)  _(disabled)_
- Slave 2 Design Capacity  _(disabled)_
- Slave 2 Full Capacity  _(disabled)_
- Slave 2 Remain Capacity  _(disabled)_
- Slave 2 State of Health
- Slave 1 Battery Volts  _(disabled)_
- Slave 1 Min Cell Volts  _(disabled)_
- Slave 1 Max Cell Volts  _(disabled)_
- Slave 1 Battery Current  _(disabled)_
- Slave 2 Battery Volts  _(disabled)_
- Slave 2 Min Cell Volts  _(disabled)_
- Slave 2 Max Cell Volts  _(disabled)_
- Slave 2 Battery Current  _(disabled)_
- Slave 2 Battery Temperature  _(auto)_
- Slave 2 In Power  _(auto)_
- Slave 2 Out Power  _(auto)_
- Slave 1 Cycles  _(disabled)_
- Slave 2 Cycles  _(disabled)_
- Status

*Switches*
- Beeper 
- DC (12V) Enabled 
- AC Enabled 
- X-Boost Enabled 
- AC Always On 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- Backup Reserve Level 
- Generator Auto Start Level 
- Generator Auto Stop Level 
- AC Charging Power 

*Selects*
- DC (12V) Charge Current 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> DELTA 2 (API) <i>(sensors: 45, switches: 8, sliders: 6, selects: 5)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Total In Power
- Total Out Power
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar In Power
- DC Out Power
- Type-C (1) Out Power
- Type-C (2) Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB QC (1) Out Power
- USB QC (2) Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Slave Battery Level  _(auto)_
- Slave Design Capacity  _(disabled)_
- Slave Full Capacity  _(disabled)_
- Slave Remain Capacity  _(disabled)_
- Slave State of Health
- Slave Battery Temperature  _(auto)_
- Slave Min Cell Temperature  _(disabled)_
- Slave Max Cell Temperature  _(disabled)_
- Slave Battery Volts  _(disabled)_
- Slave Min Cell Volts  _(disabled)_
- Slave Max Cell Volts  _(disabled)_
- Slave Cycles  _(auto)_
- Slave In Power  _(auto)_
- Slave Out Power  _(auto)_
- Status

*Switches*
- Beeper 
- USB Enabled 
- AC Always On 
- Prio Solar Charging 
- AC Enabled 
- X-Boost Enabled 
- DC (12V) Enabled 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- Backup Reserve Level 
- Generator Auto Start Level 
- Generator Auto Stop Level 
- AC Charging Power 

*Selects*
- DC (12V) Charge Current 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 
- DC (12V) Timeout 

</p></details>

<details><summary> DELTA 2 Max (API) <i>(sensors: 67, switches: 7, sliders: 6, selects: 3)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Total In Power
- Total Out Power
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar (1) In Power
- Solar (2) In Power
- Solar (1) In Volts
- Solar (2) In Volts
- Solar (1) In Amps
- Solar (2) In Amps
- DC Out Power
- Type-C (1) Out Power
- Type-C (2) Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB QC (1) Out Power
- USB QC (2) Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Battery level SOC  _(auto)_
- Slave 1 Battery Level  _(auto)_
- Slave 1 Design Capacity  _(disabled)_
- Slave 1 Full Capacity  _(disabled)_
- Slave 1 Remain Capacity  _(disabled)_
- Slave 1 Battery Temperature  _(auto)_
- Slave 1 Min Cell Temperature  _(disabled)_
- Slave 1 Max Cell Temperature  _(disabled)_
- Slave 1 Battery Volts  _(disabled)_
- Slave 1 Min Cell Volts  _(disabled)_
- Slave 1 Max Cell Volts  _(disabled)_
- Slave 1 Cycles  _(auto)_
- Slave 1 State of Health  _(auto)_
- Slave 1 In Power  _(auto)_
- Slave 1 Out Power  _(auto)_
- Slave 1 Battery level SOC  _(auto)_
- Slave 2 Battery Level  _(auto)_
- Slave 2 Design Capacity  _(disabled)_
- Slave 2 Full Capacity  _(disabled)_
- Slave 2 Remain Capacity  _(disabled)_
- Slave 2 Battery Temperature  _(auto)_
- Slave 2 Min Cell Temperature  _(disabled)_
- Slave 2 Max Cell Temperature  _(disabled)_
- Slave 2 Battery Volts  _(disabled)_
- Slave 2 Min Cell Volts  _(disabled)_
- Slave 2 Max Cell Volts  _(disabled)_
- Slave 2 Cycles  _(auto)_
- Slave 2 State of Health  _(auto)_
- Slave 2 In Power  _(auto)_
- Slave 2 Out Power  _(auto)_
- Slave 2 Battery level SOC  _(auto)_
- Status

*Switches*
- Beeper 
- USB Enabled 
- AC Always On 
- AC Enabled 
- X-Boost Enabled 
- DC (12V) Enabled 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- Backup Reserve Level 
- Generator Auto Start Level 
- Generator Auto Stop Level 
- AC Charging Power 

*Selects*
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> RIVER 2 (API) <i>(sensors: 32, switches: 5, sliders: 4, selects: 5)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Battery Charging State
- Total In Power
- Total Out Power
- Solar In Current
- Solar In Voltage
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Type-C In Power
- Solar In Power
- DC Out Power
- Type-C Out Power
- USB Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Status

*Switches*
- AC Enabled 
- AC Always On 
- X-Boost Enabled 
- DC (12V) Enabled 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- AC Charging Power 
- Backup Reserve Level 

*Selects*
- DC (12V) Charge Current 
- DC Mode 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> RIVER 2 Max (API) <i>(sensors: 32, switches: 5, sliders: 4, selects: 5)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Battery Charging State
- Total In Power
- Total Out Power
- Solar In Current
- Solar In Voltage
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Type-C In Power
- Solar In Power
- DC Out Power
- Type-C Out Power
- USB Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Status

*Switches*
- AC Enabled 
- AC Always On 
- X-Boost Enabled 
- DC (12V) Enabled 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- AC Charging Power 
- Backup Reserve Level 

*Selects*
- DC (12V) Charge Current 
- DC Mode 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> RIVER 2 Pro (API) <i>(sensors: 30, switches: 3, sliders: 3, selects: 5)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Battery Charging State
- Total In Power
- Total Out Power
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Type-C In Power
- Solar In Power
- DC Out Power
- Type-C Out Power
- USB Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Remaining Time
- Inv Out Temperature
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Status

*Switches*
- AC Enabled 
- X-Boost Enabled 
- DC (12V) Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- AC Charging Power 

*Selects*
- DC (12V) Charge Current 
- DC Mode 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> Smart Plug (API) <i>(sensors: 4, switches: 1, sliders: 1, selects: 0)</i> </summary>
<p>

*Sensors*
- Temperature
- Volts
- Current
- Power

*Switches*
- On 

*Sliders (numbers)*
- Brightness 

*Selects*

</p></details>

<details><summary> PowerStream (API) <i>(sensors: 58, switches: 0, sliders: 4, selects: 1)</i> </summary>
<p>

*Sensors*
- ESP Temperature
- Solar 1 Watts
- Solar 1 Input Potential
- Solar 1 Op Potential
- Solar 1 Current
- Solar 1 Temperature
- Solar 1 Relay Status
- Solar 1 Error Code  _(disabled)_
- Solar 1 Warning Code  _(disabled)_
- Solar 1 Status  _(disabled)_
- Solar 2 Watts
- Solar 2 Input Potential
- Solar 2 Op Potential
- Solar 2 Current
- Solar 2 Temperature
- Solar 2 Relay Status
- Solar 2 Error Code  _(disabled)_
- Solar 2 Warning Code  _(disabled)_
- Solar 2 Status  _(disabled)_
- Battery Type  _(disabled)_
- Battery Charge
- Battery Input Watts
- Battery Input Potential
- Battery Op Potential
- Battery Input Current
- Battery Temperature
- Charge Time
- Discharge Time
- Battery Error Code  _(disabled)_
- Battery Warning Code  _(disabled)_
- Battery Status  _(disabled)_
- LLC Input Potential  _(disabled)_
- LLC Op Potential  _(disabled)_
- LLC Temperature
- LLC Error Code  _(disabled)_
- LLC Warning Code  _(disabled)_
- LLC Status  _(disabled)_
- Inverter On/Off Status
- Inverter Output Watts
- Inverter Output Potential  _(disabled)_
- Inverter Op Potential
- Inverter Output Current
- Inverter Frequency
- Inverter Temperature
- Inverter Relay Status
- Inverter Error Code  _(disabled)_
- Inverter Warning Code  _(disabled)_
- Inverter Status  _(disabled)_
- Other Loads
- Smart Plug Loads
- Rated Power
- Lower Battery Limit  _(disabled)_
- Upper Battery Limit  _(disabled)_
- Wireless Error Code  _(disabled)_
- Wireless Warning Code  _(disabled)_
- LED Brightness  _(disabled)_
- Heartbeat Frequency  _(disabled)_
- Status

*Switches*

*Sliders (numbers)*
- Min Discharge Level 
- Max Charge Level 
- Brightness 
- Custom load power settings 

*Selects*
- Power supply mode 

</p></details>

<details><summary> DELTA_PRO_3 <i>(sensors: 71, switches: 6, sliders: 6, selects: 4)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Battery Level (Precise)  _(disabled)_
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Battery Level (Precise)  _(disabled)_
- Total In Power
- Total Out Power
- Main Battery Current
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar In Power
- Solar In Voltage
- Solar In Current
- DC Out Power
- DC Out Voltage
- DC Car Out Power
- DC Anderson Out Power
- Type-C (1) Out Power
- Type-C (2) Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB QC (1) Out Power
- USB QC (2) Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Solar In Energy
- Battery Charge Energy from AC
- Battery Charge Energy from DC
- Battery Discharge Energy to AC
- Battery Discharge Energy to DC
- Slave 1 Battery Level  _(auto)_
- Slave 1 Battery Level (Precise)  _(disabled)_
- Slave 1 Design Capacity  _(disabled)_
- Slave 1 Full Capacity  _(disabled)_
- Slave 1 Remain Capacity  _(disabled)_
- Slave 1 State of Health
- Slave 1 Battery Temperature  _(auto)_
- Slave 1 In Power  _(auto)_
- Slave 1 Out Power  _(auto)_
- Slave 2 Battery Level  _(auto)_
- Slave 2 Battery Level (Precise)  _(disabled)_
- Slave 2 Design Capacity  _(disabled)_
- Slave 2 Full Capacity  _(disabled)_
- Slave 2 Remain Capacity  _(disabled)_
- Slave 2 State of Health
- Slave 1 Battery Volts  _(disabled)_
- Slave 1 Min Cell Volts  _(disabled)_
- Slave 1 Max Cell Volts  _(disabled)_
- Slave 1 Battery Current  _(disabled)_
- Slave 2 Battery Volts  _(disabled)_
- Slave 2 Min Cell Volts  _(disabled)_
- Slave 2 Max Cell Volts  _(disabled)_
- Slave 2 Battery Current  _(disabled)_
- Slave 2 Battery Temperature  _(auto)_
- Slave 2 In Power  _(auto)_
- Slave 2 Out Power  _(auto)_
- Slave 1 Cycles  _(disabled)_
- Slave 2 Cycles  _(disabled)_
- Status

*Switches*
- Beeper 
- DC (12V) Enabled 
- AC Enabled 
- X-Boost Enabled 
- AC Always On 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- Backup Reserve Level 
- Generator Auto Start Level 
- Generator Auto Stop Level 
- AC Charging Power 

*Selects*
- DC (12V) Charge Current 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> DELTA Pro 3 (API) <i>(sensors: 71, switches: 6, sliders: 6, selects: 4)</i> </summary>
<p>

*Sensors*
- Main Battery Level
- Main Battery Level (Precise)  _(disabled)_
- Main Design Capacity  _(disabled)_
- Main Full Capacity  _(disabled)_
- Main Remain Capacity  _(disabled)_
- State of Health
- Battery Level
- Battery Level (Precise)  _(disabled)_
- Total In Power
- Total Out Power
- Main Battery Current
- AC In Power
- AC Out Power
- AC In Volts
- AC Out Volts
- Solar In Power
- Solar In Voltage
- Solar In Current
- DC Out Power
- DC Out Voltage
- DC Car Out Power
- DC Anderson Out Power
- Type-C (1) Out Power
- Type-C (2) Out Power
- USB (1) Out Power
- USB (2) Out Power
- USB QC (1) Out Power
- USB QC (2) Out Power
- Charge Remaining Time
- Discharge Remaining Time
- Cycles
- Battery Temperature
- Min Cell Temperature  _(disabled)_
- Max Cell Temperature  _(disabled)_
- Battery Volts  _(disabled)_
- Min Cell Volts  _(disabled)_
- Max Cell Volts  _(disabled)_
- Solar In Energy
- Battery Charge Energy from AC
- Battery Charge Energy from DC
- Battery Discharge Energy to AC
- Battery Discharge Energy to DC
- Slave 1 Battery Level  _(auto)_
- Slave 1 Battery Level (Precise)  _(disabled)_
- Slave 1 Design Capacity  _(disabled)_
- Slave 1 Full Capacity  _(disabled)_
- Slave 1 Remain Capacity  _(disabled)_
- Slave 1 State of Health
- Slave 1 Battery Temperature  _(auto)_
- Slave 1 In Power  _(auto)_
- Slave 1 Out Power  _(auto)_
- Slave 2 Battery Level  _(auto)_
- Slave 2 Battery Level (Precise)  _(disabled)_
- Slave 2 Design Capacity  _(disabled)_
- Slave 2 Full Capacity  _(disabled)_
- Slave 2 Remain Capacity  _(disabled)_
- Slave 2 State of Health
- Slave 1 Battery Volts  _(disabled)_
- Slave 1 Min Cell Volts  _(disabled)_
- Slave 1 Max Cell Volts  _(disabled)_
- Slave 1 Battery Current  _(disabled)_
- Slave 2 Battery Volts  _(disabled)_
- Slave 2 Min Cell Volts  _(disabled)_
- Slave 2 Max Cell Volts  _(disabled)_
- Slave 2 Battery Current  _(disabled)_
- Slave 2 Battery Temperature  _(auto)_
- Slave 2 In Power  _(auto)_
- Slave 2 Out Power  _(auto)_
- Slave 1 Cycles  _(disabled)_
- Slave 2 Cycles  _(disabled)_
- Status

*Switches*
- Beeper 
- DC (12V) Enabled 
- AC Enabled 
- X-Boost Enabled 
- AC Always On 
- Backup Reserve Enabled 

*Sliders (numbers)*
- Max Charge Level 
- Min Discharge Level 
- Backup Reserve Level 
- Generator Auto Start Level 
- Generator Auto Stop Level 
- AC Charging Power 

*Selects*
- DC (12V) Charge Current 
- Screen Timeout 
- Unit Timeout 
- AC Timeout 

</p></details>

<details><summary> SMART_HOME_PANEL_2 <i>(sensors: 36, switches: 13, sliders: 11, selects: 1)</i> </summary>
<p>

*Sensors*
- Grid Input Power
- Grid Input Voltage
- Grid Input Current
- Grid Input Energy
- EPS Battery Level
- EPS Input Power
- EPS Output Power
- Circuit 1 Power
- Circuit 2 Power
- Circuit 3 Power
- Circuit 4 Power
- Circuit 5 Power
- Circuit 6 Power
- Circuit 7 Power
- Circuit 8 Power
- Circuit 9 Power
- Circuit 10 Power
- Total Load Power
- Circuit 1 Energy
- Circuit 2 Energy
- Circuit 3 Energy
- Circuit 4 Energy
- Circuit 5 Energy
- Circuit 6 Energy
- Circuit 7 Energy
- Circuit 8 Energy
- Circuit 9 Energy
- Circuit 10 Energy
- Grid Status
- EPS Status
- Status

*Switches*
- EPS Enabled 
- Grid Charging Enabled 
- Circuit 1 Breaker 
- Circuit 2 Breaker 
- Circuit 3 Breaker 
- Circuit 4 Breaker 
- Circuit 5 Breaker 
- Circuit 6 Breaker 
- Circuit 7 Breaker 
- Circuit 8 Breaker 
- Circuit 9 Breaker 
- Circuit 10 Breaker 
- Load Shedding Enabled 

*Sliders (numbers)*
- Circuit 1 Priority 
- Circuit 2 Priority 
- Circuit 3 Priority 
- Circuit 4 Priority 
- Circuit 5 Priority 
- Circuit 6 Priority 
- Circuit 7 Priority 
- Circuit 8 Priority 
- Circuit 9 Priority 
- Circuit 10 Priority 
- Grid Backup Transition Delay (ms) 

*Selects*
- Backup Mode Timeout 

</p></details>

<details><summary> Smart Home Panel 2 (API) <i>(sensors: 36, switches: 13, sliders: 11, selects: 1)</i> </summary>
<p>

*Sensors*
- Grid Input Power
- Grid Input Voltage
- Grid Input Current
- Grid Input Energy
- EPS Battery Level
- EPS Input Power
- EPS Output Power
- Circuit 1 Power
- Circuit 2 Power
- Circuit 3 Power
- Circuit 4 Power
- Circuit 5 Power
- Circuit 6 Power
- Circuit 7 Power
- Circuit 8 Power
- Circuit 9 Power
- Circuit 10 Power
- Total Load Power
- Circuit 1 Energy
- Circuit 2 Energy
- Circuit 3 Energy
- Circuit 4 Energy
- Circuit 5 Energy
- Circuit 6 Energy
- Circuit 7 Energy
- Circuit 8 Energy
- Circuit 9 Energy
- Circuit 10 Energy
- Grid Status
- EPS Status
- Status

*Switches*
- EPS Enabled 
- Grid Charging Enabled 
- Circuit 1 Breaker 
- Circuit 2 Breaker 
- Circuit 3 Breaker 
- Circuit 4 Breaker 
- Circuit 5 Breaker 
- Circuit 6 Breaker 
- Circuit 7 Breaker 
- Circuit 8 Breaker 
- Circuit 9 Breaker 
- Circuit 10 Breaker 
- Load Shedding Enabled 

*Sliders (numbers)*
- Circuit 1 Priority 
- Circuit 2 Priority 
- Circuit 3 Priority 
- Circuit 4 Priority 
- Circuit 5 Priority 
- Circuit 6 Priority 
- Circuit 7 Priority 
- Circuit 8 Priority 
- Circuit 9 Priority 
- Circuit 10 Priority 
- Grid Backup Transition Delay (ms) 

*Selects*
- Backup Mode Timeout 

</p></details>

## How to
- [Add/update device](docs/integration.md)
