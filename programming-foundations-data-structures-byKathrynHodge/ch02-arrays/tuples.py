# 03 Tuples are immutable array-like structures
print("03 Tuples are immutable array-like structures")
print()

point = (5,2)
print("Point number:", point)
print("Point number, get position 1:", point[0])
print("Point number, get position 2:", point[1])


rgb_color = (0,0,0)
print("RGB color:", rgb_color)

list_points = [(5,2), (1,2), (3,4)]
print("Lists of point numbers:", list_points)

print()
def calculate_square_properties(side_lenght):
    area = side_lenght * side_lenght
    perimeter = 4 * side_lenght
    return (area, perimeter)

result = calculate_square_properties(5)
print("Calculate square properties of number 5:", result)
print("Area     :", result[0])
print("Perimeter:", result[1])

area, perimeter = calculate_square_properties(3)
print("Calculate square properties of number 3:")
print("Area     :", area)
print("Perimeter:", perimeter)
