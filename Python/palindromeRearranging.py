#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_string):
    str_collection = {}
    for char in input_string:
        if char not in str_collection:
            str_collection[char] = 1
        else:
            str_collection[char] += 1
    if len(str_collection) == 1:
        return True

    # A palindrome could only have one odd char
    odd_char = False
    for char in str_collection:
        if str_collection[char] % 2 != 0:
            if odd_char:
                return False
            odd_char = True
    return True


def main():
    case = "abac"
    print(solution(case))

if __name__ == "__main__":
    main()

