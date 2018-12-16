from homematicip.group import Group
from homematicip.base.enums import *

from typing import Iterable

class FunctionalChannel():
    """ this is the base class for the functional channels """

    def __init__(self):
        self.index = -1
        self.groupIndex = -1
        self.label = ""
        self.groupIndex = -1

        self.groups = Iterable[Group]

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        self.index = js["index"]
        self.groupIndex = js["groupIndex"]
        self.label = js["label"]

        self.groups = []
        for id in js["groups"]:
            for g in groups:
                if g.id == id:
                    self.groups.append(g)
                    break

class DeviceBaseChannel(FunctionalChannel):
    """ this is the representive of the DEVICE_BASE channel"""
    def __init__(self):
        super().__init__()
        self.unreach = None
        self.lowBat = None
        self.routerModuleSupported = False
        self.routerModuleEnabled = False
        self.rssiDeviceValue = 0
        self.rssiPeerValue = 0
        self.dutyCycle = False
        self.configPending = False

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.unreach = js["unreach"]
        self.lowBat = js["lowBat"]
        self.routerModuleSupported = js["routerModuleSupported"]
        self.routerModuleEnabled = js["routerModuleEnabled"]
        self.rssiDeviceValue = js["rssiDeviceValue"]
        self.rssiPeerValue = js["rssiPeerValue"]
        self.dutyCycle = js["dutyCycle"]
        self.configPending = js["configPending"]

class DeviceSabotageChannel(DeviceBaseChannel):
    """ this is the representive of the DEVICE_SABOTAGE channel"""
    def __init__(self):
        super().__init__()
        self.sabotage = False

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.sabotage = js["sabotage"]

class DeviceOperationLockChannel(DeviceBaseChannel):
    """ this is the representive of the DEVICE_OPERATIONLOCK channel"""
    def __init__(self):
        super().__init__()
        self.operationLockActive = False

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.operationLockActive = js["operationLockActive"]

class DeviceIncorrectPositionedChannel(DeviceBaseChannel):
    """ this is the representive of the DEVICE_INCORRECT_POSITIONED channel"""
    def __init__(self):
        super().__init__()
        self.incorrectPositioned = False

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.incorrectPositioned = js["incorrectPositioned"]

class WaterSensorChannel(FunctionalChannel):
    """ this is the representive of the WATER_SENSOR_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.acousticAlarmSignal = AcousticAlarmSignal.DISABLE_ACOUSTIC_SIGNAL
        self.acousticAlarmTiming = AcousticAlarmTiming.PERMANENT
        self.acousticWaterAlarmTrigger = WaterAlarmTrigger.NO_ALARM
        self.inAppWaterAlarmTrigger = WaterAlarmTrigger.NO_ALARM
        self.moistureDetected = False
        self.sirenWateralarmTrigger = WaterAlarmTrigger.NO_ALARM
        self.waterlevelDetected = False

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.acousticAlarmSignal = AcousticAlarmSignal.from_str(js["acousticAlarmSignal"])
        self.acousticAlarmTiming = AcousticAlarmTiming.from_str(js["acousticAlarmTiming"])
        self.acousticWaterAlarmTrigger = WaterAlarmTrigger.from_str(js["acousticWaterAlarmTrigger"])
        self.inAppWaterAlarmTrigger = WaterAlarmTrigger.from_str(js["inAppWaterAlarmTrigger"])
        self.moistureDetected = js["moistureDetected"]
        self.sirenWaterAlarmTrigger = WaterAlarmTrigger.from_str(js["sirenWaterAlarmTrigger"])
        self.waterlevelDetected = js["waterlevelDetected"]


class HeatingThermostatChannel(FunctionalChannel):
    """ this is the representive of the HEATING_THERMOSTAT_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.temperatureOffset = 0
        self.valvePosition = 0.0
        self.valveState = ValveState.ERROR_POSITION
        self.setPointTemperature = 0.0
        self.automaticValveAdaptionNeeded = False

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.temperatureOffset = js["temperatureOffset"]
        self.valvePosition = js["valvePosition"]
        self.valveState = ValveState.from_str(js["valveState"])
        self.setPointTemperature = js["setPointTemperature"]

class ShutterContactChannel(FunctionalChannel):
    """ this is the representive of the SHUTTER_CONTACT_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.windowState = WindowState.CLOSED
        self.eventDelay = None

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.windowState = WindowState.from_str(js["windowState"])
        self.eventDelay = js["eventDelay"]

class RotaryHandleChannel(ShutterContactChannel):
    """ this is the representive of the ROTARY_HANDLE_CHANNEL channel"""

class ClimateSensorChannel(FunctionalChannel):
    """ this is the representive of the CLIMATE_SENSOR_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.actualTemperature = 0
        self.humidity = 0

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.actualTemperature = js["actualTemperature"]
        self.humidity = js["humidity"]

class WallMountedThermostatWithoutDisplayChannel(ClimateSensorChannel):
    """ this is the representive of the WALL_MOUNTED_THERMOSTAT_WITHOUT_DISPLAY_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.temperatureOffset = 0

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.temperatureOffset = js["temperatureOffset"]

class WallMountedThermostatProChannel(WallMountedThermostatWithoutDisplayChannel):
    """ this is the representive of the WALL_MOUNTED_THERMOSTAT_PRO_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.display = ClimateControlDisplay.ACTUAL
        self.setPointTemperature = 0

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.setPointTemperature = js["setPointTemperature"]
        self.display = ClimateControlDisplay.from_str(js["display"])

class SmokeDetectorChannel(FunctionalChannel):
    """ this is the representive of the SMOKE_DETECTOR_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.smokeDetectorAlarmType = SmokeDetectorAlarmType.IDLE_OFF

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.smokeDetectorAlarmType = SmokeDetectorAlarmType.from_str(js["smokeDetectorAlarmType"])



class SwitchChannel(FunctionalChannel):
    """ this is the representive of the SWITCH_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.on = False
        self.profileMode = None
        self.userDesiredProfileMode = None

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.on = js["on"]
        self.profileMode = js["profileMode"]
        self.userDesiredProfileMode = js["userDesiredProfileMode"]



class SwitchMeasuringChannel(SwitchChannel):
    """ this is the representive of the SWITCH_MEASURING_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.energyCounter = 0
        self.currentPowerConsumption = 0

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.energyCounter = js["energyCounter"]
        self.currentPowerConsumption = js["currentPowerConsumption"]

class DeviceGlobalPumpControlChannel(FunctionalChannel):
    """ this is the representive of the DEVICE_GLOBAL_PUMP_CONTROL channel"""
    def __init__(self):
        super().__init__()
        self.globalPumpControl = None
        self.heatingValveType = HeatingValveType.NORMALLY_CLOSE

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.globalPumpControl = js["globalPumpControl"]
        self.heatingValveType = HeatingValveType.from_str(js["heatingValveType"])


class MotionDetectionChannel(FunctionalChannel):
    """ this is the representive of the MOTION_DETECTION_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.currentIllumination = None
        self.motionDetected = None
        self.illumination = None
        self.motionBufferActive = False
        self.motionDetected = False
        self.motionDetectionSendInterval = MotionDetectionSendInterval.SECONDS_30
        self.numberOfBrightnessMeasurements = 0

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.motionDetected = js["motionDetected"]
        self.illumination = js["illumination"]
        self.motionBufferActive = js["motionBufferActive"]
        self.motionDetected = js["motionDetected"]
        self.motionDetectionSendInterval = MotionDetectionSendInterval.from_str(js["motionDetectionSendInterval"])
        self.numberOfBrightnessMeasurements = js["numberOfBrightnessMeasurements"]
        self.currentIllumination = js["currentIllumination"]


class PresenceDetectionChannel(FunctionalChannel):
    """ this is the representive of the PRESENCE_DETECTION_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.presenceDetected = False
        self.illumination = 0

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.presenceDetected = js["presenceDetected"]
        self.illumination = js["illumination"]

class ShutterChannel(FunctionalChannel):
    """ this is the representive of the SHUTTER_CHANNEL channel"""
    def __init__(self):
        super().__init__()
        self.shutterLevel = None
        self.bottomToTopReferenceTime = None
        self.topToBottomReferenceTime = None

    def from_json(self, js, groups: Iterable[Group]):
        """ this function will load the functional channel object 
        from a json object and the given groups """
        super().from_json(js,groups)
        self.shutterLevel = js["shutterLevel"]
        self.bottomToTopReferenceTime = js["bottomToTopReferenceTime"]
        self.topToBottomReferenceTime = js["topToBottomReferenceTime"]