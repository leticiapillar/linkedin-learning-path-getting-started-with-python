# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print("Numbr integer :", myint)
print("Number float  :", myfloat)
print("String        :", mystr)
print("Boolean       :", mybool)
print("Sequence list :", mylist)
print("Sequence typle:", mytuple)
print("Dictionary    :", mydict)

# re-declaring a variable works
myint = 6
print("re-declaring myint variable with value:", myint)
myint = "some string"
print("re-declaring myint variable with value:", myint)

# to access a member of a sequence type, use []
print("access the third member of a sequence list :", mylist[2])
print("list starts on zero index                  :", mylist[0])
print("access the third member of a sequence tuple:", mytuple[2])
print("tuple starts on zero index                 :", mytuple[0])

# use slices to get parts of a sequence
print("get parts of a sequence list starts in second member:", mylist[1:5])
print("get parts of a sequence list starts in third member :", mylist[2:])
print("get parts of a sequence list jump second member     :", mylist[0:5:2])

# you can use slices to reverse a sequence
print("reverse a sequence list:", mylist[::-1])

# dictionaries are accessed via keys
print("dictionaries are accessed via keys:", mydict["two"])

# ERROR: variables of different types cannot be combined
# print("the value of number is" + 123) # trhows exception, TpeError: can only concatenate str (not "int") to str
print("the value of number is: " + str(123))


# Global vs. local variables in functions
def notChangeGlobalVariable():
    mystr = "other string value"
    print("Local scope: change mystr variable inside the function:", mystr)

def changeGlobalVariable():
    global mystr
    mystr = "change string value"
    print("Local scope: change mystr variable inside the function:", mystr)

notChangeGlobalVariable()
print("Global scope: doesn't change mystr variable inside the function:", mystr)

changeGlobalVariable()
print("Global scope: change mystr variable inside the function:", mystr)
