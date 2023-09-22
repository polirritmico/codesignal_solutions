#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You have a long strip of paper with integers written on it in a single line from
left to right. You wish to cut the paper into exactly three pieces such that
each piece contains at least one integer and the sum of the integers in each
piece is the same. You cannot cut through a number, i.e. each initial number
will unambiguously belong to one of the pieces after cutting. How many ways can
you do it?

It is guaranteed that the sum of all elements in the array is divisible by 3.

Example

For a = [0, -1, 0, -1, 0, -1], the output should be solution(a) = 4.

Here are all possible ways:
    [0, -1] [0, -1] [0, -1]
    [0, -1] [0, -1, 0] [-1]
    [0, -1, 0] [-1, 0] [-1]
    [0, -1, 0] [-1] [0, -1]

"""


def solution(integers: list[int]) -> int:
    target_region_value = sum(integers) // 3
    two_regions_value = 2 * target_region_value
    valid_cuts = 0
    current_sum = 0
    cuts = 0
    for number in integers[:-1]:
        current_sum += number
        if current_sum == target_region_value:
            cuts += 1
        if current_sum == two_regions_value:
            valid_cuts += cuts
            if target_region_value == 0:
                valid_cuts -= 1
    return valid_cuts


def main():
    case = [0, -1, 0, -1, 0, -1]
    # expected = 4
    print(solution(case))


if __name__ == "__main__":
    main()
