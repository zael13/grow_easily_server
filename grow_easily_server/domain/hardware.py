from enum import Enum
from grow_easily_server.shared.domain_model import DomainModel

try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    import sys
    import fake_rpi
    sys.modules['RPi'] = fake_rpi.RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO
    import RPi.GPIO as GPIO


class HWType(Enum):
    HTTP_SERVER = 0
    DIGITAL_WRITER = 1
    DIGITAL_READER = 2
    ANALOG_READER = 3
    DHT_TEMPERATURE = 4
    DHT_HUMIDITY = 5
    NONE = 15


class Hardware:
    HW_ON = '1'
    HW_OFF = '0'

    def __init__(self, hardware_id, name, hw_type, pins=None, value=None, delta=None):
        self.hardware_id = hardware_id
        self.name = name
        self.hw_type = hw_type
        self.pins = pins
        self.value = value
        self.delta = delta


    @classmethod
    def from_dict(cls, adict):
        hardware = Hardware(hardware_id=adict['hardware_id'],
                            name=adict['name'], hw_type=adict['hw_type'],
                            pins=adict['pins'] if ('pins' in adict) else [],
                            value=adict['value'] if ('value' in adict) else None,
                            delta=adict['delta'] if ('delta' in adict) else None)
        return hardware

    def to_dict(self):
        return {
            'hardware_id': self.hardware_id,
            'name': self.name,
            'hw_type': self.hw_type,
            'pins': self.pins,
            'value': self.value,
            'delta': self.delta
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def write(self, msg):
        raise NotImplementedError('You need to define an on method!')

    def read(self):
        raise NotImplementedError('You need to define an off method!')

    @staticmethod
    def factory(hardware_id, name, hw_type, pins=None, value=None, delta=None):
        if hw_type == HWType.HTTP_SERVER:
            return HttpServer(hardware_id, name, hw_type, pins, value, delta)
        elif hw_type == HWType.DIGITAL_WRITER:
            return DigitalWriter(hardware_id, name, hw_type, pins)
        elif hw_type == HWType.DIGITAL_READER:
            return DigitalReader(hardware_id, name, hw_type, pins, value, delta)
        elif hw_type == HWType.ANALOG_READER:
            return AnalogReader(hardware_id, name, hw_type, pins, value, delta)
        elif hw_type == HWType.DHT_TEMPERATURE or hw_type == HWType.DHT_HUMIDITY:
            return Dht(hardware_id, name, hw_type, pins, value, delta)
        else:
            raise ValueError(hw_type)


class HttpServer(Hardware):
    def __init__(self, hardware_id, name, hw_type, pins=None, value=None, delta=None):
        super().__init__(hardware_id, name, hw_type, pins, value, delta)


class DigitalWriter(Hardware):
    def __init__(self, hardware_id, name, hw_type, pins):
        super().__init__(hardware_id, name, hw_type, pins)
        if GPIO.getmode() != GPIO.BCM:
            GPIO.setmode(GPIO.BCM)
        if pins and len(pins) == 1:
            GPIO.setup(pins[0], GPIO.OUT)
            GPIO.setup(self.pins[0], GPIO.OUT, initial=int(Hardware.HW_OFF))
            self.value = Hardware.HW_OFF
        else:
            raise ValueError(pins)

    def write(self, msg):
        if msg is Hardware.HW_ON or msg is Hardware.HW_OFF:
            GPIO.output(self.pins[0], int(msg))
            self.value = msg
        else:
            raise ValueError(msg)

    def read(self):
        return self.value


class DigitalReader(Hardware):
    def __init__(self, hardware_id, name, hw_type, pins=None, value=None, delta=None):
        super().__init__(hardware_id, name, hw_type, pins, value, delta)


class AnalogReader(Hardware):
    def __init__(self, hardware_id, name, hw_type, pins=None, value=None, delta=None):
        super().__init__(hardware_id, name, hw_type, pins, value, delta)


class Dht(Hardware):
    def __init__(self, hardware_id, name, hw_type, pins=None, value=None, delta=None):
        super().__init__(hardware_id, name, hw_type, pins, value, delta)


DomainModel.register(Hardware)
