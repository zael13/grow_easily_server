from grow_easily_server.domain.hardware import Hardware
from grow_easily_server.serializers.decimal_serializer import DecimalEncoder


class HardwareEncoder(DecimalEncoder):
    def default(self, o):
        try:
            if isinstance(o, Hardware):
                to_serialize = {
                    'hardware_id': str(o.hardware_id),
                    'module_id': str(o.module_id),
                    'name': o.name,
                    'hw_type': o.hw_type,
                    'pins': o.pins,
                    'value': o.value,
                    'delta': o.delta
                }
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)
