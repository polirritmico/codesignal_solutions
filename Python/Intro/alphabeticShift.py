#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_string):
    output = ""
    letters = "abcdefghijklmnopqrstuvwxyza"
    for char in input_string:
        position = letters.index(char) + 1
        output += letters[position]
    return output


def main():
    case = "crazy"
    # expected: dsbaz
    print(solution(case))

if __name__ == "__main__":
    main()

