# Question 1
# If the current number of seconds is 59 seconds, how long will this program run?
from datetime import datetime
wait_until = datetime.now().second + 2
# wait_until = 59 + 2 # It will not stop.
while datetime.now().second != wait_until:
    print('Still waiting!')
    break
print(f'We are at {wait_until} seconds!')

print()
# Question2
# What list does this statement generate?
result = ['Monty Python' if n % 6 == 0 else 'Python' if n % 3 == 0 else 'Monty' if n % 2 == 0 else n for n in range(1, 10)]
# [1, 'Monty', 'Python', 'Monty', 5, 'Monty Python', 7, 'Monty', 'Python']
print(result)

print()
# Question 3
# Will the print statement be reached in this code?
for number in range(1, 9):
    if number % 10 == 0:
        break
else:
    print('Let\'s print something out!')


print()
# Question 4
# Will the print statement be reached in this code?
for number in range(1, 100):
    if number % 10 == 0:
        break
else:
    print('Let\'s print something out!')


