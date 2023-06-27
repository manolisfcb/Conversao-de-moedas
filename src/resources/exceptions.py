
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidTokenError(Error):
    def __init__(self, message):
        self.message = message
        self.status_code = 401
        
    def __str__(self):
        return self.message

class NotValidTokenError(Error):
    """Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        self.status_code = 401
        
class ContratoJaExisteError(Error):
    """Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        self.status_code = 400
    def getmessage(self):
        return self.message
    
