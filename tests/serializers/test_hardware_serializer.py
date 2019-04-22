from datetime import datetime
import json
import uuid
import pytest

from grow_easily_server.serializers import hardware_serializer as srs
from grow_easily_server.domain.hardware import Hardware


START_TIME = datetime(2007, 12, 5, 22, 30).timestamp()


def test_serialize_domain_trigger():
    hardware_id = str(uuid.uuid4())
    hardware = Hardware(hardware_id, "Temperature1",
                        "DHT_TEMPERATURE", [1, 2], 20.5, 2.0)


    expected_json = """
        {{
            "hardware_id": "{}",
            "name": "Temperature1",
            "hw_type": "DHT_TEMPERATURE",
            "pins": [1, 2],
            "value": 20.5,
            "delta": 2.0
        }}
    """.format(hardware_id)

    json_trigger = json.dumps(hardware, cls=srs.HardwareEncoder)

    j1 = json.loads(json_trigger)
    j2 = json.loads(expected_json)
    assert j1 == j2


def test_serialize_domain_trigger_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.now(), cls=srs.HardwareEncoder)


def test_serialize_domain_trigger_with_wrong_type():
    hardware_id = str(uuid.uuid4())
    hardware = Hardware(hardware_id, "Temperature1",
                        "DHT_TEMPERATURE", [1, 2], 20.5, 2.0)

    delattr(hardware, 'name')

    with pytest.raises(TypeError):
        json.dumps(hardware, cls=srs.HardwareEncoder)
