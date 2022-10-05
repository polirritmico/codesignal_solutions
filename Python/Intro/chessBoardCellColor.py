#!/usr/bin/env python
# -*- coding: utf-8 -*-

def color_in_chessboard(cell):
    # True → White; Black → False
    letter = cell[0]
    number = cell[1]
    if letter in "ACEG":
        if number in "1357":
            return False
    elif number in "2468":
        return False
    return True


def solution(cell1, cell2):
    if color_in_chessboard(cell1) == color_in_chessboard(cell2):
        return True
    return False


def main():
    cell1 = "C3"
    cell2 = "B5"
    print(solution(cell1, cell2))

if __name__ == "__main__":
    main()

