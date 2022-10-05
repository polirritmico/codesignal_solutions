#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_string):
    for char in input_string:
        if char.isdecimal():
            return char


def main():
    case = "var_1_Int"
    print(solution(case))

if __name__ == "__main__":
    main()

