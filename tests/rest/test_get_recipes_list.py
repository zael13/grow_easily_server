import json
from unittest import mock

from grow_easily_server.domain.recipe import Recipe
from grow_easily_server.shared import response_object as res

recipe1_dict = {
    'code': '3251a5bd-86be-428d-8ae9-6e51a8048c33',
    'duration': 200,
    'price': 10,
    'longitude': -0.09998975,
    'rating': 51.75436293
}

recipe1_domain_model = Recipe.from_dict(recipe1_dict)

recipes = [recipe1_domain_model]


@mock.patch(
    'grow_easily_server.use_cases.recipe_use_cases.RecipeListUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(recipes)

    http_response = client.get('/find_recipe')

    assert json.loads(http_response.data.decode(
        'UTF-8')) == [recipe1_dict]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'


@mock.patch(
    'grow_easily_server.use_cases.recipe_use_cases.RecipeListUseCase')
def test_get_failed_response(mock_use_case, client):
    mock_use_case().execute.return_value = \
        res.ResponseFailure.build_system_error('test message')

    http_response = client.get('/find_recipe')

    assert json.loads(http_response.data.decode('UTF-8')) == \
        {'type': 'SYSTEM_ERROR', 'message': 'test message'}
    assert http_response.status_code == 500
    assert http_response.mimetype == 'application/json'


@mock.patch(
    'grow_easily_server.use_cases.recipe_use_cases.RecipeListUseCase')
def test_request_object_initialisation_and_use_with_filters(
        mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess([])

    internal_request_object = mock.Mock()

    request_object_class = \
        'grow_easily_server.use_cases.request_objects.RecipeListRequestObject'
    with mock.patch(request_object_class) as mock_request_object:
        mock_request_object.from_dict.return_value = internal_request_object
        client.get('/find_recipe?filter_param1=value1&filter_param2=value2')

    mock_request_object.from_dict.assert_called_with(
        {'filters': {'param1': 'value1', 'param2': 'value2'}}
    )
    mock_use_case().execute.assert_called_with(internal_request_object)
