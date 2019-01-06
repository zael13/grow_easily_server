import datetime
import json
import uuid

import pytest

from grow_easily_server.serializers import recipe_serializer as srs
from grow_easily_server.domain.recipe import Recipe


def test_serialize_domain_recipe():
    code = uuid.uuid4()

    recipe = Recipe(code=code, owner=10, name=-0.09998975, duration=200, rating=51.75436293, items=['1'])

    expected_json = """
        {{
            "code": "{}",
            "duration": 200,
            "owner": 10,
            "name": -0.09998975,
            "rating": 51.75436293,
            "items": "1"
        }}
    """.format(code)

    json_recipe = json.dumps(recipe, cls=srs.RecipeEncoder)

    j1 = json.loads(json_recipe)
    j2 = json.loads(expected_json)
    assert j1 == j2


def test_serialize_domain_recipe_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=srs.RecipeEncoder)
