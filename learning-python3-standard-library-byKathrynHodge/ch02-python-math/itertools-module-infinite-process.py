# 05 Iterators with Itertools: infinite process
import itertools

# Infinite Counting
print("Infinite Counting: itertools count")

print("iterator start in 50 infinity and break in 80")
for i in itertools.count(50):
    print(i)
    if i == 80:
        break

print("iterator start in 50, jump by 5 infinity and break in 80")
for i in itertools.count(50, 5) :
    print(i)
    if i == 80:
        break


# Infinite Cycling
print("Infinite Cycling: itertools cycle")

print("iterator in 'Hello, World' string and break when x = 50")
x = 0
for i in itertools.cycle("Hello, World"):
    print(i)
    x += 1
    if x == 50:
        break

print("iterator in [1,2,3,4,5] list and break when x = 50")
x = 0
for i in itertools.cycle([1,2,3,4,5]):
    print(i)
    x += 1
    if x == 50:
        break


# Infinite Repeating
print("Infinite Repeating: itertools repeat")

print("repeat True value and break when x = 50")
x = 0
for i in itertools.repeat(True):
    print(i)
    x += 1
    if x == 50:
        break

print("repeat [1,2,3] list and break when x = 50")
x = 0
for i in itertools.repeat([1,2,3]):
    print(i)
    x += 1
    if x == 50:
        break
