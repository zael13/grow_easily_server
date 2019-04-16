from grow_easily_server.shared.domain_model import DomainModel


class Device:
    def __init__(self, device_id, user_id, recipe_id, name, start_time):
        self.deviceId = device_id
        self.userId = user_id
        self.recipeId = recipe_id
        self.name = name
        self.startTime = start_time

    @classmethod
    def from_dict(cls, adict):
        device = Device(device_id=adict['deviceId'], user_id=adict['userId'],
                        recipe_id=adict['recipeId'], name=adict['name'],
                        start_time=adict['startTime'])
        return device

    def to_dict(self):
        return {
            'deviceId': self.deviceId,
            'userId': self.userId,
            'recipeId': self.recipeId,
            'name': self.name,
            'startTime': self.startTime
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Device)
