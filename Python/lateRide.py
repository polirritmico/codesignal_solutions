#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    hours_digits = [str(char) for char in str(hours)]
    minutes_digits = [str(char) for char in str(minutes)]
    sum = 0
    for char in hours_digits + minutes_digits:
        sum += int(char)
    return sum


def main():
    case = 240
    # expected 4
    print(solution(case))

if __name__ == "__main__":
    main()

