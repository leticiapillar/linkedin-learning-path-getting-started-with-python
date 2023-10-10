# 02 Static and Instance Methods

class WordSet:
    def __init__(self) -> None:
        self.words = set()
    
    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)
    
    def cleanText(text):
        # chaining functions
        text = text.replace("!", "").replace(".", "").replace(",", "").replace("'", "")
        return text.lower()

wordSet = WordSet()
wordSet.addText("Hi, I'm Leticia!, Here is a sentence I want to to add!")
wordSet.addText("Here is another sentence  want to add.")
print(wordSet.words)

print("------------------------------")

class WordSet:
    replacePuncs = ["!", ".", ",", "'"]
    def __init__(self) -> None:
        self.words = set()
    
    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)
    
    def cleanText(text):
        # chaining functions
        for punc in WordSet.replacePuncs:
            text = text.replace(punc, "")
        return text.lower()

wordSet = WordSet()
wordSet.addText("Hi again, I'm Leticia!, Here is a sentence I want to to add!")
wordSet.addText("Here is another sentence  want to add.")
print(wordSet.words)

print("------------------------------")
# Decorators

class WordSet:
    replacePuncs = ["!", ".", ",", "'"]
    def __init__(self) -> None:
        self.words = set()
    
    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)
    
    @staticmethod
    def cleanText(text):
        # chaining functions
        for punc in WordSet.replacePuncs:
            text = text.replace(punc, "")
        return text.lower()

wordSet = WordSet()
wordSet.addText("Hi again 2, I'm Leticia!, Here is a sentence I want to to add!")
wordSet.addText("Here is another sentence  want to add.")
print(wordSet.words)
