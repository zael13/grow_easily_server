import json
from grow_easily_server.domain.device import Device
import decimal


class DeviceEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, Device):
                to_serialize = {
                    'device_id': str(o.device_id),
                    'user_id': str(o.user_id),
                    'recipe_id': str(o.recipe_id),
                    'name': o.name,
                    'start_time': o.start_time
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
