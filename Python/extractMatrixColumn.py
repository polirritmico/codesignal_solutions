#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a rectangular matrix and an integer column, return an array containing the
elements of the columnth column of the given matrix (the leftmost column is the
0th one).

Example

For

matrix = [[1, 1, 1, 2],
          [0, 5, 0, 4],
          [2, 1, 3, 6]]

and column = 2, the output should be
solution(matrix, column) = [1, 0, 3].

"""


def solution(matrix: list[int], column: int) -> list[int]:
    return [row[column] for row in matrix]


def main():
    matrix = [[1, 1, 1, 2], [0, 5, 0, 4], [2, 1, 3, 6]]
    column = 2
    # expected = [1, 0, 3]
    print(solution(matrix, column))


if __name__ == "__main__":
    main()
