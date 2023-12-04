#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Consider a bishop, a knight and a rook on an n × m chessboard. They are said to
form a triangle if each piece attacks exactly one other piece and is attacked by
exactly one piece. Calculate the number of ways to choose positions of the
pieces to form a triangle.

Note that the bishop attacks pieces sharing the common diagonal with it; the
rook attacks in horizontal and vertical directions; and, finally, the knight
attacks squares which are two squares horizontally and one square vertically, or
two squares vertically and one square horizontally away from its position.

https://codesignal.s3.amazonaws.com/uploads/1664318501/moves.png?raw=true

Example

For n = 2 and m = 3, the output should be
solution(n, m) = 8.

https://codesignal.s3.amazonaws.com/uploads/1664318502/combinations.png?raw=true

"""


def solution(rows: int, cols: int) -> int:
    """
    In 2x3 are 4 positions
    In 2x4 are 4 positions
    In 3x3 are 4 positions
    In 3x4 are 4 positions
    With reflections all * 2
    So, positions * 8
    """
    positions = 0

    if rows > 1 and cols > 2:
        positions += (rows - 1) * (cols - 2)
    if cols > 1 and rows > 2:
        positions += (cols - 1) * (rows - 2)

    if rows > 2 and cols > 2:
        positions += (rows - 2) * (cols - 2)
    if cols > 2 and rows > 2:
        positions += (cols - 2) * (rows - 2)

    if rows > 1 and cols > 3:
        positions += (rows - 1) * (cols - 3)
    if cols > 1 and rows > 3:
        positions += (cols - 1) * (rows - 3)

    if rows > 2 and cols > 3:
        positions += (rows - 2) * (cols - 3)
    if cols > 2 and rows > 3:
        positions += (cols - 2) * (rows - 3)

    return positions * 8


def main():
    rows = 3
    cols = 3
    print(solution(rows, cols))


if __name__ == "__main__":
    main()
