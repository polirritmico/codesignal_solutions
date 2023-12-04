#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a position of a knight on the standard chessboard, find the number of
different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square
vertically, or two squares vertically and one square horizontally away from it.
The complete move therefore looks like the letter L. Check out the image below
to see all valid moves for a knight piece that is placed on one of the central
squares.

https://codesignal.s3.amazonaws.com/uploads/1664394252/knight.jpg?raw=true

Example

    For cell = "a1", the output should be
    solution(cell) = 2.

    https://codesignal.s3.amazonaws.com/uploads/1664394253/ex_1.jpg?raw=true

    For cell = "c2", the output should be
    solution(cell) = 6.

    https://codesignal.s3.amazonaws.com/uploads/1664394253/ex_2.jpg?raw=true

"""


def solution(cell: str) -> int:
    border_coords = "ah18"
    inner_border_coords = "bg27"
    positions_tier = 0
    if cell[0] not in border_coords:
        positions_tier += 2 if cell[0] not in inner_border_coords else 1
    if cell[1] not in border_coords:
        positions_tier += 2 if cell[1] not in inner_border_coords else 1
    possible_movements = (2, 3, 4, 6, 8)
    return possible_movements[positions_tier]


def main():
    case = "a1"
    # expected = 2
    print(solution(case))


if __name__ == "__main__":
    main()
