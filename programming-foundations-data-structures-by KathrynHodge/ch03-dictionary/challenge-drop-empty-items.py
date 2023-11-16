# 03 Challenge: Drop empty items
print("03 Challenge: Drop empty items")

user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notification": None,
    "currency": "USD",
    "theme": None
}
print("Print user preferences:", user_preferences)

# Remove all empty items
def remove_empty_items(dictionary):
    new_dict = {}
    for k, v in dictionary.items():
        if v is not None:
            new_dict[k] = v
    return new_dict

# Using Python Dictionary Comprehension
# Remove all empty items
def remove_empty_items_v2(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None}


# Using Python Dictionary Comprehension
# Remove all empty items (None, "", 0)
def remove_empty_items_v3(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None 
                                                if v is not ""
                                                if v is not 0}


print("Original dictionary               :", user_preferences)
print("After remove empty items          :", remove_empty_items(user_preferences))
print("Python Dictionary Comprehension v2:", remove_empty_items_v2(user_preferences))

# Add two new properties in a dictionary
user_preferences["profiles"] = ""
user_preferences["logs"] = 0
print("Update original dictionary        :", user_preferences)
print("Python Dictionary Comprehension v3:", remove_empty_items_v3(user_preferences))
