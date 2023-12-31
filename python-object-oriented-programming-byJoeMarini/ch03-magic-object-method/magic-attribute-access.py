# Python Object Oriented Programming by Joe Marini course example
# 04 Using the __str__ and __repr__ magic methods


from typing import Any


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, __name: str) -> Any:
        if __name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(__name)

    # TODO: __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "price":
            if type(__value) is not float:
                raise ValueError("The 'price' attribute must be a float")
        return super().__setattr__(__name, __value)

    # TODO: __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    def __getattr__(self, name):
        return name + " is not here!"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# Try setting and accessing the price
b1.price = 25.00
print("b1 after update price:", b1.price)

# b2.price = 40 # ValueError: The 'price' attribute must be a float
b2.price = 40.1
print("b2 after update price:", b2.price)

# If an attribute doesn't exist, __getattr__ will be called
print(b1.otherattribute)
