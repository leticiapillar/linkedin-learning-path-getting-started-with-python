# Can You Hear Me Now?

# Create a function "getWithRetry" that calls a function until it receives response that is not None, and then returns that response. If it continues to get no response, it should give up after a certain number of tries (to be decided by you)

# After filling out the "getWithRetry" function, run all of the cells in this notebook in order to test the following scenarios:

# All services are up
# All services are down
# All services are down and making a request takes 0.1 seconds to execute
# What is the ideal number of retries before giving up? How do you know whether the service is down or you're just unlucky?

import random
import time
servicesAreUp = True

def getData50():
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'

def getData25():
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'    

def getData10():
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'

# Your code here!
def getWithRetry(dataFunc):
    result = None
    count = 0
    while True:
        result = dataFunc()
        if result != None or count > 5:
            break
        count += 1
    return result

# Solution by Course
def getWithRetry(dataFunc):
    maxRetries = 10
    for _ in range(0, maxRetries):
        response = dataFunc()
        if response:
            return response

# Solution using recursive function
def getWithRetry(dataFunc, retries=20):
    if retries == 0:
        return None
    return dataFunc() or getWithRetry(dataFunc, retries-1)


print("----- servicesAreUp = True -----")

# Should return 'You got the data! That only happens 50% of the time!'
result = getWithRetry(getData50)
print("result of getData50: ", result)

# Should return 'You got the data! That only happens 25% of the time!'
result = getWithRetry(getData25)
print("result of getData25: ", result)

# Should return 'You got the data! That only happens 10% of the time!'
result = getWithRetry(getData10)
print("result of getData10: ", result)

print("----- servicesAreUp = False -----")
servicesAreUp = False

# Returns None
result = getWithRetry(getData50)
print("result of getData50: ", result)

# Returns None
result = getWithRetry(getData25)
print("result of getData25: ", result)

# Returns None
result = getWithRetry(getData10)
print("result of getData10: ", result)

print("------------------------------")

def getData50():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'

def getData25():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'    

def getData10():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'

# Returns None
result = getWithRetry(getData50)
print("result of getData50:", result)
result = getWithRetry(getData25)
print("result of getData25:", result)
result = getWithRetry(getData10)
print("result of getData10:", result)
 