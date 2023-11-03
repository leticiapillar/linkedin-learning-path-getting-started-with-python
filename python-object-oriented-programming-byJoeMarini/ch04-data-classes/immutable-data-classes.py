# Python Object Oriented Programming by Joe Marini course example
# 04 Creating immutable data classes

from dataclasses import dataclass


# TODO: "The "frozen" parameter makes the class immutable
@dataclass(frozen=True)  
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def updatevalue2(self, newvalue):
        self.value2 = newvalue


obj = ImmutableClass()
print(obj.value1)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "Another value"
# print(obj.value1)
# dataclasses.FrozenInstanceError: cannot assign to field 'value1'

# TODO: even functions within the class can't change anything
obj.value2 = 4
print(obj.value2)
# dataclasses.FrozenInstanceError: cannot assign to field 'value2'
