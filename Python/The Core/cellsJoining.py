#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are writing a spreadsheet application for an ancient operating system. The
system runs on a computer so old that it can only display ASCII graphics.
Currently you are stuck with implementing the cells joining algorithm.

You are given a table in ASCII graphics, where the following characters are used
for borders: +, -, |. The rows can have different heights and the columns can
have different widths. Each cell has an area greater than 1 (excluding the
borders) and can contain any ASCII characters excluding +, - and |.

The algorithm you want to implement should merge the cells within a given
rectangular part of the table into a single cell by removing the borders between
them (i.e. replace them with space characters (' ') and replace redundant +s
with correct border symbols). The cells to join are represented by the
coordinates of the cells at the extreme bottom-left and top-right of the area.

Example
For

table = ["+----+--+-----+----+",
         "|abcd|56|!@#$%|qwer|",
         "|1234|78|^&=()|tyui|",
         "+----+--+-----+----+",
         "|zxcv|90|77777|stop|",
         "+----+--+-----+----+",
         "|asdf|~~|ghjkl|100$|",
         "+----+--+-----+----+"]

and coords = [[2, 0], [1, 1]], the output should be

solution(table, coords) = ["+----+--+-----+----+",
                           "|abcd|56|!@#$%|qwer|",
                           "|1234|78|^&=()|tyui|",
                           "+----+--+-----+----+",
                           "|zxcv 90|77777|stop|",
                           "|       +-----+----+",
                           "|asdf ~~|ghjkl|100$|",
                           "+-------+-----+----+"]


Input/Output

coords

coords[0] contains 0-based row and column indices (given in that exact order) of
the extreme bottom left cell in the area to join, and coords[1] contains indices
of the extreme top right cell of that region.

It's guaranteed that there are at least two cells to be joined, and that cells
with the given indices do exist in the table.

The rows are numbered from top to bottom while the columns are numbered from
left to right.

"""


def fix_surrounding_borders(table: list[list[str]]) -> list[str]:
    for row in range(len(table)):
        if table[row][0] == "+" and table[row][1] != "-":
            table[row][0] = "|"
        if table[row][-1] == "+" and table[row][-2] != "-":
            table[row][-1] = "|"

    for col in range(len(table[0])):
        if table[0][col] == "+" and table[1][col] != "|":
            table[0][col] = "-"
        if table[-1][col] == "+" and table[-2][col] != "|":
            table[-1][col] = "-"

    return ["".join(row) for row in table]


def solution(table: list[str], coords: list[list[int]]) -> list[str]:
    borders_rows_idx = [idx for idx in range(len(table)) if table[idx][0] == "+"]
    borders_cols_idx = [idx for idx in range(len(table[0])) if table[0][idx] == "+"]

    horizontal_remove_from_row = borders_rows_idx[coords[1][0]] + 1
    horizontal_remove_until_row = borders_rows_idx[coords[0][0] + 1]
    vertical_remove_from_col = borders_cols_idx[coords[0][1]] + 1
    vertical_remove_until_col = borders_cols_idx[coords[1][1] + 1]

    table = [[char for char in row] for row in table]
    for row in range(horizontal_remove_from_row, horizontal_remove_until_row):
        for col in range(vertical_remove_from_col, vertical_remove_until_col):
            if row == horizontal_remove_from_row and col == 0:
                table[row][col] = " "
            elif table[row][col] in "|+-":
                table[row][col] = " "

    table = fix_surrounding_borders(table)

    return table


def main():
    table = [
        "+----+--+-----+----+",
        "|abcd|56|!@#$%|qwer|",
        "|1234|78|^&=()|tyui|",
        "+----+--+-----+----+",
        "|zxcv|90|77777|stop|",
        "+----+--+-----+----+",
        "|asdf|~~|ghjkl|100$|",
        "+----+--+-----+----+",
    ]
    coords = [[2, 0], [1, 1]]
    # expected = [
    #     "+----+--+-----+----+",
    #     "|abcd|56|!@#$%|qwer|",
    #     "|1234|78|^&=()|tyui|",
    #     "+----+--+-----+----+",
    #     "|zxcv 90|77777|stop|",
    #     "|       +-----+----+",
    #     "|asdf ~~|ghjkl|100$|",
    #     "+-------+-----+----+",
    # ]
    print(*solution(table, coords), sep="\n")


if __name__ == "__main__":
    main()
