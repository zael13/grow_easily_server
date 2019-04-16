from grow_easily_server.shared.domain_model import DomainModel


class Hardware:
    def __init__(self, hardware_id, module_id, user_id, name, hw_type, pins=None, value=None, delta=None):
        self.hardware_id = hardware_id
        self.module_id = module_id
        self.user_id = user_id
        self.name = name
        self.hw_type = hw_type
        self.pins = pins
        self.value = value
        self.delta = delta


    @classmethod
    def from_dict(cls, adict):
        hardware = Hardware(hardware_id=adict['hardware_id'], module_id=adict['module_id'],
                            user_id=adict['user_id'], name=adict['name'], hw_type=adict['hw_type'],
                            pins=adict['pins'] if ('pins' in adict) else [],
                            value=adict['value'] if ('value' in adict) else None,
                            delta=adict['delta'] if ('delta' in adict) else None)
        return hardware

    def to_dict(self):
        return {
            'hardware_id': self.hardware_id,
            'module_id': self.module_id,
            'user_id': self.user_id,
            'name': self.name,
            'hw_type': self.hw_type,
            'pins': self.pins,
            'value': self.value,
            'delta': self.delta
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Hardware)
