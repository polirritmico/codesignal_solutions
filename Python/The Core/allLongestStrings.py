#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of strings, return another array containing all of its longest
strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
"""


def solution(input_array) -> list[str]:
    biggest_length = 0
    biggest_strings = []
    for string in input_array:
        string_size = len(string)
        if string_size < biggest_length:
            continue
        if string_size > biggest_length:
            biggest_length = string_size
            biggest_strings = []
        biggest_strings.append(string)
    return biggest_strings


def main():
    case = [
        "young",
        "yooooooung",
        "hot",
        "or",
        "not",
        "come",
        "on",
        "fire",
        "water",
        "watermelon",
    ]
    # expected = ["yooooooung", "watermelon"]
    print(solution(case))


if __name__ == "__main__":
    main()
