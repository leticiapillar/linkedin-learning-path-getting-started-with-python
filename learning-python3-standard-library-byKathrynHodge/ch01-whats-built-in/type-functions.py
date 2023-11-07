
nums = range(0, 10)
print("nums:", nums)
print("type of nums:", type(nums))
print("type of int :", type(1))
print("type of flot:", type(1.1))
print("type of str 'a':", type("a"))
print("type of str 'hello, world':", type('hello, world'))

class Car:
    pass

class Truck(Car):
    pass

class Motorcycle:
    pass


c1 = Car()
c2 = Car()
t1 = Truck()
m1 = Motorcycle()

print("type of c1:", type(c1))
print("type of t1:", type(t1))

print("type of c1 == t1:", type(c1) == type(t1))
print("type of c1 == c2:", type(c1) == type(c2))

print("c1 is instance of Car:", isinstance(c1, Car))
print("c2 is instance of Car:", isinstance(c2, Car))
print("t1 is instance of Car:", isinstance(t1, Car))
print("t1 is instance of Truck:", isinstance(t1, Truck))

print("m1 is instance of Car:", isinstance(m1, Car))
print("m1 is instance of Motorcycle:", isinstance(m1, Motorcycle))
