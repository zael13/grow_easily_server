from datetime import datetime
import json
import uuid
import pytest
from decimal import Decimal

from grow_easily_server.serializers import trigger_serializer as srs
from grow_easily_server.domain.trigger import Trigger


START_TIME = datetime(2007, 12, 5, 22, 30).timestamp()


def test_serialize_domain_trigger():
    trigger_id = str(uuid.uuid4())
    module_id = str(uuid.uuid4())
    trigger = Trigger(trigger_id, module_id, name="daily", start_time=Decimal(START_TIME),
                      end_time=Decimal(START_TIME+0.1), delta=5)

    expected_json = """
        {{
            "trigger_id": "{}",
            "module_id": "{}",
            "name": "daily",
            "start_time": {},
            "end_time": {},
            "delta": 5
        }}
    """.format(trigger_id, module_id, Decimal(START_TIME), Decimal(START_TIME+0.1))

    json_trigger = json.dumps(trigger, cls=srs.TriggerEncoder)

    j1 = json.loads(json_trigger)
    j2 = json.loads(expected_json)
    assert j1 == j2


def test_serialize_domain_trigger_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.now(), cls=srs.TriggerEncoder)


def test_serialize_domain_trigger_with_wrong_type():
    trigger_id = str(uuid.uuid4())
    module_id = str(uuid.uuid4())
    trigger = Trigger(trigger_id, module_id, name="daily", start_time=Decimal(START_TIME),
                      end_time=Decimal(START_TIME+0.1), delta=5)

    delattr(trigger, 'name')

    with pytest.raises(TypeError):
        json.dumps(trigger, cls=srs.TriggerEncoder)
