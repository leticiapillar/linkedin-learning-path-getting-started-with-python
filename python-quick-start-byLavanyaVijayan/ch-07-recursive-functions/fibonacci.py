def fibonacci(n):
    """Return the ntn number in the Fibonacci sequence"""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fib_sequence(n):
    seq = []
    for n in range(n):
        seq.append(fibonacci(n))
    return seq

def main():
    nums = [1,3,5,10,15]
    for n in nums:
        print(f"Fibonacci of {n} elements: {fib_sequence(n)}")

if __name__ == "__main__":
    main()
