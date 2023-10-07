# While loops

from datetime import datetime

now = datetime.now()
print("now:", now)
print("now + 2 seconds:", now.second + 2)

# While
# wait_until = datetime.now().second + 2
# while datetime.now().second != wait_until:
#     print("Still waiting!!")
# print(f"We are at {wait_until} seconds!")


# Pass
wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    pass
print(f"We are at {wait_until} seconds!")


# Break
wait_until = datetime.now().second + 2
while True:
    if datetime.now().second != wait_until:
        print(f"We are at {wait_until} seconds!")
        break


wait_until = datetime.now().second + 2
while True: # loop 1
    while datetime.now().second != wait_until: # loop 2
        print(f"We are at {wait_until} seconds!")
        break # breakis the loop 2
    break # breakis the loop 1


# Continue
wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    continue
    print("Still waiting!!")
print(f"We are at {wait_until} seconds!")

wait_until = datetime.now().second + 2
while True:
    if datetime.now().second != wait_until:
        continue
    break
print(f"We are at {wait_until} seconds!")
