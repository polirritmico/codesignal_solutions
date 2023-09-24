#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Your Informatics teacher at school likes coming up with new ways to help you
understand the material. When you started studying numeral systems, he
introduced his own numeral system, which he's convinced will help clarify
things. His numeral system has base 26, and its digits are represented by
English capital letters - A for 0, B for 1, and so on.

The teacher assigned you the following numeral system exercise: given a
one-digit number, you should find all unordered pairs of one-digit numbers whose
values add up to the number.

Example

For number = 'G', the output should be
solution(number) = ["A + G", "B + F", "C + E", "D + D"].

Translating this into the decimal numeral system we get: number = 6, so it is
["0 + 6", "1 + 5", "2 + 4", "3 + 3"].
"""


def solution(num_str: str) -> list[str]:
    number = ord(num_str) - 65
    output = []
    for num_a in range(number // 2 + 1):
        num_b = number - num_a
        output.append(f"{chr(num_a + 65)} + {chr(num_b + 65)}")
    return output


def main():
    # case = "G"
    # expected = ["A + G", "B + F", "C + E", "D + D"]
    case = "D"
    # expected = ["A + D", "B + C"]
    print(solution(case))


if __name__ == "__main__":
    main()
