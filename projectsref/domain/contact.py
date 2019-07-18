class Contact:
    """Contact information being it internal or working at the client company"""
    
    
    def __init__(self, code : str, 
                fname : str, 
                lname : str, 
                email : str, 
                phone : str, 
                is_client = False, 
                is_primary = False):
        self.code = code
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.is_client = is_client
        self.is_primary = is_primary


    @classmethod
    def from_dict(cls, dico):
        return cls(
                    code = dico["code"],
                    fname = dico["fname"],
                    lname = dico["lname"],
                    email = dico["email"],
                    phone = dico["phone"],
                    is_client = dico["is_client"],
                    is_primary = dico["is_primary"]
        )


    def to_dict(self):
        return {
                    'code' : self.code, 
                    'fname' : self.fname, 
                    'lname' : self.lname, 
                    'email' : self.email,
                    'phone' : self.phone,
                    'is_client' : self.is_client,
                    'is_primary' : self.is_primary
                }
            

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()