# Python Object Oriented Programming by Joe Marini course example
# 03 Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()
    
    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

class D(B, A):
    def __init__(self):
        super().__init__()
    
    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()
print("Class C:", C.__mro__)
c.showprops()

print()
d = D()
print("Class D:", D.__mro__)
d.showprops()
