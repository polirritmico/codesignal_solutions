#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
John Doe likes holidays very much, and he was very happy to hear that his
country's government decided to introduce yet another one. He heard that the new
holiday will be celebrated each year on the xth week of month, on weekDay.

Your task is to return the day of month on which the holiday will be celebrated
in the year yearNumber.

For your convenience, here are the lists of months names and lengths and the
list of days of the week names.

    - Months: "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December".
    - Months lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
    - Days of the week: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
    "Saturday", "Sunday".

Please, note that in leap years February has 29 days.

Example

For x = 3, weekDay = "Wednesday", month = "November", and yearNumber = 2016, the
output should be solution(x, weekDay, month, yearNumber) = 16.

The new holiday will be celebrated every November on the 3rd Wednesday of the
month. In 2016 the 3rd Wednesday falls on the 16th of November.

For x = 5, weekDay = "Thursday", month = "November", and yearNumber = 2016, the
output should be solution(x, weekDay, month, yearNumber) = -1.

There are only 4 Thursdays in November 2016.


"""

from calendar import day_name
from datetime import datetime, timedelta


def solution(week_number: int, week_day: str, month_name: str, year_number: int) -> int:
    holiday = datetime.strptime(f"{year_number}-{month_name}-1", "%Y-%B-%d").date()
    target_month = holiday.month
    target_weekday = list(day_name).index(week_day)
    while True:
        if holiday.weekday() == target_weekday:
            week_number -= 1
        if week_number == 0:
            return holiday.day
        holiday += timedelta(days=1)
        if holiday.month != target_month:
            return -1


def main():
    x = 3
    week_day = "Thursday"
    month = "January"
    year_number = 2101
    # expected = 20
    print(solution(x, week_day, month, year_number))


if __name__ == "__main__":
    main()
