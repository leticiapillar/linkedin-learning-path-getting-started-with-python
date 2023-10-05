# 04 String
import math

# Slice
print("String Slice")
name = "My name is Leticia Pillar"
print("name     : ", name)
print("name[0]  :", name[0])
print("name[1]  :", name[1])

print("name[0:7]:", name[0:7])
print("name[:7] :", name[:7])
print("name[11:]:", name[11:])

print()

myList = [1,2,3,4,5]
print("myList     :", myList)
print("myList[2:4]:", myList[2:4])
print("myList[:4] :", myList[:4])
print("myList[2:] :", myList[2:])

print("len(name)  :", len(name))
print("len(myList):", len(myList))

print()

# Formatting
print("String Formatting")
print("My number is: " + str(10))
print(f"My number is: {10}")
print(f"My number is: {10} and twice that is {2*10}")

print(f"Pi is: {math.pi}")
print(f"Pi is: {math.pi, 2}")
print("Pi is: {}".format(math.pi))

print()
# Multi-line Strings
print("Multi-line Strings")
myString="""
Here is a lonk block of tet
I can add new lines!
new line 1
new line 2 ...
"""
print(myString)
