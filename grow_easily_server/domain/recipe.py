from grow_easily_server.shared.domain_model import DomainModel

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
    def __init__(self, hw_type, name='empty name', data_type=type(str)):
        self.hw_type = hw_type
        self.name = name
        self.data_type = data_type


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


class Recipe(object):

    def __init__(self, code, duration, price, rating, longitude):
        self.code = code
        self.duration = duration
        self.price = price
        self.rating = rating
        self.longitude = longitude
        self.items = []

    @classmethod
    def from_dict(cls, adict):
        recipe = Recipe(
            code=adict['code'],
            duration=adict['duration'],
            price=adict['price'],
            rating=adict['rating'],
            longitude=adict['longitude'],
        )

        return recipe

    def to_dict(self):
        return {
            'code': self.code,
            'duration': self.duration,
            'price': self.price,
            'rating': self.rating,
            'longitude': self.longitude,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def add_item(self, item):
        if issubclass(type(item), RecipeItem):
            if not self.__is_duplicate_and_substituted(item) and \
                    not self.__is_such_controller_exist(item):
                self.items.append(item)
        else:
            raise TypeError("new item should be passed as RecipeItem object")

    def __is_duplicate_and_substituted(self, item):
        if type(item) is Controller or type(item) is PeriodicEvent:
            for n, i in enumerate(self.items):
                if type(i) is type(item) and item.hw_type is i.hw_type:
                    self.items[n] = item
                    return True

    def __is_such_controller_exist(self, item):
        for n, i in enumerate(self.items):
            if item.hw_type is i.hw_type and type(i) is Controller:
                return True

    def get_items(self):
        return self.items

    def generate(self):
        return str(self.items)


DomainModel.register(Recipe)
