# 04 Create a Timer with the Time module
import time

start = input("Start (yes/no)? ")

seconds = 0
if start == "yes":
    while seconds < 10:
        print(">", seconds)
        time.sleep(1)
        seconds += 1
print("Bye...")