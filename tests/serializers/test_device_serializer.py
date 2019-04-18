from datetime import datetime
import json
import uuid
import pytest
from decimal import Decimal

from grow_easily_server.serializers import device_serializer as srs
from grow_easily_server.domain.device import Device


START_TIME = datetime(2007, 12, 5, 22, 30).timestamp()


def test_serialize_domain_device():
    device_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())

    device = Device(device_id, user_id, name="dev1", start_time=Decimal(START_TIME))

    expected_json = """
        {{
            "device_id": "{}",
            "user_id": "{}",
            "name": "dev1",
            "start_time": {}
        }}
    """.format(device_id, user_id, Decimal(START_TIME))

    json_device = json.dumps(device, cls=srs.DeviceEncoder)

    j1 = json.loads(json_device)
    j2 = json.loads(expected_json)
    assert j1 == j2


def test_serialize_domain_device_with_float():
    device_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())

    device = Device(device_id, user_id, name="dev1", start_time=Decimal(1.1))

    expected_json = """
        {{
            "device_id": "{}",
            "user_id": "{}",
            "name": "dev1",
            "start_time": {}
        }}
    """.format(device_id, user_id, Decimal(1.1))

    json_device = json.dumps(device, cls=srs.DeviceEncoder)

    j1 = json.loads(json_device)
    j2 = json.loads(expected_json)
    assert j1 == j2


def test_serialize_domain_device_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.now(), cls=srs.DeviceEncoder)


def test_serialize_domain_device_with_wrong_type():
    device_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    device = Device(device_id, user_id, name="dev1", start_time=START_TIME)

    delattr(device, 'name')

    with pytest.raises(TypeError):
        json.dumps(device, cls=srs.DeviceEncoder)
