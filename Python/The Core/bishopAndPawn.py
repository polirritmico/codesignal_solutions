#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given the positions of a white bishop and a black pawn on the standard chess
board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to
diagonal movement. Check out the example below to see how it can move:

https://codesignal.s3.amazonaws.com/uploads/1664394254/bishop.jpg?raw=true

Example

For bishop = "a1" and pawn = "c3", the output should be
solution(bishop, pawn) = true.

https://codesignal.s3.amazonaws.com/uploads/1664394255/ex1.jpg?raw=true

For bishop = "h1" and pawn = "h3", the output should be
solution(bishop, pawn) = false.

https://codesignal.s3.amazonaws.com/uploads/1664394255/ex2.jpg?raw=true

"""


def solution(bishop: str, pawn: str) -> bool:
    bishop_col = ord(bishop[0])
    bishop_row = int(bishop[1])
    pawn_col = ord(pawn[0])
    pawn_row = int(pawn[1])
    return abs(bishop_col - pawn_col) == abs(bishop_row - pawn_row)


def main():
    bishop = "e3"
    pawn = "a7"
    # expected = True
    print(solution(bishop, pawn))


if __name__ == "__main__":
    main()
