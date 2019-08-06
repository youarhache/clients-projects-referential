class ResponseSuccess:

    SUCCESS = 'Success'

    def __init__(self, value=None):
        self.value = value
        self.type = self.SUCCESS

    def __bool__(self):
        return True


class ResponseFailure:

    RESOURCE_ERROR = 'ResourceError'
    PARAMETERS_ERROR = 'ParametersError'
    SYSTEM_ERROR = 'SystemError'

    def __init__(self, my_type, message):
        self.type = my_type
        self.message = self._format_message(message)


    def _format_message(self, message):
        if isinstance(message, Exception):
            return f"{message.__class__.__name__}: {message}"
        return message


    @property
    def value(self):
        return {"type": self.type, "message": self.message}


    def __bool__(self):
        return False

    
    @classmethod
    def build_from_invalid_request_object(cls, invalid_request):
        message = "\n".join([f"{err['parameter']}: {err['message']}" for err in invalid_request.errors])
        return cls(cls.PARAMETERS_ERROR, message)

    
    @classmethod
    def build_resource_error(cls, message=None):
        return cls(cls.RESOURCE_ERROR, message)


    @classmethod
    def build_system_error(cls, message=None):
        return cls(cls.SYSTEM_ERROR, message)


    @classmethod
    def build_parameters_error(cls, message=None):
        return cls(cls.PARAMETERS_ERROR, message)