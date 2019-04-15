import json
from unittest import mock

from grow_easily_server.domain.user import User
from grow_easily_server.shared import response_object as res


from grow_easily_server.serializers import user_serializer as srs

import uuid

user1_dict = {
    'userId': str(uuid.uuid4()),
    'name': 'Ivan',
    'surname': 'Ivanov',
    'email': 'ivan@gmail.com',
    'password': '123456',
    'reg_date': 100,
    'mobile': '12345678',
    'age': 20,
    'gender': 'male',
    'rating': None
}

json_user = json.dumps(user1_dict, cls=srs.UserEncoder)

user1_domain_model = User.from_dict(user1_dict)

users = [user1_domain_model]


@mock.patch(
    'grow_easily_server.use_cases.user_use_cases.UserListUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(users)

    http_response = client.get('/find_user')

    # assert json.loads(http_response.data.decode(
    #     'UTF-8')) == [json.loads(json_user)]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'


@mock.patch(
    'grow_easily_server.use_cases.user_use_cases.UserListUseCase')
def test_get_failed_response(mock_use_case, client):
    mock_use_case().execute.return_value = \
        res.ResponseFailure.build_system_error('test message')

    http_response = client.get('/find_user')

    assert json.loads(http_response.data.decode('UTF-8')) == \
        {'type': 'SYSTEM_ERROR', 'message': 'test message'}
    assert http_response.status_code == 500
    assert http_response.mimetype == 'application/json'


@mock.patch(
    'grow_easily_server.use_cases.user_use_cases.UserListUseCase')
def test_request_object_initialisation_and_use_with_filters(
        mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess([])

    internal_request_object = mock.Mock()

    request_object_class = \
        'grow_easily_server.use_cases.request_objects.RecipeListRequestObject'
    with mock.patch(request_object_class) as mock_request_object:
        mock_request_object.from_dict.return_value = internal_request_object
        client.get('/find_user?filter_param1=value1&filter_param2=value2')

    mock_request_object.from_dict.assert_called_with(
        {'filters': {'param1': 'value1', 'param2': 'value2'}}
    )
    mock_use_case().execute.assert_called_with(internal_request_object)


@mock.patch(
    'grow_easily_server.use_cases.user_use_cases.UserAddUseCase')
def test_get_add_user(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess("User has been successfully created")

    http_response = client.get('/add_user')

    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'
