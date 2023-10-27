# Python Object Oriented Programming by Joe Marini course example
# 05 Using composition to build complex objects

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages


class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)
    
    def getbookpagescount(self):
        pagescount = 0
        for ch in self.chapters:
            pagescount = ch.pages
        return pagescount


author1 = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, author1)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.author)
print(b1.getbookpagescount())
