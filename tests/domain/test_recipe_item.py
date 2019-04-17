import uuid
import pytest

from datetime import datetime, time, timedelta
from grow_easily_server.domain.module import HWType, \
    Event, Controller, CalendarEvent, DailyEvent, PeriodicEvent,\
    Hardware, Module

TEST_DATE = datetime(2007, 12, 5, 22, 30)
ONE_DAY = timedelta(days=1)
TEST_TIME = time(13, 30)
ONE_HOUR = timedelta(hours=1)


def test_calendar_event_should_raise_an_exception_if_not_datetime_object_used():
    with pytest.raises(TypeError):
        CalendarEvent(HWType.DHT_TEMPERATURE, "fake_item")


def test_daily_event_should_raise_an_exception_if_not_time_object_used():
    with pytest.raises(TypeError):
        DailyEvent(HWType.DHT_TEMPERATURE, "fake_item")


def test_daily_event_should_store_correct_daily_event():
    de = DailyEvent(HWType.DHT_TEMPERATURE, TEST_TIME)
    assert (de.day_time == TEST_TIME)


def test_periodic_event_should_raise_an_exception_if_not_time_object_used():
    with pytest.raises(TypeError):
        PeriodicEvent(HWType.DHT_TEMPERATURE, "fake_item")


def test_event_should_raise_an_exception_if_not_time_object_used_for_duration():
    with pytest.raises(TypeError):
        Event(HWType.DHT_TEMPERATURE, "fake_item")


def test_periodic_event_should_store_correct_periodic_event():
    pe = PeriodicEvent(HWType.DHT_TEMPERATURE, ONE_HOUR)
    assert (pe.period == ONE_HOUR)


def test_controller_event_should_store_correct_value():
    c = Controller(HWType.DHT_TEMPERATURE, 20)
    assert (c.value == 20)


# def test_hardware_should_raise_an_exception_if_code_is_not_uuid():
#     with pytest.raises(TypeError):
#         Hardware("fake", "test module", HWType.DHT_TEMPERATURE, 2)


def test_hardware_should_raise_an_exception_if_hw_type_is_not_hwtype_object():
    with pytest.raises(TypeError):
        Hardware(uuid.uuid4(), "test module", "fake", [1])


def test_hardware_should_raise_an_exception_if_module_name_is_not_string():
    with pytest.raises(TypeError):
        Hardware(uuid.uuid4(), 1, HWType.DHT_TEMPERATURE, [1])


def test_hardware_should_raise_an_exception_if_module_name_is_empty():
    with pytest.raises(ValueError):
        Hardware(uuid.uuid4(), "", HWType.DHT_TEMPERATURE, [1])


def test_hardware_should_raise_an_exception_if_module_pin_is_not_list_type():
    with pytest.raises(TypeError):
        Hardware(uuid.uuid4(), "test module", HWType.DHT_TEMPERATURE, 2)


def test_hardware_should_raise_an_exception_if_module_pin_is_less_than_zero():
    with pytest.raises(ValueError):
        Hardware(uuid.uuid4(), "test module", HWType.DHT_TEMPERATURE, [-1])


def test_hardware_should_raise_an_exception_if_module_pin_is_greater_than_16():
    with pytest.raises(ValueError):
        Hardware(uuid.uuid4(), "test module", HWType.DHT_TEMPERATURE, [17])


def test_hardware_should_raise_an_exception_if_one_of_modules_pins_is_greater_than_16():
    with pytest.raises(ValueError):
        Hardware(uuid.uuid4(), "test module", HWType.DHT_TEMPERATURE, [1, 2, 17])


def test_hardware_should_set_all_internal_values_according_init_arguments():
    code = uuid.uuid4()
    hw = Hardware(code, "test module", HWType.DHT_TEMPERATURE, [1, 2, 16])
    assert (hw.code == code)
    assert (hw.name == "test module")
    assert (hw.hw_type == HWType.DHT_TEMPERATURE)
    assert (hw.pins == [1, 2, 16])


def test_module_item_should_raise_an_exception_if_name_is_not_string_type():
    hw = Hardware(uuid.uuid4(), "test module", HWType.DHT_TEMPERATURE, [1, 2, 16])
    event = PeriodicEvent(HWType.DHT_TEMPERATURE, ONE_HOUR)
    with pytest.raises(TypeError):
        Module(uuid.uuid4(), 1, event, hw)


def test_module_item_should_raise_an_exception_if_name_is_empty():
    hw = Hardware(uuid.uuid4(), "test module", HWType.DHT_TEMPERATURE, [1, 2, 16])
    event = PeriodicEvent(HWType.DHT_TEMPERATURE, ONE_HOUR)
    with pytest.raises(ValueError):
        Module(uuid.uuid4(), "", event, hw)


def test_module_item_should_raise_an_exception_if_event_is_wrong_type():
    hw = Hardware(uuid.uuid4(), "test module", HWType.DHT_TEMPERATURE, [1, 2, 16])
    with pytest.raises(TypeError):
        Module(uuid.uuid4(), "test module", 1, hw)


def test_module_item_should_raise_an_exception_if_hardware_is_wrong_type():
    event = PeriodicEvent(HWType.DHT_TEMPERATURE, ONE_HOUR)
    with pytest.raises(TypeError):
        Module(uuid.uuid4(), "test module", event, "hw")


# def test_module_item_should_raise_an_exception_if_data_type_is_not_type():
#     event = PeriodicEvent(HWType.DHT_TEMPERATURE, ONE_HOUR)
#     hw = Hardware(uuid.uuid4(), "test module", HWType.DHT_TEMPERATURE, [1, 2, 16])
#
#     with pytest.raises(TypeError):
#         Module(uuid.uuid4(), "test module", event, hw, "string")


def test_module_should_set_all_internal_values_according_init_arguments():
    module_id = uuid.uuid4()
    event = PeriodicEvent(HWType.DHT_TEMPERATURE, ONE_HOUR)
    hw = Hardware(uuid.uuid4(), "test module", HWType.DHT_TEMPERATURE, [1, 2, 16])
    m = Module(module_id, "test module", event, hw, 20)

    print("Test 1")
    print(m)
    print("Test 2")
    print([m, m])

    assert (m.module_id == module_id)
    assert (m.name == "test module")
    assert (m.trigger_id == event)
    assert (m.hardware_id1 == hw)
    assert (m.value == 20)
