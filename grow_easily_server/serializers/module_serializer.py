from grow_easily_server.domain.recipe import Recipe
from grow_easily_server.domain.module import Module, Hardware, PeriodicEvent, HWType
from grow_easily_server.serializers.decimal_serializer import DecimalEncoder


class ModuleEncoder(DecimalEncoder):
    def default(self, o):
        try:
            if isinstance(o, Module):
                to_serialize = {
                    'module_id': str(o.module_id),
                    'name': o.name,
                    'recipe_id': o.recipe_id,
                    'value': str(o.value),
                    'delta': o.delta,
                }
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)