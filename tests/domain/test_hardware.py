import uuid
from datetime import datetime
from grow_easily_server.domain.hardware import Hardware

START_TIME = datetime(2007, 12, 5, 22, 30).timestamp()


def test_hardware_model_init():
    hardware_id = str(uuid.uuid4())
    module_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    hardware = Hardware(hardware_id, module_id, user_id, "Temperature1",
                        "DHT_TEMPERATURE", [1, 2], 20.5, 2.0)

    assert hardware.hardware_id == hardware_id
    assert hardware.module_id == module_id
    assert hardware.user_id == user_id
    assert hardware.name == "Temperature1"
    assert hardware.hw_type == "DHT_TEMPERATURE"
    assert hardware.pins == [1, 2]
    assert hardware.value == 20.5
    assert hardware.delta == 2.0


def test_hardware_model_from_dict():
    hardware_id = str(uuid.uuid4())
    module_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    hardware = Hardware.from_dict(
        {
            'hardware_id': hardware_id,
            'module_id': module_id,
            'user_id': user_id,
            'name': "Temperature1",
            'hw_type': "DHT_TEMPERATURE",
            'pins': [1, 2],
            'value': 20.5,
            'delta': 2.0,
        }
    )

    assert hardware.hardware_id == hardware_id
    assert hardware.module_id == module_id
    assert hardware.user_id == user_id
    assert hardware.name == "Temperature1"
    assert hardware.hw_type == "DHT_TEMPERATURE"
    assert hardware.pins == [1, 2]
    assert hardware.value == 20.5
    assert hardware.delta == 2.0


def test_hardware_model_to_dict():
    hardware_id = str(uuid.uuid4())
    module_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    hardware_dict = {
        'hardware_id': hardware_id,
        'module_id': module_id,
        'user_id': user_id,
        'name': "Temperature1",
        'hw_type': "DHT_TEMPERATURE",
        'pins': [1, 2],
        'value': 20.5,
        'delta': 2.0,
    }

    hardware = Hardware.from_dict(hardware_dict)

    assert hardware.to_dict() == hardware_dict


def test_hardware_model_comparison():
    hardware_id = str(uuid.uuid4())
    module_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    hardware_dict = {
        'hardware_id': hardware_id,
        'module_id': module_id,
        'user_id': user_id,
        'name': "Temperature1",
        'hw_type': "DHT_TEMPERATURE",
        'pins': [1, 2],
        'value': 20.5,
        'delta': 2.0,
    }

    hardware1 = Hardware.from_dict(hardware_dict)
    hardware2 = Hardware.from_dict(hardware_dict)

    assert hardware1 == hardware2
