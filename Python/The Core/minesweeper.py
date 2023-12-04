#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
In the popular Minesweeper game you have a board with some mines and those cells
that don't contain a mine have a number in it that indicates the total number of
mines in the neighboring cells. Starting off with some arrangement of mines we
want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]

the output should be

solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]

"""


def sum_inner_frame(center_coords: tuple[int], matrix: list[list[bool]]) -> int:
    center_element = 1 if matrix[center_coords[0]][center_coords[1]] else 0
    surrounding_sum = 0

    first_row = 0 if center_coords[0] <= 1 else center_coords[0] - 1
    first_col = 0 if center_coords[1] <= 1 else center_coords[1] - 1
    row_length = len(matrix)
    col_length = len(matrix[0])
    last_row_adjust = 1 if center_coords[0] + 1 == row_length else 2
    last_col_adjust = 1 if center_coords[1] + 1 == col_length else 2
    last_row = center_coords[0] + last_row_adjust
    last_col = center_coords[1] + last_col_adjust
    for row in range(first_row, last_row):
        for col in range(first_col, last_col):
            surrounding_sum += 1 if matrix[row][col] else 0

    if surrounding_sum > 0:
        surrounding_sum -= center_element
    return surrounding_sum


def solution(matrix: list[list[bool]]) -> list[list[int]]:
    output = []
    last_row = len(matrix)
    last_col = len(matrix[0])
    for row in range(last_row):
        new_row = []
        for col in range(last_col):
            current_coord = (row, col)
            surrounding_sum = sum_inner_frame(current_coord, matrix)
            new_row.append(surrounding_sum)
        output.append(new_row)
    return output


def main():
    case = 0
    print(solution(case))


if __name__ == "__main__":
    main()
