# 01 Datetime Module Part I
from datetime import datetime

now = datetime.now()
print("now:", now)

print("month, day, year:", now.month, now.day, now.year)
print("hour, minute, second, microsecond:", now.hour, now.minute, now.second, now.microsecond)
print("now as timezone:",now.astimezone())
