# 01 Tupples and Sets

# Sets
# You can can modify Set
# Order not garatee

mySet = {"a", "b", "c"}
print("mySet:", mySet)

mySet = set(["a", "b", "c"])
print("mySet construnctor by list:", mySet)
mySet = set(("a", "b", "c"))
print("mySet construnctor by tuple:", mySet)

myList = ["a", "b", "b", "c", "c"]
print("List constains duplicate items:", myList)

mySet = set(myList)
print("Set doen't constains duplicate items:", myList)
myList = list(set(myList))
print("List created by convert list to Set, removed duplicate items:", myList)

# You cannot access element in Set by indec
# TypeError: 'set' object is not subscriptable
# print(mySet[0])

# Add and Remove elements in Set
mySet = {"a", "b", "c"}
mySet.add("d")
print("mySet, after add 'd'element:", mySet)
mySet.remove("c")
print("mySet, after remove 'c' element:", mySet)
mySet.pop()
print("mySet, after pop element:", mySet)

# Find element in Set
mySet = {"a", "b", "c"}
print("mySet:", mySet)
print("'a' in mySet:", 'a' in mySet)
print("'z' in mySet:", 'z' in mySet)

print("len(mySet):",len(mySet))

while len(mySet):
    print("pop:", mySet.pop())
print("mySet, after pop in while:", mySet)

mySet = {"a", "b", "c"}
print("mySet:", mySet)

mySet.discard("a")
print("mySet, after discard 'a':", mySet)


# Tuple
# You cannot modify, it is immutable

myTuple = ("a", "b", "c")
print("myTuple:", myTuple)

# You can access element by index
print("myTuple[0]:", myTuple[0])
print("myTuple[2]:", myTuple[2])

# You cannot modify tuple
# TypeError: 'tuple' object does not support item assignment
# myTuple[0] = "d"

# Define function with multiple return values, return type is Tuple
def returnMytipleValues():
    return 1,2,3
print("call function returnMytipleValues() and return type: ", type(returnMytipleValues()))

def returnMytipleValues2():
    return (1,2,3)
print("call function returnMytipleValues2() and return type: ", type(returnMytipleValues2()))

# Many types to literal declare Typle
myTuple = 1,2,3
print("myTuple = 1,2,3:", myTuple, type(myTuple))

myTuple = (1,2,3)
print("myTuple = (1,2,3):", myTuple, type(myTuple))


a, b, c = returnMytipleValues()
print(f"Get return of function returnMytipleValues(), a={a}, b={b}, c={c}")