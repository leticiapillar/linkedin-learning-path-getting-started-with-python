# 06 Iterators with Itertools: Permutations and Combinations
import itertools

# Permutations: Order matters - some copies with same inputs but in different order
print("Permutations: Order matters")

nums = [1,2,3]
print(f"Permutations of {nums} list")
for n in itertools.permutations(nums):
    print(n)


namesdict = {1: "Ana", 2: "Maria", 3:"Sofia"}
print(f"Permutations of {namesdict} dictionary, show key values")
for n in itertools.permutations(namesdict):
    print(n)

namesdict = {1: "Ana", 2: "Maria", 3:"Sofia"}
print(f"Permutations of {namesdict} dictionary, show values")
for n in itertools.permutations(namesdict.values()):
    print(n)

# Combinations: Order does not matter - no copies with same inputs
print("Combinations: Order does not matter")

words = ["work", "eat", "play"]
print(f"Combinations of 2 from {words} list")
for w in itertools.combinations(words, 2):
    print(w)

colors = ["blue", "orange", "yellow", "pink", "green", "black"]
print(f"Combinations of 2 from {colors} list")
for c in itertools.combinations(colors, 2):
    print(c)

print(f"Combinations of 3 from {colors} list")
for c in itertools.combinations(colors, 3):
    print(c)
