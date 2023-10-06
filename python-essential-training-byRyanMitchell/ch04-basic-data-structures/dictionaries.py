# 03 Dictionaries

# Dictionaries
animals = {
    "a": "aardvark",
    "b": "bear",
    "c": "cat",
}

print("dictionary animals:", animals)

print("animals['a']:", animals['a'])
print("animals['c']:", animals['c'])

animals['d'] = "dog"
print("animals after add element:", animals)

animals['a'] = "antelope"
print("animals after update element:", animals)

print("get keys of dictionary animals:", animals.keys())
print("get values of dictionary animals:", animals.values())

print("get keys in list:", list(animals.keys()))

# Get element in List

# KeyError: 'e'
# print("get animals['e'], doens't exist:", animals['e'])

print("get key 'e' in dictionary where key doesn't exist (safemode):", animals.get("e"))
print("get key 'e' in dictionary where key doesn't exist (safemode):", animals.get("e", "default value"))
print("get key 'a' in dictionary where key exist (safemode):", animals.get("a"))

print("len(animals):", len(animals))

print()
animals = {
    "a": ["aardvark", "antelope"],
    "b": ["bear"],
}
print("dictionary animals:", animals)

animals["b"].append("bison")
print("animals, after append existing key:", animals)

animals["c"] = ["cat"]
print("animals, after add doens't existing 'c' key:", animals)

if 'd' not in animals:
    animals["d"] = []
print("animals, after add doens't existing 'd' key:", animals)
animals["d"] = ["dog"]
print("animals, after add existing 'd' key:", animals)


print()

# The Default Dict
from collections import defaultdict

animals = defaultdict(list)
print("The Default Dict:", animals)

animals["e"].append("elephant")
print("animals, after append:", animals)

animals["e"].append("emu")
print("animals, after append:", animals)

print("animals, get element in 'f' key:", animals["f"])
