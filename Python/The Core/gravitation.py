#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given a vertical box divided into equal columns. Someone dropped several
stones from its top through the columns. Stones are falling straight down at a
constant speed (equal for all stones) while possible (i.e. while they haven't
reached the ground or they are not blocked by another motionless stone). Given
the state of the box at some moment in time, find out which columns become
motionless first.

Example

For

rows = ["#..##",
        ".##.#",
        ".#.##",
        "....."]

the output should be solution(rows) = [1, 4].

Check out the image below for better understanding:

https://codesignal.s3.amazonaws.com/uploads/1667239865430/example.png?raw=true

"""


def solution(matrix: list[str]) -> list[int]:
    height = len(matrix)
    width = len(matrix[0])
    fall_times = []
    for col in range(width):
        stones = 0
        air = 0
        stones_in_col = sum([1 if row[col] == "#" else 0 for row in matrix])
        if stones_in_col == 0:
            fall_times.append(0)
            continue
        for row in range(height - 1, -1, -1):
            current = matrix[row][col]
            if current == "#":
                stones += 1
            else:
                air += 1
            if stones == stones_in_col:
                fall_times.append(air)
                break
    min_time = min(fall_times)
    output = []
    for col, time in enumerate(fall_times):
        if time == min_time:
            output.append(col)
    return output


def main():
    case = ["#..#.", ".##..", ".#...", ".#..."]
    # expected = [1, 4]
    print(solution(case))


if __name__ == "__main__":
    main()
