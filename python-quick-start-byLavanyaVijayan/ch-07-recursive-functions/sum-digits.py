def sum_digits(n):
    """Return the sum os digits of positive inter n"""
    if n < 10:
        return n
    else:
        all_but_last = n // 10
        last = n % 10
        return sum_digits(all_but_last) + last

def main():
    nums  = [1, 10, 12, 25, 30, 31]
    for n in nums:
        s = sum_digits(n)
        print(f"The sum digits of number {n} is {s}")

if __name__ == "__main__":
    main()
