# 02 Getting more control over formatting
from datetime import datetime

now = datetime.now()
print("now:", now)

print("day of week/month:", now.strftime("%a %A, %d"))
print("month:", now.strftime("%b %B %m"))
print("year:", now.strftime("%y %Y"))

print("Today is", now.strftime("%A, %b %d, %Y"))

print("The time is", now.strftime("%H:%M:%S %p"))