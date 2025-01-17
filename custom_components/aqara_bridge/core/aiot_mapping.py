from homeassistant.components.binary_sensor import *
from homeassistant.components.cover import *
from homeassistant.components.light import *
from homeassistant.components.sensor import *
from homeassistant.const import *

# AiotDevice Mapping
MK_MAPPING_PARAMS = "mapping_params"
MK_INIT_PARAMS = "init_params"
MK_RESOURCES = "resources"
MK_HASS_NAME = "hass_attr_name"

AIOT_DEVICE_MAPPING = [
############################ Aqara M1S网关###################################
{
    'lumi.gateway.aeu01': ["Aqara", "Gateway M1S", "ZHWG15LM"],
    'lumi.gateway.acn01': ["Aqara", "Gateway M1S", "ZHWG15LM"],
    'lumi.gateway.acn004': ["Aqara", "Gateway M1S 22", "ZHWG15LM"],
    'lumi.gateway.agl002': ["Aqara", "Gateway M1S Gen2", "ZHWG15LM"],
    'lumi.gateway.aqhm02': ["Aqara", "Gateway", "ZHWG15LM"],
    'lumi.gateway.aqhm01': ["Aqara", "Gateway", "ZHWG15LM"],
    'params': [
        {
            "light": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "light",
                    "color_mode": ColorMode.HS,
                    "supported_color_modes": [ColorMode.BRIGHTNESS, ColorMode.HS],
                },
                MK_RESOURCES: {
                    "toggle": ("14.7.111", "_attr_is_on"),
                    "color": ("14.7.85", "_attr_hs_color"),
                    "brightness": ("14.7.1006", "_attr_brightness"),
                }
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "illuminance",
                    "device_class": SensorDeviceClass.ILLUMINANCE,
                    "state_class": "measurement",
                    "unit_of_measurement": LIGHT_LUX
                },
                MK_RESOURCES: {"illumination": ("0.3.85", "_attr_native_value")},
            }
        }
    ]
},
###########################绿米H1、E1、M2网关####################################
{
    'lumi.gateway.sacn01': ["Aqara", "Smart Hub H1", "QBCZWG11LM"],
    'lumi.gateway.aqcn02': ["Aqara", "Hub E1", "ZHWG16LM"],
    'lumi.gateway.iragl01': ["Aqara", "GateWay M2", ""],
    'lumi.gateway.iragl5': ["Aqara", "GateWay M2", ""],
    'lumi.gateway.iragl7': ["Aqara", "GateWay M2", ""],
    'lumi.gateway.iragl8': ["Aqara", "GateWay M2 22", ""],
    'lumi.gateway.aq1': ["Aqara", "GateWay M2", ""],
    'params': []
},
################################墙壁开关#########################################
###单键
{
    # 墙壁开关（零火线单键版）
    'lumi.ctrl_ln1.v1': ["Aqara", "Wall Switch (Single Rocker)", ""],
    # 墙壁开关H1M（零火线单键版）
    'lumi.switch.acn029': ["Aqara", "Wall Switch H1M (Single Rocker)", ""],
    # 墙壁开关X1（零火线单键版）
    'lumi.switch.acn004':["Aqara", "Wall Switch X1 (Single Rocker)", ""],
    # 墙壁开关H1（零火线单键版）
    'lumi.switch.n1acn1':["Aqara", "Wall Switch H1 (Single Rocker)", "QBKG27LM"],
    # 墙壁开关T1（零火线单键版）
    'lumi.switch.b1nacn01': ["Aqara", "Wall Switch T1 (Single Rocker)", ""],
    # 墙壁开关D1（零火线单键版）
    'lumi.switch.b1nacn02': ["Aqara", "Wall Switch D1 (Single Rocker)", ""],
    # 墙壁开关E1（零火线单键版）
    'lumi.switch.b1nc01': ["Aqara", "Wall Switch E1 (Single Rocker)", ""],
    'params': [
        {
            "switch": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "wall_switch",
                },
                MK_RESOURCES: {
                    "toggle": ("4.1.85", "_attr_is_on"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi")
                }
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "power",
                    "device_class": BinarySensorDeviceClass.POWER,
                    "state_class": "measurement",
                    "unit_of_measurement": UnitOfPower.WATT},
                MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")}
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "energy",
                    "device_class": SensorDeviceClass.ENERGY,
                    "state_class": "total_increasing",
                    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR},
                MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
            }
        }
    ]
},

{
    # 墙壁开关（单火线单键版）
    'lumi.ctrl_neutral1.v1': ["Aqara", "Wall Switch (Single Rocker)", "QBKG04LM"],
    # 墙壁开关X1（单火线单键版）
    'lumi.switch.acn001':["Aqara", "Wall Switch X1 (Single Rocker)", ""],
    # 墙壁开关H1（单火线单键版）
    'lumi.switch.l1acn1':["Aqara", "Wall Switch H1 (Single Rocker)", "QBKG27LM"],
    # 墙壁开关T1（单火线单键版）
    'lumi.switch.b1lacn01': ["Aqara", "Wall Switch T1 (Single Rocker)", ""],
    # 墙壁开关D1（单火线单键版）
    'lumi.switch.b1lacn02': ["Aqara", "Wall Switch D1 (Single Rocker)", ""],
    # 墙壁开关E1（单火线单键版）
    'lumi.switch.b1lc04': ["Aqara", "Wall Switch E1 (Single Rocker)", ""],
    'params': [
        {
            "switch": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "wall_switch",
                },
                MK_RESOURCES: {
                    "toggle": ("4.1.85", "_attr_is_on"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi")
                }
            }
        }
    ]
},
###双键
{
    # 墙壁开关（零火线双键版）
    'lumi.ctrl_ln2.v1': ["Aqara", "Wall Switch (Double Rocker)", ""],
    # 墙壁开关H1M（零火线双键版）
    'lumi.switch.acn030': ["Aqara", "Wall Switch H1M (Double Rocker)", ""],
    # 墙壁开关X1（零火线双键版）
    'lumi.switch.acn005':["Aqara", "Wall Switch X1 (Double Rocker)", ""],
    # 墙壁开关H1（零火线双键版）
    'lumi.switch.n2acn1':["Aqara", "Wall Switch H1 (Double Rocker)", "QBKG27LM"],
    # 墙壁开关T1（零火线双键版）
    'lumi.switch.b2nacn01': ["Aqara", "Wall Switch T1 (Double Rocker)", ""],
    # 墙壁开关D1（零火线双键版）
    'lumi.switch.b2nacn02': ["Aqara", "Wall Switch D1 (Double Rocker)", ""],
    # 墙壁开关E1（零火线双键版）
    'lumi.switch.b2nc01': ["Aqara", "Wall Switch E1 (Double Rocker)", ""],
    'params': [
        {
            "switch": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "wall_switch",
                },
                MK_RESOURCES: {
                    "toggle": ("4.{}.85", "_attr_is_on"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                },
                MK_MAPPING_PARAMS: {"ch_count": 2},
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "power",
                    "device_class": BinarySensorDeviceClass.POWER,
                    "state_class": "measurement",
                    "unit_of_measurement": UnitOfPower.WATT},
                MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")}
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "energy",
                    "device_class": SensorDeviceClass.ENERGY,
                    "state_class": "total_increasing",
                    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR},
                MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
            }
        }
    ]
},
{
    # 墙壁开关（单火线双键版）
    'lumi.ctrl_neutral2.v1': ["Aqara", "Wall Switch (Double Rocker)", "QBKG04LM"],
    # 墙壁开关X1（单火线双键版）
    'lumi.switch.acn002':["Aqara", "Wall Switch X1 (Double Rocker)", ""],
    # 墙壁开关H1（单火线双键版）
    'lumi.switch.l2acn1':["Aqara", "Wall Switch H1 (Double Rocker)", "QBKG28LM"],
    # 墙壁开关T1（单火线双键版）
    'lumi.switch.b2lacn01': ["Aqara", "Wall Switch T1 (Double Rocker)", ""],
    # 墙壁开关D1（单火线双键版）
    'lumi.switch.b2lacn02': ["Aqara", "Wall Switch D1 (Double Rocker)", "QBKG21LM"],
    # 墙壁开关E1（单火线双键版）
    'lumi.switch.b2lc04': ["Aqara", "Wall Switch E1 (Double Rocker)", "QBKG21LM"],
    'params': [
        {
            "switch": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "wall_switch",
                },
                MK_RESOURCES: {
                    "toggle": ("4.{}.85", "_attr_is_on"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                },
                MK_MAPPING_PARAMS: {"ch_count": 2},
            }
        }
    ]
},
###三键
{
    # 墙壁开关H1M（零火线三键版）
    'lumi.switch.acn031': ["Aqara", "Wall Switch H1M (Three Rocker)", ""],
    # 墙壁开关X1（零火线三键版）
    'lumi.switch.acn006':["Aqara", "Wall Switch X1 (Three Rocker)", ""],
    # 墙壁开关H1（零火线三键版）
    'lumi.switch.n3acn1':["Aqara", "Wall Switch H1 (Three Rocker)", "QBKG27LM"],
    # 墙壁开关T1（零火线三键版）
    'lumi.switch.b3n01': ["Aqara", "Wall Switch T1 (Three Rocker)", ""],

    #智能场景面板开关 S1（零火线三键版）
    'lumi.switch.n4acn4': ["Aqara", "screen panel S1 (Three Rocker)", ""],
    # # 妙控开关S1E（零火线三键版、无线开关6个）
    # 'lumi.switch.acn032':["Aqara", "Wall Switch S1E WIFI 3+6", ""],
    'params': [
        {
            "switch": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "wall_switch",
                },
                MK_RESOURCES: {
                    "toggle": ("4.{}.85", "_attr_is_on"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi")
                },
                MK_MAPPING_PARAMS: {"ch_count": 3},
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "power",
                    "device_class": BinarySensorDeviceClass.POWER,
                    "state_class": "measurement",
                    "unit_of_measurement": UnitOfPower.WATT},
                MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")}
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "energy",
                    "device_class": SensorDeviceClass.ENERGY,
                    "state_class": "total_increasing",
                    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR},
                MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
            }
        }
    ]
},
{
    # 墙壁开关X1（单火线三键版）
    'lumi.switch.acn003':["Aqara", "Wall Switch X1 (Three Rocker)", ""],
    # 墙壁开关H1（单火线三键版）
    'lumi.switch.l3acn1':["Aqara", "Wall Switch H1 (Three Rocker)", "QBKG29LM"],
    # 墙壁开关T1（单火线三键版）
    'lumi.switch.b3l01': ["Aqara", "Wall Switch T1 (Three Rocker)", ""],
    'params': [
        {
            "switch": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "wall_switch",
                },
                MK_RESOURCES: {
                    "toggle": ("4.{}.85", "_attr_is_on"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi")
                },
                MK_MAPPING_PARAMS: {"ch_count": 3},
            }
        }
    ]
},
##########################通断器、插座开关#######################################
{
    # 单路控制器 T1（单火版）
    'lumi.switch.l0acn1': ["Aqara", "Wall Switch (Single Rocker)", ""],
    # 单路控制器（零火版）
    'lumi.switch.n0acn2': ["Aqara", "Wall Switch (Single Rocker)", ""],
    # 智能插座 (国标)
    'lumi.plug.v1': ["Xiaomi", "Plug", "ZNCZ02LM"],
    # 智能插座 (国标)
    'lumi.plug.aq1': ["Xiaomi", "Plug", ""],
    # 智能插座T1 (国标)
    'lumi.plug.macn01': ["Aqara", "Plug T1", ""],
    # 智能墙壁插座 X1（USB版）
    'lumi.plug.acn003': ["Aqara", "Smart Wall Outlet X1(USB)", ""],
    # 智能墙壁插座 H1（USB版）
    'lumi.plug.sacn03': ["Aqara", "Smart Wall Outlet H1(USB)", "QBCZWG11LM"],
    # 智能墙壁插座 H1
    'lumi.plug.sacn02': ["Aqara", "Smart Wall Outlet H1", "QBCZWG11LM"],
    'params': [
        {
            "switch": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "switch"
                },
                MK_RESOURCES: {
                    "toggle": ("4.1.85", "_attr_is_on"),
                    "power": ("0.12.85", "_attr_current_power_w"),
                    "energy": ("0.13.85", "_attr_today_energy_kwh"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                }
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "power",
                    "device_class": BinarySensorDeviceClass.POWER,
                    "state_class": "measurement",
                    "unit_of_measurement": UnitOfPower.WATT},
                MK_RESOURCES: {"power": ("0.12.85", "_attr_native_value")}
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "energy",
                    "device_class": SensorDeviceClass.ENERGY,
                    "state_class": "total_increasing",
                    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR},
                MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
            }
        }
    ]
},
###############################调光器###########################################
{
    #LED灯泡（可调色温）
    'lumi.light.aqcn02': ["Aqara", "Bulb", "ZNLDP12LM"],
    #吸顶灯MX650（可调色温）
    'lumi.light.cwopcn02': ["Aqara", "Opple MX650", "XDD12LM"],
    #吸顶灯MX480（可调色温）
    'lumi.light.cwopcn03': ["Aqara", "Opple MX480", "XDD13LM"],
    #Aqara智能调光模块T1（0-10v）
    'lumi.light.cwacn1': ["Aqara", "0-10V Dimmer", "ZNTGMK12LM"],
    #射灯（可调色温）
    'lumi.light.cwjwcn01': ["Aqara", "Jiawen 0-12V Dimmer", "Z204"],
    'params': [
        {
            "light": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "light",
                    "color_mode": ColorMode.XY,  # 写hs为rgb模式 xy为色温模式
                    "supported_color_mode": [ColorMode.BRIGHTNESS, ColorMode.COLOR_TEMP],
                    "min_mireds": 153,
                    "max_mireds": 370
                },
                MK_RESOURCES: {
                    "toggle": ("4.1.85", "_attr_is_on"),
                    "brightness": ("14.1.85", "_attr_brightness"),
                    "color_temp": ("14.2.85", "_attr_color_temp"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                }
            }
        }
    ]
},

{
    # Aqara LED灯泡 T1
    'lumi.light.cwac02': ["Aqara", "Bulb T1", "ZNLDP13LM"],
    'params': [
        {
            "light": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "light",
                    "color_mode": ColorMode.XY,  #写hs为rgb模式 xy为色温模式
                    "supported_color_mode": [ColorMode.BRIGHTNESS, ColorMode.COLOR_TEMP],
                },
                MK_RESOURCES: {
                    "toggle": ("4.1.85", "_attr_is_on"),
                    "brightness": ("1.7.85", "_attr_brightness"),
                    "color_temp": ("1.9.85", "_attr_color_temp"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                }
            }
        }
    ]
},

{
    #Aqara智能调光模块 T1
    'lumi.light.rgbac1': ["Aqara", "RGBW LED Controller T1", "ZNTGMK11LM"],
    'params': [
        {
            "light": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "light",
                    "color_mode": ColorMode.HS,  # 写hs为rgb模式 xy为色温模式
                    "supported_color_mode": [ColorMode.BRIGHTNESS, ColorMode.HS],
                },
                MK_RESOURCES: {
                    "toggle": ("4.1.85", "_attr_is_on"),
                    "brightness": ("14.1.85", "_attr_brightness"),
                    "color_temp": ("14.2.85", "_attr_color_temp"),
                    "color": ("14.8.85", "_attr_hs_color"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                }
            }
        }
    ]
},

{
    #Aqara智能灯带驱动模块
    'lumi.dimmer.rcbac1': ["Aqara", "RGBW LED Dimmer", "ZNDDMK11LM"],
    'params': [
        {
            "light": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "light",
                    # 颜色模式XY转换有问题，无法根据云端值拆分计算
                    "color_mode": ColorMode.XY,  #写hs为rgb模式 xy为色温模式
                    "supported_color_mode": [ColorMode.BRIGHTNESS, ColorMode.COLOR_TEMP],
                    "min_mireds": 153,
                    "max_mireds": 370
                },
                MK_RESOURCES: {
                    "toggle": ("4.1.85", "_attr_is_on"),
                    "brightness": ("14.1.85", "_attr_brightness"),
                    "color_temp": ("14.2.85", "_attr_color_temp"),
                    "color": ("14.8.85", "_attr_hs_color"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi")
                }
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "energy",
                    "device_class": SensorDeviceClass.ENERGY,
                    "state_class": "total_increasing",
                    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR},
                MK_RESOURCES: {"energy": ("0.13.85", "_attr_native_value")},
            }
        }
    ]
},

{
    #轨道格栅灯 H1（12头）
    'lumi.light.acn008': ["Aqara", "H1 LED Light", ""],
    'params': [
        {
            "light": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "light",
                    # 颜色模式XY转换有问题，无法根据云端值拆分计算
                    "color_mode": ColorMode.XY,  #写hs为rgb模式 xy为色温模式
                    "supported_color_mode": [ColorMode.BRIGHTNESS, ColorMode.COLOR_TEMP],
                    "min_mireds": 153,
                    "max_mireds": 370
                },
                MK_RESOURCES: {
                    "toggle": ("4.1.85", "_attr_is_on"),
                    "brightness": ("14.1.85", "_attr_brightness"),
                    "color_temp": ("14.2.85", "_attr_color_temp"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi")
                }
            }
        }
    ]
},

{
    ##################################无线开关##################################
    # 无线开关（贴墙式单键版）
    'lumi.remote.b186acn01': ["Aqara", "Single Wall Button", "WXKG03LM"],
    # 无线开关
    'lumi.remote.b1acn01': ["Aqara", "Wireless Remote Switch (Single Rocker)", ""],
    # 无线开关（升级版）
    'lumi.sensor_switch.aq3' : ["Aqara", "Wireless Remote Switch Plus (Single Rocker)", ""],
    # 无线开关H1（贴墙式单键版）
    'lumi.remote.b18ac1': ["Aqara", "Wireless Remote Switch H1 (Single Rocker)", "WXKG14LM"],
    # 无线开关E1（贴墙式单键版）
    'lumi.remote.b1acn02': ["Aqara", "Wireless Remote Switch E1 (Single Rocker)", "WXKG12LM"],
    # 无线开关E1（贴墙式单键版）
    'lumi.remote.acn003': ["Aqara", "Wireless Remote Switch E1 (Single Rocker)", "WXKG16LM"],
    # 无线开关D1（贴墙式单键版）
    'lumi.remote.b186acn02': ["Aqara", "Wireless Remote Switch D1 (Single Rocker)", "WXKG06LM"],
    # 无线开关T1（贴墙式单键版）
    'lumi.remote.b186acn03': ["Aqara", "Wireless Remote Switch T1 (Single Rocker)", ""],
    # 无线开关E1 mini
    'lumi.remote.acn007': ["Aqara", "Single Wall Button E1", "WXKG20LM"],
    'params': [
        {
            "button": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "action",
                    "device_class": "",
                    "state_class": "",
                    "unit_of_measurement": ""
                },
                MK_RESOURCES: {"button": ("13.1.85", "_attr_press_type")},
            }
        }
    ]
},
###无线双键
{
    # 无线开关（贴墙式双键版）
    'lumi.remote.b286acn01': ["Aqara", "Double Wall Button", "WXKG02LM"],
    # 无线开关H1（贴墙式双键版）
    'lumi.remote.b28ac1': ["Aqara", "Wireless Remote Switch H1 (Double Rocker)", "WXKG15LM"],
    # 无线开关E1（贴墙式双键版）
    'lumi.remote.acn004': ["Aqara", "Wireless Remote Switch E1 (Double Rocker)", "WXKG17LM"],
    # 无线开关D1（贴墙式双键版）
    'lumi.remote.b286acn02': ["Aqara", "Wireless Remote Switch D1 (Double Rocker)", "WXKG07LM"],
    # 无线开关T1（贴墙式双键版）
    'lumi.remote.b286acn03': ["Aqara", "Wireless Remote Switch T1 (Double Rocker)", ""],
    'params': [
        {
            "button": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "action",
                    "device_class": "",
                    "state_class": "",
                    "unit_of_measurement": ""
                },
                MK_RESOURCES: {"button": ("13.{}.85", "_attr_press_type")},
                MK_MAPPING_PARAMS: {"ch_count": 2},
            }
        }
    ]
},
###无线四键
{
    # 无线开关（四键版）
    'lumi.remote.b486opcn01': ["Aqara", "Wireless Remote Switch (Four Rocker)", ""],
    'params': [
        {
            "button": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "action",
                    "device_class": "",
                    "state_class": "",
                    "unit_of_measurement": ""
                },
                MK_RESOURCES: {"button": ("13.{}.85", "_attr_press_type")},
                MK_MAPPING_PARAMS: {"ch_count": 4},
            }
        }
    ]
},
###无线六键
{
    # 无线开关（六键版）
    'lumi.remote.b486opcn01': ["Aqara", "Wireless Remote Switch (Six Rocker)", ""],
    'params': [
        {
            "button": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "action",
                    "device_class": "",
                    "state_class": "",
                    "unit_of_measurement": ""
                },
                MK_RESOURCES: {"button": ("13.{}.85", "_attr_press_type")},
                MK_MAPPING_PARAMS: {"ch_count": 6},
            }
        }
    ]
},
###无线旋钮
{
    #智能旋钮开关 H1（无线版）
    'lumi.remote.rkba01': ["Aqara", "Wireless rotary switch H1", ""],
    'params': [
        {
            "button": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "action",
                    "device_class": "",
                    "state_class": "",
                    "unit_of_measurement": ""
                },
                MK_RESOURCES: {"button": ("13.1.85", "_attr_press_type")},
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "rotation_angle",
                    "device_class": "",
                    "state_class": "",
                    "unit_of_measurement": ""
                },
                MK_RESOURCES: {"state": ("0.22.85", "_attr_native_value")},
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "press_rotation_angle",
                    "device_class": "",
                    "state_class": "",
                    "unit_of_measurement": ""
                },
                MK_RESOURCES: {"state": ("0.29.85", "_attr_native_value")},
            }
        }
    ]
},
###############################传感器###########################################
###温湿度
{
    # 小米温湿度传感器
    'lumi.sensor_ht.v1': ["Xiaomi", "TH Sensor", "WSDCGQ01LM"],
    # 温湿度传感器T1
    'lumi.sensor_ht.agl02': ["Aqara", "T1 TH Sensor", ""],
    # 温湿度传感器
    'lumi.weather.v1': ["Aqara", "TH Sensor", "WSDCGQ11LM"],
    'params': [
        {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "temperature",
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "state_class": "measurement",
                    "unit_of_measurement": UnitOfTemperature.CELSIUS
                },
                MK_RESOURCES: {"temperature": ("0.1.85", "_attr_native_value")},
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "humidity",
                    "device_class": SensorDeviceClass.HUMIDITY,
                    "state_class": "measurement",
                    "unit_of_measurement": PERCENTAGE
                },
                MK_RESOURCES: {"humidity": ("0.2.85", "_attr_native_value")},
            }
        }
    ]
},
###人体传感器
{
    # 小米-人体移动传感器
    'lumi.sensor_motion.v1': ["Xiaomi", "Motion Sensor", "RTCGQ01LM"],
    'lumi.sensor_motion.v2': ["Xiaomi", "Motion Sensor", "RTCGQ01LM"],
    # 人体移动传感器
    'lumi.sensor_motion.aq2': ["Aqara", "Motion Sensor", "RTCGQ11LM"],
    'params': [
        {
            "binary_sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "motion",
                    "device_class": BinarySensorDeviceClass.MOTION
                },
                MK_RESOURCES: {
                    "motion": ("3.1.85", "_attr_native_value"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    "voltage": ("8.0.2008", "_attr_voltage")
                },
            }
        }
    ]
},
###高精度人体传感器
{
    # 高精度人体传感器
    'lumi.motion.agl04': ["Aqara", "Precision Motion Sensor", "RTCGQ13LM"],
    'params': [
        {
            "binary_sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "motion",
                    "device_class": BinarySensorDeviceClass.MOTION
                },
                MK_RESOURCES: {
                    "motion": ("3.1.85", "_attr_native_value"),
                    "detect_time": ("8.0.2115","_attr_detect_time"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    "voltage": ("8.0.2008", "_attr_voltage")
                },
            }
        }
    ]
},
###人体存在传感器
{
    # 人体存在
    'lumi.motion.ac01': ["Aqara", "Presence Sensor FP1", "RTCZCGQ11LM"],
    'params': [
        {
            "binary_sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "exist",
                    "device_class": BinarySensorDeviceClass.MOTION
                },
                MK_RESOURCES: {
                    "exist": ("4.1.85", "_attr_native_value"),
                    "monitor_type": ("3.51.85", "_attr_monitor_type"),
                    "direction_status": ("13.27.85", "_attr_direction_status"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi")
                },
            }
        }
    ]
},
###门窗传感器
{
    # 门窗传感器
    'lumi.sensor_magnet.v1': ["Xiaomi", "Door Sensor", "MCCGQ01LM"],
    'lumi.sensor_magnet.v2': ["Xiaomi", "Door Sensor", "MCCGQ01LM"],
    'lumi.sensor_magnet.aq2': ["Aqara", "Door Sensor", "MCCGQ11LM"],
    # 门窗传感器T1
    'lumi.magnet.agl02': ["Aqara", "Door Sensor T1", "MCCGQ12LM"],
    # 门窗传感器E1
    'lumi.magnet.acn001': ["Aqara", "Door Sensor E1", "MCCGQ14LM"],
    # 门窗传感器P1
    'lumi.magnet.ac01': ["Aqara", "Door Sensor P1", "MCCGQ13LM"],
    'params': [
        {
            "binary_sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "contact",
                    "device_class": CoverDeviceClass.DOOR
                },
                MK_RESOURCES: {
                    "status": ("3.1.85", "_attr_native_value"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    "voltage": ("8.0.2008", "_attr_voltage")
                },
            }
        }
    ]
},
###水浸传感器
{
    # 水浸传感器
    'lumi.sensor_wleak.aq1': ["Aqara", "Water Leak Sensor", "SJCGQ11LM"],
    'lumi.sensor_wleak.v1': ["Aqara", "Water Leak Sensor", ""],
    'lumi.flood.agl02': ["Aqara", "Water Leak Sensor T1", "SJCGQ12LM"],
    'lumi.flood.acn001': ["Aqara", "Water Leak Sensor E1", "SJCGQ13LM"],
    'params': [
        {
            "binary_sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "moisture",
                    "device_class": BinarySensorDeviceClass.MOISTURE
                },
                MK_RESOURCES: {
                    "moisture": ("3.1.85", "_attr_is_on"),
                    "zigbee_lqi": ("8.0.2007", "_attr_zigbee_lqi"),
                    "voltage": ("8.0.2008", "_attr_voltage")
                },
            }
        }
    ]
},
###烟雾传感器
{
    # Xiaomi 烟雾报警器
    'lumi.sensor_smoke.v1': ["Xiaomi", "Smoke Sensor", "JTYJ-GD-01LM/BW"],
    'lumi.sensor_smoke.acn03': ["Xiaomi", "Smoke Sensor", ""],
    'params': [
        {
            "binary_sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "smoke",
                    "device_class": BinarySensorDeviceClass.SMOKE
                },
                MK_RESOURCES: {
                    "smoke": ("13.1.85", "_attr_is_on")
                },
            }
        },
    ]
},
###############################门锁#############################################
{
    #P100门锁
    'aqara.lock.wbzac1': ["Aqara", "DoorLock P100", ""],
    'params': [
        {
            "binary_sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "contact",
                    "device_class": CoverDeviceClass.DOOR
                },
                MK_RESOURCES: {
                    "status": ("13.12.85", "_attr_native_value"),
                },
            }
        }, {
            "sensor": {
                MK_INIT_PARAMS: {
                    MK_HASS_NAME: "contact",
                    "device_class": "",
                    "state_class": "",
                    "unit_of_measurement": ""
                },
                MK_RESOURCES: {
                    "status": ("13.2.85", "_attr_native_value")
                },
            }
        }
    ]
}
]

##################################特殊设备######################################
SPECIAL_DEVICES_INFO = {
    # VRF空调控制器
    "lumi.airrtc.vrfegl01": {
        "toggle": {0: "on", 1: "off"},
        "hvac_mode": {
            0: "heat",
            1: "cool",
            2: "auto",
            3: "dry",
            4: "fan_only",
        },
        "fan_mode": {0: "low", 1: "middle", 2: "high", 3: "auto"},
        "swing_mode": {0: "horizontal", 1: "vertical", 2: "both"},
        "swing_toggle": {1: "off"},
    }
}
