import uuid
from datetime import datetime
from grow_easily_server.domain.measurement import Measurement

measurementId = uuid.uuid4()
deviceId = uuid.uuid4()
image_id = uuid.uuid4()
TIMESTAMP = datetime(2007, 12, 5, 22, 30).timestamp()


def test_measurement_model_init():
    measurement = Measurement(measurementId, deviceId, TIMESTAMP,
                              temperature=22.3,
                              moisture=68.2,
                              ph_level=6.5,
                              height=32.8,
                              water_level=0.2,
                              image_id=image_id,
                              exhaust_hood=True,
                              light=True,
                              fertilizer=False,
                              custom1=22.1,
                              custom2="test_val",
                              custom3=None)

    assert measurement.measurementId == measurementId
    assert measurement.deviceId == deviceId
    assert measurement.timestamp == TIMESTAMP
    assert measurement.temperature == 22.3
    assert measurement.moisture == 68.2
    assert measurement.phLevel == 6.5
    assert measurement.height == 32.8
    assert measurement.waterLevel == 0.2
    assert measurement.imageId == image_id
    assert measurement.exhaustHood is True
    assert measurement.light is True
    assert measurement.fertilizer is False
    assert measurement.custom1 == 22.1
    assert measurement.custom2 == "test_val"
    assert measurement.custom3 is None


def test_measurement_model_from_dict():
    measurement = Measurement.from_dict(
        {
            'measurementId': measurementId,
            'deviceId': deviceId,
            'timestamp': TIMESTAMP,
            'temperature': 22.3,
            'moisture': 68.2,
            'phLevel': 6.5,
            'height': 32.8,
            'waterLevel': 0.2,
            'imageId': image_id,
            'exhaustHood': True,
            'light': True,
            'fertilizer': False,
            'custom1': 22.1,
            'custom2': 'test_val',
            'custom3': None
        }
    )

    assert measurement.measurementId == measurementId
    assert measurement.deviceId == deviceId
    assert measurement.timestamp == TIMESTAMP
    assert measurement.temperature == 22.3
    assert measurement.moisture == 68.2
    assert measurement.phLevel == 6.5
    assert measurement.height == 32.8
    assert measurement.waterLevel == 0.2
    assert measurement.imageId == image_id
    assert measurement.exhaustHood is True
    assert measurement.light is True
    assert measurement.fertilizer is False
    assert measurement.custom1 == 22.1
    assert measurement.custom2 == "test_val"
    assert measurement.custom3 is None


def test_measurement_model_to_dict():
    measurement_dict = {
        'measurementId': measurementId,
        'deviceId': deviceId,
        'timestamp': TIMESTAMP,
        'temperature': 22.3,
        'moisture': 68.2,
        'phLevel': 6.5,
        'height': 32.8,
        'waterLevel': 0.2,
        'imageId': image_id,
        'exhaustHood': True,
        'light': True,
        'fertilizer': False,
        'custom1': 22.1,
        'custom2': 'test_val',
        'custom3': None
    }

    measurement = Measurement.from_dict(measurement_dict)

    assert measurement.to_dict() == measurement_dict


def test_measurement_model_comparison():
    measurement_dict = {
        'measurementId': measurementId,
        'deviceId': deviceId,
        'timestamp': TIMESTAMP,
        'temperature': 22.3,
        'moisture': 68.2,
        'phLevel': 6.5,
        'height': 32.8,
        'waterLevel': 0.2,
        'imageId': image_id,
        'exhaustHood': True,
        'light': True,
        'fertilizer': False,
        'custom1': 22.1,
        'custom2': 'test_val',
        'custom3': None
    }

    measurement1 = Measurement.from_dict(measurement_dict)
    measurement2 = Measurement.from_dict(measurement_dict)

    assert measurement1 == measurement2


def test_measurement_model_from_partial_dict():
    measurementId = uuid.uuid4()
    measurement = Measurement.from_dict(
        {
            'measurementId': measurementId,
            'deviceId': deviceId,
            'timestamp': TIMESTAMP,
            'temperature': None,
            'moisture': None,
            'phLevel': None,
            'height': None,
            'waterLevel': None,
            'imageId': None,
            'exhaustHood': None,
            'light': None,
            'fertilizer': None,
            'custom1': None,
            'custom2': None,
            'custom1': None,
        }
    )

    assert measurement.measurementId == measurementId
    assert measurement.deviceId == deviceId
    assert measurement.timestamp == TIMESTAMP
    assert measurement.temperature is None
    assert measurement.moisture is None
    assert measurement.phLevel is None
    assert measurement.height is None
    assert measurement.waterLevel is None
    assert measurement.imageId is None
    assert measurement.exhaustHood is None
    assert measurement.light is None
    assert measurement.fertilizer is None
    assert measurement.custom1 is None
    assert measurement.custom2 is None
    assert measurement.custom3 is None
