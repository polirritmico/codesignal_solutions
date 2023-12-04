#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with
digits so that each column, each row, and each of the nine 3 × 3 sub-grids that
compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct
solution to Sudoku.

Example

    For

grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]

the output should be
solution(grid) = true;

    For

grid = [[8, 3, 6, 5, 3, 6, 7, 2, 9],
        [4, 2, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 1, 2, 1, 4, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]

the output should be
solution(grid) = false.

The output should be false: each of the nine 3 × 3 sub-grids should contain all
of the digits from 1 to 9. These examples are represented on the image below.

https://codesignal.s3.amazonaws.com/uploads/1667239894092/example.png?raw=true

"""


def solution(grid: list[list[int]]) -> bool:
    for row in grid:
        row_numbers = []
        for number in row:
            if number in row_numbers:
                return False
            row_numbers.append(number)

            size = len(grid)

    for col in range(size):
        col_numbers = []
        for row in grid:
            number = row[col]
            if number in col_numbers:
                return False
            col_numbers.append(number)

    for row_offset in range(0, 7, 3):
        for col_offset in range(0, 7, 3):
            numbers_square_3x3 = []
            for row in range(3):
                row += row_offset
                for col in range(3):
                    col += col_offset
                    number = grid[row][col]
                    if number in numbers_square_3x3:
                        return False
                    numbers_square_3x3.append(number)
    return True


def main():
    case = [
        [1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 4, 6, 9, 8, 1, 4, 3, 2],
        [2, 7, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5],
    ]
    print(solution(case))


if __name__ == "__main__":
    main()
