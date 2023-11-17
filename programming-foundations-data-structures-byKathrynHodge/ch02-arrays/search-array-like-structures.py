# 04 Search Array Like Structure: Linear Search
print("04 Search Array Like Structure: Linear Search")
print()

numbers = [2, 4, 7, 3, 9]
print("List of numbers:", numbers)

# Create a function to search the number in array
# Big O: O(n)
def linear_search(item, array):
    for element in array:
        if element == item:
            return True
    return False

print("Find the number in list of numbers, using linear search function")
exists = linear_search(7, numbers)
print("7 exists:", exists)
exists = linear_search(5, numbers)
print("5 exists:", exists)

print("Find the number in list of numbers, using pythonic")
exists = 7 in numbers
print("7 exists:", exists)
exists = 5 in numbers
print("5 exists:", exists)

print("Find the number in list of numbers, get index position")
index = numbers.index(7)
print("index position of 7 is:", index)
index = numbers.index(5)
print("index position of 5 is:", index)
# ValueError: 5 is not in list


