from grow_easily_server.domain.device import Device
from grow_easily_server.serializers.decimal_serializer import DecimalEncoder

class DeviceEncoder(DecimalEncoder):
    def default(self, o):
        try:
            if isinstance(o, Device):
                to_serialize = {
                    'device_id': str(o.device_id),
                    'user_id': str(o.user_id),
                    'name': o.name,
                    'start_time': o.start_time
                }
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)
