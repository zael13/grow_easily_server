from grow_easily_server.shared.domain_model import DomainModel
from grow_easily_server.domain.RecipeItem import RecipeItem, Controller, PeriodicEvent


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
