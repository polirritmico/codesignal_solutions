#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_string):
    reading_number = ""
    numbers_sum = 0
    for char in input_string:
        if char.isdigit():
            reading_number += char
            continue
        # not number and prev is number
        if reading_number != "":
            numbers_sum += int(reading_number)
        reading_number = ""

    if reading_number != "":
            numbers_sum += int(reading_number)
    return numbers_sum


def main():
    case = "1a1 2"
    print(solution(case))

if __name__ == "__main__":
    main()

