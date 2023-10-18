#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imagine a standard chess board with only two white and two black knights placed
in their standard starting positions: the white knights on b1 and g1; the black
knights on b8 and g8.

https://codesignal.s3.amazonaws.com/uploads/1664318503/initial_pos.png?raw=true

There are two players: one plays for white, the other for black. During each
move, the player picks one of his knights and moves it to an unoccupied square
according to standard chess rules. Thus, a knight on d5 can move to any of the
following squares: b6, c7, e7, f6, f4, e3, c3, and b4, as long as it is not
occupied by either a friendly or an enemy knight.

https://codesignal.s3.amazonaws.com/uploads/1664394254/knight.jpg?raw=true

The players take turns in making moves, starting with the white player. Given
the configuration p of the knights after an unspecified number of moves,
determine whose turn it is.

Example

For p = "b1;g1;b8;g8", the output should be
solution(p) = true.

The configuration corresponds to the initial state of the game. Thus, it's
white's turn.

Input/Output

- [input] string p
    The positions of the four knights, starting with white knights, separated by a
    semicolon, in the chess notation.

    Guaranteed constraints:
    p.length = 11.

- [output] boolean
    true if white is to move, false otherwise

"""


def solution(positions: str) -> bool:
    distances = {
        "white_left": [
            [4, 5, 4, 5, 4, 5, 4, 5],
            [3, 4, 3, 4, 3, 4, 5, 4],
            [4, 3, 4, 3, 4, 3, 4, 5],
            [3, 2, 3, 2, 3, 4, 3, 4],
            [2, 3, 2, 3, 2, 3, 4, 3],
            [1, 2, 1, 4, 3, 2, 3, 4],
            [2, 3, 2, 1, 2, 3, 4, 3],
            [3, 0, 3, 2, 3, 2, 3, 4],
        ],
    }
    distances["white_right"] = list(row[::-1] for row in distances["white_left"])
    distances["black_left"] = list(distances["white_left"][::-1])
    distances["black_right"] = list(row[::-1] for row in distances["black_left"])

    white1 = (int(positions[1:2]) - 1, ord(positions[0:1][0]) - 97)
    white2 = (int(positions[4:5]) - 1, ord(positions[3:4][0]) - 97)
    black1 = (int(positions[7:8]) - 1, ord(positions[6:7][0]) - 97)
    black2 = (int(positions[10:11]) - 1, ord(positions[9:10][0]) - 97)

    white1_dist = distances["white_left"][white1[0]][white1[1]]
    white2_dist = distances["white_right"][white2[0]][white2[1]]
    black1_dist = distances["black_left"][black1[0]][black1[1]]
    black2_dist = distances["black_right"][black2[0]][black2[1]]

    total_moves = white1_dist + white2_dist + black1_dist + black2_dist
    return total_moves % 2 == 0


def main():
    case = "f8;h1;f3;c2"
    # expected = False
    print(solution(case))


if __name__ == "__main__":
    main()
