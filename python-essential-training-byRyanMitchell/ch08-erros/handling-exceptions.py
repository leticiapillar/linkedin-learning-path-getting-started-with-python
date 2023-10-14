# 02 Handling Exceptions
import time

# Try / Except
print("Try / Except")
def causeError():
    try:
        return 1/0
    except Exception as e:
        return e
print("calls causeError function:", causeError())

def causeError():
    try:
        return 1/0
    except Exception:
        print("There was some sort of error!")
causeError()

print()
# Finally
print("Finally")

def causeError():
    try:
        return 1/0
    except Exception:
        print("There was some sort of error!")
    finally:
        print("This will always execute!")
causeError()

def causeError():
    try:
        return 1/1
    except Exception:
        print("There was some sort of error!")
    finally:
        print("This will always execute!")
causeError()

def causeError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception:
        print("There was some sort of error!")
    finally:
        print(f"Function took {time.time() - start} seconds to execute" )
causeError()

print()
# Catching Exceptions by Type
print("Catching Exceptions by Type")

def causeError():
    try:
        return 1/0
    except ZeroDivisionError as e:
        print("There was zero division error!")
    except Exception:
        print("There was general exception error!")
causeError()

def causeError():
    try:
        return 1 + "a"
    except TypeError:
        print("There was type error!")
    except ZeroDivisionError:
        print("There was zero division error!")
    except Exception:
        print("There was general exception error!")
causeError()

print()
# Custom Decorators
print("Custom Decorators")
def handleException(func):
    def wrapper():
        try:
            func()
        except TypeError:
            print("HandleException: There was type error!")
        except ZeroDivisionError:
            print("HandleException: There was zero division error!")
        except Exception:
            print("HandleException: There was general exception error!")
    return wrapper

@handleException
def causeError():
    return 1/0
causeError()

print()
# Raising Exceptions
print("Raising Exceptions")

@handleException
def raiseError():
    raise Exception()
raiseError()

def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print("HandleException: There was type error!")
        except ZeroDivisionError:
            print("HandleException: There was zero division error!")
        except Exception:
            print("HandleException: There was general exception error!")
    return wrapper

@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print("n equals to:", n)
raiseError(0)
raiseError(1)
raiseError("a")
