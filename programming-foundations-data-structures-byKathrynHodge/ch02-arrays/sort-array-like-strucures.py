# 05 Sort Array Liske Strucutre
print("05 Sort Array Liske Strucutre")
print()

numbers = [2, 4, 7, 3, 9]
print("List of numbers:", numbers)
print("Sorted list    :", sorted(numbers))
print("Reversed list  :", sorted(numbers, reverse=True))

students_grades = [("Sarah", 89), ("Anna", 98), ("Maria", 96), ("Rebecca", 81)]
print("Students grade (tuple)       :", students_grades)
print("Sorted by alphabetical name  :", sorted(students_grades))
print("Reversed by alphabetical name:", sorted(students_grades, reverse=True))
print("Sorted by grade (asc)        :", sorted(students_grades, key=lambda x:x[1]))
print("Sorted by grade (desc)       :", sorted(students_grades, key=lambda x:x[1], reverse=True))
