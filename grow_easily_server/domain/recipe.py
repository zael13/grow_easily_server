from grow_easily_server.shared.domain_model import DomainModel
from grow_easily_server.domain.module import Trigger, Controller, PeriodicEvent


class Recipe(object):

    def __init__(self, code, owner, name, rating, duration):
        self.code = code
        self.owner = owner
        self.duration = duration
        self.rating = rating
        self.name = name
        self.items = []

    @classmethod
    def from_dict(cls, adict):
        recipe = Recipe(code=adict['code'], owner=adict['owner'], name=adict['name'], rating=adict['rating'],
                        duration=adict['duration'])

        return recipe

    def to_dict(self):
        return {
            'code': self.code,
            'duration': self.duration,
            'owner': self.owner,
            'rating': self.rating,
            'name': self.name,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def add_item(self, item):
        if issubclass(type(item), Trigger):
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
