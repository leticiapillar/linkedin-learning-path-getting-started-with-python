# 03 Challenge: Matching Parentheses
print("03 Challenge: Matching Parentheses")

from collections import deque

def mathing_parentheses(string):
    return string.count("(") == string.count(")")

def check_matching_parentheses(string):
    stack = deque()
    for s in string:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if not stack: return False
            stack.pop()
    return len(stack) == 0


strings_match = ["()", "(hi there)", "(hell)o", "((linkedin))learning"]
strings_not_match = ["(hi(there", "()ok)", "((incremet)", ")linkedin()"]

print("Matching")
for s in strings_match:
    print(f"{s} = {mathing_parentheses(s)}")

print()

print("Not Mathing")
for s in strings_not_match:
    print(f"{s} = {mathing_parentheses(s)}")

print()
print("Matching using stack function")
for s in strings_match:
    print(f"{s} = {check_matching_parentheses(s)}")

print()
print("Not Mathing using stack function")
for s in strings_not_match:
    print(f"{s} = {check_matching_parentheses(s)}")
