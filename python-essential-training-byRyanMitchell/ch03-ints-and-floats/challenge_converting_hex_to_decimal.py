"""
Converting Hexadecimal to Decimal
Hexadecimal or "base 16" uses all of the numbers 0 - 9, plus a few others to signify higher numbers:

A = 10

B = 11

C = 12

D = 13

E = 14

F = 15

Therefore, the number 'D' in hexadecimal would be 13 in decimal.

The number '1A' in hexadecimal would be 26 in decimal. Just like we have the "tens" place in base 10, hexadecimal has the "sixteens" place. So 1A would be 16 + 10 or 26.

And just like decimal has the "hundreds" place (because 10 * 10 is 100), hexadecimal has the "256's" place (because 16 * 16 is 256) So 'ABC' in hexadecimal is (256 * 10) + (16 * 11) + (1 * 12) or 2,748

"""

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    convert = True
    for h in hexNum:
        if h not in hexNumbers:
            convert = False
            break
    if convert:
        return int(hexNum,16)
    return None

def hexToDec_sol2(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    
    if len(hexNum) == 3:
        return hexNumbers[hexNum[0]] * 256 + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[2]]
    if len(hexNum) == 2:
        return hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]]
    if len(hexNum) == 1:
        return hexNumbers[hexNum[0]]

def hexToDec_sol3(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    
    exponent = 0
    decimalValue = 0
    for char in hexNum[::-1]:
        decimalValue = decimalValue +hexNumbers[char] * (16**exponent)
        exponent += 1
    return decimalValue


# 10
print(hexToDec('A'))
print(hexToDec_sol2('A'))
print(hexToDec_sol3('A'))

# 0
print(hexToDec('0'))
print(hexToDec_sol2('0'))
print(hexToDec_sol3('0'))

# 27
print(hexToDec('1B'))
print(hexToDec_sol2('1B'))
print(hexToDec_sol3('1B'))

# 960
print(hexToDec('3C0'))
print(hexToDec_sol2('3C0'))
print(hexToDec_sol3('3C0'))

# None
print(hexToDec('A6G'))
print(hexToDec_sol2('A6G'))
print(hexToDec_sol3('A6G'))

# None
print(hexToDec('ZZTOP'))
print(hexToDec_sol2('ZZTOP'))
print(hexToDec_sol3('ZZTOP'))

# 3932160
print(hexToDec_sol3('3C0000'))
