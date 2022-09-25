#!/usr/bin/env python
# -*- coding: utf-8 -*-

def clockwise_direction_generator():
    while True:
        yield "→"
        yield "↓"
        yield "←"
        yield "↑"


def next_coord(current_position, direction):
    if direction == "→":
        vector = (0, 1)
    elif direction == "↓":
        vector = (1, 0)
    elif direction == "←":
        vector = (0, -1)
    elif direction == "↑":
        vector = (-1, 0)
    return (current_position[0] + vector[0], current_position[1] + vector[1])


def check_valid_coord(check_position, matrix, size):
    row = check_position[0]
    col = check_position[1]
    if row < 0 or row >= size or col < 0 or col >= size:
        return False
    if matrix[row][col] != 0:
        return False
    return True


def solution(size):
    matrix = [[0 for row_element in range(size)] for rows in range(size)]
    direction = clockwise_direction_generator()
    current_direction = next(direction)
    current_position = (0, 0)
    for step in range(1, (size ** 2) + 1):
        matrix[current_position[0]][current_position[1]] = step
        next_position = next_coord(current_position, current_direction)
        if not check_valid_coord(next_position, matrix, size):
            current_direction = next(direction)
            next_position = next_coord(current_position, current_direction)
        current_position = next_position
    return matrix


def main():
    case = 3
    #expected = [[1,2,3],
    #            [8,9,4],
    #            [7,6,5]]
    print(solution(case))

if __name__ == "__main__":
    main()

