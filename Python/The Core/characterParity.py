#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a character, check if it represents an odd digit, an even digit or not a
digit at all.

Example

    For symbol = '5', the output should be
    solution(symbol) = "odd";
    For symbol = '8', the output should be
    solution(symbol) = "even";
    For symbol = 'q', the output should be
    solution(symbol) = "not a digit".

"""


def solution(symbol: str) -> str:
    if not symbol.isdecimal():
        return "not a digit"
    return "even" if int(symbol) % 2 == 0 else "odd"


def main():
    case = 0
    print(solution(case))


if __name__ == "__main__":
    main()
