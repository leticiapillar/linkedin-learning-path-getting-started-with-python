#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
    
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print(f"Driving my {self.engine} Car at {self.speed} km/h")


class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if hassidecar:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engine = enginetype

    def drive(self, speed):
        super().drive(speed)
        print(f"Driving my {self.engine} Motorcycle at {self.speed} km/h")



car1 = Car("gas")
car2 = Car("eletric")
mc1 = Motorcycle("gas", True)

print(f"Car 1 works by {car1.engine} and has {car1.wheels} wheels")
print(f"Car 2 works by {car2.engine} and has {car2.wheels} wheels")
print(f"Motorcycle 1 works by {mc1.engine} and has {mc1.wheels} wheels")

car1.drive(30)
car2.drive(45)
mc1.drive(50)
