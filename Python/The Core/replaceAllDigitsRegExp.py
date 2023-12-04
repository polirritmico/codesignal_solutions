#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement the missing code, denoted by ellipses. You may not modify the
pre-existing code.

Implement a function that replaces each digit in the given string with a '#'
character.

Example

For input = "There are 12 points", the output should be
solution(input) = "There are ## points".

"""

import re


def solution(inputString):
    return re.sub(r"[0-9]", "#", inputString)


def main():
    case = "There are 12 points"
    # expected = "There ara ## points"
    print(solution(case))


if __name__ == "__main__":
    main()
