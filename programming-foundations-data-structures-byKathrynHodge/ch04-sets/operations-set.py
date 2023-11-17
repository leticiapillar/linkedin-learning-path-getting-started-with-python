# 02 Operations on sets in Python
print("02 Operations on sets in Python")

set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}

print("Set A:", set_a)
print("Set B:", set_b)

print()

union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)
difference_set_ab = set_a.difference(set_b)
difference_set_ba = set_b.difference(set_a)
symmetric_difference_set = set_a.symmetric_difference(set_b)

print("Union set a and b             :", union_set)
print("Intersection set a and b      :", intersection_set)
print("Differece set a and b         :", difference_set_ab)
print("Differece set b and a         :", difference_set_ba)
print("Symetric differece set a and b:", symmetric_difference_set)
