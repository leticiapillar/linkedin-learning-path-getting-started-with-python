# 01 Errors and Exceptions


# Stacktrace Error
# print(1 / 0)
# ZeroDivisionError: division by zero

def causeError():
    return 1/0
# causeError()
# File "../../errors-and-exceptions.py", line 8, in <module>
#       causeError()
# File "../../errors-and-exceptions.py", line 7, in causeError
#     return 1/0
#            ~^~
# ZeroDivisionError: division by zero

def callCauseError():
    return causeError()

# callCauseError()
# File "../../ch08-erros/errors-and-exceptions.py", line 19, in <module>
#   callCauseError()
# File "../../ch08-erros/errors-and-exceptions.py", line 17, in callCauseError
#   return causeError()
#            ^^^^^^^^^^^^
# File "../../ch08-erros/errors-and-exceptions.py", line 7, in causeError
#   return 1/0
#            ~^~
# ZeroDivisionError: division by zero

# Try / Except
try:
    1/0
except Exception as e:
    print(type(e))
# <class