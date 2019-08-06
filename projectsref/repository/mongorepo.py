import pymongo
from projectsref.domain import contact


class MongoRepo:
    def __init__(self, connection_data):
        client = pymongo.MongoClient(
            host=connection_data['host'],
            username=connection_data['user'],
            password=connection_data['password'],
            authSource='admin')
        self.db = client[connection_data['dbname']]

    
    def list_contacts(self, filters=None):
        collection = self.db.contacts

        if filters is None:
            result = collection.find()
            return [contact.Contact.from_dict(d) for d in result]
        else:
            mongo_filters = {}
            for key, value in filters.items():
                key, operator = key.split('__')

                filter_value = mongo_filters.get(key, {})

                if key in {'is_client', 'is_primary'}:
                    value = self._get_bool(value)
                
                filter_value[f'${operator}'] = value
                mongo_filters[key] = filter_value

                result = collection.find(mongo_filters)
                return [contact.Contact.from_dict(d) for d in result]

    
    def _get_bool(self, value):
        if value in {'true', 'True'}:
            return True
        elif value in {'false', 'False'}:
            return False
        else:
            return bool(value)