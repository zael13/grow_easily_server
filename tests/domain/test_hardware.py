import uuid
import pytest
from unittest import mock
from datetime import datetime
from grow_easily_server.domain.hardware import HWType, Hardware, HttpServer, \
    DigitalWriter, DigitalReader, AnalogReader, Dht

START_TIME = datetime(2007, 12, 5, 22, 30).timestamp()


def test_hardware_model_init():
    hardware_id = str(uuid.uuid4())
    hardware = Hardware(hardware_id, "Temperature1",
                        "DHT_TEMPERATURE", [1, 2], 20.5, 2.0)

    assert hardware.hardware_id == hardware_id
    assert hardware.name == "Temperature1"
    assert hardware.hw_type == "DHT_TEMPERATURE"
    assert hardware.pins == [1, 2]
    assert hardware.value == 20.5
    assert hardware.delta == 2.0


def test_hardware_model_from_dict():
    hardware_id = str(uuid.uuid4())
    hardware = Hardware.from_dict(
        {
            'hardware_id': hardware_id,
            'name': "Temperature1",
            'hw_type': "DHT_TEMPERATURE",
            'pins': [1, 2],
            'value': 20.5,
            'delta': 2.0,
        }
    )

    assert hardware.hardware_id == hardware_id
    assert hardware.name == "Temperature1"
    assert hardware.hw_type == "DHT_TEMPERATURE"
    assert hardware.pins == [1, 2]
    assert hardware.value == 20.5
    assert hardware.delta == 2.0


def test_hardware_model_to_dict():
    hardware_id = str(uuid.uuid4())
    hardware_dict = {
        'hardware_id': hardware_id,
        'name': "Temperature1",
        'hw_type': "DHT_TEMPERATURE",
        'pins': [1, 2],
        'value': 20.5,
        'delta': 2.0,
    }

    hardware = Hardware.from_dict(hardware_dict)

    assert hardware.to_dict() == hardware_dict


def test_hardware_model_comparison():
    hardware_id = str(uuid.uuid4())
    hardware_dict = {
        'hardware_id': hardware_id,
        'name': "Temperature1",
        'hw_type': "DHT_TEMPERATURE",
        'pins': [1, 2],
        'value': 20.5,
        'delta': 2.0,
    }

    hardware1 = Hardware.from_dict(hardware_dict)
    hardware2 = Hardware.from_dict(hardware_dict)

    assert hardware1 == hardware2


def test_hardware_on_should_raise_an_exeption():
    hw = Hardware(str(uuid.uuid4()),
                  "Temperature1", "DHT_TEMPERATURE", [1, 2], 20.5, 2.0)

    with pytest.raises(NotImplementedError):
        hw.write(Hardware.HW_ON)


def test_hardware_off_should_raise_an_exeption():
    hw = Hardware(str(uuid.uuid4()),
                  "Temperature1", "DHT_TEMPERATURE", [1, 2], 20.5, 2.0)

    with pytest.raises(NotImplementedError):
        hw.read()


def test_hardware_factory_should_return_http_server_class():
    hw = Hardware.factory(str(uuid.uuid4()),
                  "Temperature1", HWType.HTTP_SERVER, [1, 2], 20.5, 2.0)

    assert isinstance(hw, HttpServer)


def test_hardware_factory_should_return_digital_writer_class():
    hw = Hardware.factory(str(uuid.uuid4()),
                  "Temperature1", HWType.DIGITAL_WRITER, [5], 20.5, 2.0)

    assert isinstance(hw, DigitalWriter)


def test_hardware_factory_should_return_digital_reader_class():
    hw = Hardware.factory(str(uuid.uuid4()),
                  "Temperature1", HWType.DIGITAL_READER, [1, 2], 20.5, 2.0)

    assert isinstance(hw, DigitalReader)


def test_hardware_factory_should_return_digital_reader_class():
    hw = Hardware.factory(str(uuid.uuid4()),
                  "Temperature1", HWType.DIGITAL_READER, [1, 2], 20.5, 2.0)

    assert isinstance(hw, DigitalReader)


def test_hardware_factory_should_return_analog_reader_class():
    hw = Hardware.factory(str(uuid.uuid4()),
                  "Temperature1", HWType.ANALOG_READER, [1, 2], 20.5, 2.0)

    assert isinstance(hw, AnalogReader)


def test_hardware_factory_should_return_dht_class():
    hw = Hardware.factory(str(uuid.uuid4()),
                  "Temperature1", HWType.DHT_TEMPERATURE, [1, 2], 20.5, 2.0)

    assert isinstance(hw, Dht)

    hw = Hardware.factory(str(uuid.uuid4()),
                      "Temperature1", HWType.DHT_HUMIDITY, [1, 2], 20.5, 2.0)

    assert isinstance(hw, Dht)


def test_hardware_factory_should_raise_value_error_if_there_is_no_such_type():
    with pytest.raises(ValueError):
        Hardware.factory(str(uuid.uuid4()), "Temperature1",
                              "fake", [1, 2], 20.5, 2.0)


def test_digital_writer_init_should_raise_value_error_if_there_is_no_pins():
    with pytest.raises(ValueError):
        Hardware.factory(str(uuid.uuid4()), "Temperature1",
                          HWType.DIGITAL_WRITER, None)


def test_digital_writer_init_should_raise_value_error_if_there_is_more_than_1_pins():
    with pytest.raises(ValueError):
        Hardware.factory(str(uuid.uuid4()), "Temp", HWType.DIGITAL_WRITER, [1, 2])


@mock.patch('RPi.GPIO')
def test_digital_writer_init_should_set_up_bcm_mode(mock_gpio):
    mock_gpio.getmode().return_value = 1
    mock_gpio.setmode(11).return_value = None

    Hardware.factory(str(uuid.uuid4()), "Temp", HWType.DIGITAL_WRITER, [1])
    mock_gpio.setmode.assert_any_call(11)


def test_digital_writer_write_should_set_pin_to_1_after_write_on():
    hw = Hardware.factory(str(uuid.uuid4()), "Temp", HWType.DIGITAL_WRITER, [1])

    hw.write(Hardware.HW_ON)
    assert hw.value == Hardware.HW_ON


def test_digital_writer_write_should_set_pin_to_0_after_write_off():
    hw = Hardware.factory(str(uuid.uuid4()), "Temp", HWType.DIGITAL_WRITER, [1])

    hw.write(Hardware.HW_OFF)
    assert hw.value == Hardware.HW_OFF


def test_digital_writer_write_should_raise_value_error_in_other_than_on_or_off():
    hw = Hardware.factory(str(uuid.uuid4()), "Temp", HWType.DIGITAL_WRITER, [1])

    with pytest.raises(ValueError):
        hw.write("fake")


def test_digital_writer_read_should_return_value():
    hw = Hardware.factory(str(uuid.uuid4()), "Temp", HWType.DIGITAL_WRITER, [1])

    hw.write(Hardware.HW_ON)
    assert hw.read() == Hardware.HW_ON


#def test_digital_reader_init_should_raise_value_error_if_there_is_no_pins():
#    with pytest.raises(ValueError):
#        Hardware.factory(str(uuid.uuid4()), "Temp", HWType.DIGITAL_READER, None)
