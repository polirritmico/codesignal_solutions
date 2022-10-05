#!/usr/bin/env python
# -*- coding: utf-8 -*-

def valid_coord(row, col):
    if row > 7 or row < 0 or col > 7 or col < 0:
        return False
    return True


def solution(bishop_str_coord, pawn_str_coord):
    if bishop_str_coord == pawn_str_coord:
        raise Exception("ERROR: Both pieces in the same coord")
    bishop_row = ord(bishop_str_coord[0]) - ord('a')
    bishop_col = int(bishop_str_coord[1]) - 1
    pawn_row = ord(pawn_str_coord[0]) - ord('a')
    pawn_col = int(pawn_str_coord[1]) - 1
    up = 1
    down = -1
    left = -1
    right = 1

    current_row = bishop_row
    current_col = bishop_col
    # Up left
    while valid_coord(current_row, current_col):
        if current_row == pawn_row and current_col == pawn_col:
            return True
        current_row += up
        current_col += left

    current_row = bishop_row
    current_col = bishop_col
    # Up right
    while valid_coord(current_row, current_col):
        if current_row == pawn_row and current_col == pawn_col:
            return True
        current_row += up
        current_col += right

    current_row = bishop_row
    current_col = bishop_col
    # Down left
    while valid_coord(current_row, current_col):
        if current_row == pawn_row and current_col == pawn_col:
            return True
        current_row += down
        current_col += left

    current_row = bishop_row
    current_col = bishop_col
    # Down right
    while valid_coord(current_row, current_col):
        if current_row == pawn_row and current_col == pawn_col:
            return True
        current_row += down
        current_col += right

    return False


def main():
    bishop = "e7"
    pawn = "d6"
    print(solution(bishop, pawn))

if __name__ == "__main__":
    main()

