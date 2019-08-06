import pytest
from projectsref.repository import mongorepo


pytestmark = pytest.mark.integration

def test_contacts_list_without_filters(docker_setup, mg_data, mg_database):
    repo = mongorepo.MongoRepo(docker_setup["mongo"])
    repo_contacts = repo.list_contacts()

    assert set([c.code for c in repo_contacts]) == set([d["code"] for d in mg_data])


def test_contacts_list_code_filter(docker_setup, mg_data, mg_database):
    repo = mongorepo.MongoRepo(docker_setup["mongo"])
    repo_contacts = repo.list_contacts(filters= {'code__eq': '211f70f3-f667-4960-85bd-0941eaa9a362'})

    assert set([c.code for c in repo_contacts]) == set(['211f70f3-f667-4960-85bd-0941eaa9a362'])


def test_contacts_list_lname_filter(docker_setup, mg_data, mg_database):
    repo = mongorepo.MongoRepo(docker_setup["mongo"])
    repo_contacts = repo.list_contacts(filters= {'lname__eq': 'Lname1'})

    assert set([c.code for c in repo_contacts]) == set(['9245cc17-7dfe-42c2-8929-0614a259dea5'])
    assert repo_contacts[0].lname == "Lname1"


def test_contacts_list_fname_filter(docker_setup, mg_data, mg_database):
    repo = mongorepo.MongoRepo(docker_setup["mongo"])
    repo_contacts = repo.list_contacts(filters= {'fname__eq': 'Fname2'})

    assert [c.code for c in repo_contacts] == ['211f70f3-f667-4960-85bd-0941eaa9a362']
    assert repo_contacts[0].fname == "Fname2"


def test_contacts_list_full_name_filter(docker_setup, mg_data, mg_database):
    repo = mongorepo.MongoRepo(docker_setup["mongo"])
    repo_contacts = repo.list_contacts(filters= {'lname__eq': 'Lname3'
                                                ,'fname__eq': 'Fname3'})

    assert [c.code for c in repo_contacts] == ['d937c48c-5b85-4d28-891c-bd7730ff6290']
    assert repo_contacts[0].lname == "Lname3"
    assert repo_contacts[0].fname == "Fname3"


def test_contacts_list_is_client_filter(docker_setup, mg_data, mg_database):
    repo = mongorepo.MongoRepo(docker_setup["mongo"])
    repo_contacts = repo.list_contacts(filters= {'is_client__eq': True})

    assert set([c.code for c in repo_contacts]) == set(['d937c48c-5b85-4d28-891c-bd7730ff6290', 
                                                        '7fe224f5-5943-4650-a484-9987fa5ebcbf'])

def test_contacts_list_is_primary_filter(docker_setup, mg_data, mg_database):
    repo = mongorepo.MongoRepo(docker_setup["mongo"])
    repo_contacts = repo.list_contacts(filters= {'is_primary__eq': 'false'})

    assert set([c.code for c in repo_contacts]) == set(['211f70f3-f667-4960-85bd-0941eaa9a362',
                                                        'd937c48c-5b85-4d28-891c-bd7730ff6290'])
    assert repo_contacts[0].is_primary == False