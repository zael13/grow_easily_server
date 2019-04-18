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
                    'trigger_id': o.trigger_id,
                    'hardware_id1': o.hardware_id1,
                    'value': str(o.value),
                }
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)
