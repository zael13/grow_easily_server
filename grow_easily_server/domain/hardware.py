from grow_easily_server.shared.domain_model import DomainModel


class Hardware:
    def __init__(self, hardware_id, module_id, user_id, name, hw_type, pins=None, value=None, delta=None):
        self.hardwareId = hardware_id
        self.moduleId = module_id
        self.userId = user_id
        self.name = name
        self.hwType = hw_type
        self.pins = pins
        self.value = value
        self.delta = delta


    @classmethod
    def from_dict(cls, adict):
        hardware = Hardware(hardware_id=adict['hardwareId'], module_id=adict['moduleId'],
                            user_id=adict['userId'], name=adict['name'], hw_type=adict['hwType'],
                            pins=adict['pins'] if ('pins' in adict) else [],
                            value=adict['value'] if ('value' in adict) else None,
                            delta=adict['delta'] if ('delta' in adict) else None)
        return hardware

    def to_dict(self):
        return {
            'hardwareId': self.hardwareId,
            'moduleId': self.moduleId,
            'userId': self.userId,
            'name': self.name,
            'hwType': self.hwType,
            'pins': self.pins,
            'value': self.value,
            'delta': self.delta
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Hardware)
