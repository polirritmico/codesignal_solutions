#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A nonogram is also known as Paint by Numbers and Japanese Crossword. The aim in
this puzzle is to color the grid into black and white squares. At the top of
each column, and at the side of each row, there are sets of one or more numbers
which describe the runs of black squares in that row/column in exact order. For
example, if you see 10 1 along some column/row, this indicates that there will
be a run of exactly ten black squares, followed by one or more white squares,
followed by a single black square. The cells along the edges of the grid can
also be white.

You are given a square nonogram of size size. Its grid is given as a square
matrix nonogramField of size (size + 1) / 2 + size, where the first (size + 1) /
2 cells of each row and and each column define the numbers for the corresponding
row/column, and the rest size × size cells define the the grid itself.

Determine if the given nonogram has been solved correctly.

Note: here / means integer division.

Example

For size = 5 and

nonogramField = [["-", "-", "-", "-", "-", "-", "-", "-"],
                    ["-", "-", "-", "2", "2", "1", "-", "1"],
                    ["-", "-", "-", "2", "1", "1", "3", "3"],
                    ["-", "3", "1", "#", "#", "#", ".", "#"],
                    ["-", "-", "2", "#", "#", ".", ".", "."],
                    ["-", "-", "2", ".", ".", ".", "#", "#"],
                    ["-", "1", "2", "#", ".", ".", "#", "#"],
                    ["-", "-", "5", "#", "#", "#", "#", "#"]]

the output should be solution(size, nonogramField) = true;

For size = 5 and

nonogramField = [["-", "-", "-", "-", "-", "-", "-", "-"],
                    ["-", "-", "-", "-", "-", "1", "-", "-"],
                    ["-", "-", "-", "3", "3", "2", "5", "5"],
                    ["-", "-", "3", ".", ".", ".", "#", "#"],
                    ["-", "2", "2", "#", "#", "#", "#", "#"],
                    ["-", "-", "5", "#", "#", "#", "#", "#"],
                    ["-", "-", "5", "#", "#", "#", "#", "#"],
                    ["-", "-", "2", ".", ".", ".", "#", "#"]]

the output should be solution(size, nonogramField) = false.

There are three mistakes in the nonogram:
    - In the 5th (1-based) row there are numbers ["-", "2", "2"], so there
    should be two runs of 2 black squares separated by at least one white
    square. However, there is only one run of 5 black squares.
    - In the 6th column there are numbers ["-", "1", "2"], so there should be a
    run of exactly 1 black square, followed by one or more white squares,
    followed by another 2 black squares. However, there is a single run of 3
    black squares not separated by white ones.
    - Finally, in the 4th row there are numbers ["-", "-", "3"], so there should
    be a single run of exactly 3 black squares. However, there is just a
    2-square run in that row.

nonogramField: A square matrix of strings of size (size + 1) / 2 + size defining
the puzzle field. The first (size + 1) / 2 cells of each row and each column
define the numbers for this row/column. If there is no number in the cell, its
value is "-". The remaining size × size cells define the grid, where string "#"
denotes black cells and string "." denotes white ones.

"""


def solution(size: int, nonogram: list[list[str]]) -> bool:
    header_size = (size + 1) // 2
    columns = [column for column in zip(*nonogram)][header_size:]
    rows = [row for row in nonogram[header_size:]]
    for full_column in columns:
        header = full_column[:header_size]
        col = full_column[header_size:]
        expected_counts = [int(count) for count in header if count != "-"]
        groups_in_col = "".join(col).split(".")
        counts = list(filter(None, [group.count("#") for group in groups_in_col]))
        if counts != expected_counts:
            return False
    for full_row in rows:
        header = full_row[:header_size]
        row = full_row[header_size:]
        expected_counts = [int(count) for count in header if count != "-"]
        groups_in_row = "".join(row).split(".")
        counts = list(filter(None, [group.count("#") for group in groups_in_row]))
        if expected_counts != counts:
            return False
    return True


def main():
    size = 5
    nonogram_field = [
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "5", "4", "5", "4", "5"],
        ["-", "1", "3", "#", "#", "#", ".", "#"],
        ["-", "-", "5", "#", "#", "#", "#", "#"],
        ["-", "-", "5", "#", "#", "#", "#", "#"],
        ["-", "-", "5", "#", "#", "#", "#", "#"],
        ["-", "3", "1", "#", ".", "#", "#", "#"],
    ]
    # expected = False
    # size = 5
    # nonogram_field = [
    #     ["-", "-", "-", "-", "-", "-", "-", "-"],
    #     ["-", "-", "-", "2", "2", "1", "-", "1"],
    #     ["-", "-", "-", "2", "1", "1", "3", "3"],
    #     ["-", "3", "1", "#", "#", "#", ".", "#"],
    #     ["-", "-", "2", "#", "#", ".", ".", "."],
    #     ["-", "-", "2", ".", ".", ".", "#", "#"],
    #     ["-", "1", "2", "#", ".", ".", "#", "#"],
    #     ["-", "-", "5", "#", "#", "#", "#", "#"],
    # ]
    # expected = True
    print(solution(size, nonogram_field))


if __name__ == "__main__":
    main()
