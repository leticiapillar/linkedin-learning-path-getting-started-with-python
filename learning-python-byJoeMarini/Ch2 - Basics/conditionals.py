#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    print("conditional flow uses if, elif, else:")
    if x > y:
        result = "x greater than y"
    elif x == y:
        result = "x equals to y"
    else:
        result = "x less than y"
    print(result)

    # conditional statements let you use "a if C else b"
    print("conditional statements let you use 'a if C else b':")
    result = "x greater than y" if x > y else "x less than y or equal to"
    print(result)

    # match-case makes it easy to compare multiple values
    # new feature of Python 3.10+
    print("match-case makes it easy to compare multiple values:")
    # value = "one"
    # value = "two"
    # value = "four"
    value = 56
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3,4)
        case _:
            result = -1
    print(result)


if __name__ == "__main__":
    main()
