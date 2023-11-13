#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Let's play Tetris! But first we need to define the rules, especially since they
probably differ from the way you've played Tetris before.

There is an empty field with 20 rows and 10 columns, which is initially empty.
Random pieces appear on the field, each composed of four square blocks. You
can't change the piece's shape, but you can rotate it 90 degree clockwise
(possibly several times) and choose which columns it will appear within. Once
you've rotated the piece and have set its starting position, it appears at the
topmost row where you placed it and falls down until it can't fall any further.
The objective of the game is to create horizontal lines composed of 10 blocks.
When such a line is created, it disappears, and all lines above the deleted one
move down. The player receives 1 point for each deleted row.

Your task is to implement an algorithm that places each new piece optimally. The
piece is considered to be placed optimally if:

- The total number of blocks in the rows this piece will occupy after falling
  down is maximized;
- Among all positions with that value maximized, this position requires the
  least number of rotations;
- Among all positions that require the minimum number of rotations, this one is
  the leftmost one (i.e. the leftmost block's position is as far to the left as
  possible).

The piece can't leave the field. It is guaranteed that it is always possible to
place the Tetris piece in the field.

Implement this algorithm and calculate the number of points that you will get
for the given set of pieces.

Example

For

pieces = [[[".", "#", "."],
           ["#", "#", "#"]],
          [["#", ".", "."],
           ["#", "#", "#"]],
          [["#", "#", "."],
           [".", "#", "#"]],
          [["#", "#", "#", "#"]],
          [["#", "#", "#", "#"]],
          [["#", "#"],
           ["#", "#"]]]

the output should be
solution(pieces) = 1.

For this explanation, we are representing each block by the index of the piece
it belongs to. After the first 5 blocks fall, the field looks like this:

...
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . 3 4
. . . . . . . . 3 4
. 0 . 1 . 2 2 . 3 4
0 0 0 1 1 1 2 2 3 4

Note that the 0th, 1st, and 2nd pieces all fell down without rotating, while the
3rd and the 4th pieces were rotated one time each.

Since there is now a row composed of 10 blocks, it is deleted, and you get 1
point.

When the last piece falls, the final field looks like this:

...
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
5 5 . . . . . . 3 4
5 5 . . . . . . 3 4
. 0 . 1 . 2 2 . 3 4

Input/Output

[input] array.array.array.char pieces

A non-empty array of pieces in the order in which they fall. Each piece is
represented as a rectangular matrix, where '#' represents a block and '.'
represents an empty cell.

Each piece consists of 4 blocks, and each block shares a common side with at
least one another block. It's guaranteed that each piece contains neither empty
rows nor empty columns.

[output] integer

The number of points you will have by the end of the game.

"""


class Piece:
    bottom_row_weight: int
    coord: list[int, int]
    shape: list[list[str]]
    width: int
    height: int
    rotations: int

    def __init__(self, shape: list[list[str]]) -> None:
        self.shape = shape
        self.height = len(shape)
        self.width = len(shape[0])
        self.coord = [0, 0]
        self.rotations = 0

    def rotate_clockwise(self) -> list[list[str]]:
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        self.height = len(self.shape)
        self.width = len(self.shape[0])
        self.rotations += 1
        return self.shape


class Tetris:
    rows: int
    cols: int
    field: list[list[str]]
    points: int

    def __init__(self, rows: int = 20, cols: int = 10) -> None:
        self.rows = rows
        self.cols = cols
        self.field = [["." for _ in range(self.cols)] for _ in range(self.rows)]
        self.points = 0

    def find_optimal_move(self, piece: Piece) -> list[int, int]:
        best_score = 0
        best_positions = []
        original_field = list(line.copy() for line in self.field)
        for rotation in range(4):
            for col in range(self.cols - piece.width + 1):
                self.field = list(line.copy() for line in original_field)
                piece.coord[1] = col
                self.drop_piece(piece)
                current_score = self.count_row_points(piece.coord[0] + piece.height - 1)
                if current_score > best_score:
                    best_score = current_score
                    best_positions = [(current_score, rotation, col)]
                elif current_score == best_score:
                    best_positions.append((current_score, rotation, col))
            piece.rotate_clockwise()

        self.field = original_field
        if len(best_positions) == 1:
            best_position = best_positions[0]
        else:
            criteria = (lambda score: -score[0], lambda rot: rot[1], lambda ht: ht[2])
            best_position = min(best_positions, key=lambda x: criteria)
        piece.coord[1] = best_position[2]
        while piece.rotations % 4 != best_position[1]:
            piece.rotate_clockwise()

    def count_row_points(self, row: int) -> int:
        return self.field[row].count("#")

    def get_drop_piece_row(self, piece: Piece) -> int:
        lowest_valid_row = 0
        for top_shape_row in range(self.rows + 1 - piece.height):
            if self.piece_collision(piece, top_shape_row, piece.coord[1]):
                break
            lowest_valid_row = top_shape_row
        return lowest_valid_row

    def drop_piece(self, piece: Piece) -> None:
        lowest_valid_row = self.get_drop_piece_row(piece)
        piece.coord[0] = lowest_valid_row
        self.set_piece_in_field(piece)

    def set_piece_in_field(self, piece: Piece) -> None:
        for row, shape_line in enumerate(piece.shape):
            for col, piece_char in enumerate(shape_line):
                x = piece.coord[0] + row
                y = piece.coord[1] + col
                if piece_char != ".":
                    self.field[x][y] = piece_char

    def piece_collision(self, piece: Piece, row: int, col: int) -> bool:
        for piece_row, shape_line in enumerate(piece.shape):
            for piece_col, piece_char in enumerate(shape_line):
                field_char = self.field[piece_row + row][piece_col + col]
                if piece_char == "#" and field_char != ".":
                    return True
        return False

    def remove_filled_lines(self) -> int:
        filled_lines_rows = self.get_filled_lines()
        lines_to_remove = len(filled_lines_rows)
        if lines_to_remove > 0:
            for line_number in filled_lines_rows:
                self.remove_line(line_number)
        return lines_to_remove

    def get_filled_lines(self) -> list[int]:
        filled_lines = []
        for line_number, line in enumerate(self.field):
            if all(char == "#" for char in line):
                filled_lines.append(line_number)
        return filled_lines

    def remove_line(self, line_number: int) -> None:
        new_line = ["." for _ in range(self.cols)]
        del self.field[line_number]
        self.field.insert(0, new_line)


def solution(pieces: list[list[list[str]]]) -> int:
    tetris = Tetris()
    for piece_raw in pieces:
        one_piece = Piece(piece_raw)
        tetris.find_optimal_move(one_piece)
        tetris.drop_piece(one_piece)
        tetris.points += tetris.remove_filled_lines()
    return tetris.points


def main():
    case = [
        [[".", "#", "#"], ["#", "#", "."]],
        [[".", "#", "."], ["#", "#", "#"]],
        [["#", "#", "."], [".", "#", "#"]],
        [[".", "#", "."], ["#", "#", "#"]],
        [["#", "#", "#", "#"]],
        [["#", ".", "."], ["#", "#", "#"]],
        [["#", "#"], ["#", "#"]],
        [["#", "#", "#"], [".", ".", "#"]],
        [[".", "#", "#"], ["#", "#", "."]],
        [[".", "#", "."], ["#", "#", "#"]],
        [["#", "#", "."], [".", "#", "#"]],
        [[".", "#", "."], ["#", "#", "#"]],
        [["#", "#", "#", "#"]],
        [["#", ".", "."], ["#", "#", "#"]],
        [["#", "#"], ["#", "#"]],
        [["#", "#", "#"], [".", ".", "#"]],
    ]
    # expected = 3
    print(solution(case))


if __name__ == "__main__":
    main()
