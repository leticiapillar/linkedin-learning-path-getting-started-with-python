# 05 Dictionary Comprehensions

print("Dictionary Comprehensions")

animalList = [("a", "aardvark"), ("b", "bear"), ("c", "cat"), ("d", "dog")]
print("animalList:", animalList)

animals = {item[0]: item[1] for item in animalList}
print("convert list of tuples in dictionary:", animals)

animals = {key: value for key, value in animalList}
print("convert list of tuples in dictionary:", animals)

print("dict items:", animals.items())

print("convert dict items to list:", list(animals.items()))

dictAnimals = [{"letter": key, "name": value} for key, value in animals.items()]
print("convert animals dict items in dictionary", dictAnimals)
