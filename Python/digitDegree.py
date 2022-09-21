#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(number):
    if number < 10:
        return 0
    # Got two or more digits, so already one digit degree:
    digit_degree = 1
    # number to list of integers:
    digit_list = [int(digit) for digit in str(number)]
    digit_sum = sum(digit_list)
    # Recursive call. If digit_sum is < 10 then we get the
    # base case in the recursion:
    digit_degree += solution(digit_sum)
    return digit_degree


def main():
    case = 877
    # expected → 2
    print(solution(case))

if __name__ == "__main__":
    main()

