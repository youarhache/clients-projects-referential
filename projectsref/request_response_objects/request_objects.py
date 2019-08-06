import collections

class InvalidRequestObj:

    def __init__(self):
        self.errors = []


    def add_error(self, parameter, message):
        self.errors.append({'parameter':parameter, 'message': message})

    
    def has_errors(self):
        return len(self.errors) > 0


    def __bool__(self):
        return False


class ValidRequestObj:

    def __bool__(self):
        return True


class ContactsListRequestObj(ValidRequestObj):

    accepted_filters = ['code__eq', 'fname__eq', 'lname__eq', 'email__eq', 'is_client__eq', 'is_primary__eq']

    def __init__(self, filters=None):
        self.filters = filters


    @classmethod
    def from_dict(cls, dico):
        invalid_req = InvalidRequestObj()
        if 'filters' in dico:
            if not isinstance(dico['filters'], collections.Mapping):
                invalid_req.add_error('filters', 'Is not a dictionnary')
                return invalid_req
            for key, value in dico['filters'].items():
                if key not in cls.accepted_filters:
                    invalid_req.add_error('filters', f'Key {key} cannot be used')
        if invalid_req.has_errors():
            return invalid_req
        return cls(filters=dico.get('filters', None))
