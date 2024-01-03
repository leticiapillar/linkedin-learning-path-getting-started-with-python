# try out the Python queue functions
from collections import deque

# TODO: create a new empty deque object that will function as a queue
queue = deque()

# TODO: add some items to the queue
for i in range(1,10):
    queue.append(i)

# TODO: print the queue contents
print(queue)

# TODO: pop an item off the front of the queue
x = queue.popleft()
print("remove first item:", x)
print(queue)

x = queue.pop() #
print("default remove last item:", x)
print(queue)
