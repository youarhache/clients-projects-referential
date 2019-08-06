import pytest
import json
from unittest import mock
from projectsref.domain import contact
from projectsref.request_response_objects import request_objects as req, response_objects as resp

cntct_dico = {"code" : '50975341-f4f1-4b53-9906-f789ceb31eba', 
        "fname" : 'First Name', 
        "lname" : 'LastName', 
        "email" : 'firstname.lastname@talan.com',
        "phone" : '0600000000',
        "is_client" : True,
        "is_primary": True}
cntcts =  [contact.Contact.from_dict(cntct_dico)]

@mock.patch('projectsref.usecases.contact_usecases.ContactListUseCase')
def test_get_contacts(mock_usecase, client):
    mock_usecase().execute.return_value = resp.ResponseSuccess(cntcts)
    http_response = client.get('/api/contacts')

    mock_usecase().execute.assert_called
    args, kwargs = mock_usecase().execute.call_args
    assert args[0].filters == {}
    assert json.loads(http_response.data.decode('utf-8')) == [cntct_dico]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'


@mock.patch('projectsref.usecases.contact_usecases.ContactListUseCase')
def test_get_contacts_with_filters(mock_usecase, client):
    mock_usecase().execute.return_value = resp.ResponseSuccess(cntcts)
    http_response = client.get('/api/contacts?filter_code__eq=50975341-f4f1-4b53-9906-f789ceb31eba&filter_is_client__eq=1')
    args, kwargs = mock_usecase().execute.call_args
    assert args[0].filters == {'code__eq': '50975341-f4f1-4b53-9906-f789ceb31eba', 'is_client__eq' : '1'}
    assert json.loads(http_response.data.decode('utf-8')) == [cntct_dico]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'
