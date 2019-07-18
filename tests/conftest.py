import pytest

from projectsref.app import create_app
from projectsref.flask_settings import TestConfig

@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)