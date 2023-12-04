#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n):
    return ((((n+1) | n) + 1) | n) - n
    return second_rightmost_zero_bit(n)


def second_rightmost_zero_bit(n):
    reversed_binary_string = format(n, "32b")[::-1]
    first_zero = False
    for position in range(len(reversed_binary_string)):
        current_value = reversed_binary_string[position]
        if current_value == "0" and first_zero:
            return 2 ** position
        if current_value == "0":
            first_zero = True



def main():
    case = 37
    #expected = 8
    print(solution(case))

if __name__ == "__main__":
    main()

