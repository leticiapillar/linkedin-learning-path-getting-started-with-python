# 04 Control Flow

# if/else statements
a = True
if a:
    print("It is true!")
    print("Also print this")
else:
    print("It is false!")
print("Always print this")

a = True
b = False
c = True
if a:
    print("It is true!")
    print("Also print this")
    if b:
        print("Both are true")
        if c:
            print("All three are true")
else:
    print("It is false!")
print("Always print this")

a = 100
if a > 100:
    print("a > 100")
elif a > 50:
    print("a > 50")
elif a > 25:
    print("a > 25")
else:
    print("a < 25")
print("Always print this")


# Foor loops
nums = [1,2,3,4,5]
for n in nums:
    print(n)

# While loops
a = 0
while a < 5:
    print(a)
    a += 1


