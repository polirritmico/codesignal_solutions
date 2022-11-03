#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(number):
    reversed_number_str = str(number)[::-1]
    prev_zero = True
    for char in reversed_number_str:
        if char != '0':
            prev_zero = False
        elif not prev_zero:
            return True
    return False


def main():
    case = 902200100
    #expected = True
    print(solution(case))

if __name__ == "__main__":
    main()

