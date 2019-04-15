from grow_easily_server.shared.domain_model import DomainModel
from grow_easily_server.domain.module import Module, Controller, PeriodicEvent


class Recipe(object):

    def __init__(self, code, owner, name, duration, rating, items=None):
        self.code = code
        self.owner = owner
        self.name = name
        self.duration = duration
        self.rating = rating
        self.items = []

        if items:
            for i in items:
                self.add_item(i)

    @classmethod
    def from_dict(cls, adict):
        recipe = Recipe(code=adict['code'],
                        owner=adict['owner'],
                        name=adict['name'],
                        duration=adict['duration'],
                        rating=adict['rating'],
                        items=adict['items'])

        return recipe

    def to_dict(self):
        return {
            'code': self.code,
            'duration': self.duration,
            'owner': self.owner,
            'rating': self.rating,
            'name': self.name,
            'items': ''.join(self.items),
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def add_item(self, item):
        if issubclass(type(item), Module):
            if not self.__is_duplicate_and_substituted(item):
                self.items.append(item)
        else:
            raise TypeError("new item should be passed as RecipeItem object")

    def __is_duplicate_and_substituted(self, item):
        if type(item.trigger) is Controller or type(item.trigger) is PeriodicEvent:
            for n, i in enumerate(self.items):
                if isinstance(i.hardware, type(item.hardware)) and \
                   item.hardware.hw_type is i.hardware.hw_type:
                    self.items[n] = item
                    return True

    def get_items(self):
        return self.items

    def generate(self):
        return str(self.items)


DomainModel.register(Recipe)
