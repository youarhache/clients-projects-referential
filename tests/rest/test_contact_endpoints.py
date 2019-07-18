import pytest
import json
from unittest import mock
from projectsref.domain import contact

cntct_dico = {"code" : '50975341-f4f1-4b53-9906-f789ceb31eba', 
        "fname" : 'First Name', 
        "lname" : 'LastName', 
        "email" : 'firstname.lastname@talan.com',
        "phone" : '0600000000',
        "is_client" : True,
        "is_primary": True}
cntcts =  [contact.Contact.from_dict(cntct_dico)]

@mock.patch('projectsref.usecases.contact_usecases.ContactListAllUseCase')
def test_get_contacts(mock_usecase, client):
    mock_usecase().execute.return_value = cntcts
    http_response = client.get('/api/contacts')

    mock_usecase().execute.assert_called_with()
    assert json.loads(http_response.data.decode('utf-8')) == [cntct_dico]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'