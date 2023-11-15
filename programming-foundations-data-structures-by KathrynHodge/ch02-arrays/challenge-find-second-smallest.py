# 06 Challenge: find the second smallest

# Using built-in python function
def find_second_smallest(my_list):
    if len(my_list) < 2: return None
    return sorted(my_list)[1]

my_list = [5, 8, 3, 2, 6]
print("My list        :", [5, 8, 3, 2, 6])
print("Second smallest:", find_second_smallest(my_list))


# Not using built-in python function
def find_second_smallest_v2(my_list):
    if len(my_list) < 2: return None
    first = float("inf")
    second = float("inf")
    for n in my_list:
        if n < first:
            second = first
            first = n
        elif n < second:
            second = n
    return second

my_list = [5, 8, 3, 2, 6]
print("My list        :", [5, 8, 3, 2, 6])
print("Second smallest:", find_second_smallest_v2(my_list))
