from grow_easily_server.domain.trigger import Trigger
from grow_easily_server.serializers.decimal_serializer import DecimalEncoder


class TriggerEncoder(DecimalEncoder):
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
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)
