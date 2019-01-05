import datetime
import json
import uuid

import pytest

from grow_easily_server.serializers import recipe_serializer as srs
from grow_easily_server.domain.recipe import Recipe


def test_serialize_domain_recipe():
    code = uuid.uuid4()

    recipe = Recipe(
        code=code,
        duration=200,
        price=10,
        longitude=-0.09998975,
        rating=51.75436293
    )

    expected_json = """
        {{
            "code": "{}",
            "duration": 200,
            "price": 10,
            "longitude": -0.09998975,
            "rating": 51.75436293
        }}
    """.format(code)

    json_recipe = json.dumps(recipe, cls=srs.RecipeEncoder)

    assert json.loads(json_recipe) == json.loads(expected_json)


def test_serialize_domain_recipe_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=srs.RecipeEncoder)
