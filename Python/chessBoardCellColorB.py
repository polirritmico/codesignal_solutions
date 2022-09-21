#!/usr/bin/env python
# -*- coding: utf-8 -*-

def color_in_chessboard(cell):
    # True → White; Black → False
    # A → 65; 1 → 49; || A, 1 → odd
    letter = ord(cell[0])
    number = ord(cell[1])
    if letter % 2 == 0 and number % 2 == 0:
        return False
    elif letter % 2 == 1 and number % 2 == 1:
        return False
    return True


def solution(cell1, cell2):
    return color_in_chessboard(cell1) == color_in_chessboard(cell2)


def main():
    cell1 = "C3"
    cell2 = "B5"
    print(solution(cell1, cell2))

if __name__ == "__main__":
    main()

