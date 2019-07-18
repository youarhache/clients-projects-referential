import json

class ContactJsonEncoder(json.JSONEncoder):
    """Encodes a contact model to json"""

    def default(self, o):
        try:
            to_serialize = {
                            'code' : str(o.code), 
                            'fname' : o.fname, 
                            'lname' : o.lname, 
                            'email' : o.email,
                            'phone' : o.phone,
                            'is_client' : o.is_client,
                            'is_primary' : o.is_primary
                        }
            return to_serialize
        except AttributeError:
            return super().default(o)