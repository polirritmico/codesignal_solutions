#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Check if the given string is a correct time representation of the 24-hour clock.

Example

    For time = "13:58", the output should be
    solution(time) = true;
    For time = "25:51", the output should be
    solution(time) = false;
    For time = "02:76", the output should be
    solution(time) = false.

"""


def solution(time: str) -> bool:
    splitted_time = time.split(":")
    if len(splitted_time) != 2:
        return False
    for section in splitted_time:
        if not section.isdecimal():
            return False
    hour = int(splitted_time[0])
    minute = int(splitted_time[1])
    if hour < 0 or hour > 23:
        return False
    if minute < 0 or minute > 59:
        return False
    return True


def main():
    case = "13:58"
    print(solution(case))


if __name__ == "__main__":
    main()
