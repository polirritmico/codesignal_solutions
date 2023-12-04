#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_array):
    if len(input_array) == 0:
        return input_array
    first_elem = input_array[0]
    input_array[0] = input_array[-1]
    input_array[-1] = first_elem
    return input_array
    


def main():
    case = [23, 54, 12, 3, 4, 56, 23, 12, 5, 324]
    print(solution(case))

if __name__ == "__main__":
    main()

