from grow_easily_server.shared.domain_model import DomainModel


class Trigger:
    def __init__(self, trigger_id, name, start_time=None, end_time=None, delta=None):
        self.triggerId = trigger_id
        self.name = name
        self.startTime = start_time
        self.endTime = end_time
        self.delta = delta


    @classmethod
    def from_dict(cls, adict):
        trigger = Trigger(trigger_id=adict['triggerId'], name=adict['name'],
                          start_time=adict['startTime'] if ('startTime' in adict) else None,
                          end_time=adict['endTime'] if ('endTime' in adict) else None,
                          delta=adict['delta'] if ('delta' in adict) else None)
        return trigger

    def to_dict(self):
        return {
            'triggerId': self.triggerId,
            'name': self.name,
            'startTime': self.startTime,
            'endTime': self.endTime,
            'delta': self.delta
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Trigger)
