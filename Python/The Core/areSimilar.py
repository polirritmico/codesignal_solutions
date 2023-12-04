#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Two arrays are called similar if one can be obtained from another by swapping at
most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

    For a = [1, 2, 3] and b = [1, 2, 3], the output should be
    solution(a, b) = true.

    The arrays are equal, no need to swap any elements.

    For a = [1, 2, 3] and b = [2, 1, 3], the output should be
    solution(a, b) = true.

    We can obtain b from a by swapping 2 and 1 in b.

    For a = [1, 2, 2] and b = [2, 1, 1], the output should be
    solution(a, b) = false.

    Any swap of any two elements either in a or in b won't make a and b equal.

"""


def solution(array_a: list[int], array_b: list[int]) -> bool:
    diff_a = []
    diff_b = []
    for a, b in zip(array_a, array_b):
        if a != b:
            diff_a.append(a)
            diff_b.insert(0, b)
    length = len(diff_a)

    return length == 0 or (length == 2 and diff_a == diff_b)


def main():
    a = [1, 2, 3]
    b = [1, 2, 3]
    # expected = True
    print(solution(a, b))


if __name__ == "__main__":
    main()
