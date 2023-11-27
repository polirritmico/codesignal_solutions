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


class Fractal:
    fractal: list[list[str]]

    def __init__(self):
        self.fractal: list[list[str]] = [
            [" ", "_", " "],
            [" ", " ", "|"],
            [" ", "_", " "],
        ]

    def rotate_clockwise(self, turns: int = 1, table=None):
        rotated = table if table is not None else self.fractal
        for _ in range(turns):
            rotated = [*map(list, zip(*rotated[::-1]))]
        return self.rotate_chars(rotated) if turns % 2 != 0 else rotated

    def rotate_chars(self, table: list[list[str]]) -> list:
        for row in range(len(table)):
            for col in range(len(table[0])):
                char = table[row][col]
                table[row][col] = "_" if char == "|" else "|" if char == "_" else " "
        return table

    def make_even_fractal(self, table=None):
        base = table if table is not None else self.fractal

        btm_left = self.rotate_clockwise(table=base)
        top_right = self.rotate_clockwise(turns=2, table=base)
        btm_right = btm_left
        join_line = self.make_mid_horizontal_join_line(base)

        self.fractal = self.assemble_parts_even(
            base, top_right, btm_left, btm_right, join_line
        )
        return self.fractal

    def make_mid_horizontal_join_line(self, base_fractal) -> list[str]:
        spaces = " " * (len(base_fractal[0]) - 1)
        return list("|" + spaces + "_" + spaces + "|")

    def assemble_parts_even(self, top_left, top_right, btm_left, btm_right, join):
        spaces = " " * (len(top_left[0]) * 2 - 1)
        join = list("|" + spaces + "|")

        fractal = []
        for left, right in zip(top_left, top_right):
            fractal.append(left + [" "] + right)
        fractal.append(join)
        for left, right in zip(btm_left, btm_right):
            fractal.append(left + [" "] + right)

        mid_row = len(top_left) + 1
        mid_col = len(top_left[0])
        fractal[mid_row][mid_col] = "_"
        return fractal

    def make_odd_fractal(self, table=None):
        base = table if table is not None else self.fractal

        btm_left = self.rotate_clockwise(turns=2, table=base)
        top_right = self.rotate_clockwise(turns=3, table=base)
        btm_right = top_right
        join_line = self.make_mid_vertical_join_line(base)

        self.fractal = self.assemble_parts_odd(
            base, top_right, btm_left, btm_right, join_line
        )
        return self.fractal

    def make_mid_vertical_join_line(self, base_fractal) -> list[str]:
        spaces = " " * (len(base_fractal) * 2 - 1)
        return list("_" + spaces + "_")

    def assemble_parts_odd(self, top_left, top_right, btm_left, btm_right, join):
        fractal = []
        mid_height = len(top_left) + 1
        mid_width = len(top_left[0])
        horizontal_separator = list(" " * (mid_width * 2 + 1))
        for left, mid, right in zip(top_left, join[:mid_height], top_right):
            fractal.append(left + [mid] + right)
        fractal.append(horizontal_separator)
        for left, mid, right in zip(btm_left, join[mid_height:], btm_right):
            fractal.append(left + [mid] + right)
        fractal[mid_height][mid_width + 1] = "|"
        return fractal

    def generate_drawing(self) -> list[list[str]]:
        draw = self.fractal.copy()
        draw = self.merge_lines_upwards(draw)
        draw = self.add_missing_horizontal_lines(draw)
        draw = self.remove_empty_lines(draw)
        return draw

    def add_missing_horizontal_lines(self, fractal_drawing):
        for x, row in enumerate(fractal_drawing):
            for y in range(len(row) - 2):
                if row[y] == "_" and row[y + 1] == " " and row[y + 2] == "_":
                    row[y + 1] = "_"
        return fractal_drawing

    def merge_lines_upwards(self, fractal):
        height = len(fractal)
        width = len(fractal[0])
        for row in range(2, height, 2):
            for col in range(width):
                if fractal[row - 1][col] == " " and fractal[row][col] != " ":
                    fractal[row - 1][col] = fractal[row][col]
                    fractal[row][col] = " "
        return fractal

    def remove_empty_lines(self, fractal):
        for row in fractal:
            if all(char == " " for char in row):
                fractal.remove(row)
        return fractal

    def generate_fractal_iterations(self, iterations: int) -> None:
        for iteration in range(2, iterations + 1):
            if iteration % 2 == 0:
                self.make_even_fractal(self.fractal)
            else:
                self.make_odd_fractal(self.fractal)


def P(table, ascii_mode=True):
    print()
    output = ""
    if not ascii_mode:
        for row in table:
            print(row, sep="\n")
            output += "".join(row)
            output += "\n"
    else:
        for row in table:
            print("".join(row))
            output += "".join(row)
            output += "\n"
    print()
    return output


def solution(iterations: int):
    fractal = Fractal()
    fractal.generate_fractal_iterations(iterations)
    return fractal.generate_drawing()


def main():
    case = 3
    P(solution(case))


if __name__ == "__main__":
    main()
