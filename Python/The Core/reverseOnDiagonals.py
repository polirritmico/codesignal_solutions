#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The longest diagonals of a square matrix are defined as follows:

    - the first longest diagonal goes from the top left corner to the bottom
    right one;
    - the second longest diagonal goes from the top right corner to the
    bottom left one.

Given a square matrix, your task is to reverse the order of elements on both of
its longest diagonals.

Example

For

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

the output should be

solution(matrix) = [[9, 2, 7],
                    [4, 5, 6],
                    [3, 8, 1]]

"""


def solution(matrix: list[int]) -> list[int]:
    output = [row.copy() for row in matrix]
    for coord in range(len(matrix)):
        output[coord][coord] = matrix[-1 - coord][-1 - coord]
        output[coord][-1 - coord] = matrix[-1 - coord][coord]
    return output


def main():
    case = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # expected = [[9, 2, 7], [4, 5, 6], [3, 8, 1]]
    print(solution(case))


if __name__ == "__main__":
    main()
