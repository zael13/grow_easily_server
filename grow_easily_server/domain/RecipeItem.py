from datetime import datetime, time
from enum import Enum


class HWType(Enum):
    HTTP_SERVER = 0
    DIGITAL_WRITER = 1
    DIGITAL_READER = 2
    ANALOG_READER = 3
    DHT_TEMPERATURE = 4
    DHT_HUMIDITY = 5
    NONE = 15


class RecipeItem:
    def __init__(self, hw_type=None, trigger_type=None, name='empty name', data_type=type(str), hardware=None):
        self.name = name
        self.data_type = data_type
        self.trigger_type = trigger_type
        self.hardware = hardware
        self.hw_type = hw_type


class Hardware:
    def __init__(self, code, name, hw_type, pins=None):
        if type(name) is not str:
            raise TypeError("Module name should be only String type")
        elif not len(name):
            raise ValueError("Module name should be empty")
        elif type(hw_type) is not HWType:
            raise TypeError("Hardware should be HWType type object")
        elif pins is not None and not isinstance(pins, list):
            raise TypeError("Pin should be List type")
        for pin in pins:
            if pin < 0 or pin > 16:
                raise ValueError("Pin should not be less than zero and greater than 16")

        self.code = code
        self.name = name
        self.hw_type = hw_type
        self.pins = pins


class Controller(RecipeItem):
    def __init__(self, item_type, value):
        RecipeItem.__init__(self, item_type)
        self.value = value


class Event(RecipeItem):
    def __init__(self, item_type, duration):
        RecipeItem.__init__(self, item_type)
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
