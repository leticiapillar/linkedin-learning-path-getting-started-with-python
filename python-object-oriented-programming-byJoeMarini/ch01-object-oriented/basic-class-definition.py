# Python Object Oriented Programming by Joe Marini course example
# 02 Basic class definitions


# TODO: create a basic class
class Book:
    def __init__(self, name):
        self.name = name


# TODO: create instances of the class
b1 = Book("Fluent Python: Clear, Concise, and Effective Programming")
b2 = Book("Grokking Algorithms: An illustrated Guide For Programmers and Other Curious People")


# TODO: print the class and property
print("Book 1:", b1)
print("Book 1 name:", b1.name)
