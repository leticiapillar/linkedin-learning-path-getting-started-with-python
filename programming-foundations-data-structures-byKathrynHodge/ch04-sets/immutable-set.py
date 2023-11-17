# 03 Immutable a set in Python
print("03 Immutable a set in Python")

primary_colors = frozenset(["red", "yellow", "blue"])
print("Primary colors:", primary_colors)

is_primary = "green" in primary_colors
print("Green is a primary color?", is_primary)
is_primary = "blue" in primary_colors
print("Blue is a primary color?", is_primary)

# You cannot add new value in a frozene set
# primary_colors.add("green")
# AttributeError: 'frozenset' object has no attribute 'add'
