import json
from grow_easily_server.domain.measurement import Measurement
import decimal


class MeasurementEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, Measurement):
                to_serialize = {
                    'measurement_id': str(o.measurement_id),
                    'device_id': str(o.device_id),
                    'timestamp': o.timestamp,
                    'temperature': o.temperature,
                    'moisture': o.moisture,
                    'ph_level': o.ph_level,
                    'height': o.height,
                    'water_level': o.water_level,
                    'image_id': str(o.image_id),
                    'exhaust_hood': o.exhaust_hood,
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


