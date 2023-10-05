# 03 Booleans

# Casting Booleans
print("Casting Booleans")

print("bool(1), result True:", bool(1))
print("bool(0), result False:", bool(0))

print("bool(-1), result True:", bool(-1))
print("bool(1j), result True:", bool(1j))

print("bool(0.0), result False:", bool(0.0))
print("bool(0j) , result False:", bool(0j))

print("bool('True'), result True  :", bool('True'))
print("bool('False'), result True :", bool('False'))
print("bool('string'), result True:", bool('string'))

print("bool(''), result False:", bool(''))
print("bool(' '), result True:", bool(' '))

print("list bool([]), result False  : ", bool([]))
print("list bool([1,2]), result True: ", bool([1,2]))

print("dictionary bool({}), result False             : ", bool({}))
print("dictionary bool({'name': 'Anna'}), result True: ", bool({"name": "Anna"}))

print("bool(None), result False: ", bool(None))

myList = [1,2]
if myList:
    print("My list has some values")
if bool(myList):
    print("My list has some values too")

a = 5
b = 5
if a - b:
    print("a and b are not equal")
print("bool(a - b), result False:", bool(a - b))
print("bool(a == b), result True:", bool(a == b))

print()
# Boolean Logic
print("Boolean Logic")

weatherIsNice = False
haveUmbrella = True

print(f"weatherIsNice is {weatherIsNice}, and haveUmbrella is {haveUmbrella}")
print("not haveUmbrella                 :", not haveUmbrella)
print("not haveUmbrella or weatherIsNice:", not haveUmbrella or weatherIsNice)
if not haveUmbrella or weatherIsNice:
    print("Stay inside")
else:
    print("Go for walk")

if (not haveUmbrella) or weatherIsNice:
    print("Stay inside")
else:
    print("Go for walk")

print()
weatherIsNice = True
haveUmbrella = False
print(f"weatherIsNice is {weatherIsNice}, and haveUmbrella is {haveUmbrella}")
print("not haveUmbrella                 :", not haveUmbrella)
print("not haveUmbrella or weatherIsNice:", not haveUmbrella or weatherIsNice)
if not haveUmbrella or weatherIsNice:
    print("Stay inside")
else:
    print("Go for walk")

if (not haveUmbrella) or weatherIsNice:
    print("Stay inside")
else:
    print("Go for walk")

if (not haveUmbrella) or (not weatherIsNice):
    print("Stay inside")
else:
    print("Go for walk")

if haveUmbrella or weatherIsNice:
    print("Go for walk")
else:
    print("Stay inside")
