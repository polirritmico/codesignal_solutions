#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a positive integer number and a certain length, we need to modify the
given number to have a specified length. We are allowed to do that either by
cutting out leading digits (if the number needs to be shortened) or by adding 0s
in front of the original number.

Example

    For number = 1234 and width = 2, the output should be
    solution(number, width) = "34";
    For number = 1234 and width = 4, the output should be
    solution(number, width) = "1234";
    For number = 1234 and width = 5, the output should be
    solution(number, width) = "01234".
"""


def solution(number: int, width: int) -> str:
    number = str(number).zfill(width)
    char_index = 0 - width
    return number[char_index:]


def main():
    number = 1234
    width = 2
    # expected = "34"
    number = 23456
    width = 4
    # expected = "3456"
    print(solution(number, width))


if __name__ == "__main__":
    main()
