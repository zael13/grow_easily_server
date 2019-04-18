from grow_easily_server.shared.domain_model import DomainModel


class Device:
    def __init__(self, device_id, user_id, name, start_time):
        self.device_id = device_id
        self.user_id = user_id
        self.name = name
        self.start_time = start_time

    @classmethod
    def from_dict(cls, adict):
        device = Device(device_id=adict['device_id'], user_id=adict['user_id'], name=adict['name'],
                        start_time=adict['start_time'])
        return device

    def to_dict(self):
        return {
            'device_id': self.device_id,
            'user_id': self.user_id,
            'name': self.name,
            'start_time': self.start_time
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Device)
