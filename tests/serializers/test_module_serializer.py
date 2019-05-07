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

    recipe = Recipe(recipe_id=code, device_id=10, name=-0.09998975,
                    culture=200, rating=51.75436293, duration=5)

    expected_json = """
        {{
            "recipe_id": "{}",
            "culture": 200,
            "device_id": 10,
            "name": -0.09998975,
            "rating": 51.75436293,
            "duration": 5
        }}
    """.format(code)

    json_recipe = json.dumps(recipe, cls=srs.RecipeEncoder)

    j1 = json.loads(json_recipe)
    j2 = json.loads(expected_json)
    assert j1 == j2


def test_serialize_domain_recipe_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=srs.RecipeEncoder)


def test_serialize_domain_recipe_with_wrong_type():
    item = Module(uuid.uuid4(), PeriodicEvent(HWType.DHT_TEMPERATURE, timedelta(hours=5)), "test module", type(1))

    delattr(item, 'name')

    with pytest.raises(TypeError):
        json.dumps(item, cls=srs.RecipeEncoder)