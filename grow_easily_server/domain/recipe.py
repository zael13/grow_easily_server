from grow_easily_server.shared.domain_model import DomainModel
from grow_easily_server.domain.module import Module, Controller, PeriodicEvent


class Recipe(object):

    def __init__(self, recipe_id, device_id, name, culture, rating=None, duration=None):
        self.recipe_id = recipe_id
        self.device_id = device_id
        self.name = name
        self.culture = culture
        self.rating = rating
        self.duration = duration

    @classmethod
    def from_dict(cls, adict):
        recipe = Recipe(recipe_id=adict['recipe_id'],
                        device_id=adict['device_id'],
                        name=adict['name'],
                        culture=adict['culture'],
                        rating=adict['rating'] if ('rating' in adict) else None,
                        duration=adict['duration'] if ('duration' in adict) else None)
        return recipe

    def to_dict(self):
        return {
            'recipe_id': self.recipe_id,
            'device_id': self.device_id,
            'name': self.name,
            'culture': self.culture,
            'rating': self.rating,
            'duration': self.duration,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Recipe)
