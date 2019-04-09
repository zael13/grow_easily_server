from datetime import datetime
import json
import uuid

import pytest

from grow_easily_server.serializers import user_serializer as srs
from grow_easily_server.domain.user import User


TEST_DATE = datetime(2007, 12, 5, 22, 30)


def test_serialize_domain_user():
    code = uuid.uuid4()

    user = User(code, name="Ivan", surname="Ivanov", email="ivan@gmail.com",
                password="123456", reg_date=TEST_DATE, mobile="12345678",
                age=20, gender="male")

    expected_json = """
        {{
            "code": "{}",
            "name": "Ivan",
            "surname": "Ivanov",
            "email": "ivan@gmail.com",
            "password": "123456",
            "reg_date": 1196890200.0,
            "mobile": "12345678",
            "age": 20,
            "gender": "male",
            "rating": "{}"
        }}
    """.format(code, None, [])

    json_user = json.dumps(user, cls=srs.UserEncoder)

    j1 = json.loads(json_user)
    j2 = json.loads(expected_json)
    assert j1 == j2


def test_serialize_domain_user_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.now(), cls=srs.UserEncoder)