#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_array):
    max_abs_diff = (-10 ** 6) - 1
    length = len(input_array)
    prev = input_array[0]
    next = input_array[2]

    for i in range(1, length - 1):
        current = input_array[i]
        prev = input_array[i-1]
        next = input_array[i+1]
        buff = max(abs(current - prev), abs(current - next))
        max_abs_diff = buff if buff > max_abs_diff else max_abs_diff

    return max_abs_diff



def main():
    case = 0
    print(solution(case))

if __name__ == "__main__":
    main()

