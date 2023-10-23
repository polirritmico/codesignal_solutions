#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Chess Bishop Dream

In ChessLand there is a small but proud chess bishop with a recurring dream. In
the dream the bishop finds itself on an n × m chessboard with mirrors along each
edge, and it is not a bishop but a ray of light. This ray of light moves only
along diagonals (the bishop can't imagine any other types of moves even in its
dreams), it never stops, and once it reaches an edge or a corner of the
chessboard it reflects from it and moves on.

Given the initial position and the direction of the ray, find its position after
k steps where a step means either moving from one cell to the neighboring one or
reflecting from a corner of the board.

Example

For boardSize = [3, 7], initPosition = [1, 2],
initDirection = [-1, 1], and k = 13, the output should be
solution(boardSize, initPosition, initDirection, k) = [0, 1].

Here is the bishop's path:

[1, 2] -> [0, 3] -(reflection from the top edge)-> [0, 4] ->
[1, 5] -> [2, 6] -(reflection from the bottom right corner)-> [2, 6] ->
[1, 5] -> [0, 4] -(reflection from the top edge)-> [0, 3] ->
[1, 2] -> [2, 1] -(reflection from the bottom edge)-> [2, 0] -(reflection from the left edge)->
[1, 0] -> [0, 1]

https://codesignal.s3.amazonaws.com/uploads/1664318502/example.png?raw=true
"""

from typing import Optional


def solution(
    board_size: list[int], init_pos: list[int], init_dir: list[int], steps: int
) -> list[int]:
    current_pos = init_pos
    current_dir = init_dir
    at_init_position_counter = 0
    full_diagonal_path = []
    while at_init_position_counter != 2:
        full_diagonal_path.append(current_pos)
        next_pos = [current_pos[0] + current_dir[0], current_pos[1] + current_dir[1]]
        direction_changes = 0
        if next_pos[0] < 0 or next_pos[0] >= board_size[0]:
            direction_changes += 1
            current_dir[0] *= -1
            next_pos[0] = current_pos[0]
        if next_pos[1] < 0 or next_pos[1] >= board_size[1]:
            direction_changes += 1
            current_dir[1] *= -1
            next_pos[1] = current_pos[1]

        if direction_changes != 2:
            current_pos = next_pos
        if current_pos == init_pos:
            at_init_position_counter += 1

    total_steps_in_full_path = len(full_diagonal_path)
    final_position = steps % total_steps_in_full_path
    return full_diagonal_path[final_position]


def main():
    board_size = [3, 7]
    init_position = [1, 2]
    init_direction = [-1, 1]
    k = 13
    # expected = [0, 1]
    print(solution(board_size, init_position, init_direction, k))


if __name__ == "__main__":
    main()
