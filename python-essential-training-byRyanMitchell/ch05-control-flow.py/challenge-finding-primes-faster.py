# Faster Prime Finding
#
# Write a function that returns a list of all primes up to a given number.
#
# For each number, in order to determine if it is prime, take the following steps:
#
#   1. Find the square root of the number
#   2. Find all the primes up to that square root
#   3. Test to see if any of those primes are divisors
#
# If a number has no prime divisors, it is prime!

def allPrimesUpTo(num):
    primes = [2]
    for number in range(3, num):
        sqrRoot = number ** 0.5
        for factor in primes:
            if number % factor == 0:
                break
            if factor > sqrRoot:
                primes.append(number)
                break
    return primes

list = allPrimesUpTo(100)
print(list)

list = allPrimesUpTo(1000)
print(list)
