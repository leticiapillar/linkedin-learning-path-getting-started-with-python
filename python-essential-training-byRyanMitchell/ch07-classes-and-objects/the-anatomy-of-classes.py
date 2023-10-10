# 01 The Anatomy of a Class

# Instance Atributes
print("Instance Atributes")
class Dog:
    def __init__(self, name) -> None:
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + "says: Bark!")

myDog = Dog("Rover")
print(myDog.name)
print(myDog.legs)

# AttributeError: type object 'Dog' has no attribute 'legs'
# print(Dog.legs)

print()
# Static Attibutes
print("Static Attibutes")
class Dog:
    legs = 4
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        print(self.name + "says: Bark!")

myDog = Dog("Rover")
print(f"My dog {myDog.name} has {myDog.legs} legs")

print("Prints Dog.legs: ", Dog.legs)
Dog.legs = 3
print("Update Dog.legs: ", Dog.legs)
myDog = Dog("Jhosh")
print(f"My dog {myDog.name} has {myDog.legs} legs")

print()
# Create method get
class Dog:
    _legs = 4
    def __init__(self, name) -> None:
        self.name = name
    
    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + "says: Bark!")

myDog = Dog("Bath")
print(f"My dog {myDog.name} has {myDog.getLegs()} legs")

myDog = Dog("Bob")
myDog._legs = 3
print(f"My dog {myDog.name} has {myDog.getLegs()} legs")
print("Prints Dog._legs: ", Dog._legs)
