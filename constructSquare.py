#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string consisting of lowercase English letters, find the largest square
number which can be obtained by reordering the string's characters and
replacing them with any digits you need (leading zeros are not allowed) where
same characters always map to the same digits and different characters always
map to different digits.

If there is no solution, return -1.

Example

    - For s = "ab", the output should be
    solution(s) = 81.
    The largest 2-digit square number with different digits is 81.

    - For s = "zzz", the output should be
    solution(s) = -1.
    There are no 3-digit square numbers with identical digits.

    - For s = "aba", the output should be
    solution(s) = 900.
    It can be obtained after reordering the initial string into "baa" and
    replacing "a" with 0 and "b" with 9.

"""

import math


def is_square(number: int) -> bool:
    square_root = math.sqrt(number)
    return math.ceil(square_root) == math.floor(square_root)


def solution(input_str: str) -> int:
    letters_count = {letter: input_str.count(letter) for letter in input_str}
    different_characters = len(letters_count)
    if different_characters > 10:
        raise ValueError("More than 10 diff letters")
    letters_replacements = {
        letter: [num for num in range(10)] for letter in letters_count
    }
    print(letters_replacements)

    largest_sqr = 0
    for left_num in range(9, 0, -1):
        pass

    # inside for
    iteration_replacementes = [values.pop() for values in letters_replacements.values()]
    print(iteration_replacementes)

    return -1 if largest_sqr < 1 else largest_sqr


def main():
    # case = "abbcd"
    case = "ab"
    # expected = 81
    print(solution(case))


if __name__ == "__main__":
    main()
