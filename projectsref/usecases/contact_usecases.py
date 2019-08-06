from projectsref.request_response_objects import response_objects as resp

class ContactListUseCase:
    """Use case : list of contacts, clients and internal"""
    
    def __init__(self, repo):
        self._repo = repo

    
    def execute(self, request):
        if not request:
            return resp.ResponseFailure.build_from_invalid_request_object(request)
        try:
            data = self._repo.list_contacts(filters = request.filters)
            return resp.ResponseSuccess(data)
        except Exception as e:
            return resp.ResponseFailure.build_system_error(f"{e.__class__.__name__}: {e}")