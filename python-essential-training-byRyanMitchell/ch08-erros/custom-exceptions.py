# 03 Custom Exceptions

print("Custom Exceptions")
class CustomException(Exception):
    pass

def causeError():
    raise CustomException()
# causeError()
# CustomException:

def causeError():
    raise CustomException("You called the causeError function!")
# causeError()
# CustomException: You called the causeError function!

print()
# Adding Attributes
print("Adding Attributes")

class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self,):
        super().__init__(f"Status code: {self.statusCode} and message is: {self.message}")

class NotFound(HttpException):
    statusCode = 404
    message = "Resource not found"

class ServerError(HttpException):
    statusCode = 500
    message = "The server messed up!"

def raiseNotFoundError():
    raise NotFound()

def raiseServerError():
    raise ServerError()

# raiseNotFoundError()
# NotFound: Status code: 404 and message is: Resource not found

raiseServerError()
# ServerError: Status code: 500 and message is: The server messed up!