class Dog():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking.")
    
    def addYear(self):
        self.age += 1
    
    def getInfo(self):
        print(f"{self.name} is {self.age} years old.")

class Poodle(Dog):
    def __init__(self, name, age, color, weight) -> None:
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    
    def bark(self, manner="energeticaly"):
        print(f"{self.name} is barking {manner}.")

    def getInfo(self):
        print(f"{self.name} is {self.age} years old {self.color} poodle and weight {self.weight} pounds.")


class Corgi(Dog):
    def __init__(self, name, age, color, weight) -> None:
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    
    def bark(self, manner="briefly"):
        print(f"{self.name} is barking {manner}.")

    def getInfo(self):
        print(f"{self.name} is {self.age} years old {self.color} corgi and weight {self.weight} pounds.")


def main():
    ella = Dog("Ella", 3.5)
    ella.getInfo()
    ella.bark()
    ella.addYear()
    ella.getInfo()

    bob = Poodle("Bob", 3, "white", 25)
    bob.getInfo()
    bob.bark()
    bob.addYear()
    bob.getInfo()

    peppi = Poodle("Peppi", 5, "white", 20)
    peppi.getInfo()
    peppi.bark()
    peppi.addYear()
    peppi.getInfo()

if __name__ == "__main__":
    main()




