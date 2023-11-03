# Python Object Oriented Programming by Joe Marini course example
# 01 Using data classes to represent data objects

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"{self.title}, by {self.author}"


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print("book 1:", b1)

# TODO: comparing two dataclasses - they implement __eq__
print("b1 == b2:", b1 == b2)

# TODO: change some fields
print("Book 3 before update:", b3.bookinfo())
b3.title = "Another title of book"
b3.price = 49.95
print("Book 3 after update:", b3.bookinfo())
