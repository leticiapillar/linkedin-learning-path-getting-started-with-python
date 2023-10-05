# 02 Data Structure

# List
my_list = [1,2,3,4]
print(my_list)

my_list = ["apple", "banana", "avocado"]
print(my_list)

my_list = [1, "list", False, []]
print(my_list)

my_list = [[1,2,3], [False, True], ["apple", "avocado"]]
print(my_list)
print ("size of my list:", len(my_list))

# Sets
# don't have duplicated values
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))
print("size of set:", len(my_set))


my_set = {1,1,1,2,2,3}
print(my_set)
print(type(my_set))

print("equals list [1,2] == [1,2]:", [1,2] == [1,2])
print("equals list [1,2] == [2,1]:", [1,2] == [2,1])

print("equals set {1,2,3} == {1,2,3}:", {1,2,3} == {1,2,3})
print("equals set {1,2,3} == {3,2,1}:", {1,2,3} == {3,2,1})
print("equals set {1,2,3} == {3,2,1,1,1}:", {1,2,3} == {3,2,1,1,1})

# Tuples
# Are immutable
my_tuple = (1,2,3)
print(my_tuple)
print("size of tuple:", len(my_tuple))

print("you can change list", my_list.append(6))
# print("you cannot change tuple", my_tuple.append(6)) # AttributeError: 'tuple' object has no attribute 'append'


# Dictionaries
my_dictionary = {
    "apple": "a red fruit",
    "bear" : "a scaridy animal",
}
print("print all values:", my_dictionary)
print("print value of apple key:", my_dictionary["apple"])

# Have duplicate key, use the last value
my_dictionary = {
    "apple": "a red fruit",
    "bear" : "a scaridy animal",
    "apple": "sometimes a green fuit",
}
print("print value of apple key:", my_dictionary["apple"])
