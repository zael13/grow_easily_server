from datetime import datetime, time
from enum import Enum


class Module:
    def __init__(self, code, name, trigger, hardware, data_type=type(str)):
        self.__check_input_values(name, trigger, hardware, data_type)

        self.code = code
        self.name = name
        self.trigger = trigger
        self.hardware = hardware
        self.data_type = data_type


    @staticmethod
    def __check_input_values(name, trigger, hardware, data_type):
        if type(name) is not str:
            raise TypeError("Module name should be only String type")
        elif not len(name):
            raise ValueError("Module name should not be empty")
        elif not isinstance(trigger, Trigger):
            raise TypeError("Trigger argument should be Trigger instance object")
        elif not isinstance(hardware, Hardware):
            raise TypeError("Hardware argument should be Hardware instance object")
        elif type(data_type) is not type:
            raise TypeError("Data_type argument should be type object")


class ImpactType(Enum):
    LIGHTING = 0
    WATERING = 1
    HEATING = 2
    BLOWING = 3
    FERTILIZING = 4
    PH_METER = 5
    WEIGHTING = 6
    COMMUNICATING = 7
    STORING = 8


class Trigger:
    def __init__(self, hw_type=None):
        self.hw_type = hw_type


class Controller(Trigger):
    def __init__(self, item_type, value):
        Trigger.__init__(self, item_type)
        self.value = value


class Event(Trigger):
    def __init__(self, item_type, duration):
        Trigger.__init__(self, item_type)
        if type(duration) is not time and duration != 0:
            raise TypeError("Duration should be passed as time object or zero")
        self.duration = duration


class PeriodicEvent(Event):
    def __init__(self, item_type, period, duration=0):
        Event.__init__(self, item_type, duration)
        if type(period) is not time:
            raise TypeError("period should be passed as time object")
        self.period = period


class DailyEvent(Event):
    def __init__(self, item_type, day_time, duration=0):
        Event.__init__(self, item_type, duration)
        if type(day_time) is not time:
            raise TypeError("day_time should be passed as time object")
        self.day_time = day_time


class CalendarEvent(Event):
    def __init__(self, item_type, calendar_time, duration=0):
        Event.__init__(self, item_type, duration)
        if type(calendar_time) is not datetime:
            raise TypeError("calendar_time should be passed as datetime object")
        self.calendar_time = calendar_time


class HWType(Enum):
    HTTP_SERVER = 0
    DIGITAL_WRITER = 1
    DIGITAL_READER = 2
    ANALOG_READER = 3
    DHT_TEMPERATURE = 4
    DHT_HUMIDITY = 5
    NONE = 15


class Hardware:
    def __init__(self, code, name, hw_type, pins=None):
        self.__check_input_values(name, hw_type, pins)

        self.code = code
        self.name = name
        self.hw_type = hw_type
        self.pins = pins

    @staticmethod
    def __check_input_values(name, hw_type, pins):
        if type(name) is not str:
            raise TypeError("Module name should be only String type")
        elif not len(name):
            raise ValueError("Module name should not be empty")
        elif not isinstance(hw_type, HWType):
            raise TypeError("Hardware should be HWType type object")
        elif pins is not None and not isinstance(pins, list):
            raise TypeError("Pin should be List type")
        for pin in pins:
            if pin < 0 or pin > 16:
                raise ValueError("Pin should not be less than zero and greater than 16")