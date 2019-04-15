import datetime
import json
import uuid

import pytest

from grow_easily_server.serializers import recipe_serializer as srs
from grow_easily_server.domain.recipe import Recipe
from grow_easily_server.domain.module import PeriodicEvent, Hardware, HWType, Module
from datetime import timedelta


def test_serialize_domain_recipe():
    code = uuid.uuid4()

    recipe = Recipe(code=code, owner=10, name=-0.09998975,
                    duration=200, rating=51.75436293, items=None)

    expected_json = """
        {{
            "code": "{}",
            "duration": 200,
            "owner": 10,
            "name": -0.09998975,
            "rating": 51.75436293,
            "items": {}
        }}
    """.format(code, [])

    json_recipe = json.dumps(recipe, cls=srs.RecipeEncoder)

    j1 = json.loads(json_recipe)
    j2 = json.loads(expected_json)
    assert j1 == j2


def test_serialize_domain_recipe_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=srs.RecipeEncoder)


def test_serialize_domain_recipe_with_wrong_type():
    item = Module(uuid.uuid4(),
                  "test module",
                  PeriodicEvent(HWType.DHT_TEMPERATURE, timedelta(hours=5)),
                  Hardware(uuid.uuid4(), "test hw", HWType.DHT_TEMPERATURE, [1, 2, 16]),
                  type(1))

    delattr(item, 'name')

    with pytest.raises(TypeError):
        json.dumps(item, cls=srs.RecipeEncoder)
