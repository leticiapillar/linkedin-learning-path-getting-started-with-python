#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("It is a basic function")


# TODO: function that takes arguments
def func2(arg1, arg2):
    print("arg1:", arg1, " arg2: ", arg2)


# TODO: function that returns a value
def cube(x):
    return x * x * x


# TODO: function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


# TODO: function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

def multily_multi_add(arg1, *args):
    result = 0
    for x in args:
        result = result + x
    return arg1 * result

# call func1 and print message inside function
func1()
# call func1 and print message inside function, 
# btw func1 and doesn't have return value, by default it return None, so print() prints None
print("function func1 doesn't have return value, so external print function prints: ",  func1())
# print None because doesn't call func1 as a function, forgot () in the end
print(func1)


# call func2 and print the args values
func2(12, 34)
# call func2 and print the args values, 
# btw func2 and doesn't have return value, by default it return None, so print() prints None
print("external print function prints:", func2(12, 34))
# call cube function and return the x value multipy 3 times
print("cube valye by x is:", cube(3))


# call power function passing num argument
print("the power result is:", power(2))
# call power function passing num and x arguments
print("the power result is:", power(2, 3))
# call power function passing num and x arguments, but informed name of argument when call function
print("the power result is:", power(num=2, x=3))
# call power function passing num and x arguments, but informed name of argument inversed when call function
print("the power result is:", power(x=3, num=2))

# call multi_add passing 1 argument value
print("the sum of (1) is:", multi_add(1))
# call multi_add passing 3 argument value
print("the sum of (1,2,3) is:", multi_add(1,2,3))
# call multi_add passing 5 argument value
print("the sum of (1,2,3,4,5) is:", multi_add(1,2,3,40,21))

# call msg_multi_add passing 1 argument value
print("the multiply by 2 of sum (1,2,3) is:", multily_multi_add(2, 1,2,3))
