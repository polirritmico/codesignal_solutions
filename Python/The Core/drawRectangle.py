#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are implementing a command-line version of the Paint app. Since the command
line doesn't support colors, you are using different characters to represent
pixels. Your current goal is to support rectangle x1 y1 x2 y2 operation, which
draws a rectangle that has an upper left corner at (x1, y1) and a lower right
corner at (x2, y2). Here the x-axis points from left to right, and the y-axis
points from top to bottom.

Given the initial canvas state and the array that represents the coordinates of
the two corners, return the canvas state after the operation is applied. For the
details about how rectangles are painted, see the example.

Example

For

canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]

and rectangle = [1, 1, 4, 3], the output should be

solution(canvas, rectangle) = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                               ['a', '*', '-', '-', '*', 'a', 'a', 'a'],
                               ['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
                               ['b', '*', '-', '-', '*', 'b', 'b', 'b'],
                               ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]

Here is the rectangle, colored for illustration:


[['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
['a', '*', '-', '-', '*', 'a', 'a', 'a'],
['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
['b', '*', '-', '-', '*', 'b', 'b', 'b'],
['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]

Note that rectangle sides are depicted as -s and |s, asterisks (*) stand for its
corners and all of the other "pixels" remain the same.
"""


def solution(canvas: list[str], rectangle: list[int]) -> list[str]:
    top_left_y = rectangle[1]
    top_left_x = rectangle[0]
    top_right_y = rectangle[1]
    top_right_x = rectangle[2]
    btm_left_y = rectangle[3]
    btm_left_x = rectangle[0]
    btm_right_y = rectangle[3]
    btm_right_x = rectangle[2]

    canvas[top_left_y][top_left_x] = "*"
    canvas[top_right_y][top_right_x] = "*"
    canvas[btm_left_y][btm_left_x] = "*"
    canvas[btm_right_y][btm_right_x] = "*"

    for x in range(top_left_x + 1, top_right_x):
        canvas[top_left_y][x] = "-"
        canvas[btm_left_y][x] = "-"
    for y in range(top_left_y + 1, btm_left_y):
        canvas[y][top_left_x] = "|"
        canvas[y][top_right_x] = "|"

    return canvas


def main():
    canvas = [
        ["a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a"],
        ["a", "a", "a", "a", "a", "a", "a", "a"],
        ["b", "b", "b", "b", "b", "b", "b", "b"],
        ["b", "b", "b", "b", "b", "b", "b", "b"],
    ]
    rectangle = [1, 1, 4, 3]
    # expected = [
    #     ["a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "*", "-", "-", "*", "a", "a", "a"],
    #     ["a", "|", "a", "a", "|", "a", "a", "a"],
    #     ["b", "*", "-", "-", "*", "b", "b", "b"],
    #     ["b", "b", "b", "b", "b", "b", "b", "b"],
    # ]
    for line in solution(canvas, rectangle):
        print(line)


if __name__ == "__main__":
    main()
