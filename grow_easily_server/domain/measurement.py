from grow_easily_server.shared.domain_model import DomainModel


class Measurement:
    def __init__(self,
                 measurement_id,
                 device_id,
                 timestamp,
                 temperature=None,
                 moisture=None,
                 ph_level=None,
                 height=None,
                 water_level=None,
                 image_id=None,
                 heater=None,
                 exhaust_hood=None,
                 light=None,
                 fertilizer=None,
                 custom1=None,
                 custom2=None,
                 custom3=None
    ):
        self.measurementId = measurement_id
        self.deviceId = device_id
        self.timestamp = timestamp
        self.temperature = temperature
        self.moisture = moisture
        self.phLevel = ph_level
        self.height = height
        self.waterLevel = water_level
        self.imageId = image_id
        self.heater = heater
        self.exhaustHood = exhaust_hood
        self.light = light
        self.fertilizer = fertilizer
        self.custom1 = custom1
        self.custom2 = custom2
        self.custom3 = custom3

    @classmethod
    def from_dict(cls, adict):
        measurement = Measurement(measurement_id=adict['measurementId'],
                                  device_id=adict['deviceId'],
                                  timestamp=adict['timestamp'],
                                  temperature=adict['temperature'] if ('temperature' in adict) else None,
                                  moisture=adict['moisture'] if ('moisture' in adict) else None,
                                  ph_level=adict['phLevel'] if ('phLevel' in adict) else None,
                                  height=adict['height'] if ('height' in adict) else None,
                                  water_level=adict['waterLevel'] if ('waterLevel' in adict) else None,
                                  image_id=adict['imageId'] if ('imageId' in adict) else None,
                                  exhaust_hood=adict['exhaustHood'] if ('exhaustHood' in adict) else None,
                                  light=adict['light'] if ('light' in adict) else None,
                                  fertilizer=adict['fertilizer'] if ('fertilizer' in adict) else None,
                                  custom1=adict['custom1'] if ('custom1' in adict) else None,
                                  custom2=adict['custom2'] if ('custom2' in adict) else None,
                                  custom3=adict['custom3'] if ('custom3' in adict) else None
                                  )
        return measurement

    def to_dict(self):
        return {
            'measurementId': self.measurementId,
            'deviceId': self.deviceId,
            'timestamp': self.timestamp,
            'temperature': self.temperature,
            'moisture': self.moisture,
            'phLevel': self.phLevel,
            'height': self.height,
            'waterLevel': self.waterLevel,
            'imageId': self.imageId,
            'exhaustHood': self.exhaustHood,
            'light': self.light,
            'fertilizer': self.fertilizer,
            'custom1': self.custom1,
            'custom2': self.custom2,
            'custom3': self.custom3
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Measurement)
