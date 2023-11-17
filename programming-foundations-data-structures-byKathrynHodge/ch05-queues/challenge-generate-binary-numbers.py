# 02 Challenge: Generate binary numbers
print("02 Challenge: Generate binary numbers")

from collections import deque

binary_queue = deque()
binary_queue.append(bin(1))
print("Generate binary of 1:", binary_queue)

print("Generate binary numbers 2 to 10")
for n in range(2, 10):
    binary_queue.append(bin(n))

print("Print binary queue:", binary_queue)


print()
# Print binary queue: deque(['0b1', '0b10', '0b11', '0b100', '0b101', '0b110', '0b111', '0b1000', '0b1001'])
def print_binary_number(n):
    if n <= 0:
        return
    
    bdeque = deque()
    bdeque.append(1)
    for i in range(n):
        number = bdeque.popleft()
        print(number)
        bdeque.append(number * 10)
        bdeque.append(number * 10 + 1)

print("Print binary number to 6")
print_binary_number(6)
print()

print("Print binary number to -6")
print_binary_number(-6)
print()

print("Print binary number to 10")
print_binary_number(10)
print()