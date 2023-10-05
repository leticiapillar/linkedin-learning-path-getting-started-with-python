# Functions

print("Hello, Wolrd!")

def mutiplyByThree(val):
    return 3 * val
print("call function mutiplyByThree:", mutiplyByThree(4))

def mutiply(val1, val2):
    return val1 * val2
print("call function mutiply:", mutiply(3, 4))

nums = [1,2,3]
print("nums list:", nums)
def appendFour(myList):
    myList.append(4)
appendFour(nums)
print("nums list after appendfour function:", nums)


# None
msg = "It is a message 1"
print("External print funcation return value:",print("Prints messages value:", msg))

# print(None + 1) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
a = None
print(type(a))


