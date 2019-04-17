from grow_easily_server.shared.domain_model import DomainModel
from grow_easily_server.domain.module import Module, Controller, PeriodicEvent


class Recipe(object):

    def __init__(self, recipe_id, user_id, name, culture, rating, modules=None):
        self.recipe_id = recipe_id
        self.user_id = user_id
        self.name = name
        self.culture = culture
        self.rating = rating
        self.modules = modules

        # if modules:
        #     for i in modules:
        #         self.add_item(i)

    @classmethod
    def from_dict(cls, adict):
        recipe = Recipe(recipe_id=adict['recipe_id'],
                        user_id=adict['user_id'],
                        name=adict['name'],
                        culture=adict['culture'],
                        rating=adict['rating'],
                        modules=adict['modules'] if ('modules' in adict) else None)
        return recipe

    def to_dict(self):
        return {
            'recipe_id': self.recipe_id,
            'culture': self.culture,
            'user_id': self.user_id,
            'rating': self.rating,
            'name': self.name,
            'modules': ''.join(self.modules),
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def add_item(self, item):
        if issubclass(type(item), Module):
            if not self.__is_duplicate_and_substituted(item):
                self.modules.append(item)
        else:
            raise TypeError("new item should be passed as RecipeItem object")

    def __is_duplicate_and_substituted(self, item):
        if type(item.trigger_id) is Controller or type(item.trigger_id) is PeriodicEvent:
            for n, i in enumerate(self.modules):
                if isinstance(i.hardware_id1, type(item.hardware_id1)) and \
                   item.hardware_id1.hw_type is i.hardware_id1.hw_type:
                    self.modules[n] = item
                    return True

    def get_modules(self):
        return self.modules

    def generate(self):
        return str(self.modules)


DomainModel.register(Recipe)
