# 02 Other types os Numbers

from decimal import Decimal, getcontext

# Integers
print("int('100'), convert to int       :", int('100'))
print("int('100', 2), convert to base 2 :", int('100', 2))
print("int('1ab', 16), convert to base 16:", int('1ab', 16))

# TypeError: int() can't convert non-string with explicit base
# print("int(100, 2), convert to base 2:", int(100, 2))

print("1.2 - 1.0:", 1.2 - 1.0)
print()

# Decimals
print("print getcontext prec=28:", getcontext())
print("Decimal(1)/Decimal(3): ", Decimal(1)/Decimal(3))

print()
getcontext().prec=4
print("update getcontext prec=4:", getcontext())
print("Decimal(1)/Decimal(3): ", Decimal(1)/Decimal(3))

print()
getcontext().prec=2
print("update getcontext prec=4:", getcontext())
print("Decimal(1)/Decimal(3): ", Decimal(1)/Decimal(3))

print()
print("Decimal(3.14): ", Decimal(3.14))
# Prints Decimal(3.14):  3.140000000000000124344978758017532527446746826171875
print("Decimal('3.14'): ", Decimal('3.14'))

print("round(1.2 - 1.0)   : ", round(1.2 - 1.0))
print("round(1.2 - 1.0, 2): ", round(1.2 - 1.0, 2))
