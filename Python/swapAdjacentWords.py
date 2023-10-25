#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement the missing code, denoted by ellipses. You may not modify the
pre-existing code.

You are given a string consisting of words separated by whitespace characters,
where the words consist only of English letters. Your task is to swap pairs of
consecutive words and return the result.

Example

    For s = "CodeFight On", the output should be
    solution(s) = "On CodeFight";
    For s = "How are you today guys", the output should be
    solution(s) = "are How today you guys".


Input/Output

A string consisting of whitespace characters (' ') and English letters. There is
exactly one whitespace character between two consecutive words, and both the
first and the last characters of s are not equal to ' '.

"""

import re


def solution(s):
    return re.sub(r"(\S*)( )?(\S*)( )?", r"\3\2\1\4", s)


def main():
    case = "CodeFight On"
    # expected = "On CodeFight"
    print(solution(case))


if __name__ == "__main__":
    main()
