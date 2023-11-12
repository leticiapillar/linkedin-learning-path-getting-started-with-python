# 01 Command Line Arguments
import sys

# Print Arguments
print("Print Arguments")
print(f"Number of arguments: {len(sys.argv)}")
print(f"Arguments: {sys.argv}")


# Remove Arguments
print("Remove Arguments")
sys.argv.remove(sys.argv[0])
print(f"Arguments: {sys.argv}")


# Sum up the Arguments
print("Sum up the Arguments")
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        n = int(arg)
        sum += n
    except Exception:
        print("Argument is no a number")

print(f"Sum of arguments is: {sum}")
