import pytest
import uuid
from unittest import mock
from projectsref.domain import contact as c
from projectsref.usecases import contact_usecases as uc
from projectsref.request_response_objects import request_objects as req, response_objects as resp


@pytest.fixture
def domain_contacts():
    cntct1 = c.Contact(code=str(uuid.uuid4()),
                       fname = "Fname1",
                       lname = "Lname1",
                       email = "fname.lname1@talan.com",
                       phone = "0100000001",
                       is_client= False,
                       is_primary= True)
    cntct2 = c.Contact(code=str(uuid.uuid4()),
                       fname = "Fname2",
                       lname = "Lname2",
                       email = "fname.lname2@talan.com",
                       phone = "0100000002",
                       is_client= False,
                       is_primary= False)
    cntct3 = c.Contact(code=str(uuid.uuid4()),
                       fname = "Fname3",
                       lname = "Lname3",
                       email = "fname.lname3@talan.com",
                       phone = "0100000003",
                       is_client= True,
                       is_primary= False)
    cntct4 = c.Contact(code=str(uuid.uuid4()),
                       fname = "Fname4",
                       lname = "Lname4",
                       email = "fname.lname4@talan.com",
                       phone = "0100000004",
                       is_client= True,
                       is_primary= True)
    cntct5 = c.Contact(code=str(uuid.uuid4()),
                       fname = "Fname5",
                       lname = "Lname5",
                       email = "fname.lname5@talan.com",
                       phone = "0100000005",
                       is_client= False,
                       is_primary= True)
    
    return [cntct1, cntct2, cntct3, cntct4, cntct5]
    

def test_use_case_contact_list_without_filters(domain_contacts):
    repo = mock.Mock()
    repo.list_contacts.return_value = domain_contacts
    my_uc = uc.ContactListUseCase(repo)

    request = req.ContactsListRequestObj()
    response = my_uc.execute(request)

    assert bool(response) is True
    repo.list_contacts.assert_called_with(filters=None)
    assert response.value == domain_contacts


def test_use_case_contact_list_with_filters(domain_contacts):
    repo = mock.Mock()
    repo.list_contacts.return_value = domain_contacts
    my_uc = uc.ContactListUseCase(repo)

    qry_filters = {"code__eq": 1}
    request = req.ContactsListRequestObj.from_dict({"filters": qry_filters})
    response = my_uc.execute(request)

    assert bool(response) is True
    repo.list_contacts.assert_called_with(filters=qry_filters)
    assert response.value == domain_contacts


def test_use_case_contact_list_bad_request():
    repo = mock.Mock()
    my_uc = uc.ContactListUseCase(repo)
    request = req.ContactsListRequestObj.from_dict({"filters": 0})
    response = my_uc.execute(request)

    assert bool(response) is False
    assert response.value == {"type": resp.ResponseFailure.PARAMETERS_ERROR,
                             "message": "filters: Is not a dictionnary"}

def test_use_case_contact_list_generic_exception():
    repo = mock.Mock()
    repo.list_contacts.side_effect = Exception("Ceci est un message d'erreur")
    my_uc = uc.ContactListUseCase(repo)

    request = req.ContactsListRequestObj.from_dict({})
    response = my_uc.execute(request)

    assert bool(response) is False
    assert response.value == {"type": resp.ResponseFailure.SYSTEM_ERROR,
                            "message": "Exception: Ceci est un message d'erreur"}