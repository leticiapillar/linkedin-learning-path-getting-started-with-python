# 01 Use deque as queue
print("01 Use deque as queue")

from collections import deque

person_names_queue = deque()
person_names_queue.append("Anna")
person_names_queue.append("Maria")
person_names_queue.append("Sophia")
person_names_queue.append("Rebecca")
person_names_queue.append("Diana")

print("Print queue of person names:", person_names_queue)
print("Len of person names queue  :", len(person_names_queue))
print("Deque left name            :", person_names_queue.popleft())

print("Deque all names:")
while len(person_names_queue) > 0:
    process = person_names_queue.popleft()
    print(process)
