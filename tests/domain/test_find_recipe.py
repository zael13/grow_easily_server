import pytest
import uuid
from grow_easily_server.domain.recipe import Recipe

from datetime import datetime, time, timedelta
from grow_easily_server.domain.module import HWType, \
    Controller, CalendarEvent, Module, Hardware

TEST_DATE = datetime(2007, 12, 5, 22, 30)
ONE_DAY = timedelta(days=1)
TEST_TIME = time(13, 30)
ONE_HOUR = timedelta(hours=1)


def test_recipe_model_init():
    code = uuid.uuid4()
    recipe = Recipe(code, owner=10, name=-0.09998975, duration=200, rating=51.75436293)
    assert recipe.code == code
    assert recipe.duration == 200
    assert recipe.owner == 10
    assert recipe.name == -0.09998975
    assert recipe.rating == 51.75436293


def test_recipe_model_from_dict():
    code = uuid.uuid4()
    recipe = Recipe.from_dict(
        {
            'code': code,
            'duration': 200,
            'owner': 10,
            'name': -0.09998975,
            'rating': 51.75436293,
            'items': ''
        }
    )
    assert recipe.code == code
    assert recipe.duration == 200
    assert recipe.owner == 10
    assert recipe.name == -0.09998975
    assert recipe.rating == 51.75436293


# def test_recipe_model_from_dict():
#     code = uuid.uuid4()
#     item = ["temp", "1", "2"]
#     recipe = Recipe.from_dict(
#         {
#             'code': code,
#             'duration': 200,
#             'owner': 10,
#             'name': -0.09998975,
#             'rating': 51.75436293,
#             'items': item
#         }
#     )
#     assert recipe.code == code
#     assert recipe.duration == 200
#     assert recipe.owner == 10
#     assert recipe.name == -0.09998975
#     assert recipe.rating == 51.75436293
#     assert recipe.items == item

def test_recipe_model_to_dict():
    recipe_dict = {
        'code': uuid.uuid4(),
        'duration': 200,
        'owner': 10,
        'name': -0.09998975,
        'rating': 51.75436293,
        'items': ''
    }

    recipe = Recipe.from_dict(recipe_dict)

    assert recipe.to_dict() == recipe_dict


def test_recipe_model_comparison():
    recipe_dict = {
        'code': uuid.uuid4(),
        'duration': 200,
        'owner': 10,
        'name': -0.09998975,
        'rating': 51.75436293,
        'items': ''
    }
    recipe1 = Recipe.from_dict(recipe_dict)
    recipe2 = Recipe.from_dict(recipe_dict)

    assert recipe1 == recipe2


def test_recipe_should_create_empty_list_of_events_after_initialization():
    recipe = Recipe(uuid.uuid4(), owner=10, name=-0.09998975, duration=200, rating=51.75436293)
    assert recipe.get_items() == []


# def test_add_item_should_should_add_new_event_to_the_list():
#     recipe = Recipe(uuid.uuid4(), owner=10, name=-0.09998975, duration=200, rating=51.75436293)
#     recipe.add_item(Controller(HWType.DHT_TEMPERATURE, 1))
#     assert(len(recipe.get_items()) == 1)


def test_add_string_item_should_raise_the_wrong_type_exception():
    recipe = Recipe(uuid.uuid4(), owner=10, name=-0.09998975, duration=200, rating=51.75436293)
    with pytest.raises(TypeError):
        recipe.add_item("string")


def test_add_the_controller_of_the_same_type_twice_should_substitute_old_value_with_new():
    recipe = Recipe(uuid.uuid4(), owner=10, name=-0.09998975, duration=200, rating=51.75436293)
    hw = Hardware(uuid.uuid4(), "Temperature", HWType.DHT_TEMPERATURE, [1, 2, 16])
    m1 = Module(uuid.uuid4(), "Temperature", Controller(HWType.DHT_TEMPERATURE, 1), hw, int)
    m2 = Module(uuid.uuid4(), "Temperature", CalendarEvent(HWType.DHT_HUMIDITY, TEST_DATE), hw, int)
    m3 = Module(uuid.uuid4(), "Temperature", Controller(HWType.DHT_TEMPERATURE, 2), hw, int)

    recipe.add_item(m1)
    recipe.add_item(m2)
    recipe.add_item(m3)

    assert(len(recipe.get_items()) == 2)
    assert(recipe.items[0].trigger.value == 2)

# def test_add_the_calendar_event_of_the_same_type_twice_should_not_substitute_old_value():
#     recipe = Recipe(uuid.uuid4(), owner=10, name=-0.09998975, duration=200, rating=51.75436293)
#     recipe.add_item(CalendarEvent(HWType.DHT_TEMPERATURE, TEST_DATE))
#     recipe.add_item(CalendarEvent(HWType.DHT_TEMPERATURE, TEST_DATE + ONE_DAY))
#     assert(len(recipe.get_items()) == 2)
#     assert(recipe.items[0].calendar_time == TEST_DATE)


# def test_add_the_daily_event_of_the_same_type_twice_should_not_substitute_old_value():
#     recipe = Recipe(uuid.uuid4(), owner=10, name=-0.09998975, duration=200, rating=51.75436293)
#     recipe.add_item(DailyEvent(HWType.DHT_TEMPERATURE, TEST_TIME))
#     recipe.add_item(DailyEvent(HWType.DHT_TEMPERATURE, time(15, 30)))
#     assert(len(recipe.get_items()) == 2)
#     assert(recipe.items[0].day_time == TEST_TIME)


# def test_new_added_items_should_not_have_the_s_ame_type_as_existing_controller():
#     recipe = Recipe(uuid.uuid4(), owner=10, name=-0.09998975, duration=200, rating=51.75436293)
#     recipe.add_item(Controller(HWType.DHT_TEMPERATURE, 1))
#     recipe.add_item(CalendarEvent(HWType.DHT_TEMPERATURE, TEST_DATE))
#     assert(len(recipe.get_items()) == 1)


def test_generate_should_return_string():
    recipe = Recipe(uuid.uuid4(), owner=10, name=-0.09998975, duration=200, rating=51.75436293)
    assert(isinstance(recipe.generate(), str))
