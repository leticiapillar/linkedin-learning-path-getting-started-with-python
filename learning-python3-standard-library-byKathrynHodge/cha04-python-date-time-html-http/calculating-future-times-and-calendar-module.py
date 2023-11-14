# 03 Calendar Module
from datetime import datetime, timedelta
import calendar

now = datetime.now()
print("Now:", now)

todayAfter2Days = now + timedelta(days=2)
todayBeforeThreeWeeks = now - timedelta(weeks=3)
print("Today after 2 days  :", todayAfter2Days.date())
print("Today before 3 weeks:", todayBeforeThreeWeeks.date())
print("after 2 days > 3 weeks before?", todayAfter2Days > todayBeforeThreeWeeks)

print("Calendar")
augOf2000 = calendar.month(2000, 8)
print(augOf2000)

weekdayOfAug2000 = calendar.weekday(2000,8,22)
print("weekday of 08/22/2000:", weekdayOfAug2000)

print("2023 is leap?", calendar.isleap(2023))
print("2024 is leap?", calendar.isleap(2024))

