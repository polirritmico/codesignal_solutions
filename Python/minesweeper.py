#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum_inner_frame(center_coords, matrix) -> int:
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


def solution(matrix):
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
    matrix = [[True,False,False,True],
              [False,False,True,False],
              [True,True,False,True]]
    #expected = [[0,2,2,1],
    #            [3,4,3,3],
    #            [1,2,3,1]]
    print(solution(matrix))

if __name__ == "__main__":
    main()

