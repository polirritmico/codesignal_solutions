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

    def generate_iterations(self, iterations: int) -> None:
        for iteration in range(2, iterations + 1):
            if iteration % 2 == 0:
                btm_left = self.rotate_clockwise()
                top_right = self.rotate_clockwise(turns=2)
                self.assemble_parts_even(self.fractal, top_right, btm_left, btm_left)
            else:
                btm_left = self.rotate_clockwise(turns=2)
                top_right = self.rotate_clockwise(turns=3)
                self.assemble_parts_odd(self.fractal, top_right, btm_left, top_right)

    def rotate_clockwise(self, turns: int = 1) -> list[list[str]]:
        rotated = self.fractal
        for _ in range(turns):
            rotated = [*map(list, zip(*rotated[::-1]))]
        return self.rotate_chars(rotated) if turns % 2 != 0 else rotated

    def rotate_chars(self, table: list[list[str]]) -> list[list[str]]:
        for row in range(len(table)):
            for col in range(len(table[0])):
                char = table[row][col]
                table[row][col] = "_" if char == "|" else "|" if char == "_" else " "
        return table

    def assemble_parts_even(
        self, top_left: list, top_right: list, btm_left: list, btm_right: list
    ) -> None:
        parts_width = len(top_left[0])
        horizontal_separator = list("|" + " " * (parts_width * 2 - 1) + "|")

        fractal = []
        for left, right in zip(top_left, top_right):
            fractal.append(left + [" "] + right)
        fractal.append(horizontal_separator)
        for left, right in zip(btm_left, btm_right):
            fractal.append(left + [" "] + right)

        middle_row = len(top_left) + 1
        fractal[middle_row][parts_width] = "_"
        self.fractal = fractal

    def assemble_parts_odd(
        self, top_left: list, top_right: list, btm_left: list, btm_right: list
    ) -> None:
        parts_width = len(top_left[0])
        parts_height = len(top_left)
        horizontal_sep = list(" " * (parts_width * 2 + 1))
        vertical_sep = list("_" + " " * (parts_height * 2 - 1) + "_")

        fractal = []
        for left, mid, right in zip(top_left, vertical_sep, top_right):
            fractal.append(left + [mid] + right)
        fractal.append(horizontal_sep)
        middle_row = parts_width + 1
        for left, mid, right in zip(btm_left, vertical_sep[middle_row:], btm_right):
            fractal.append(left + [mid] + right)

        fractal[parts_height][middle_row] = "|"
        self.fractal = fractal

    def finish_and_export(self) -> list[list[str]]:
        self.merge_lines_upwards()
        self.add_missing_horizontal_lines()
        self.remove_empty_lines()
        return self.fractal

    def add_missing_horizontal_lines(self) -> None:
        for x, row in enumerate(self.fractal):
            for y in range(len(row) - 2):
                if row[y] == "_" and row[y + 1] == " " and row[y + 2] == "_":
                    row[y + 1] = "_"

    def merge_lines_upwards(self) -> None:
        for row in range(2, len(self.fractal), 2):
            for col in range(len(self.fractal[0])):
                if self.fractal[row - 1][col] == " " and self.fractal[row][col] != " ":
                    self.fractal[row - 1][col] = self.fractal[row][col]
                    self.fractal[row][col] = " "

    def remove_empty_lines(self) -> None:
        self.fractal = list(
            filter(lambda row: any(char != " " for char in row), self.fractal)
        )


def solution(iterations: int):
    fractal = Fractal()
    fractal.generate_iterations(iterations)
    return fractal.finish_and_export()


def P(table):
    """Print function for debugging"""
    print()
    for row in table:
        print("".join(row))
    print()


def main():
    case = 6
    P(solution(case))


if __name__ == "__main__":
    main()
