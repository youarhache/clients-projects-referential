import uuid
from projectsref.domain import contact

def test_contact_model_init():
    code = str(uuid.uuid4())
    cntct = contact.Contact(code, 
                            fname = 'First Name', 
                            lname = 'LastName', 
                            email = 'firstname.lastname@talan.com',
                            phone = '0600000000',
                            is_client = True,
                            is_primary= True)
    assert cntct.code == code
    assert cntct.fname == 'First Name'
    assert cntct.lname == 'LastName'
    assert cntct.email == 'firstname.lastname@talan.com'


def test_contact_model_form_dict():
    code = str(uuid.uuid4())
    cntct = contact.Contact.from_dict(
                        {
                            'code' : code, 
                            'fname' : 'First Name', 
                            'lname' : 'LastName', 
                            'email' : 'firstname.lastname@talan.com',
                            'phone' : '0600000000',
                            'is_client' : True,
                            'is_primary' : True
                        })
    assert cntct.code == code
    assert cntct.fname == 'First Name'
    assert cntct.lname == 'LastName'
    assert cntct.email == 'firstname.lastname@talan.com'


def test_contact_model_to_dict():
    code = str(uuid.uuid4())
    dico = {
            'code' : code, 
            'fname' : 'First Name', 
            'lname' : 'LastName', 
            'email' : 'firstname.lastname@talan.com',
            'phone' : '0600000000',
            'is_client' : True,
            'is_primary' : True
        }
    cntct = contact.Contact.from_dict(dico)
    assert cntct.to_dict() == dico


def test_contact_model_equal():
    code = str(uuid.uuid4())
    dico = {
            'code' : code, 
            'fname' : 'First Name', 
            'lname' : 'LastName', 
            'email' : 'firstname.lastname@talan.com',
            'phone' : '0600000000',
            'is_client' : True,
            'is_primary' : True
        }
    cntct1 = contact.Contact.from_dict(dico)
    cntct2 = contact.Contact.from_dict(dico)
    assert cntct1 == cntct2