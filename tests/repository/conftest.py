import pymongo
import pytest


def mg_is_responsive(ip, docker_setup):
    try:
        client = pymongo.MongoClient(
            host= docker_setup['mongo']['host'],
            username= docker_setup['mongo']['user'],
            password= docker_setup['mongo']['password'],
            authSource= 'admin')
        
        client.admin.command('ismaster')
        return True
    except pymongo.errors.ServerSelectionTimeoutError:
        return False


@pytest.fixture(scope='session')
def mg_client(docker_ip, docker_services, docker_setup):
    docker_services.wait_until_responsive(
        timeout= 30.0, pause=0.1,
        check= lambda: mg_is_responsive(docker_ip, docker_setup)
    )

    client = pymongo.MongoClient(
            host= docker_setup['mongo']['host'],
            username= docker_setup['mongo']['user'],
            password= docker_setup['mongo']['password'],
            authSource= 'admin')
    
    yield client

    client.close()


@pytest.fixture(scope='session')
def mg_database_empty(mg_client, docker_setup):
    db = mg_client[docker_setup['mongo']['dbname']]

    yield db

    mg_client.drop_database(docker_setup['mongo']['dbname'])


@pytest.fixture(scope='function')
def mg_data():
    #ToDo: create some data for tests
    return [
        {'code' : '9245cc17-7dfe-42c2-8929-0614a259dea5',
        'fname' : "Fname1",
        'lname' : "Lname1",
        'email' : "fname.lname1@talan.com",
        'phone' : "0100000001",
        'is_client' : False,
        'is_primary' : True},
        {'code' : '211f70f3-f667-4960-85bd-0941eaa9a362',
        'fname' : "Fname2",
        'lname' : "Lname2",
        'email' : "fname.lname2@talan.com",
        'phone' : "0100000002",
        'is_client' : False,
        'is_primary' : False},
        {'code' : 'd937c48c-5b85-4d28-891c-bd7730ff6290',
        'fname' : "Fname3",
        'lname' : "Lname3",
        'email' : "fname.lname3@talan.com",
        'phone' : "0100000003",
        'is_client' : True,
        'is_primary' : False},
        {'code' :'7fe224f5-5943-4650-a484-9987fa5ebcbf',
        'fname' : "Fname4",
        'lname' : "Lname4",
        'email' : "fname.lname4@talan.com",
        'phone' : "0100000004",
        'is_client' : True,
        'is_primary' : True},
        {'code' : '059a2d9c-08c9-4a74-9a8d-3e1213f18f69',
        'fname' : "Fname5",
        'lname' : "Lname5",
        'email' : "fname.lname5@talan.com",
        'phone' : "0100000005",
        'is_client' : False,
        'is_primary' : True}]


@pytest.fixture(scope='function')
def mg_database(mg_database_empty, mg_data):
    contacts_collection = mg_database_empty.contacts

    contacts_collection.insert_many(mg_data)

    yield mg_database_empty

    contacts_collection.delete_many({})
