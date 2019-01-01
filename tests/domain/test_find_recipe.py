import uuid
from grow_easily_server.domain.recipe import Recipe


def test_recipe_model_init():
    code = uuid.uuid4()
    recipe = Recipe(code, size=200, price=10,
                    longitude=-0.09998975,
                    latitude=51.75436293)
    assert recipe.code == code
    assert recipe.size == 200
    assert recipe.price == 10
    assert recipe.longitude == -0.09998975
    assert recipe.latitude == 51.75436293


def test_recipe_model_from_dict():
    code = uuid.uuid4()
    recipe = Recipe.from_dict(
        {
            'code': code,
            'size': 200,
            'price': 10,
            'longitude': -0.09998975,
            'latitude': 51.75436293
        }
    )
    assert recipe.code == code
    assert recipe.size == 200
    assert recipe.price == 10
    assert recipe.longitude == -0.09998975
    assert recipe.latitude == 51.75436293


def test_recipe_model_to_dict():
    recipe_dict = {
        'code': uuid.uuid4(),
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293
    }

    recipe = Recipe.from_dict(recipe_dict)

    assert recipe.to_dict() == recipe_dict


def test_recipe_model_comparison():
    recipe_dict = {
        'code': uuid.uuid4(),
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293
    }
    recipe1 = Recipe.from_dict(recipe_dict)
    recipe2 = Recipe.from_dict(recipe_dict)

    assert recipe1 == recipe2
