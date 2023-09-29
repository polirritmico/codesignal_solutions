#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given array of integers, for each position i, search among the previous
positions for the last (from the left) position that contains a smaller value.
Store this value at position i in the answer. If no such value can be found,
store -1 instead.

Example

For items = [3, 5, 2, 4, 5], the output should be
solution(items) = [-1, 3, -1, 2, 4].
"""


def solution(items: list[int]) -> list[int]:
    output = [-1]
    for check_num_pos, check_num in enumerate(items):
        for left_num_pos in range(check_num_pos, 0, -1):
            left_current = items[left_num_pos - 1]
            if left_current < check_num:
                output.append(left_current)
                break
            elif left_num_pos == 1:
                output.append(-1)
    return output


def main():
    case = [3, 5, 2, 4, 5]
    # expected = [-1, 3, -1, 2, 4]
    print(solution(case))


if __name__ == "__main__":
    main()
