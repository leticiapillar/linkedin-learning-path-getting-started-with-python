# 03 Random Module
import random

# Random Numbers
print("Random Numbers")
print("random number 0 to 1   :", random.random())
print("randrange number 0 or 1:", random.randrange(2))
print("randrange number 1 to 6:", random.randrange(1, 7))

print()
for _ in range(5):
    print("random number 0 to 1   :", random.random())
    print("randrange number 0 or 1:", random.randrange(2))
    print("randrange number 1 to 6:", random.randrange(1, 7))


# Random Choices
print("Random Choices")
print("random sample, choose 5 numbers of 0 to 99:", random.sample(range(100), 5))

pets = ["cat", "dog", "bird", "fish"]
print("list of pets:", pets)
print("choise a pet:", random.choice(pets))

cards = ["Jack", "Queen", "King", "Ace"]
print("list of cards:", cards)
random.shuffle(cards)
print("shuffle cards:", cards)

print()
for _ in range(3):
    print("choise a pet:", random.choice(pets))
    random.shuffle(cards)
    print("shuffle cards:", cards)
