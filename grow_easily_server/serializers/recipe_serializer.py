from grow_easily_server.domain.recipe import Recipe
from grow_easily_server.domain.module import Module, Hardware, PeriodicEvent, HWType
from grow_easily_server.serializers.decimal_serializer import DecimalEncoder


class RecipeEncoder(DecimalEncoder):
    def default(self, o):
        try:
            if isinstance(o, Recipe):
                to_serialize = {
                    'recipe_id': str(o.recipe_id),
                    'device_id': o.device_id,
                    'name': o.name,
                    'culture': o.culture,
                    'rating': o.rating,
                    'duration': o.duration
                }
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)
