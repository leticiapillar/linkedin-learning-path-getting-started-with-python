# Count the number of instances of a particular weekday in a given month/year

import calendar

def count_days(year, month, whichday):
    # Your code goes here.
    weeksofmonth = calendar.monthcalendar(year, month)
    dayscount = 0
    for week in weeksofmonth:
        if week[whichday] != 0:
            dayscount += 1    
    return dayscount


def main():
    inputs = [
        [2025,12,0], # (December 2025, Monday), Result: There are 5 Monday in December 2025
        [2030,1,5],  # (January 2030, Saturday), Result: There are 4 Saturdays in January 2030
    ]
    for i in inputs:
        days = count_days(i[0], i[1], i[2])
        print(f"There are {days} days in {i}")


if __name__ == "__main__":
    main()
