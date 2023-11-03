# Python Object Oriented Programming by Joe Marini course example
# 03 Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, value) -> bool:
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")
        return self.title == value.title and self.author == value.author and self.price == value.price

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")
        return self.price >= value.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value) -> bool:
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")
        return self.price < value.price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
print("b1 == b3?", b1 == b3)
print("b1 == b2?", b1 == b2)

# print("b1 == 42?", b1 == 42)
# ValueError: Can't compare book to non-book type

# TODO: Check for greater and lesser value
print("b1 price >= b2 price?", b1 >= b2)
print("b1 price <  b4 price?", b1 >= b4)


# TODO: Now we can sort them too
books = [b1, b3, b2, b4]
print("books before sort:", [book.title for book in books])
books.sort()
print("books after sort :", [book.title for book in books])
