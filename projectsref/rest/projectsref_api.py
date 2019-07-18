import json
from flask import Blueprint, Request, Response
from projectsref import usecases as uc
from projectsref import serializers as ser

blueprint = Blueprint('projectsref', __name__)

#Setting up the database

@blueprint.route('/api/contacts', methods=['GET'])
def get_contacts():
    usecase = uc.contact_usecases.ContactListAllUseCase(None)
    data = usecase.execute()
    return Response(json.dumps(data, cls = ser.contact_json_serializer.ContactJsonEncoder),
                     mimetype='application/json', 
                     status=200)