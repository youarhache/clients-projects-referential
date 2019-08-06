import json
from flask import Blueprint, request, Response
from projectsref import usecases as uc
from projectsref import serializers as ser
from projectsref.request_response_objects import request_objects as req, response_objects as resp
from projectsref.repository import mongorepo as mr

blueprint = Blueprint('projectsref', __name__)

STATUS_CODES = {
                resp.ResponseSuccess.SUCCESS: 200,
                resp.ResponseFailure.RESOURCE_ERROR: 404,
                resp.ResponseFailure.PARAMETERS_ERROR: 400,
                resp.ResponseFailure.SYSTEM_ERROR: 500}

#ToDo : Setting up the reposetup = {
connection_data = {            
                    'dbname': "talanprojectsdb",
                    'user': "root",
                    'password': "projectrefdb",
                    'host': '192.168.99.100', # to be modified
                    'port': 27017}


@blueprint.route('/api/contacts', methods=['GET'])
def get_contacts():
    qry_params = {'filters': {}}
    for arg, values in request.args.items():
        if arg.startswith('filter_'):
            qry_params['filters'][arg.replace('filter_', '')] = values

    my_req = req.ContactsListRequestObj.from_dict(qry_params)

    repo = mr.MongoRepo(connection_data)
    usecase = uc.contact_usecases.ContactListUseCase(repo)

    my_resp = usecase.execute(my_req)
    return Response(json.dumps(my_resp.value, cls = ser.contact_json_serializer.ContactJsonEncoder),
                     mimetype='application/json', 
                     status=STATUS_CODES[my_resp.type])