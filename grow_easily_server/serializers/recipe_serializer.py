import json
from grow_easily_server.domain.recipe import Recipe
from grow_easily_server.domain.module import Module, Hardware, PeriodicEvent, HWType


class RecipeEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, Recipe):
                to_serialize = {
                    'code': str(o.code),
                    'duration': o.duration,
                    'owner': o.owner,
                    'rating': o.rating,
                    'name': o.name,
                    'items': o.items
                }
            elif isinstance(o, Module):
                to_serialize = {
                    'code': str(o.code),
                    'name': o.name,
                    'trigger': o.trigger,
                    'hardware': o.hardware,
                    'data_type': str(o.data_type),
                }
            elif isinstance(o, Hardware):
                to_serialize = {
                    'code': str(o.code),
                    'name': o.name,
                    'hw_type': o.hw_type,
                    'pins': o.pins
                }
            elif isinstance(o, PeriodicEvent):
                to_serialize = {
                    'type': o.__class__.__name__,
                    'impact': o.hw_type,
                    'period': str(int(o.period.total_seconds())),
                    'duration': str(int(o.duration.total_seconds()))
                }
            elif isinstance(o, HWType):
                to_serialize = str(o.name)  # {'hw_type': str(o.name)}
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)
