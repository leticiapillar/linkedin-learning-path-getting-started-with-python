# 07 Least to Greatest
nums = [1, 5, -4, 3, -3]
print("List of nums:", nums)
print("sorted least to greatest:", sorted(nums))
print("sorted greatest to least:", sorted(nums, reverse=True))


# Alphabetically
names = ["Ana", "Maria", "Leticia", "Gabi"]
print("List of names:", names)
print("sorted alphabetically:", sorted(names))

names = ["Ana", "maria", "Leticia", "gabi"]
print("List of names, case senssitive:", names)
print("sorted alphabetically, default:", sorted(names))
print("sorted alphabetically, with key=str.lower:", sorted(names, key=str.lower))

# Key Parameters
txt = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
print("text:", txt)
print("sorted text, default:", sorted(txt.split()))
print("sorted text, with key=str.upper:", sorted(txt.split(), key=str.upper))

myDict = {789: "GHI", 123: "ABC", 456: "DEF", 101: "JKL"}
print("my dict:", myDict)
print("sorted keys, default:", sorted(myDict))
print("sorted keys, reversed:", sorted(myDict, reverse=True))

students = [("alicia", "B", 15), ("anna", "A", 17), ("john", "F", 14), ("bob", "C", 13)]
print("tuple students:", students)
print("sorted by first column :", sorted(students, key=lambda s:s[0]))
print("sorted by second column:", sorted(students, key=lambda s:s[1]))
print("sorted by third column :", sorted(students, key=lambda s:s[2]))





