# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_FORMATS = ("PAPERBACK", "HARDCOVER", "EBOOK", "AUDIOBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # TODO: create a static method
    @staticmethod
    def getbookformats(cls):
        return cls.BOOK_FORMATS

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, format):
        self.title = title
        if format not in Book.BOOK_FORMATS:
            raise ValueError(f"{format} is not a valid format type")
        else:
            self.format = format


# TODO: access the class attribute
print("Access the class attribute")
print("Book formats:", Book.BOOK_FORMATS)


# TODO: Create some book instances
print("Create some book instances")
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "EBOOK")
#b3 = Book("Title 3", "HQ") # ValueError: HQ is not a valid format type

# TODO: Use the static method to access a singleton object
print("Use the static method to access a singleton object")
books = Book.getbooklist()
print("Book list before:", books)
books.append(b1)
books.append(b2)
print("Book list after:", books)
