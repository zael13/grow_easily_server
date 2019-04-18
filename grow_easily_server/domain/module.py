from datetime import datetime, timedelta, time
from enum import Enum


class Module:
    def __init__(self, module_id, recipe_id, name, value=None, delta=None):
        self.module_id = module_id
        self.recipe_id = recipe_id
        self.name = name
        self.value = value
        self.delta = delta

    @classmethod
    def from_dict(cls, adict):
        module = Module(module_id=adict['module_id'], recipe_id=adict['recipe_id'], name=adict['name'],
                        value=adict['value'] if ('value' in adict) else None,
                        delta=adict['delta'] if ('delta' in adict) else None)
        return module

    def to_dict(self):
        return {
            'module_id': self.module_id,
            'recipe_id': self.recipe_id,
            'name': self.name,
            'value': self.value,
            'delta': ''.join(self.delta),
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


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
        if type(duration) is not timedelta and duration != 0:
            raise TypeError("Duration should be passed as timedelta object or zero")
        self.duration = duration


class PeriodicEvent(Event):
    def __init__(self, item_type, period, duration=timedelta(seconds=0)):
        Event.__init__(self, item_type, duration)
        if type(period) is not timedelta:
            raise TypeError("period should be passed as timedelta object")
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
