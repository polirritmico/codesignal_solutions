#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]

the output should be

solution(picture) = ["*****",
                     "*abc*",
                     "*ded*",
                     "*****"]
"""


def solution(picture: list[str]) -> list[str]:
    original_width = max([len(line) for line in picture])
    horizontal_margin = "*" * (original_width + 2)
    output = [horizontal_margin]
    for line in picture:
        width_diff = original_width - len(line)
        indent = " " * width_diff
        output.append("*" + line + indent + "*")
    output.append(horizontal_margin)
    return output


def main():
    case = ["abc", "ded"]
    # expected = ["*****", "*abc*", "*ded*", "*****"]
    print(solution(case))


if __name__ == "__main__":
    main()
