#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Your task is to draw a special fractal after n iterations. The fractal consists
of unit connectors "|" and "_".

For n = 1 the fractal looks as follows:

_
_|

Now assume that you have already made N iterations and drawn the f(N) fractal.
To draw the f(N + 1) fractal do the following: Note that every fractal has
exactly two edge points which can be connected to the edge points of other
fractals using the unit connectors. At first, take the f(N) fractal and place it
in the top left corner. As the next step, put f(N) rotated by 0°, 90°, 180° or
270° in the remaining 3 quarters - top right, bottom left and bottom right - so
that it is possible to connect all four of them by adding exactly 3 unit
connectors between the adjacent fractal edge points. Note that there is always
exactly one possible combination of rotations which allows to connect all 4 f(N)
fractals together.

See examples below for better understanding.

Example

    For n = 1, the output should be

solution(n) = [[" ", "_", " "],
               [" ", "_", "|"]]

In other words, it should represent      _
the following picture:                   _|

    For n = 2, the output should be

solution(n) = [[" ", "_", " ", " ", " ", "_", " "],
               [" ", "_", "|", " ", "|", "_", " "],
               ["|", " ", " ", "_", " ", " ", "|"],
               ["|", "_", "|", " ", "|", "_", "|"]]

Or, to put it differently:
 _   _
 _| |_
|  _  |
|_| |_|

    For n = 3, the output should be

solution(n) = [
    [" ", "_", " ", " ", " ", "_", "_", "_", " ", " ", " ", "_", "_", "_", " "],
    [" ", "_", "|", " ", "|", "_", " ", " ", "|", "_", "|", " ", " ", "_", "|"],
    ["|", " ", " ", "_", " ", " ", "|", " ", " ", "_", " ", " ", "|", "_", " "],
    ["|", "_", "|", " ", "|", "_", "|", " ", "|", " ", "|", "_", "_", "_", "|"],
    [" ", "_", " ", " ", " ", "_", " ", " ", "|", " ", " ", "_", "_", "_", " "],
    ["|", " ", "|", "_", "|", " ", "|", " ", "|", "_", "|", " ", " ", "_", "|"],
    ["|", "_", " ", " ", " ", "_", "|", " ", " ", "_", " ", " ", "|", "_", " "],
    [" ", "_", "|", " ", "|", "_", "_", "_", "|", " ", "|", "_", "_", "_", "|"]
]

The fractal looks as follows:

 _   ___   ___
 _| |_  |_|  _|
|  _  |  _  |_
|_| |_| | |___|
 _   _  |  ___
| |_| | |_|  _|
|_   _|  _  |_
 _| |___| |___|


Input/Output

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 6.

[output] array.array.char

Each character can be an underscore ("_"), a vertical bar ("|") or a whitespace
character (" ").

"""


def P(table):
    print()
    for line in table:
        print("".join(line))
    print()


def rotate_clockwise(table):
    rotated = [*map(list, zip(*table[::-1]))]
    return rotate_chars(rotated)


def rotate_chars(table: list[list[str]]) -> list:
    for row in range(len(table)):
        for col in range(len(table[0])):
            char = table[row][col]
            table[row][col] = "_" if char == "|" else "|" if char == "_" else " "
    return table


def add_horizontals_char_if_needed(table):
    for row in range(len(table)):
        for col in range(0, len(table) - 2, 3):
            col1 = table[row][col]
            col2 = table[row][col + 1]
            col3 = table[row][col + 2]
            if col1 == "_" and col2 == " " and col3 == "_":
                table[row][col + 1] == "_"
    return table


def move_verticals_down(table):
    for row in range(2, len(table), 3):
        for col in range(len(table[0])):
            if table[row - 1][col] == " " and table[row][col] != " ":
                table[row - 1][col] = table[row][col]
                table[row][col] = " "

    return table


def remove_empty_lines(table):
    def empty_lines_filter(row):
        return not all(char == " " for char in row)

    filtered_table = list(filter(empty_lines_filter, table))
    return filtered_table


def connect_parts(figure, is_horizontal):
    if is_horizontal:
        mid_row = len(figure) // 2
        mid_col = len(figure[0]) // 2
        figure[mid_row][0] = "|"
        figure[mid_row][-1] = "|"
        figure[mid_row][mid_col] = "_"
    else:
        mid_row = len(figure) // 2
        mid_col = len(figure[0]) // 2
        figure[0][mid_col] = "_"
        figure[-1][mid_col] = "_"
        figure[mid_row][mid_col + 1] = "|"
    return figure


def assemble_figure(top_left, top_right, btm_left, btm_right):
    merged = []
    for left, right in zip(top_left, top_right):
        merged.append(left + [" "] + right)
    for left, right in zip(btm_left, btm_right):
        merged.append(left + [" "] + right)
    return merged


def solution(iterations: int):
    base = [
        [" ", "_", " "],
        [" ", " ", "|"],
        [" ", "_", " "],
    ]

    fractal = base
    for iteration in range(iterations - 1):
        even_iteration = iteration % 2 == 0
        if even_iteration:
            btm_left = rotate_clockwise(fractal)
            top_right = rotate_clockwise(btm_left)
            btm_right = btm_left
        else:
            btm_left = rotate_clockwise(rotate_clockwise(fractal))
            top_right = rotate_clockwise(btm_left)
            btm_right = top_right

        fractal = assemble_figure(fractal, top_right, btm_left, btm_right)
        fractal = connect_parts(fractal, even_iteration)
        fractal = add_horizontals_char_if_needed(fractal)
        fractal = move_verticals_down(fractal)
        fractal = remove_empty_lines(fractal)
        P(fractal)
    print()
    return fractal


def main():
    case = 3
    print(solution(case))


if __name__ == "__main__":
    main()
