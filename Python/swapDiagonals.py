#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The longest diagonals of a square matrix are defined as follows:

    - the first longest diagonal goes from the top left corner to the bottom right
    one;
    - the second longest diagonal goes from the top right corner to the bottom
    left one.

Given a square matrix, your task is to swap its longest diagonals by exchanging
their elements at the corresponding positions.

Example

For

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

the output should be

solution(matrix) = [[3, 2, 1],
                    [4, 5, 6],
                    [9, 8, 7]]

"""


def solution(matrix: list[int]) -> list[int]:
    output = [row.copy() for row in matrix]
    for coord in range(len(matrix)):
        # left top to btm right -> right top to btm left:
        output[coord][coord] = matrix[coord][-1 - coord]
        # right top to btm left -> left top to btm right:
        output[coord][-1 - coord] = matrix[coord][coord]
    return output


def main():
    case = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # expected = [[3, 2, 1], [4, 5, 6], [9, 8, 7]]
    print(solution(case))


if __name__ == "__main__":
    main()
