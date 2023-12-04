#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
John has always had trouble remembering chess game positions. To help himself
with remembering, he decided to store game positions in strings. He came up with
the following position notation:

- The notation is built for the current game position row by row from top to
  bottom, with '/' separating each row notation;
- Within each row, the contents of each square are described from the leftmost
  column to the rightmost;
- Each piece is identified by a single letter taken from the standard English
  names ('P' = pawn, 'N' = knight, 'B' = bishop, 'R' = rook, 'Q' = queen,
  'K' = king);
- White pieces are designated using upper-case letters ("PNBRQK") while black
  pieces use lowercase ("pnbrqk");
- Empty squares are noted using digits 1 through 8 (the number of empty squares
  from the last piece);
- Empty lines are noted as "8".

For example, for the initial position (shown in the picture below) the notation
will look like this:

    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

https://codesignal.s3.amazonaws.com/uploads/1664394256/initial.jpg?raw=true

After the white pawn moves from e2 to e4, the notation will be as follows:

    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"

https://codesignal.s3.amazonaws.com/uploads/1664394256/example.jpg?raw=true

John has written down some positions using his notation, and now he wants to
rotate the board 90 degrees clockwise and see what notation for the new board
would look like. Help him with this task.

Example

For notation = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR", the output
should be solution(notation) =
"RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr".

The notation corresponds to the initial position with one move made (white pawn
from e2 to e4). After rotating the board, it will look like this:

    So, the notation of the new position is
    "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr".

"""


def solution(notation: str) -> str:
    for num in range(1, 9):
        notation = notation.replace(str(num), "_" * num)
    original_board_rows = notation.split("/")
    rotated_board = list(zip(*original_board_rows[::-1]))

    rotated_board_string_rows = list("".join(row) for row in rotated_board)
    rotated_board_notation = "/".join(rotated_board_string_rows)
    for num in range(8, 0, -1):
        rotated_board_notation = rotated_board_notation.replace("_" * num, str(num))

    return rotated_board_notation


def main():
    case = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"
    # expected = "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr"
    print(solution(case))


if __name__ == "__main__":
    main()
