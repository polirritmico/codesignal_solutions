#!/usr/bin/env python
# -*- coding: utf-8 -*-

def not_valid(char):
    value = ord(char)
    if value > 64 and value < 71:
        return False
    if value > 47 and value < 58:
        return False
    return True


def solution(input_string):
    if len(input_string) != 17:
        return False
    digits_collection = input_string.split('-')
    if len(digits_collection) != 6:
        return False
    for digit in digits_collection:
        if not_valid(digit[0]) or not_valid(digit[1]):
            return False
    return True


def main():
    case = "00-1B-63-84-45-E6"
    print(solution(case))


if __name__ == "__main__":
    main()

