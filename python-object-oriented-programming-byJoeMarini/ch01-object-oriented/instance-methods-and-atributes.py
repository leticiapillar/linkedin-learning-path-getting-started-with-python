# Python Object Oriented Programming by Joe Marini course example
# 03Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret atribute"

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price
    
    def setdiscount(self, amount):
        self._discount = amount


# TODO: create some book instances
print("Create some book instances")
b1 = Book("Fluent Python, 2nd Edition", "Luciano Ramalho", 1012, 39.95)
b2 = Book("Grokking Algorithms: An illustrated Guide For Programmers and Other Curious People", "Aditya Bhargava", 256, 40.33)
print("b1:", b1)
print("b2:", b2)


# TODO: print the price of book1
print("Print the price of book1")
print(b1.getprice())


# TODO: try setting the discount
print("Try setting the discount")
b1.setdiscount(0.25)
print("Price after discount 25%:", b1.getprice())


# TODO: properties with double underscores are hidden by the interpreter
print("Properties with double underscores are hidden by the interpreter")
print("b1._discount:", b1._discount)

# print("b1.__secret:", b1.__secret)
# AttributeError: 'Book' object has no attribute '__secret'

#print("b1.Book__secret:", b1.Book__secret)
# AttributeError: 'Book' object has no attribute 'Book__secret'. Did you mean: '_Book__secret'?
