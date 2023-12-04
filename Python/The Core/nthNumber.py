#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement the missing code, denoted by ellipses. You may not modify the
pre-existing code.

You are given a string s of characters that contains at least n numbers (here,
a number is defined as a consecutive series of digits, where any character
immediately to the left and right of the series are not digits). The numbers may
contain leading zeros, but it is guaranteed that each number has at least one
non-zero digit in it.

Your task is to find the nth number and return it as a string without leading
zeros.

Example

For s = "8one 003number 201numbers li-000233le number444" and n = 4,
the output should be
solution(s, n) = "233".

"""
import re


def solution(s, n):
    pattern = r"(?:[^1-9]*(\d+)){" + str(n) + "}"
    return re.match(pattern, s).group(1)


def main():
    s = "some023020 num ber 033 02103 32 meh peh beh 4328 "
    n = 5
    # expected = "4328"
    print(solution(s, n))


if __name__ == "__main__":
    main()
