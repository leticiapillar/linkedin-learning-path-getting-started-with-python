# 02 Variables and Scopes

# Function Scope
print("Function Scope")
def performOperation(*args, **kwargs):
    print("*args   :", args)
    print("**kwargs:", kwargs)

performOperation(1, 2, operation="sum")

print()
# locals()
def performOperation(*args, **kwargs):
    print("local scope:", locals())

performOperation(1, 2, operation="multiply")

print()
# globals()
globals_variables = globals()
print("globals variables:", globals_variables)

print()
# Global and Local Scope
message = "Some global data"

def function1(varA, varB):
    print("global scope:", message)
    print("local scope :", locals())

def function2(varC, varD):
    print("global scope:", message)
    print("local scope :", locals())

function1(1, 2)
function1(3, 4)

print()
message = "Some global data two"
varA = 2
def function1(varA, varB):
    message = "Some local data"
    print("local scope varA:", varA)
    print("local scope     :", message)
    print("local scope     :", locals())

def function2(varC, varD):
    print("global scope varA:", varA)
    print("global scope     :", message)
    print("local scope      :", locals())

function1(1, 2)
function1(3, 4)

print()
def function3(varE, varF):
    message = "Some local data"
    print("local scope varA:", varA)
    def inner_function(varE, varF):
        print(f"inner function local scope: {locals()}")
    
    print("function 3 local scope:", locals())
    inner_function(123, 456)

function3(5, 6)
