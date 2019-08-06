import pymongo

setup = {
            'dbname': "talanprojectsdb",
            'user': "root",
            'password': "projectrefdb",
            'host': '192.168.99.100', # to be modified
            'port': 27017
        }


client = pymongo.MongoClient(host=setup['host'],
                            username=setup['user'],
                            password=setup['password'],
                            authSource="admin",
                            serverSelectionTimeoutMS=60000)


db = client[setup["dbname"]]

contacts_data = [
        {'code' : '9245cc17-7dfe-42c2-8929-0614a259dea5',
        'fname' : "Fname1",
        'lname' : "Lname1",
        'email' : "fname.lname1@talan.com",
        'phone' : "0100000001",
        'is_client' : False,
        'is_primary' : True},
        {'code' : '211f70f3-f667-4960-85bd-0941eaa9a362',
        'fname' : "Fname2",
        'lname' : "Lname2",
        'email' : "fname.lname2@talan.com",
        'phone' : "0100000002",
        'is_client' : False,
        'is_primary' : False},
        {'code' : 'd937c48c-5b85-4d28-891c-bd7730ff6290',
        'fname' : "Fname3",
        'lname' : "Lname3",
        'email' : "fname.lname3@talan.com",
        'phone' : "0100000003",
        'is_client' : True,
        'is_primary' : False},
        {'code' :'7fe224f5-5943-4650-a484-9987fa5ebcbf',
        'fname' : "Fname4",
        'lname' : "Lname4",
        'email' : "fname.lname4@talan.com",
        'phone' : "0100000004",
        'is_client' : True,
        'is_primary' : True},
        {'code' : '059a2d9c-08c9-4a74-9a8d-3e1213f18f69',
        'fname' : "Fname5",
        'lname' : "Lname5",
        'email' : "fname.lname5@talan.com",
        'phone' : "0100000005",
        'is_client' : False,
        'is_primary' : True}]

contacts_collection = db.contacts

contacts_collection.insert_many(contacts_data)