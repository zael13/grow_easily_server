import json
from grow_easily_server.domain.device import Device
import decimal


class DeviceEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, Device):
                to_serialize = {
                    'deviceId': str(o.deviceId),
                    'userId': str(o.userId),
                    'recipeId': str(o.recipeId),
                    'name': o.name,
                    'startTime': o.startTime
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
