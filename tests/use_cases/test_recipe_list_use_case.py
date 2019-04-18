import uuid

import pytest
from unittest import mock

from grow_easily_server.domain.recipe import Recipe
from grow_easily_server.shared import response_object as res
from grow_easily_server.use_cases import request_objects as req
from grow_easily_server.use_cases import recipe_use_cases as uc


@pytest.fixture
def domain_recipes():
    recipe_1 = Recipe(
        recipe_id=uuid.uuid4(),
        device_id=39,
        culture=215,
        name=-0.09998975,
        rating=51.75436293,
    )

    recipe_2 = Recipe(
        recipe_id=uuid.uuid4(),
        device_id=66,
        culture=405,
        name=0.18228006,
        rating=51.74640997,
    )

    recipe_3 = Recipe(
        recipe_id=uuid.uuid4(),
        device_id=60,
        culture=56,
        name=0.27891577,
        rating=51.45994069,
    )

    recipe_4 = Recipe(
        recipe_id=uuid.uuid4(),
        device_id=60,
        culture=93,
        name=0.33894476,
        rating=51.39916678,
    )

    return [recipe_1, recipe_2, recipe_3, recipe_4]


def test_recipe_list_without_parameters(domain_recipes):
    repo = mock.Mock()
    repo.list.return_value = domain_recipes

    recipe_list_use_case = uc.RecipeListUseCase(repo)
    request_object = req.RecipeListRequestObject.from_dict({})

    response_object = recipe_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=None)

    assert response_object.value == domain_recipes


def test_recipe_list_with_filters(domain_recipes):
    repo = mock.Mock()
    repo.list.return_value = domain_recipes

    recipe_list_use_case = uc.RecipeListUseCase(repo)
    qry_filters = {'a': 5}
    request_object = req.RecipeListRequestObject.from_dict({'filters': qry_filters})

    response_object = recipe_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_recipes


def test_recipe_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    recipe_list_use_case = uc.RecipeListUseCase(repo)
    request_object = req.RecipeListRequestObject.from_dict({})

    response_object = recipe_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }


def test_recipe_list_handles_bad_request():
    repo = mock.Mock()

    recipe_list_use_case = uc.RecipeListUseCase(repo)
    request_object = req.RecipeListRequestObject.from_dict({'filters': 5})

    response_object = recipe_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "filters: Is not iterable"
    }
