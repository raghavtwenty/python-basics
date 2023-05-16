"""
Q1. Separate current date and time using lambda function
                        author @raghav
Date Created : 8 Dec 2021 | Last Updated : 10 Dec 2021
"""


# Importing Required Libraries
import datetime


# Main
now = datetime.datetime.now()

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
ti = str(t(now))

print("\nSeparating Current Year, Month, Date, Time.\n")
print(f"YEAR: {year(now)}")
print(f"MONTH: {month(now)}")
print(f"DAY: {day(now)}")
print(f"TIME: {ti[:8]}")
