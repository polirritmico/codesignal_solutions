#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(input_str: str) -> int:
    input_unique_chars = len(set(input_str))
    if input_unique_chars > 10:
        raise ValueError("More than 10 diff letters")

    input_str_length = len(input_str)
    max_base = int((10**input_str_length) ** 0.5)
    min_base = int((10 ** (input_str_length - 1)) ** 0.5)
    for current_base in range(max_base, min_base - 1, -1):
        current_square = current_base**2
        number = str(current_square)
        number_unique_chars = len(set(number))
        if input_unique_chars != number_unique_chars:
            continue

        number_chars = {char: number.count(char) for char in number}
        input_chars = {char: input_str.count(char) for char in input_str}
        sorted_digits = sorted(number_chars.values())
        sorted_chars = sorted(input_chars.values())
        if sorted_digits == sorted_chars:
            return current_square
    return -1


def main():
    # case = "ab"
    # expected = 81
    # case = "aba"
    # expected = 900
    # case = "aaaabbcde"
    # expected = 999950884
    case = "abcbbb"
    # expected = 810000
    print(solution(case))


if __name__ == "__main__":
    main()
