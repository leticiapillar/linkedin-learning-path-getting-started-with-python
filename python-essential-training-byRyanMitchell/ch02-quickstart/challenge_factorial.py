# Factorial Challenge
# The factorial function gives the number of possible arrangements of a set of items of length "n"
# 
# For example, there are 4! ("four factorial") or 24 ways to arrange four items, which can be calculated as: 4 * 3 * 2 * 1
# 
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# 
# etc.
# 
# In a set of 0 items (an empty set) there is only one way to arrange the items, therefore, 0! = 1
# 
# For the purposes of this exercise, factorials are only defined for positive integers (including 0)


# Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1

    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result

def factorial_recursive(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    
    return num * factorial_recursive(num - 1)


# return 120
f = factorial(5)
fr = factorial_recursive(5)
print(f"factorial: {f}, recursice: {fr}")

# return 720
f = factorial (6)
fr = factorial_recursive(6)
print(f"factorial: {f}, recursice: {fr}")

# return 1
f = factorial(0)
fr = factorial_recursive(0)
print(f"factorial: {f}, recursice: {fr}")

# return None
f = factorial(-2)
fr = factorial_recursive(-2)
print(f"factorial: {f}, recursice: {fr}")

# return None
f = factorial(1.2)
fr = factorial_recursive(1.2)
print(f"factorial: {f}, recursice: {fr}")

# return None
f = factorial('spam spam spam spam spam spam')
fr = factorial_recursive('spam spam spam spam spam spam')
print(f"factorial: {f}, recursice: {fr}")
