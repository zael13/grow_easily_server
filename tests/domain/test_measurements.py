import uuid
from datetime import datetime
from grow_easily_server.domain.measurement import Measurement

measurement_id = uuid.uuid4()
device_id = uuid.uuid4()
image_id = uuid.uuid4()
TIMESTAMP = datetime(2007, 12, 5, 22, 30).timestamp()


def test_measurement_model_init():
    measurement = Measurement(measurement_id, device_id, TIMESTAMP,
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

    assert measurement.measurement_id == measurement_id
    assert measurement.device_id == device_id
    assert measurement.timestamp == TIMESTAMP
    assert measurement.temperature == 22.3
    assert measurement.moisture == 68.2
    assert measurement.ph_level == 6.5
    assert measurement.height == 32.8
    assert measurement.water_level == 0.2
    assert measurement.image_id == image_id
    assert measurement.exhaust_hood is True
    assert measurement.light is True
    assert measurement.fertilizer is False
    assert measurement.custom1 == 22.1
    assert measurement.custom2 == "test_val"
    assert measurement.custom3 is None


def test_measurement_model_from_dict():
    measurement = Measurement.from_dict(
        {
            'measurement_id': measurement_id,
            'device_id': device_id,
            'timestamp': TIMESTAMP,
            'temperature': 22.3,
            'moisture': 68.2,
            'ph_level': 6.5,
            'height': 32.8,
            'water_level': 0.2,
            'image_id': image_id,
            'exhaust_hood': True,
            'light': True,
            'fertilizer': False,
            'custom1': 22.1,
            'custom2': 'test_val',
            'custom3': None
        }
    )

    assert measurement.measurement_id == measurement_id
    assert measurement.device_id == device_id
    assert measurement.timestamp == TIMESTAMP
    assert measurement.temperature == 22.3
    assert measurement.moisture == 68.2
    assert measurement.ph_level == 6.5
    assert measurement.height == 32.8
    assert measurement.water_level == 0.2
    assert measurement.image_id == image_id
    assert measurement.exhaust_hood is True
    assert measurement.light is True
    assert measurement.fertilizer is False
    assert measurement.custom1 == 22.1
    assert measurement.custom2 == "test_val"
    assert measurement.custom3 is None


def test_measurement_model_to_dict():
    measurement_dict = {
        'measurement_id': measurement_id,
        'device_id': device_id,
        'timestamp': TIMESTAMP,
        'temperature': 22.3,
        'moisture': 68.2,
        'ph_level': 6.5,
        'height': 32.8,
        'water_level': 0.2,
        'image_id': image_id,
        'exhaust_hood': True,
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
        'measurement_id': measurement_id,
        'device_id': device_id,
        'timestamp': TIMESTAMP,
        'temperature': 22.3,
        'moisture': 68.2,
        'ph_level': 6.5,
        'height': 32.8,
        'water_level': 0.2,
        'image_id': image_id,
        'exhaust_hood': True,
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
    measurement_id = uuid.uuid4()
    measurement = Measurement.from_dict(
        {
            'measurement_id': measurement_id,
            'device_id': device_id,
            'timestamp': TIMESTAMP,
            'temperature': None,
            'moisture': None,
            'ph_level': None,
            'height': None,
            'water_level': None,
            'image_id': None,
            'exhaust_hood': None,
            'light': None,
            'fertilizer': None,
            'custom1': None,
            'custom2': None,
            'custom1': None,
        }
    )

    assert measurement.measurement_id == measurement_id
    assert measurement.device_id == device_id
    assert measurement.timestamp == TIMESTAMP
    assert measurement.temperature is None
    assert measurement.moisture is None
    assert measurement.ph_level is None
    assert measurement.height is None
    assert measurement.water_level is None
    assert measurement.image_id is None
    assert measurement.exhaust_hood is None
    assert measurement.light is None
    assert measurement.fertilizer is None
    assert measurement.custom1 is None
    assert measurement.custom2 is None
    assert measurement.custom3 is None
