#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# result = 10/0
# print(result)
# Throws this exception: ZeroDivisionError: division by zero

# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
    result = 10/0
except:
    print("The program didn't work!")


# TODO: You can also catch specific exceptions
try:
    number = input("What should you divide 10 by? ")
    result = 10 / int(number)
    print(f"10 divide by {number} is {result}")
except ZeroDivisionError as e:
    print("The program didn't work, you cannot division by zero!")
except ValueError as e:
    print("The program didn't work, you didn't type a number!")
finally:
    print("This line always printed!")
