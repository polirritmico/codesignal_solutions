#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of strings, sort them in the order of increasing lengths. If two
strings have the same length, their relative order must be the same as in the
initial array.

Example

For

inputArray = ["abc", "", "aaa", "a", "zz"]

the output should be

solution(inputArray) = ["", "a", "zz", "abc", "aaa"]

"""


def solution(input_array: list[str]) -> list[str]:
    return sorted(input_array, key=len)


def main():
    case = ["a", "c", "a", "a"]
    # expected = ["a", "c", "a", "a"]
    print(solution(case))


if __name__ == "__main__":
    main()
