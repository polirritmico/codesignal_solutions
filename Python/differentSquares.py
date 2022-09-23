#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(matrix):
    squares_2x2 = set()
    rows = len(matrix)
    cols = len(matrix[0])
    if rows < 2 or cols < 2:
        return 0

    for row in range(rows - 1):
        for col in range(cols - 1):
            square = (matrix[row][col], matrix[row][col+1],
                      matrix[row+1][col], matrix[row+1][col+1])
            squares_2x2.add(square)
    print(squares_2x2)
    return len(squares_2x2)


def main():
    case = [[1,2,1], 
            [2,2,2],
            [2,2,2]]
    # expected 3
    print(solution(case))

if __name__ == "__main__":
    main()

