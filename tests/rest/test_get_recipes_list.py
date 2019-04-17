# import json
# from unittest import mock
#
# from grow_easily_server.domain.recipe import Recipe
# from grow_easily_server.shared import response_object as res
#
#
# from grow_easily_server.serializers import recipe_serializer as srs
# from grow_easily_server.domain.module import PeriodicEvent, Hardware, HWType, Module
# from datetime import timedelta
# import uuid
# item = Module(uuid.uuid4(),
#               "test module",
#               PeriodicEvent(HWType.DHT_TEMPERATURE, timedelta(hours=5)),
#               Hardware(uuid.uuid4(), "test hw", HWType.DHT_TEMPERATURE, [1, 2, 16]),
#               type(1))
#
#
# recipe1_dict = {
#     'recipe_id': '3251a5bd-86be-428d-8ae9-6e51a8048c33',
#     'culture': 200,
#     'user_id': 10,
#     'name': -0.09998975,
#     'rating': 51.75436293,
#     'modules': [item]
# }
#
#
# json_recipe = json.dumps(recipe1_dict, cls=srs.RecipeEncoder)
#
# recipe1_domain_model = Recipe.from_dict(recipe1_dict)
#
# recipes = [recipe1_domain_model]
#
#
# @mock.patch(
#     'grow_easily_server.use_cases.recipe_use_cases.RecipeListUseCase')
# def test_get(mock_use_case, client):
#     mock_use_case().execute.return_value = res.ResponseSuccess(recipes)
#
#     http_response = client.get('/find_recipe')
#
#     assert json.loads(http_response.data.decode(
#         'UTF-8')) == [json.loads(json_recipe)]
#     assert http_response.status_code == 200
#     assert http_response.mimetype == 'application/json'
#
#
# @mock.patch(
#     'grow_easily_server.use_cases.recipe_use_cases.RecipeListUseCase')
# def test_get_failed_response(mock_use_case, client):
#     mock_use_case().execute.return_value = \
#         res.ResponseFailure.build_system_error('test message')
#
#     http_response = client.get('/find_recipe')
#
#     assert json.loads(http_response.data.decode('UTF-8')) == \
#         {'type': 'SYSTEM_ERROR', 'message': 'test message'}
#     assert http_response.status_code == 500
#     assert http_response.mimetype == 'application/json'
#
#
# @mock.patch(
#     'grow_easily_server.use_cases.recipe_use_cases.RecipeListUseCase')
# def test_request_object_initialisation_and_use_with_filters(
#         mock_use_case, client):
#     mock_use_case().execute.return_value = res.ResponseSuccess([])
#
#     internal_request_object = mock.Mock()
#
#     request_object_class = \
#         'grow_easily_server.use_cases.request_objects.RecipeListRequestObject'
#     with mock.patch(request_object_class) as mock_request_object:
#         mock_request_object.from_dict.return_value = internal_request_object
#         client.get('/find_recipe?filter_param1=value1&filter_param2=value2')
#
#     mock_request_object.from_dict.assert_called_with(
#         {'filters': {'param1': 'value1', 'param2': 'value2'}}
#     )
#     mock_use_case().execute.assert_called_with(internal_request_object)
