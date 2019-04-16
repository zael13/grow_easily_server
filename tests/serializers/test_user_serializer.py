from datetime import datetime
import json
import uuid

import pytest

from grow_easily_server.serializers import user_serializer as srs
from grow_easily_server.domain.user import User
from decimal import Decimal

TEST_DATE = datetime(2007, 12, 5, 22, 30)


def test_serialize_domain_user():
    userId = uuid.uuid4()

    user = User(userId, name="Ivan", surname="Ivanov", email="ivan@gmail.com",
                password="123456", reg_date=Decimal(TEST_DATE.timestamp()), mobile="12345678",
                age=Decimal(20.5), gender="male")

    expected_json = """
        {{
            "userId": "{}",
            "name": "Ivan",
            "surname": "Ivanov",
            "email": "ivan@gmail.com",
            "password": "123456",
            "reg_date": 1196890200.0,
            "mobile": "12345678",
            "age": 20.5,
            "gender": "male",
            "rating": "{}"
        }}
    """.format(userId, None, [])

    json_user = json.dumps(user, cls=srs.UserEncoder)

    j1 = json.loads(json_user)
    j2 = json.loads(expected_json)
    assert j1 == j2


def test_serialize_domain_user_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.now(), cls=srs.UserEncoder)


def test_serialize_domain_user_with_wrong_type():
    user = User(uuid.uuid4(), name="Ivan", surname="Ivanov", email="ivan@gmail.com",
                password="123456", reg_date=TEST_DATE.timestamp(), mobile="12345678",
                age=20, gender="male")

    delattr(user, 'gender')

    with pytest.raises(TypeError):
        json.dumps(user, cls=srs.UserEncoder)
