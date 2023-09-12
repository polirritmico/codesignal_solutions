#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Check whether the given string is a subsequence of the plaintext alphabet.

Example

    For s = "effg", the output should be
    solution(s) = false;
    For s = "cdce", the output should be
    solution(s) = false;
    For s = "ace", the output should be
    solution(s) = true;
    For s = "bxz", the output should be
    solution(s) = true.
"""


def solution(input: str) -> bool:
    prev_char = input[0]
    for char in input[1:]:
        if char <= prev_char:
            return False
        prev_char = char
    return True


def main():
    case = "effg"
    print(solution(case))


if __name__ == "__main__":
    main()
