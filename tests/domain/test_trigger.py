import uuid
from datetime import datetime
from grow_easily_server.domain.trigger import Trigger

START_TIME = datetime(2007, 12, 5, 22, 30).timestamp()


def test_trigger_model_init():
    trigger_id = str(uuid.uuid4())
    module_id = str(uuid.uuid4())
    trigger = Trigger(trigger_id, module_id, name="daily", start_time=START_TIME,
                      end_time=START_TIME+10, delta=5)

    assert trigger.trigger_id == trigger_id
    assert trigger.module_id == module_id
    assert trigger.name == "daily"
    assert trigger.start_time == START_TIME
    assert trigger.end_time == START_TIME+10
    assert trigger.delta == 5


def test_trigger_model_from_dict():
    trigger_id = str(uuid.uuid4())
    module_id = str(uuid.uuid4())
    trigger = Trigger.from_dict(
        {
            'trigger_id': trigger_id,
            'module_id': module_id,
            'name': "daily",
            'start_time': START_TIME,
            'end_time': START_TIME+10,
            'delta': 5,
        }
    )

    assert trigger.trigger_id == trigger_id
    assert trigger.module_id == module_id
    assert trigger.name == "daily"
    assert trigger.start_time == START_TIME
    assert trigger.end_time == START_TIME+10
    assert trigger.delta == 5


def test_trigger_model_to_dict():
    trigger_id = str(uuid.uuid4())
    module_id = str(uuid.uuid4())
    trigger_dict = {
        'trigger_id': trigger_id,
        'module_id': module_id,
        'name': "daily",
        'start_time': START_TIME,
        'end_time': START_TIME + 10,
        'delta': 5,
    }

    trigger = Trigger.from_dict(trigger_dict)

    assert trigger.to_dict() == trigger_dict


def test_trigger_model_comparison():
    trigger_id = str(uuid.uuid4())
    module_id = str(uuid.uuid4())
    trigger_dict = {
        'trigger_id': trigger_id,
        'module_id': module_id,
        'name': "daily",
        'start_time': START_TIME,
        'end_time': START_TIME + 10,
        'delta': 5,
    }

    trigger1 = Trigger.from_dict(trigger_dict)
    trigger2 = Trigger.from_dict(trigger_dict)

    assert trigger1 == trigger2