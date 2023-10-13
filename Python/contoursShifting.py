#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Contours Shifting

Mark got a rectangular array matrix for his birthday, and now he's thinking
about all the fun things he can do with it. He likes shifting a lot, so he
decides to shift all of its i-contours in a clockwise direction if i is even,
and counterclockwise if i is odd.

Here is how Mark defines i-contours:

    - the 0-contour of a rectangular array as the union of left and right
      columns as well as top and bottom rows;
    - consider the initial matrix without the 0-contour: its 0-contour is the
      1-contour of the initial matrix;
    - define 2-contour, 3-contour, etc. in the same manner by removing
      0-contours from the obtained arrays.

Implement a function that does exactly what Mark wants to do to his matrix.

Example

For

matrix = [[ 1,  2,  3,  4],
          [ 5,  6,  7,  8],
          [ 9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20]]

the output should be

solution(matrix) = [[ 5,  1,  2,  3],
                    [ 9,  7, 11,  4],
                    [13,  6, 15,  8],
                    [17, 10, 14, 12],
                    [18, 19, 20, 16]]

For matrix = [[238, 239, 240, 241, 242, 243, 244, 245]],
the output should be
solution(matrix) = [[245, 238, 239, 240, 241, 242, 243, 244]].

Note, that if a contour is represented by a 1 × n array, its center is
considered to be below it.

For

matrix = [[238], [239], [240], [241], [242], [243], [244], [245]]

the output should be

solution(matrix) = [[245], [238], [239], [240], [241], [242], [243], [244]]

If a contour is represented by an n × 1 array, its center is considered to be to
the left of it.

"""


def solution(matrix: list, contour_level: int = 0) -> list:
    clockwise = contour_level % 2 == 0
    height = len(matrix)
    if height == 1:
        if clockwise:
            return [matrix[0][-1:] + matrix[0][:-1]]
        else:
            return [matrix[0][1:] + matrix[0][:1]]
    width = len(matrix[0])
    if width == 1:
        if clockwise:
            return matrix[-1:] + matrix[:-1]
        else:
            return matrix[1:] + matrix[:1]

    # Rotate outer section
    contour_top = [num for num in matrix[0]]
    contour_btm = [num for num in matrix[-1]]
    contour_left = [row[0] for row in matrix]
    contour_right = [row[-1] for row in matrix]
    if clockwise:
        contour_top = [contour_left.pop(1)] + contour_top[:-1]
        contour_right = contour_right[:-1]
        contour_btm = contour_btm[1:] + [contour_right.pop(-1)]
        contour_left = contour_left[1:]
    else:
        contour_left = [contour_top.pop(0)] + contour_left[1:-1]
        contour_btm = [contour_left.pop(-1)] + contour_btm[:-1]
        contour_right = contour_right[1:]
        contour_top = contour_top + [contour_right.pop(0)]
    # (At this point left and right do not include their top and btm elements)
    for i, value in enumerate(contour_top):
        matrix[0][i] = value
    for i, value in enumerate(contour_btm):
        matrix[-1][i] = value
    for i, value in enumerate(contour_left):
        matrix[i + 1][0] = value
    for i, value in enumerate(contour_right):
        matrix[i + 1][-1] = value

    # Recursive call inner matrix and join it with the current one
    if width > 2 and height > 2:
        inner_matrix = []
        for row in matrix[1:-1]:
            inner_row = []
            for col in row[1:-1]:
                inner_row.append(col)
            inner_matrix.append(inner_row)
        if len(inner_matrix) != 0:
            rotated_inner = solution(inner_matrix, contour_level + 1)
            for y in range(height - 2):
                for x in range(width - 2):
                    matrix[y + 1][x + 1] = rotated_inner[y][x]
    return matrix


def main():
    # case = [
    #     [1, 2, 3, 4, 5],
    #     [6, 7, 8, 9, 10],
    #     [11, 12, 13, 14, 15],
    #     [16, 17, 18, 19, 20],
    # ]
    # expected = [
    #     [6, 1, 2, 3, 4],
    #     [11, 8, 9, 14, 5],
    #     [16, 7, 12, 13, 10],
    #     [17, 18, 19, 20, 15],
    # ]
    case = [[1, 4], [3, 5], [55, 55], [23, 56]]
    # expected = [[3, 1], [55, 4], [23, 5], [56, 55]]
    for line in solution(case):
        print(line)


if __name__ == "__main__":
    main()
