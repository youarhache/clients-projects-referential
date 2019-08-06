import pytest

from projectsref.app import create_app
from projectsref.flask_settings import TestConfig

import os
import yaml
import tempfile

@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)


#adding a command line to isolate integration tests
def pytest_addoption(parser):
    parser.addoption("--integration", action="store_true",
    help="run integration tests")


def pytest_runtest_setup(item):
    if 'integration' in item.keywords and not item.config.getvalue("integration"):
        pytest.skip("need --integration option to run")


#fixtures for database docker container
@pytest.fixture(scope='session')
def docker_setup(docker_ip):
    return {
            'mongo':{
                    'dbname': 'talanprojectsdb',
                    'user': 'testuser',
                    'password': 'testp@ssword',
                    'host': docker_ip
            }
    }


@pytest.fixture(scope='session')
def docker_tmpfile():
    f = tempfile.mkstemp()
    
    yield f
    
    os.remove(f[1])


@pytest.fixture(scope='session')
def docker_compose_file(docker_tmpfile, docker_setup):
    content = {
        'version': '3.1',
        'services': {
            'mongo': {
                'restart': 'always',
                'image': 'mongo',
                'ports': ["27017:27017"],
                'environment': [
                    f'MONGO_INITDB_ROOT_USERNAME={docker_setup["mongo"]["user"]}',
                    f'MONGO_INITDB_ROOT_PASSWORD={docker_setup["mongo"]["password"]}'
                ]
            }
        }
    }

    with os.fdopen(docker_tmpfile[0], 'w') as f:
        f.write(yaml.dump(content))
    
    return docker_tmpfile[1]