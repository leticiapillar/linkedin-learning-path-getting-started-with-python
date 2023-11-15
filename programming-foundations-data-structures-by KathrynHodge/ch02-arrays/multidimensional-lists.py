# 02 Multidimensional Lists
print("02 Multidimensional Lists")
print()

seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

print("Names of students in seating chart:")
print(seating_chart)

print()
print("List students name by line")
for i, students in enumerate(seating_chart):
    print(f"Line {i}, students names {students}")

print()
print("List students name by each posistion")
for i, students in enumerate(seating_chart):
    for j, name in enumerate(students):
        print(f"{name} is in row {i+1}, seat {j+1}")
