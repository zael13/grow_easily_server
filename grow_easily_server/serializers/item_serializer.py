from grow_easily_server.serializers.user_serializer import UserEncoder
from grow_easily_server.serializers.device_serializer import DeviceEncoder
from grow_easily_server.serializers.recipe_serializer import RecipeEncoder
from grow_easily_server.serializers.hardware_serializer import HardwareEncoder
from grow_easily_server.serializers.trigger_serializer import TriggerEncoder
from grow_easily_server.serializers.measurement_serializer import MeasurementEncoder
from grow_easily_server.serializers.module_serializer import ModuleEncoder


class ItemEncoder(UserEncoder, DeviceEncoder, RecipeEncoder, ModuleEncoder,
                  HardwareEncoder, TriggerEncoder, MeasurementEncoder):
    def default(self, o):
        try:
            return super().default(o)
        except AttributeError:
            print(AttributeError)
