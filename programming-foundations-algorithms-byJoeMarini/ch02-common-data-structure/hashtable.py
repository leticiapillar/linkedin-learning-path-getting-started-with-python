# demonstrate hashtable usage


# TODO: create a hashtable all at once
ht1 = { "key1": 1, "key2": 2, "key3": "three"}
print(ht1)

# TODO: create a hashtable progressively
ht2 = dict()
ht2["key1"] = 1
ht2["key2"] = 2
ht2["key3"] = "three"
print(ht2)

# TODO: try to access a nonexistent key
# print("key5 by ht2: ", ht2["key4"])

# TODO: replace an item
ht2["key2"] = "2A"
print(ht2)

# TODO: iterate the keys and values in the dictionary
for k,v in ht1.items():
    print(k, v)
