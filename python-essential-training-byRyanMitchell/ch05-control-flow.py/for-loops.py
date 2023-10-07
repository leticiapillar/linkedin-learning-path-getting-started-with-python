# For
myList = [1,2,3,4,5]
for item in myList:
    print(item)


# Pass
animalLookup = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear'],
    'c': ['cat'],
    'd': ['dog'],
}

for letter, animals in animalLookup.items():
    pass

for letter, animals in animalLookup.items():
    print(letter, animals)


# Continue
for letter, animals in animalLookup.items():
    if len(animals) > 1:
        continue
    print(f"Olny one animal! {animals[0]}")


# Break
for letter, animals in animalLookup.items():
    if len(animals) > 1:
        print(f"Found {len(animals)} animals {animals}")
        break


# For / Else
for number in range(2, 100):
    for factor in range(2, int(number ** 0.5) +1):
        if number % factor == 0:
            break
    else:
        print(f"{number} is prime!")

print()

# More complicated to read this code
for number in range(2, 100):
    found_factors = False
    for factor in range(2, int(number ** 0.5) +1):
        if number % factor == 0:
            found_factors = True
    if not found_factors:
        print(f"{number} is prime!")
