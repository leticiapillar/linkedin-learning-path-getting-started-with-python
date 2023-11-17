# 02 Use deque as a Stack - LIFO (Last In First Out)
print("02 Use deque as a Stack")

from collections import deque

history_stack = deque()
history_stack.append("https://google.com")
history_stack.append("https://linkedin.com")
history_stack.append("https://stackoverflow.com")
history_stack.append("https://w3school.com")

history_stack.reverse()
print("History stack       :", history_stack)
print("Len of history stack:", len(history_stack))

top_history = history_stack.popleft()
print("Remove top of history stack:", top_history)
print("History stack              :", history_stack)

top_history = history_stack[-1]
print("Top of history stack  :", top_history)
print("History stack is empty?", not history_stack)
print("Len of history stack  :", len(history_stack))

