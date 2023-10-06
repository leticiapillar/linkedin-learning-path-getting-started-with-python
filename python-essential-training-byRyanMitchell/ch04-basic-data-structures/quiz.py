# Question 3
# Then, you are asked to produce this structure:
# {
#         1: ['i', 'a'],
#         2: ['we', 'be', 'it'],
#         3: ['are', 'few', 'too']
# }

values = [[1, 'i', 'a'], ['2', 'we', 'be', 'it'], [3, 'are', 'few', 'too']]
dict = {item[0]: item[1:] for item in values}
print(dict)

print()
# Question 5
# Which option lists the numbers 100 to 0, backwards, by increments of 5? ([100, 95, 90,..., 0])
print(list(range(101))[::-5])