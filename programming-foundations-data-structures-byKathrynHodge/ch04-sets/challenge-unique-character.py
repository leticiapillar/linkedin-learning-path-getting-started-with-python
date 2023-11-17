# 04 Challenge Unique Character
print("04 Challenge Unique Character")
def has_unique_character(data):
    unique = set(data)
    return len(unique) == len(data)


print('sample     :', has_unique_character('sample'))
print('hello world:', has_unique_character('hello world'))
print('linkedin   :', has_unique_character('linkedin'))
print('python     :', has_unique_character('python'))
