# 04 List Comprehensions

# List Comprehensions
print("List Comprehensions")

myList = [1,2,3,4,5]
print("myList:", myList)
print("Mutiply by 2 each item of myList:", [2*item for item in myList])

print()
# List comprehensions with filters
print("List comprehensions with filters")
myList = list(range(100))
print("myList with 100 elements:", len(myList))

filteredList = [item for item in myList if item % 10 == 0]
print("get items divided by 10 where module equals zero:", filteredList)

filteredList = [item for item in myList if item % 10 < 3]
print("get items divided by 10 where module less than 3:", filteredList)

print()
# List comprehensions with functions
print("List comprehensions with functions")

myString = "My name is Leticia Lisboa. I live in Brazil"
print("myString:", myString)
print("split string by period:", myString.split("."))
print("split string by space:", myString.split())

def cleanWord(word):
    return word.replace(".", "").lower()

words = [cleanWord(word) for word in myString.split()]
print("split myString and clean each word removing period:", words)

words = [cleanWord(word) for word in myString.split() if len(cleanWord(word)) < 3]
print("split myString and remove period if string size less than 3:", words)

print()
# Nested list comprehensions
print("Nested list comprehensions")
words = [[cleanWord(word) for word in sentence.split()] for sentence in myString.split(".")]
print("create a list woth two items:", words)