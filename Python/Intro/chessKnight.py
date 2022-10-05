#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_valid(row, col):
    if row > 7 or row < 0 or col > 7 or col < 0:
        return False
    return True

def solution(knight_coords):
    # Movements: row, col
    left_up = (1, -2)
    up_left = (2, -1)
    up_right = (2, 1)
    right_up = (1, 2)
    right_down = (-1, 2)
    down_right = (-2, 1)
    down_left = (-2, -1)
    left_down = (-1, -2)
    movements = [left_up, left_down, right_up, right_down,
                 up_left, up_right, down_left, down_right]

    knight_row = ord(knight_coords[0]) - ord('a')
    knight_col = int(knight_coords[1]) - 1
    valid_moves = 0
    for move in movements:
        target_row = knight_row + move[0]
        target_col = knight_col + move[1]
        if is_valid(target_row, target_col):
            valid_moves += 1
    return valid_moves


def main():
    case = "h6" #4
    print(solution(case))

if __name__ == "__main__":
    main()

