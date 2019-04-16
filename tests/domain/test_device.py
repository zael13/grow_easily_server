import uuid
from datetime import datetime
from grow_easily_server.domain.device import Device

START_TIME = datetime(2007, 12, 5, 22, 30).timestamp()


def test_device_model_init():
    device_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    recipe_id = str(uuid.uuid4())
    device = Device(device_id, user_id, recipe_id, name="dev1", start_time=START_TIME)

    assert device.device_id == device_id
    assert device.user_id == user_id
    assert device.recipe_id == recipe_id
    assert device.name == "dev1"
    assert device.start_time == START_TIME


def test_device_model_from_dict():
    device_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    recipe_id = str(uuid.uuid4())
    device = Device.from_dict(
        {
            'device_id': device_id,
            'user_id': user_id,
            'recipe_id': recipe_id,
            'name': 'dev1',
            'start_time': START_TIME,
        }
    )

    assert device.device_id == device_id
    assert device.user_id == user_id
    assert device.recipe_id == recipe_id
    assert device.name == "dev1"
    assert device.start_time == START_TIME


def test_device_model_to_dict():
    device_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    recipe_id = str(uuid.uuid4())
    device_dict = {
        'device_id': device_id,
        'user_id': user_id,
        'recipe_id': recipe_id,
        'name': 'dev1',
        'start_time': START_TIME,
    }

    device = Device.from_dict(device_dict)

    assert device.to_dict() == device_dict


def test_device_model_comparison():
    device_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    recipe_id = str(uuid.uuid4())
    device_dict = {
        'device_id': device_id,
        'user_id': user_id,
        'recipe_id': recipe_id,
        'name': 'dev1',
        'start_time': START_TIME,
    }

    device1 = Device.from_dict(device_dict)
    device2 = Device.from_dict(device_dict)

    assert device1 == device2
