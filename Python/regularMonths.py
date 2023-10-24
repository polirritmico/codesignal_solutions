#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
In an effort to be more innovative, your boss introduced a strange new
tradition: the first day of every month you're allowed to work from home. You
like this rule when the day falls on a Monday, because any excuse to skip rush
hour traffic is great!

You and your colleagues have started calling these months regular months. Since
you're a fan of working from home, you decide to find out how far away the
nearest regular month is, given that the currMonth has just started.

For your convenience, here is a list of month lengths (from January to December,
respectively):

    Month lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.

Please, note that in leap years February has 29 days.

Example

For currMonth = "02-2016", the output should be solution(currMonth) = "08-2016".

February of 2016 year is regular, but it doesn't count since it has started
already, so the next regular month is August of 2016 - which is the answer.
string currMonth

Input/Output

A string representing the current month in the format mm-yyyy, where mm is the
number of the month (1-based, i.e. 01 for January, 02 for February and so on)
and yyyy is the year.

"""

from datetime import datetime as dt


def solution(current_month: str) -> str:
    current = dt.strptime(current_month, "%m-%Y")
    while True:
        if current.month == 12:
            current = current.replace(year=current.year + 1, month=1)
        else:
            current = current.replace(month=current.month + 1)
        if current.weekday() == 0:
            return current.strftime("%m-%Y")


def main():
    case = "12-2016"
    # expected = "08-2016"
    print(solution(case))


if __name__ == "__main__":
    main()
