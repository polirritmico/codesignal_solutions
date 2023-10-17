#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a rectangular matrix of integers, check if it is possible to rearrange its
rows in such a way that all its columns become strictly increasing sequences
(read from top to bottom).

Example

    For

    matrix = [[2, 7, 1],
              [0, 2, 0],
              [1, 3, 1]]

    the output should be
    solution(matrix) = false;

    For

    matrix = [[6, 4],
              [2, 2],
              [4, 3]]

    the output should be
    solution(matrix) = true.

"""


def solution(matrix: list[int]) -> bool:
    columns_in_matrix = len(matrix[0])
    first_column = [(row[0], idx) for idx, row in enumerate(matrix)]
    sorted_matrix = []
    for position in sorted(first_column):
        row_idx_in_matrix = position[1]
        sorted_matrix.append(matrix[row_idx_in_matrix])
    sorted_cols = [[row[i] for row in sorted_matrix] for i in range(columns_in_matrix)]
    for column in sorted_cols:
        previous = column[0]
        for number in column[1:]:
            if number <= previous:
                return False
            previous = number
    return True


def main():
    case = [[2, 7, 1], [0, 2, 0], [1, 3, 1]]
    # expected = False
    print(solution(case))


if __name__ == "__main__":
    main()
