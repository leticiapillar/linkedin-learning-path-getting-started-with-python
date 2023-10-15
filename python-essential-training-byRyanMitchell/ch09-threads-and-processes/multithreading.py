# 02 Threads

import threading
import time

def longSquare(num):
    time.sleep(1)
    return num**2

print([longSquare(n) for n in range(0, 5)])

print("----------")

t1 = threading.Thread(target=longSquare, args=(1,))
t2 = threading.Thread(target=longSquare, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()

print("----------")

def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}
t1 = threading.Thread(target=longSquare, args=(1,results))
t2 = threading.Thread(target=longSquare, args=(2,results))

t1.start()
t2.start()

t1.join()
t2.join()

print("results:", results)

print("----------")
def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}
threads = [threading.Thread(target=longSquare, args=(n,results)) for n in range(0, 100)]
[t.start() for t in threads]
[t.join() for t in threads]
print("results:", results)

