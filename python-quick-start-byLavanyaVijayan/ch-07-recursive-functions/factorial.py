def factorial(n):
    """Return the factorial of positive number"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    nums  = [1, 2, 3, 5]
    for n in nums:
        f = factorial(n)
        print(f"Factorial the {n}! is {f}")

if __name__ == "__main__":
    main()
