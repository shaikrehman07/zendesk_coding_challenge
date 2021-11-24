# Base class for custom exception
class CustomException(Exception):
    pass

#Exception if response status code is 401
class AuthorizeException(CustomException):
    pass

#Exception if response status code is 404
class ValueNotFoundException(CustomException):
    pass

#Exception if response status code is 403
class ForbiddenException(CustomException):
    pass