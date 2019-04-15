import uuid
import datetime

import pytest
from unittest import mock

from grow_easily_server.domain.user import User
from grow_easily_server.shared import response_object as res
from grow_easily_server.use_cases import request_objects as req
from grow_easily_server.use_cases import user_use_cases as uc


TEST_DATE = datetime.datetime(2007, 12, 5, 22, 30)


@pytest.fixture
def domain_users():
    user_1 = User(
        userId=uuid.uuid4(),
        name='Vova',
        surname='Ivanov',
        email='vova@gmail.com',
        password='1234',
        reg_date=TEST_DATE.timestamp(),
        mobile='12345678',
        age=20,
        gender='male',
        rating=4.0,
    )

    user_2 = User(
        userId=uuid.uuid4(),
        name='Ivan',
        surname='Ivanov',
        email='ivanov@gmail.com',
        password='1234',
        reg_date=TEST_DATE.timestamp(),
        mobile='12345678',
        age=20,
        gender='male',
        rating=3.0,
    )

    user_3 = User(
        userId=uuid.uuid4(),
        name='Maksym',
        surname='Ivanov',
        email='maks@gmail.com',
        password='1234',
        reg_date=TEST_DATE.timestamp(),
        mobile='12345678',
        age=30,
        gender='male',
        rating=2.0,
    )

    user_4 = User(
        userId=uuid.uuid4(),
        name='Den',
        surname='Ivanov',
        email='den@gmail.com',
        password='1234',
        reg_date=TEST_DATE.timestamp(),
        mobile='12345678',
        age=25,
        gender='male',
        rating=1.0,
    )

    return [user_1, user_2, user_3, user_4]


def test_user_list_without_parameters(domain_users):
    repo = mock.Mock()
    repo.list.return_value = domain_users

    user_list_use_case = uc.UserListUseCase(repo)
    request_object = req.RecipeListRequestObject.from_dict({})

    response_object = user_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=None)

    assert response_object.value == domain_users


def test_user_list_with_filters(domain_users):
    repo = mock.Mock()
    repo.list.return_value = domain_users

    user_list_use_case = uc.UserListUseCase(repo)
    qry_filters = {'a': 5}
    request_object = req.RecipeListRequestObject.from_dict({'filters': qry_filters})

    response_object = user_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_users


def test_user_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    user_list_use_case = uc.UserListUseCase(repo)
    request_object = req.RecipeListRequestObject.from_dict({})

    response_object = user_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }


def test_user_list_handles_bad_request():
    repo = mock.Mock()

    user_list_use_case = uc.UserListUseCase(repo)
    request_object = req.RecipeListRequestObject.from_dict({'filters': 5})

    response_object = user_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "filters: Is not iterable"
    }


def test_user_add_insert_an_item():
    repo = mock.Mock()

    user_add_use_case = uc.UserAddUseCase(repo)
    request_object = req.RecipeListRequestObject.from_dict({'filters': 5})

    response_object = user_add_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "filters: Is not iterable"
    }


def test_user_add_handles_bad_request(domain_users):
    repo = mock.Mock()
    repo.list.return_value = domain_users

    user_add_use_case = uc.UserAddUseCase(repo)
    qry_filters = {'email': "test@gmail.com"}
    request_object = req.RecipeListRequestObject.from_dict({'filters': qry_filters})

    response_object = user_add_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "Such user is already exist"
    }


def test_user_add_with_filters(domain_users):
    repo = mock.Mock()
    repo.list.return_value = []

    user_add_use_case = uc.UserAddUseCase(repo)
    qry_filters = {'email': "test@gmail.com",
                   'name': "test",
                   'surname': "test",
                   'password': "pass",
                   'reg_date': 12345,
                   'userId': "12345"}
    request_object = req.RecipeListRequestObject.from_dict({'filters': qry_filters})

    response_object = user_add_use_case.execute(request_object)

    assert bool(response_object) is True
    assert response_object.value == "User has been successfully created"
