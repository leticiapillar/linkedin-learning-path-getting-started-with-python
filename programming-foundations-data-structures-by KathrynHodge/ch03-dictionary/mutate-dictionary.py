# 02 Mutate a dictionary in Python
print("02 Mutate a dictionary in Python")

person = {
    "name": "Anna",
    "language": "Portuguese",
    "color": "Green",
    "number": 8,
    "pets": ["dog", "cat", "bird"],
    "age": 35
}

print("Print person:", person)

# Update values in dictionary
person["language"] = "English"
print("Update language:", person)

person["number"] = 6
print("Update number:", person)

person["pets"] = person["pets"] + ["fish"]
print("Update pets:", person)

# Delete key in dictinary
del person["number"]
print("Update key number:", person)

# Removed item in a dictionary
removed = person.pop("color")
print("Removed color key:", removed)
print("Print person:", person)

# Removed item in a dictionary, safety, if don't exist the key
removed = person.pop("city", "N/A")
print("Removed city key:", removed)
print("Print person:", person)

# Add new key in dictionary
person["city"] = "New York"
print("Add key city:", person)
