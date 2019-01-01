import pytest


from grow_easily_server.app import create_app
from grow_easily_server.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)
