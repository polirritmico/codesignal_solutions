#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Define an alphabet reflection as follows: a turns into z, b turns into y, c
turns into x, ..., n turns into m, m turns into n, ..., z turns into a.

Define a string reflection as the result of applying the alphabet reflection to
each of its characters.

Reflect the given string.

Example

For inputString = "name", the output should be
solution(inputString) = "mznv".
"""


def solution(input_str: str) -> str:
    return "".join([chr(219 - ord(char)) for char in input_str])


def main():
    case = "name"
    # expected = "mznv"
    print(solution(case))


if __name__ == "__main__":
    main()
