# Date Detection
# Write a regular expression that can detect dates in the DD/MM/YYYY format.
# Assume that the days range from 01 to 31, the months range from 01 to 12,
# and the years range from 1000 to 2999.
# Note that if the day or month is a single digit, it’ll have a leading zero.
#
# The regular expression doesn’t have to detect correct days for each month or for leap years;
# it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
# Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date.
# April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days.
# February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100,
# unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a
# reasonably sized regular expression that can detect a valid date.

import re
date = "25/01/2004"

def date_checker(date):
    dateRegex = re.compile(r"(\d{2})/([0-1]\d)/([0-2]\d\d\d)")

    day = int(dateRegex.search(date).group(1))
    month = int(dateRegex.search(date).group(2))
    year = int(dateRegex.search(date).group(3))

    if month == 4 or 6 or 9 or 11 and day == 31:
        print("False! Too many days in a month!")




    elif month == 2:
        if day > 28 and year % 4 != 0:
            print("False! February can't have more than 29 days in non-leap years!")
        elif day > 28 and year % 4 == 0 and year % 100 == 0:
            print("False! February can't have more than 28 days in leap years divisible by 100")
        elif day > 29 and year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            print("False: february can't have more than 29 days in leap years divisible by 100 and 400")
        elif day > 29 and year % 4 == 0:
            print("False, february can't have more than 29 days in leap years!")
    return True