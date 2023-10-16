# 03 JSON
import json
from json import JSONDecodeError, JSONEncoder

# Loading JSON file
print("Loading JSON file")
jsonString = '{"a": "apple", "b": "bear", "c": "cat"}'
print("jsonString:", jsonString)
print("json loads as jsonString:", json.loads(jsonString))

# Throws JSONDecoderError
print("Throws JSONDecoderError")
jsonString = '{"a": "apple", "b": "bear", "c": "cat", }'
print("jsonString:", jsonString)
try:
    json.loads(jsonString)
except JSONDecodeError as e:
    print("Could not parse JSON!", type(e))

print("print as dictionary:", {"a": "apple", "b": "bear", "c": "cat", })

print()
# Dumping JSON
print("Dumping JSON")
pythonDict = {"a": "apple", "b": "bear", "c": "cat", }
print("json dumps:", json.dumps(pythonDict))

print()
# Custom JSON Decorders
print("Dumping JSON")

class Animal:
    def __init__(self, name):
        self.name = name

# pythonDict = {"a": Animal("aardvark"), "b": Animal("bear"), "c": Animal("cat"), }
# print("Animal json dumps:", json.dumps(pythonDict))
# TypeError: Object of type Animal is not JSON serializable

class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Animal:
            return o.name
        return super().default(o)

pythonDict = {"a": Animal("aardvark"), "b": Animal("bear"), "c": Animal("cat"), }
print("Animal json dumps (AnimalEncoder):", json.dumps(pythonDict, cls=AnimalEncoder))
