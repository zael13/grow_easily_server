from grow_easily_server.domain.recipe import Recipe
from grow_easily_server.domain.module import Module, Hardware, PeriodicEvent, HWType
from grow_easily_server.serializers.decimal_serializer import DecimalEncoder


class RecipeEncoder(DecimalEncoder):
    def default(self, o):
        try:
            if isinstance(o, Recipe):
                to_serialize = {
                    'recipe_id': str(o.recipe_id),
                    'culture': o.culture,
                    'user_id': o.user_id,
                    'rating': o.rating,
                    'name': o.name,
                    'modules': o.modules
                }
            elif isinstance(o, Module):
                to_serialize = {
                    'module_id': str(o.module_id),
                    'name': o.name,
                    'trigger_id': o.trigger_id,
                    'hardware_id1': o.hardware_id1,
                    'value': str(o.value),
                }
            elif isinstance(o, Hardware):
                to_serialize = {
                    'recipe_id': str(o.code),
                    'name': o.name,
                    'hw_type': o.hw_type,
                    'pins': o.pins
                }
            elif isinstance(o, PeriodicEvent):
                to_serialize = {
                    'type': o.__class__.__name__,
                    'impact': o.hw_type,
                    'period': str(int(o.period.total_seconds())),
                    'culture': str(int(o.duration.total_seconds()))
                }
            elif isinstance(o, HWType):
                to_serialize = str(o.name)  # {'hw_type': str(o.name)}
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)
