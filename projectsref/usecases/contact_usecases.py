class ContactListAllUseCase:
    """Use case : list all the contacts, clients and internal"""
    
    def __init__(self, repo):
        self._repo = repo

    
    def execute(self):
        return self._repo.list_all_contacts()