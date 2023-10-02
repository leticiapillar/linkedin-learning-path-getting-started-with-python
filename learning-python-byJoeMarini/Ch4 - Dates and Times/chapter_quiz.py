import calendar
from datetime import date, datetime, timedelta

# Of the following examples, which one will correctly print the name of tomorrow's day of the week?
today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be "+days[(today.weekday()+1)%7])

# What calendar class will you use to create a Python list of weeks for a given month, where each week is a Python list of days?"
print(calendar.monthcalendar(2023,8))

# Your program needs to alert the user if their password expires in less than 7 days. Assuming the password expiration date is in the texp variable, what option will work best?
texp = date.today()
if ((texp-date.today()).days<7):
    print("password will expire soon!")

# Which strftime() code prints the abbreviated weekday name?
now = datetime.now()
print(now.strftime("%a"))

# Of the following examples, which one will generate a date and time output in the following format?
# 13-Mar-2020 16:42:58
# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("%d-%b-%Y %H:%M:%S"))

# Which code can you use to print a text-formatted monthly calendar for every month in the current year, using Sunday as the first day of the week?
import calendar
import datetime
year = datetime.datetime.now().year
cal = calendar.TextCalendar(calendar.SUNDAY)
for m in range(1,13):
    print(cal.formatmonth(year, m, 0, 0))

# You need to calculate tomorrow's date. Which option should you choose?
today = date.today()
print(today)
# Option A:
tomorrow = today+timedelta(days=1)
print(tomorrow)
# Option B:
tomorrow = date(today.year,today.month,today.day+1)
print(tomorrow)
