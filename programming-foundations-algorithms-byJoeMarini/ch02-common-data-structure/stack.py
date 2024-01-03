# try out the Python stack functions

# TODO: create a new empty stack
stack = []

# TODO: push items onto the stack
for i in range(1, 10):
    stack.append(i)

# TODO: print the stack contents
print(stack)

# TODO: pop an item off the stack
x = stack.pop()
print("remove last item:", x)
print(stack)

x = stack.pop(2)
print("remove third item:", x)
print(stack)
