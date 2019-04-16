import json
from grow_easily_server.domain.trigger import Trigger
import decimal


class TriggerEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, Trigger):
                to_serialize = {
                    'trigger_id': str(o.trigger_id),
                    'module_id': str(o.module_id),
                    'name': o.name,
                    'start_time': o.start_time,
                    'end_time': o.end_time,
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
