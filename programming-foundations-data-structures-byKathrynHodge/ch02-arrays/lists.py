# 01 Lists
print("01 Lists")

numbers = [0, 1, 3, 4, 2 , 0, 1, 0, 3, 2 , 1, 0, 1, 2, 0]
print("List of numbers:", numbers)

# Get element by index, ordered
print("get 1st element:", numbers[0])
print("get 3rd element:", numbers[2])
print("get 5th element:", numbers[5])

# Get element by index, reversed
print("get last element (reversed):", numbers[-1])
print("get 2nd element (reversed):", numbers[-2])

# Get size of list elements
size = len(numbers)
print("get size of list:", size)

# Sum of elements, using for to sum elements
sum_elements = 0
for n in numbers:
    sum_elements += n
print("Sum os elements:", sum_elements)

# Avarage of elements, sum / size
avg = sum_elements / size
print("Avarage of elements:", avg)


print()
# Using buit-in functions 
print("Using buit-in functions")
print("Sum os elements:", sum(numbers))

# statistics module — Mathematical statistics functions¶
print("Using  statistics module")
import statistics
print("Avarage of elements:", statistics.mean(numbers))

print()
# Update elements of list
print("Update elements of list")

print("get 1st element:", numbers[0])
numbers[0] = 5
print("get 1st element, after update:", numbers[0])

print("get last element (reversed):", numbers[-1])
numbers[-1] = 4
print("get last element, after update:", numbers[-1])

print("Increment elements of list")
print("get 2st element:", numbers[1])
numbers[1] = numbers[1] + 1
print("get 2st element, after update:", numbers[1])

print("List of numbers:", numbers)

print()
# Manipulate elements of list
print("Manipulate elements of list")
numbers.append(8)
print("Add element, in the end position:", numbers)
numbers.remove(8)
print("Remove element, by value        :", numbers)



