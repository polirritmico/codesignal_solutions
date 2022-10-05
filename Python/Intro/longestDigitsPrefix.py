#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_string):
    if not input_string[0].isdecimal():
        return ""
    output = ""
    for char in input_string:
        if char.isdecimal():
            output += char
        else:
            break
    return output


def main():
    case = "123aa1"
    print(solution(case))

if __name__ == "__main__":
    main()

