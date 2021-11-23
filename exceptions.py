class CustomException(Exception):
    pass

class AuthorizeException(CustomException):
    pass

class ValueNotFoundException(CustomException):
    pass

class ForbiddenException(CustomException):
    pass