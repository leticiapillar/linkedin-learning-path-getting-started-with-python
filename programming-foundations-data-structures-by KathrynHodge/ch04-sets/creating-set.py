# 01 Creating a set in Python
print("01 Creating a set in Python")

primary_colors = set(["red", "yellow", "blue"])
print("Primary colors:", primary_colors)

is_primary = "green" in primary_colors
print("Green is a primary color?", is_primary)
is_primary = "blue" in primary_colors
print("Blue is a primary color?", is_primary)

print()
letters = set(['a', 'b'])
print("Letters:", letters)

letters.add('c')
print("Add letter c:", letters)

letters.add('d')
print("Add letter d:", letters)

letters.add('c')
print("Add letter c again:", letters)
