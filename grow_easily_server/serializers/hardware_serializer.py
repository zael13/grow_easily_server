import json
from grow_easily_server.domain.hardware import Hardware
import decimal


class HardwareEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, Hardware):
                to_serialize = {
                    'hardware_id': str(o.hardware_id),
                    'module_id': str(o.module_id),
                    'user_id': str(o.user_id),
                    'name': o.name,
                    'hw_type': o.hw_type,
                    'pins': o.pins,
                    'value': o.value,
                    'delta': o.delta
                }
            elif isinstance(o, decimal.Decimal):
                if o % 1 == 0:
                    return int(o)
                else:
                    return float(o)
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)
