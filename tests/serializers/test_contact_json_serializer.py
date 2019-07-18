import json
import uuid
from projectsref.serializers import contact_json_serializer as ser
from projectsref.domain import contact as c


def test_serialize_domain_contact():
    code = uuid.uuid4()

    cntct = c.Contact(code, 
                    fname = 'First Name', 
                    lname = 'LastName', 
                    email = 'firstname.lastname@talan.com',
                    phone = '0100000000',
                    is_client = False,
                    is_primary= True)

    target = f"""
                {{
                    "code" : "{code}", 
                    "fname" : "First Name", 
                    "lname" : "LastName", 
                    "email" : "firstname.lastname@talan.com",
                    "phone" : "0100000000",
                    "is_client" : false,
                    "is_primary" : true
                }}
     """

    serialized = json.dumps(cntct, cls = ser.ContactJsonEncoder)
    assert json.loads(target) == json.loads(serialized)


