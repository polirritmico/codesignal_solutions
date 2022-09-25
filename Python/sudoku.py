#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(grid):
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
    case = [[1,3,4,2,5,6,9,8,7], 
            [4,6,8,5,7,9,3,2,1], 
            [7,9,2,8,1,3,6,5,4], 
            [9,2,3,1,4,5,8,7,6], 
            [3,5,7,4,6,8,2,1,9], 
            [6,8,1,7,9,2,5,4,3], 
            [5,7,6,9,8,1,4,3,2], 
            [2,4,5,6,3,7,1,9,8], 
            [8,1,9,3,2,4,7,6,5]]
    print(solution(case))

if __name__ == "__main__":
    main()

