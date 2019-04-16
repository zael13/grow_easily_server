import json
from grow_easily_server.domain.hardware import Hardware
import decimal


class HardwareEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, Hardware):
                to_serialize = {
                    'hardwareId': str(o.hardwareId),
                    'moduleId': str(o.moduleId),
                    'userId': str(o.userId),
                    'name': o.name,
                    'hwType': o.hwType,
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
