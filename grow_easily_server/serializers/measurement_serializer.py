import json
from grow_easily_server.domain.measurement import Measurement
import decimal


class MeasurementEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, Measurement):
                to_serialize = {
                    'measurementId': str(o.measurementId),
                    'deviceId': str(o.deviceId),
                    'timestamp': o.timestamp,
                    'temperature': o.temperature,
                    'moisture': o.moisture,
                    'phLevel': o.phLevel,
                    'height': o.height,
                    'waterLevel': o.waterLevel,
                    'imageId': str(o.imageId),
                    'exhaustHood': o.exhaustHood,
                    'light': o.light,
                    'fertilizer': o.fertilizer,
                    'custom1': o.custom1,
                    'custom2': o.custom2,
                    'custom3': o.custom3
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


