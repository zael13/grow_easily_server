from grow_easily_server.shared.domain_model import DomainModel


class Trigger:
    def __init__(self, trigger_id, module_id, name, start_time=None, end_time=None, delta=None):
        self.trigger_id = trigger_id
        self.module_id = module_id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.delta = delta


    @classmethod
    def from_dict(cls, adict):
        trigger = Trigger(trigger_id=adict['trigger_id'], module_id=adict['module_id'], name=adict['name'],
                          start_time=adict['start_time'] if ('start_time' in adict) else None,
                          end_time=adict['end_time'] if ('end_time' in adict) else None,
                          delta=adict['delta'] if ('delta' in adict) else None)
        return trigger

    def to_dict(self):
        return {
            'trigger_id': self.trigger_id,
            'module_id': self.module_id,
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'delta': self.delta
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Trigger)
