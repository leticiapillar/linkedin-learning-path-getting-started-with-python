# 01 Use a list as a Stack - LIFO (Last In First Out)
print("01 Use a list as a Stack")

card_stack = []
card_stack.append("Jack of Hearts")
card_stack.append("2 of Diamonds")
card_stack.append("10 of Spades")
card_stack.append("Queen of Hearts")

#print("Card stack:", card_stack)
print("Card stack       :", card_stack[::-1])
print("Len of card stack:", len(card_stack))

print()

# Front (botton) -- Back(top)
top_card = card_stack.pop()
print("Remove top of card:", top_card)
print("Card stack        :", card_stack[::-1])

top_card = card_stack[-1]
print("Top of card stack :", top_card)

print("Card stack is empty?", not card_stack)
print("Len of card stack:", len(card_stack))
