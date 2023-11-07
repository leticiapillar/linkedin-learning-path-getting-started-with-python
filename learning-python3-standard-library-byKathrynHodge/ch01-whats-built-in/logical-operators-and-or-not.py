# 01 Python Logical Operators: And, Or, Not:

# What is a Boolean?
isTrue = True
isFalse = False
print(f"is true : {isTrue}")
print(f"is false: {isFalse}")


# Logical Operators -> Special Operators for Booleans

# AND
# true and true --> true
# false and true --> false
# true and false --> false
# false and false --> false
print("true and true  :", isTrue and isTrue)
print("false and true :", isFalse and isTrue)
print("true and false :", isTrue and isFalse)
print("false and false:", isFalse and isFalse)


# OR
# true or true --> true
# false or true --> true
# true or false --> true
# false or false --> false
print("true or true  :", isTrue or isTrue)
print("false or true :", isFalse or isTrue)
print("true or false :", isTrue or isFalse)
print("false or false:", isFalse or isFalse)


# NOT
# true --> false
# false --> true
print("not true :", not isTrue)
print("not false:", not isFalse)
