# 03 Process
from multiprocess import Process
import time
import threading

def longSquare(num, results):
    time.sleep(1)
    print(num**2)
    print("Finished computing!")

results = {}
threads = [Process(target=longSquare, args=(n,results)) for n in range(0, 10)]
[t.start() for t in threads]
[t.join() for t in threads]


results = {}
threads = [threading.Thread(target=longSquare, args=(n,results)) for n in range(0, 10)]
[t.start() for t in threads]
[t.join() for t in threads]
print("results:", results)
