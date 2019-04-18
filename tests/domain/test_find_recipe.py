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
    recipe_id = uuid.uuid4()
    recipe = Recipe(recipe_id, device_id=10, name=-0.09998975, culture=200, rating=51.75436293)
    assert recipe.recipe_id == recipe_id
    assert recipe.culture == 200
    assert recipe.device_id == 10
    assert recipe.name == -0.09998975
    assert recipe.rating == 51.75436293


def test_recipe_model_from_dict():
    recipe_id = uuid.uuid4()
    recipe = Recipe.from_dict(
        {
            'recipe_id': recipe_id,
            'culture': 200,
            'device_id': 10,
            'name': -0.09998975,
            'rating': 51.75436293,
            'duration': ''
        }
    )
    assert recipe.recipe_id == recipe_id
    assert recipe.culture == 200
    assert recipe.device_id == 10
    assert recipe.name == -0.09998975
    assert recipe.rating == 51.75436293


# def test_recipe_model_from_dict():
#     recipe_id = uuid.uuid4()
#     item = ["temp", "1", "2"]
#     recipe = Recipe.from_dict(
#         {
#             'recipe_id': recipe_id,
#             'culture': 200,
#             'device_id': 10,
#             'name': -0.09998975,
#             'rating': 51.75436293,
#             'duration': item
#         }
#     )
#     assert recipe.recipe_id == recipe_id
#     assert recipe.culture == 200
#     assert recipe.device_id == 10
#     assert recipe.name == -0.09998975
#     assert recipe.rating == 51.75436293
#     assert recipe.duration == item

def test_recipe_model_to_dict():
    recipe_dict = {
        'recipe_id': uuid.uuid4(),
        'culture': 200,
        'device_id': 10,
        'name': -0.09998975,
        'rating': 51.75436293,
        'duration': ''
    }

    recipe = Recipe.from_dict(recipe_dict)

    assert recipe.to_dict() == recipe_dict


def test_recipe_model_comparison():
    recipe_dict = {
        'recipe_id': uuid.uuid4(),
        'culture': 200,
        'device_id': 10,
        'name': -0.09998975,
        'rating': 51.75436293,
        'duration': ''
    }
    recipe1 = Recipe.from_dict(recipe_dict)
    recipe2 = Recipe.from_dict(recipe_dict)

    assert recipe1 == recipe2


# def test_recipe_should_create_empty_list_of_events_after_initialization():
#     recipe = Recipe(uuid.uuid4(), device_id=10, name=-0.09998975, culture=200, rating=51.75436293)
#     assert recipe.get_duration() == []


# def test_add_item_should_should_add_new_event_to_the_list():
#     recipe = Recipe(uuid.uuid4(), device_id=10, name=-0.09998975, culture=200, rating=51.75436293)
#     recipe.add_item(Controller(HWType.DHT_TEMPERATURE, 1))
#     assert(len(recipe.get_duration()) == 1)


# def test_add_string_item_should_raise_the_wrong_type_exception():
#     recipe = Recipe(uuid.uuid4(), device_id=10, name=-0.09998975, culture=200, rating=51.75436293)
#     with pytest.raises(TypeError):
#         recipe.add_item("string")


# def test_add_the_controller_of_the_same_type_twice_should_substitute_old_value_with_new():
#     recipe = Recipe(uuid.uuid4(), device_id=10, name=-0.09998975, culture=200, rating=51.75436293)
#     hw = Hardware(uuid.uuid4(), "Temperature", HWType.DHT_TEMPERATURE, [1, 2, 16])
#     m1 = Module(uuid.uuid4(), "Temperature", Controller(HWType.DHT_TEMPERATURE, 1), hw, int)
#     m2 = Module(uuid.uuid4(), "Temperature", CalendarEvent(HWType.DHT_HUMIDITY, TEST_DATE), hw, int)
#     m3 = Module(uuid.uuid4(), "Temperature", Controller(HWType.DHT_TEMPERATURE, 2), hw, int)
#
#     recipe.add_item(m1)
#     recipe.add_item(m2)
#     recipe.add_item(m3)
#
#     assert(len(recipe.get_duration()) == 2)
#     assert(recipe.duration[0].trigger_id.value == 2)

# def test_add_the_calendar_event_of_the_same_type_twice_should_not_substitute_old_value():
#     recipe = Recipe(uuid.uuid4(), device_id=10, name=-0.09998975, culture=200, rating=51.75436293)
#     recipe.add_item(CalendarEvent(HWType.DHT_TEMPERATURE, TEST_DATE))
#     recipe.add_item(CalendarEvent(HWType.DHT_TEMPERATURE, TEST_DATE + ONE_DAY))
#     assert(len(recipe.get_duration()) == 2)
#     assert(recipe.duration[0].calendar_time == TEST_DATE)


# def test_add_the_daily_event_of_the_same_type_twice_should_not_substitute_old_value():
#     recipe = Recipe(uuid.uuid4(), device_id=10, name=-0.09998975, culture=200, rating=51.75436293)
#     recipe.add_item(DailyEvent(HWType.DHT_TEMPERATURE, TEST_TIME))
#     recipe.add_item(DailyEvent(HWType.DHT_TEMPERATURE, time(15, 30)))
#     assert(len(recipe.get_duration()) == 2)
#     assert(recipe.duration[0].day_time == TEST_TIME)


# def test_new_added_duration_should_not_have_the_s_ame_type_as_existing_controller():
#     recipe = Recipe(uuid.uuid4(), device_id=10, name=-0.09998975, culture=200, rating=51.75436293)
#     recipe.add_item(Controller(HWType.DHT_TEMPERATURE, 1))
#     recipe.add_item(CalendarEvent(HWType.DHT_TEMPERATURE, TEST_DATE))
#     assert(len(recipe.get_duration()) == 1)

#
# def test_generate_should_return_string():
#     recipe = Recipe(uuid.uuid4(), device_id=10, name=-0.09998975, culture=200, rating=51.75436293)
#     assert(isinstance(recipe.generate(), str))
