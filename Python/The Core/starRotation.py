#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Star Rotation

Consider a (2k+1) × (2k+1) square subarray of an integer integers matrix. Let's
call the union of the square's two longest diagonals, middle column and middle
row a star. Given the coordinates of the star's center in the matrix and its
width, rotate it 45 · t degrees clockwise preserving position of all matrix
elements that do not belong to the star.

Example

    For

    matrix = [[1, 0, 0, 2, 0, 0, 3],
              [0, 1, 0, 2, 0, 3, 0],
              [0, 0, 1, 2, 3, 0, 0],
              [8, 8, 8, 9, 4, 4, 4],
              [0, 0, 7, 6, 5, 0, 0],
              [0, 7, 0, 6, 0, 5, 0],
              [7, 0, 0, 6, 0, 0, 5]]

    width = 7, center = [3, 3], and t = 1, the output should be

    solution(matrix, width, center, t) = [[8, 0, 0, 1, 0, 0, 2],
                                          [0, 8, 0, 1, 0, 2, 0],
                                          [0, 0, 8, 1, 2, 0, 0],
                                          [7, 7, 7, 9, 3, 3, 3],
                                          [0, 0, 6, 5, 4, 0, 0],
                                          [0, 6, 0, 5, 0, 4, 0],
                                          [6, 0, 0, 5, 0, 0, 4]]

    For

    matrix = [[1, 0, 0, 2, 0, 0, 3],
              [0, 1, 0, 2, 0, 3, 0],
              [0, 0, 1, 2, 3, 0, 0],
              [8, 8, 8, 9, 4, 4, 4],
              [0, 0, 7, 6, 5, 0, 0]]

    width = 3, center = [1, 5], and t = 81, the output should be

    solution(matrix, width, center, t) = [[1, 0, 0, 2, 0, 0, 0],
                                          [0, 1, 0, 2, 3, 3, 3],
                                          [0, 0, 1, 2, 0, 0, 0],
                                          [8, 8, 8, 9, 4, 4, 4],
                                          [0, 0, 7, 6, 5, 0, 0]]

"""


def solution(matrix: list, width: int, center: list[int], t: int) -> list:
    y_center = center[0]
    x_center = center[1]
    input_star = [[] for _ in range(8)]
    radius = (width - 1) // 2
    for step_in in range(radius):
        x_left = x_center - radius + step_in
        x_right = x_center + radius - step_in
        y_top = y_center - radius + step_in
        y_btm = y_center + radius - step_in
        input_star[0].append((y_center, x_left))
        input_star[1].append((y_top, x_left))
        input_star[2].append((y_top, x_center))
        input_star[3].append((y_top, x_right))
        input_star[4].append((y_center, x_right))
        input_star[5].append((y_btm, x_right))
        input_star[6].append((y_btm, x_center))
        input_star[7].append((y_btm, x_left))
    turns = t % 8
    output_star = [row for row in input_star[-turns:] + input_star[:-turns]]
    output_matrix = [row.copy() for row in matrix]
    for ray in range(8):
        for original, target in zip(input_star[ray], output_star[ray]):
            output_matrix[original[0]][original[1]] = matrix[target[0]][target[1]]
    return output_matrix


def main():
    matrix = [
        # 0  1  2  3  4  5  6
        [1, 0, 0, 2, 0, 0, 3],  # 0
        [0, 1, 0, 2, 0, 3, 0],  # 1
        [0, 0, 1, 2, 3, 0, 0],  # 2
        [8, 8, 8, 9, 4, 4, 4],  # 3
        [0, 0, 7, 6, 5, 0, 0],  # 4
    ]
    width = 3
    center = [1, 5]
    t = 81
    # expected = [
    #     [1, 0, 0, 2, 0, 0, 0],
    #     [0, 1, 0, 2, 3, 3, 3],
    #     [0, 0, 1, 2, 0, 0, 0],
    #     [8, 8, 8, 9, 4, 4, 4],
    #     [0, 0, 7, 6, 5, 0, 0],
    # ]

    # matrix = [
    #     ["tl1", "   ", "   ", "tm1", "   ", "   ", "tr1"],
    #     ["", "tl2", "   ", "tm2", "   ", "tr2", "   "],
    #     ["   ", "   ", "tl3", "tm3", "tr3", "   ", "   "],
    #     ["ml1", "ml2", "ml3", "mid", "mr3", "mr2", "mr1"],
    #     ["   ", "   ", "bl3", "bm3", "br3", "   ", "   "],
    #     ["   ", "bl2", "   ", "bm2", "   ", "br2", "   "],
    #     ["bl1", "   ", "   ", "bm1", "   ", "   ", "br1"],
    # ]
    # width = 7
    # center = [3, 3]
    # t = 1
    for line in solution(matrix, width, center, t):
        print(line)


if __name__ == "__main__":
    main()
