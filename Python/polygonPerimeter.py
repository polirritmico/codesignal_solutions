#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You have a rectangular white board with some black cells. The black cells create
a connected black figure, i.e. it is possible to get from any black cell to any
other one through connected adjacent (sharing a common side) black cells.

Find the perimeter of the black figure assuming that a single cell has unit
length.

It's guaranteed that there is at least one black cell on the table.

Example

For
matrix = [[false, true,  true ],
          [true,  true,  false],
          [true,  false, false]]

the output should be
solution(matrix) = 12.

https://codesignal.s3.amazonaws.com/uploads/1664318505/example1.png?raw=true

For

matrix = [[true, true,  true],
          [true, false, true],
          [true, true,  true]]

the output should be
solution(matrix) = 16.

https://codesignal.s3.amazonaws.com/uploads/1664318506/example2.png?raw=true

"""


def solution(matrix: list[list[bool]]) -> int:
    height = len(matrix)
    width = len(matrix[0])
    perimeter = 0
    for y in range(height):
        for x in range(width):
            if not matrix[y][x]:
                continue
            borders = 4
            if y != 0 and matrix[y - 1][x]:
                borders -= 1
            if y != height - 1 and matrix[y + 1][x]:
                borders -= 1
            if x != 0 and matrix[y][x - 1]:
                borders -= 1
            if x != width - 1 and matrix[y][x + 1]:
                borders -= 1
            perimeter += borders
    return perimeter


def main():
    case = [[False, True, True], [True, True, False], [True, False, False]]
    # expected = 12
    print(solution(case))


if __name__ == "__main__":
    main()
