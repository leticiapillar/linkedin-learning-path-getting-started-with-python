# Python Object Oriented Programming by Joe Marini course example
# 03 implementing default values in data classes

from dataclasses import dataclass, field
import random

def generate_price():
    return float(random.randrange(20, 50))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No author"
    pages: int = 0
    # price: float = 0.00
    # price: float = field(default=10.00)
    price: float = field(default_factory=generate_price)

# Create a empty book object
# b1 = Book()
# print(b1)
# TypeError: Book.__init__() missing 4 required positional arguments: 'title', 'author', 'pages', and 'price'

# Create a default book object, without price defined default value
# b1 = Book()
# print(b1)
# TypeError: non-default argument 'price' follows default argument

# Create a default book object
b1 = Book()
print(b1)
# Book(title='No title', author='No author', pages=0, price=0.0)

# Create a specified book, price is set by field operator
b1 = Book("Title of book 1", "Author of book 1", 500)
b2 = Book("Title of book 2", "Author of book 2", 520)
print(b1)
print(b2)
# Book(title='Title of book 1', author='Author of book 1', pages=500, price=10.0)
# Book(title='Title of book 2', author='Author of book 2', pages=520, price=10.0)

# Create a specified book, price is set by field operator, using default factory
b3 = Book("Title of book 3", "Author of book 3", 500)
b4 = Book("Title of book 4", "Author of book 4", 520)
print(b3)
print(b4)
