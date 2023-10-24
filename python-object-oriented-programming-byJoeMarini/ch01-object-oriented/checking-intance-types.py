# Python Object Oriented Programming by Joe Marini course example
# Checking class types and instances


class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")


# TODO: use type() to inspect the object type
print("Use type() to inspect the object type")
print("Book 1 type:", type(b1))
print("Newspaper 1 type:", type(n1))


# TODO: compare two types together
print("Compare two types together")
print("b1 equals type b2?", type(b1) == type(b2))
print("n1 equals type n2?", type(n1) == type(n2))
print("n1 equals type b2?", type(n1) == type(b2))


# TODO: use isinstance to compare a specific instance to a known type
print("Use isinstance to compare a specific instance to a known type")
print("b1 is instance of Book?", isinstance(b1, Book))
print("n1 is instance of Newspaper?", isinstance(n1, Newspaper))
print("n2 is instance of object?", isinstance(n2, object))
