import uuid
import pytest

from grow_easily_server.domain.user import User
from datetime import datetime
TEST_DATE = datetime(2007, 12, 5, 22, 30)


def test_user_model_init():
    code = uuid.uuid4()
    user = User(code, name="Ivan", surname="Ivanov", email="ivan@gmail.com",
                password="123456", reg_date=TEST_DATE, mobile="12345678",
                age=20, gender="male")

    assert user.code == code
    assert user.name == "Ivan"
    assert user.surname == "Ivanov"
    assert user.email == "ivan@gmail.com"
    assert user.password == "123456"
    assert user.reg_date == TEST_DATE
    assert user.mobile == "12345678"
    assert user.age == 20
    assert user.gender == "male"
    assert user.rating is None


def test_user_model_from_dict():
    code = uuid.uuid4()
    user = User.from_dict(
        {
            'code': code,
            'name': 'Ivan',
            'surname': 'Ivanov',
            'email': 'ivan@gmail.com',
            'password': '123456',
            'reg_date': TEST_DATE,
            'mobile': '12345678',
            'age': 20,
            'gender': 'male',
            'rating': None
        }
    )

    assert user.code == code
    assert user.name == "Ivan"
    assert user.surname == "Ivanov"
    assert user.email == "ivan@gmail.com"
    assert user.password == "123456"
    assert user.reg_date == TEST_DATE
    assert user.mobile == "12345678"
    assert user.age == 20
    assert user.gender == "male"
    assert user.rating is None


def test_recipe_model_to_dict():
    user_dict = {
            'code': uuid.uuid4(),
            'name': 'Ivan',
            'surname': 'Ivanov',
            'email': 'ivan@gmail.com',
            'password': '123456',
            'reg_date': TEST_DATE,
            'mobile': '12345678',
            'age': 20,
            'gender': 'male',
            'rating': None
        }

    user = User.from_dict(user_dict)

    assert user.to_dict() == user_dict
