# 01 The Anatomy of a Function
import math

# Functions
print("Functions")
def performOperation(num1, num2, operation):
    if operation == "sum":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2

result = performOperation(2,3, "sum")
print("sum:", result)

result = performOperation(2,3, "multiply")
print("multiply:", result)

print()
# Named Parameters
print("Named Parameters")
def performOperation(num1, num2, operation="sum"):
    if operation == "sum":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2

result = performOperation(2,3)
print("sum:", result)

result = performOperation(2,3, operation="multiply")
print("multiply:", result)

def performOperation(num1, num2, operation="sum", message="Default message"):
    print(message)
    if operation == "sum":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2

result = performOperation(2,3, operation="multiply", message="Message 1")
print("multiply:", result)

result = performOperation(2,3, message="Message 2", operation="multiply")
print("multiply:", result)

print()
# *args
def performOperation(*args):
    print("*args equals tuple type:", args)

performOperation(1,2,3)

def performOperation(*args, **kwargs):
    print("*args equals tuple type       :", args)
    print("*kwargs equals dictionary type:", kwargs)

performOperation(1,2,3, operation="sum")

def performOperation(*args, operation="sum"):
    if operation == "sum":
        return sum(args)
    if operation == "multiply":
        return math.prod(args)

result = performOperation(1,2,3,4,5, operation="sum")
print("sum of *args:", result)

def performOperation(*args, **kwkwargs):
    if kwkwargs.get("operation") == "sum":
        return sum(args)
    if kwkwargs.get("operation") == "multiply":
        return math.prod(args)

result = performOperation(1,2,3,4,5, operation="sum")
print("sum of *args and **kwkwargs:", result)
result = performOperation(1,2,3,4,5, operation="multiply")
print("multiply of *args and **kwkwargs:", result)
