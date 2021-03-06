import pytest
import uuid
from grow_easily_server.domain.recipe import Recipe

from datetime import datetime, time, timedelta
from grow_easily_server.domain.module import HWType, \
    Event, Controller, CalendarEvent, DailyEvent, PeriodicEvent

TEST_DATE = datetime(2007, 12, 5, 22, 30)
ONE_DAY = timedelta(days=1)
TEST_TIME = time(13, 30)
ONE_HOUR = timedelta(hours=1)


def test_recipe_model_init():
    code = uuid.uuid4()
    recipe = Recipe(code, duration=200, price=10,
                    longitude=-0.09998975,
                    rating=51.75436293)
    assert recipe.code == code
    assert recipe.duration == 200
    assert recipe.price == 10
    assert recipe.longitude == -0.09998975
    assert recipe.rating == 51.75436293


def test_recipe_model_from_dict():
    code = uuid.uuid4()
    recipe = Recipe.from_dict(
        {
            'code': code,
            'duration': 200,
            'price': 10,
            'longitude': -0.09998975,
            'rating': 51.75436293
        }
    )
    assert recipe.code == code
    assert recipe.duration == 200
    assert recipe.price == 10
    assert recipe.longitude == -0.09998975
    assert recipe.rating == 51.75436293


def test_recipe_model_to_dict():
    recipe_dict = {
        'code': uuid.uuid4(),
        'duration': 200,
        'price': 10,
        'longitude': -0.09998975,
        'rating': 51.75436293
    }

    recipe = Recipe.from_dict(recipe_dict)

    assert recipe.to_dict() == recipe_dict


def test_recipe_model_comparison():
    recipe_dict = {
        'code': uuid.uuid4(),
        'duration': 200,
        'price': 10,
        'longitude': -0.09998975,
        'rating': 51.75436293
    }
    recipe1 = Recipe.from_dict(recipe_dict)
    recipe2 = Recipe.from_dict(recipe_dict)

    assert recipe1 == recipe2


def test_recipe_should_create_empty_list_of_events_after_initialization():
    recipe = Recipe(uuid.uuid4(), duration=200, price=10,
                    longitude=-0.09998975,
                    rating=51.75436293)
    assert recipe.get_items() == []


def test_add_item_should_should_add_new_event_to_the_list():
    recipe = Recipe(uuid.uuid4(), duration=200, price=10,
                    longitude=-0.09998975,
                    rating=51.75436293)
    recipe.add_item(Controller(HWType.DHT_TEMPERATURE, 1))
    assert(len(recipe.get_items()) == 1)


def test_add_string_item_should_raise_the_wrong_type_exception():
    recipe = Recipe(uuid.uuid4(), duration=200, price=10,
                    longitude=-0.09998975,
                    rating=51.75436293)
    with pytest.raises(TypeError):
        recipe.add_item("string")


def test_add_the_controller_of_the_same_type_twice_should_substitute_old_value_with_new():
    recipe = Recipe(uuid.uuid4(), duration=200, price=10,
                    longitude=-0.09998975,
                    rating=51.75436293)
    recipe.add_item(Controller(HWType.DHT_TEMPERATURE, 1))
    recipe.add_item(Controller(HWType.DHT_TEMPERATURE, 2))
    assert(len(recipe.get_items()) == 1)
    assert(recipe.items[0].value == 2)


def test_add_the_calendar_event_of_the_same_type_twice_should_not_substitute_old_value():
    recipe = Recipe(uuid.uuid4(), duration=200, price=10,
                    longitude=-0.09998975,
                    rating=51.75436293)
    recipe.add_item(CalendarEvent(HWType.DHT_TEMPERATURE, TEST_DATE))
    recipe.add_item(CalendarEvent(HWType.DHT_TEMPERATURE, TEST_DATE + ONE_DAY))
    assert(len(recipe.get_items()) == 2)
    assert(recipe.items[0].calendar_time == TEST_DATE)


def test_add_the_daily_event_of_the_same_type_twice_should_not_substitute_old_value():
    recipe = Recipe(uuid.uuid4(), duration=200, price=10,
                    longitude=-0.09998975,
                    rating=51.75436293)
    recipe.add_item(DailyEvent(HWType.DHT_TEMPERATURE, TEST_TIME))
    recipe.add_item(DailyEvent(HWType.DHT_TEMPERATURE, time(15, 30)))
    assert(len(recipe.get_items()) == 2)
    assert(recipe.items[0].day_time == TEST_TIME)


def test_new_added_items_should_not_have_the_s_ame_type_as_existing_controller():
    recipe = Recipe(uuid.uuid4(), duration=200, price=10,
                    longitude=-0.09998975,
                    rating=51.75436293)
    recipe.add_item(Controller(HWType.DHT_TEMPERATURE, 1))
    recipe.add_item(CalendarEvent(HWType.DHT_TEMPERATURE, TEST_DATE))
    assert(len(recipe.get_items()) == 1)


def test_generate_should_return_string():
    recipe = Recipe(uuid.uuid4(), duration=200, price=10,
                    longitude=-0.09998975,
                    rating=51.75436293)
    recipe.add_item(Controller(HWType.DHT_TEMPERATURE, 1))
    assert(type(recipe.generate()) == type(""))