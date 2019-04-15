import uuid
from datetime import datetime
from grow_easily_server.domain.user import User

TEST_DATE = datetime(2007, 12, 5, 22, 30)


def test_user_model_init():
    userId = uuid.uuid4()
    user = User(userId, name="Ivan", surname="Ivanov", email="ivan@gmail.com",
                password="123456", reg_date=TEST_DATE, mobile="12345678",
                age=20, gender="male")

    assert user.userId == userId
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
    userId = uuid.uuid4()
    user = User.from_dict(
        {
            'userId': userId,
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

    assert user.userId == userId
    assert user.name == "Ivan"
    assert user.surname == "Ivanov"
    assert user.email == "ivan@gmail.com"
    assert user.password == "123456"
    assert user.reg_date == TEST_DATE
    assert user.mobile == "12345678"
    assert user.age == 20
    assert user.gender == "male"
    assert user.rating is None


def test_user_model_to_dict():
    user_dict = {
        'userId': uuid.uuid4(),
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


def test_user_model_comparison():
    user_dict = {
        'userId': uuid.uuid4(),
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

    user1 = User.from_dict(user_dict)
    user2 = User.from_dict(user_dict)

    assert user1 == user2


def test_user_model_from_partial_dict():
    userId = uuid.uuid4()
    user = User.from_dict(
        {
            'userId': userId,
            'name': 'Ivan',
            'surname': 'Ivanov',
            'email': 'ivan@gmail.com',
            'password': '123456',
            'reg_date': TEST_DATE.timestamp(),
        }
    )

    assert user.userId == userId
    assert user.name == "Ivan"
    assert user.surname == "Ivanov"
    assert user.email == "ivan@gmail.com"
    assert user.password == "123456"
    assert user.reg_date == TEST_DATE.timestamp()
    assert user.mobile is None
    assert user.age is None
    assert user.gender is None
    assert user.rating is None
