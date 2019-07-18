from datetime import datetime

class Company:
    """Defines the company in which the projects are taking place"""

    def __init__(self, code : str,
                 name : str,
                 group : str,
                 last_visited : datetime):
        self.code = code
        self.name = name
        self.group = group
        self.last_visited = last_visited
    

    @classmethod
    def from_dict(cls, dico):
        return cls(
                    code = dico["code"],
                    name = dico["name"],
                    group = dico["group"],
                    last_visited = dico["last_visited"]
        )

    
    def to_dict(self):
        return {
            "code" : self.code,
            "name" : self.name,
            "group" : self.group,
            "last_visited" : self.last_visited
        }


    def __eq__(self, other):
        return self.to_dict() == other.to_dict()