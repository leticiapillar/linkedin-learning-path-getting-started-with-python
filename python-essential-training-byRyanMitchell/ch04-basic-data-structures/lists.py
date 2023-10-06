# 01 Lists

# List Slicing

myList = [1,2,3,4,5]
print("myList:", myList)
print("myList[3:]:", myList[3:])
print("myList[0:6:2]:", myList[0:6:2])
print("myList[0:6:3]:", myList[0:6:3])
print("myList[::2]:", myList[::2])

for i in range(100):
    print(i)

myList = list(range(100))
print("myList[::10]:", myList[::10])
print("myList[::-10]:", myList[::-10])

# Modifying Lists
myList = [1,2,3,4,5]
print("myList:", myList)
myList.append(6)
print("myList after append:", myList)

myList.insert(3, "a new value")
print("myList after insert:", myList)

myList.remove("a new value")
print("myList after remove:", myList)

myList.pop()
print("myList after pop:", myList)

while len(myList):
    print("pop:", myList.pop())

a = [1,2,3,4,5]
b = a
print("lista a:", a)
print("lista b, (b = a):", b)
a.append(6)
print("lista a, after append:", a)
print("lista b, after append:", b)

a = [1,2,3,4,5]
b = a.copy()
print("lista a:", a)
print("lista b, (b = a.copy()):", b)
a.append(6)
print("lista a, after append:", a)
print("lista b, after append:", b)
