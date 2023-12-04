#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pawn race is a game for two people, played on an ordinary 8 × 8 chessboard. The
first player has a white pawn, the second one - a black pawn. Initially the
pawns are placed somewhere on the board so that the 1st and the 8th rows are not
occupied. Players take turns to make a move.

White pawn moves upwards, black one moves downwards. The following moves are
allowed:

    - one-cell move on the same vertical in the allowed direction;
    - two-cell move on the same vertical in the allowed direction, if the pawn
    is standing on the 2nd (for the white pawn) or the 7th (for the black pawn)
    row. Note that even with the two-cell move a pawn can't jump over the
    opponent's pawn;
    - capture move one cell forward in the allowed direction and one cell to the
    left or to the right.

https://codesignal.s3.amazonaws.com/uploads/1664318502/move_types.png?raw=true

The purpose of the game is to reach the the 1st row (for the black pawn) or the
8th row (for the white one), or to capture the opponent's pawn.

Given the initial positions and whose turn it is, determine who will win or
declare it a draw (i.e. it is impossible for any player to win). Assume that the
players play optimally.

Example

    For white = "e2", black = "e7", and toMove = 'w', the output should be
    solution(white, black, toMove) = "draw";
    For white = "e3", black = "d7", and toMove = 'b', the output should be
    solution(white, black, toMove) = "black";
    For white = "a7", black = "h2", and toMove = 'w', the output should be
    solution(white, black, toMove) = "white".

"""


def solution(white: str, black: str, to_move: str) -> str:
    white_col = ord(white[0]) - 97
    white_row = int(white[1])
    black_col = ord(black[0]) - 97
    black_row = int(black[1])

    vertical_distance = black_row - white_row
    if white_col == black_col and vertical_distance > 0:
        return "draw"

    white_first = to_move == "w"
    is_a_race = abs(black_col - white_col) != 1
    past_capture_chance = vertical_distance < 1
    if is_a_race or past_capture_chance:
        white_to_win = (8 - white_row) if white_row != 2 else (7 - white_row)
        black_to_win = (black_row - 1) if black_row != 7 else (black_row - 2)

        if white_to_win == black_to_win:
            return "white" if white_first else "black"
        return "white" if white_to_win < black_to_win else "black"

    if vertical_distance == 1:
        return "white" if white_first else "black"

    if black_row == 7 and white_row == 2:
        return "black" if white_first else "white"
    if white_row == 2:
        if white_first:
            return "black" if black_row == 4 or black_row < 3 else "white"
        else:
            return "white" if black_row == 6 or black_row == 4 else "black"
    if black_row == 7:
        if white_first:
            return "black" if white_row == 3 or white_row == 5 else "white"
        else:
            return "white" if white_row == 5 or white_row > 6 else "black"

    if vertical_distance % 2:
        return "white" if white_first else "black"
    else:
        return "black" if white_first else "white"


def main():
    white = "h3"
    black = "g6"
    to_move = "b"
    # expected = "black"
    print(solution(white, black, to_move))


if __name__ == "__main__":
    main()
