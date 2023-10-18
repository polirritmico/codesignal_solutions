#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
In the Land Of Chess, bishops don't really like each other. In fact, when two
bishops happen to stand on the same diagonal, they immediately rush towards the
opposite ends of that same diagonal.

Given the initial positions (in chess notation) of two bishops, bishop1 and
bishop2, calculate their future positions. Keep in mind that bishops won't move
unless they see each other along the same diagonal.

Example

For bishop1 = "d7" and bishop2 = "f5", the output should be
solution(bishop1, bishop2) = ["c8", "h3"].

https://codesignal.s3.amazonaws.com/uploads/1664394254/ex_1.jpg?raw=true

For bishop1 = "d8" and bishop2 = "b5", the output should be
solution(bishop1, bishop2) = ["b5", "d8"].

https://codesignal.s3.amazonaws.com/uploads/1664394254/ex_2.jpg?raw=true

The bishops don't belong to the same diagonal, so they don't move.


"""


def solution(bishop1: str, bishop2: str) -> list[str]:
    borders = "ah18"
    if abs(ord(bishop1[0]) - ord(bishop2[0])) != abs(int(bishop1[1]) - int(bishop2[1])):
        return sorted([bishop1, bishop2])

    bishop1_horizontal_move = -1 if bishop1[0] < bishop2[0] else 1
    bishop2_horizontal_move = 1 if bishop1[0] < bishop2[0] else -1
    bishop1_vertical_move = -1 if bishop1[1] < bishop2[1] else 1
    bishop2_vertical_move = 1 if bishop1[1] < bishop2[1] else -1

    while bishop1[0] not in borders and bishop1[1] not in borders:
        col = ord(bishop1[0]) + bishop1_horizontal_move
        row = ord(bishop1[1]) + bishop1_vertical_move
        bishop1 = chr(col) + chr(row)
    while bishop2[0] not in borders and bishop2[1] not in borders:
        col = ord(bishop2[0]) + bishop2_horizontal_move
        row = ord(bishop2[1]) + bishop2_vertical_move
        bishop2 = chr(col) + chr(row)
    return sorted([bishop1, bishop2])


def main():
    bishop1 = "d7"
    bishop2 = "f5"
    # expected = ["c8", "h3"]
    # bishop1 = "d8"
    # bishop2 = "b5"
    # expected = ["b5", "d8"]
    print(solution(bishop1, bishop2))


if __name__ == "__main__":
    main()
