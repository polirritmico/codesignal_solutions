#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
An amazon (also known as a queen + knight compound) is an imaginary chess piece
that can move like a queen or a knight (or, equivalently, like a rook, bishop,
or knight). The diagram below shows all squares which the amazon can attack from
e4 (circles represent knight-like moves while crosses correspond to queen-like
moves).

https://codesignal.s3.amazonaws.com/uploads/1664318503/amazon.png?raw=true

Recently, you've come across a diagram with only three pieces left on the board:
a white amazon, the white king, and the black king. It's black's move. You don't
have time to determine whether the game is over or not, but you'd like to figure
it out in your head. Unfortunately, the diagram is smudged and you can't see the
position of the black king, so you'll need to consider all possible positions.

Given the positions of the white pieces on a standard chessboard (using
algebraic notation), your task is to determine the number of possible black
king's positions such that:

    - it's checkmate (i.e. black's king is under the amazon's attack and it
      cannot make a valid move);
    - it's check (i.e. black's king is under the amazon's attack but it can
      reach a safe square in one move);
    - it's stalemate (i.e. black's king is on a safe square but it cannot make a
      valid move);
    - black's king is on a safe square and it can make a valid move.

Note that two kings cannot be placed on two adjacent squares (including two
diagonally adjacent ones).

Example

For king = "d3" and amazon = "e4", the output should be
solution(king, amazon) = [5, 21, 0, 29].

https://codesignal.s3.amazonaws.com/uploads/1664318503/example1.png?raw=true

Red crosses correspond to the checkmate positions, orange pluses refer to check
positions, and green circles denote safe squares.

For king = "a1" and amazon = "g5", the output should be
solution(king, amazon) = [0, 29, 1, 29].

https://codesignal.s3.amazonaws.com/uploads/1664318503/example2.png?raw=true

The stalemate position is marked by a blue square.

Output

array.integer

An array of four integers, each equal to the number of black's king positions
corresponding to a specific situation. More specifically, the array should be of
the form [checkmate positions, check positions, stalemate positions, safe
positions].

"""


def fill_amazon_diagonals(
    amazon_col: int, amazon_row: int, board: list[list[str]]
) -> list[list[str]]:
    for row, col in zip(range(amazon_row - 1, -1, -1), range(amazon_col - 1, -1, -1)):
        if board[row][col] == "K":
            break
        if board[row][col] == "*":
            board[row][col] = "a"
    for row, col in zip(range(amazon_row - 1, -1, -1), range(amazon_col + 1, 8)):
        if board[row][col] == "K":
            break
        if board[row][col] == "*":
            board[row][col] = "a"
    for row, col in zip(range(amazon_row + 1, 8), range(amazon_col - 1, -1, -1)):
        if board[row][col] == "K":
            break
        if board[row][col] == "*":
            board[row][col] = "a"
    for row, col in zip(range(amazon_row + 1, 8), range(amazon_col + 1, 8)):
        if board[row][col] == "K":
            break
        if board[row][col] == "*":
            board[row][col] = "a"
    return board


def fill_amazon_vertical_and_horizontal(
    amazon_col: int, amazon_row: int, board: list[list[str]]
) -> list[list[str]]:
    for col in range(amazon_col - 1, -1, -1):
        if board[amazon_row][col] == "K":
            break
        if board[amazon_row][col] == "*":
            board[amazon_row][col] = "a"
    for col in range(amazon_col + 1, 8):
        if board[amazon_row][col] == "K":
            break
        if board[amazon_row][col] == "*":
            board[amazon_row][col] = "a"
    for row in range(amazon_row - 1, -1, -1):
        if board[row][amazon_col] == "K":
            break
        if board[row][amazon_col] == "*":
            board[row][amazon_col] = "a"
    for row in range(amazon_row + 1, 8):
        if board[row][amazon_col] == "K":
            break
        if board[row][amazon_col] == "*":
            board[row][amazon_col] = "a"
    return board


def fill_amazon_surrounding(
    amazon_col: int, amazon_row: int, board: list[list[str]]
) -> list[list[str]]:
    for row in range(amazon_row - 2, amazon_row + 3, 1):
        for col in range(amazon_col - 2, amazon_col + 3, 1):
            if col >= 0 and col < 8 and row >= 0 and row < 8 and board[row][col] == "*":
                board[row][col] = "a"
    return board


def fill_amazon_area_in_board(
    amazon_col: int, amazon_row: int, board: list[list[str]]
) -> list[list[str]]:
    board[amazon_row][amazon_col] = "A"
    board = fill_amazon_vertical_and_horizontal(amazon_col, amazon_row, board)
    board = fill_amazon_diagonals(amazon_col, amazon_row, board)
    board = fill_amazon_surrounding(amazon_col, amazon_row, board)
    return board


def fill_king_area_in_board(
    king_col: int, king_row: int, board: list[list[str]]
) -> list[list[str]]:
    for row in range(king_row - 1, king_row + 2, 1):
        for col in range(king_col - 1, king_col + 2, 1):
            if row >= 0 and row < 8 and col >= 0 and col < 8:
                board[row][col] = "k"
    board[king_row][king_col] = "K"
    return board


def fill_board(
    king_col: int, king_row: int, amazon_col: int, amazon_row: int
) -> list[list[str]]:
    board = [["*" for _ in range(8)] for _ in range(8)]
    board = fill_king_area_in_board(king_col, king_row, board)
    board = fill_amazon_area_in_board(amazon_col, amazon_row, board)
    return board


def get_surroundings(
    center_row: int, center_col: int, board: list[list[str]]
) -> list[str]:
    v_start = center_row - 1 if center_row > 0 else 0
    v_stop = center_row + 2 if center_row < 7 else 8
    h_start = center_col - 1 if center_col > 0 else 0
    h_stop = center_col + 2 if center_col < 7 else 8
    sub_board = [row[h_start:h_stop] for row in board[v_start:v_stop]]
    output = [square for row in sub_board for square in row]
    output.remove(board[center_row][center_col])
    return output


def count_checkmates(board: list[list[str]], protected_amazon: bool) -> int:
    checkmates = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] != "a":
                continue
            surroundings = get_surroundings(row, col, board)
            escape_squares = surroundings.count("*")
            capture_amazon = surroundings.count("A") if not protected_amazon else 0
            if escape_squares + capture_amazon == 0:
                checkmates += 1
    return checkmates


def count_stalemates(board: list[list[str]], protected_amazon) -> int:
    stalemates = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == "*":
                surroundings = get_surroundings(row, col, board)
                if surroundings.count("*") == 0:
                    stalemates += 1
    return stalemates


def solution(king: str, amazon: str) -> list[int]:
    amazon_col = ord(amazon[0]) - 97
    amazon_row = int(amazon[1]) - 1
    king_col = ord(king[0]) - 97
    king_row = int(king[1]) - 1
    board = fill_board(king_col, king_row, amazon_col, amazon_row)
    protected_amazon = abs(amazon_col - king_col) < 2 and abs(amazon_row - king_row) < 2

    checkmates = count_checkmates(board, protected_amazon)
    checks = sum(row.count("a") for row in board) - checkmates
    stalemates = count_stalemates(board, protected_amazon)
    safe_squares = sum(row.count("*") for row in board) - stalemates

    return [checkmates, checks, stalemates, safe_squares]


def main():
    king = "f3"
    amazon = "f2"
    # expected = [6, 11, 0, 38]
    print(solution(king, amazon))


if __name__ == "__main__":
    main()
