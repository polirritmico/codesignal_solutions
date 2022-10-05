#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(number):
    number_str = str(number)
    max_value = 0
    length = len(number_str)
    for i in range(length):
        sub_string = number_str[0:i] + number_str[i+1:]
        max_value = max(int(sub_string), max_value)
    return max_value


def main():
    case = 152 #52
    print(solution(case))

if __name__ == "__main__":
    main()

