#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.
Example
matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

the output should be solution(matrix) = 6.
Here are all 6 different 2 × 2 squares:

    1 2
    2 2
    2 1
    2 2
    2 2
    2 2
    2 2
    1 2
    2 2
    2 3
    2 3
    2 1
"""


def solution(matrix: list[list[int]]):
    matrix_x_len = len(matrix[0])
    matrix_y_len = len(matrix)
    if matrix_y_len < 2 or matrix_x_len < 2:
        return 0
    unique_squares = []
    for x in range(matrix_x_len - 1):
        for y in range(matrix_y_len - 1):
            current_square = (
                f"{matrix[y][x]} {matrix[y][x+1]} {matrix[y+1][x]} {matrix[y+1][x+1]}"
            )
            if current_square not in unique_squares:
                unique_squares.append(current_square)
    return len(unique_squares)


def main():
    # matrix = [[1, 2, 1], [2, 2, 2], [2, 2, 2], [1, 2, 3], [2, 2, 1]]
    matrix = [
        [1, 2, 1],
        [2, 2, 2],
        [2, 2, 2],
        [1, 2, 3],
        [2, 2, 1],
    ]
    print(solution(matrix))


if __name__ == "__main__":
    main()
