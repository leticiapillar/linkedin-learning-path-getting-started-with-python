# 01 If, Elif and Else

# If statements with "FizzBuzz"
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, FizzBuzz, 16

print("If statements with 'FizzBuzz'")
for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    else:
        if n % 3 == 0:
            print("Fizz")
        else:
            if n % 5 == 0:
                print("Buzz")
            else:
                print(n)

for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

print()
# Single Line if statements
print("Single Line if statements")
n = 3
print("Fizz" if n % 3 == 0 else n)
n = 5
print("Fizz" if n % 3 == 0 else n)

n = 5
print("Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n)

n = 15
print("FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n)

print()
resut = ["FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n for n in range(1, 101)]
print(resut)
