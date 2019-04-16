from datetime import datetime
import json
import uuid

import pytest

from grow_easily_server.serializers import measurement_serializer as srs
from grow_easily_server.domain.measurement import Measurement
from decimal import Decimal

measurementId = str(uuid.uuid4())
deviceId = str(uuid.uuid4())
image_id = str(uuid.uuid4())
TIMESTAMP = datetime(2007, 12, 5, 22, 30).timestamp()


def test_serialize_domain_measurement():
    measurement = Measurement(measurementId, deviceId, TIMESTAMP,
                              temperature=22.3,
                              moisture=68.2,
                              ph_level=6.5,
                              height=32.8,
                              water_level=0.2,
                              image_id=image_id,
                              exhaust_hood=1,
                              light=1,
                              fertilizer=0,
                              custom1=22.1,
                              custom2="test_val",
                              custom3=None)

    expected_json = """
        {{
        "measurementId": "{}",
        "deviceId": "{}",
        "timestamp": {},
        "temperature": 22.3,
        "moisture": 68.2,
        "phLevel": 6.5,
        "height": 32.8,
        "waterLevel": 0.2,
        "imageId": "{}",
        "exhaustHood": 1,
        "light": 1,
        "fertilizer": 0,
        "custom1": 22.1,
        "custom2": "test_val",
        "custom3": null
        }}
    """.format(measurementId, deviceId, TIMESTAMP, image_id)

    json_measurement = json.dumps(measurement, cls=srs.MeasurementEncoder)

    j1 = json.loads(json_measurement)
    j2 = json.loads(expected_json)
    assert j1 == j2


def test_serialize_domain_measurement_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.now(), cls=srs.MeasurementEncoder)


def test_serialize_domain_measurement_with_wrong_type():
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

    delattr(measurement, 'height')

    with pytest.raises(TypeError):
        json.dumps(measurement, cls=srs.MeasurementEncoder)
