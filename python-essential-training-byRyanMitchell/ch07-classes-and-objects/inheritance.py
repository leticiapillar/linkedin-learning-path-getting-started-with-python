# 03 Class Inheritance
class Dog:
    _legs = 4
    def __init__(self, name) -> None:
        self.name = name
    
    def getLegs(self):
        return self._legs

    def speak(self):
        print(f"{self.name} says: Bark!")

class Chihuahua(Dog):
    def speak(self):
        print(f"{self.name} says: Yap yap yap!")
    def wagTail(self):
        print("Vigorous wagging!")

dog = Chihuahua("Roxy")
dog.speak()
dog.wagTail()

dog = Dog("Roxy")
dog.speak()

print()
# Extending built-in classes
myList = list() # list() is class

class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)

uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)
print("uniqueList:", uniqueList)

print()

class UniqueList(list):
    
    def __init__(self):
        super().__init__()
        self.someProperty = 'Unique List!'
        

    def append(self, item):
        if item in self:
            return
        super().append(item)
        
uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)
print("uniqueList:", uniqueList)
print("uniqueList.someProperty: ",uniqueList.someProperty)