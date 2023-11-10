#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are most likely familiar with the game 2048.

2048 is played on a gray 4 × 4 grid with numbered tiles that slide smoothly when
a player moves them using one of the four arrow keys - Up, Down, Left or Right.
On every turn, a new tile with a value of either 2 or 4 randomly appears on an
empty spot of the board. After one of the keys is pressed, the tiles slide as
far as possible in the chosen direction until they are stopped either by another
tile or by the edge of the grid. If two tiles with the same number collide while
moving, they merge into a tile with this number doubled. You can't merge an
already merged tile in the same turn. If there are more than 2 tiles in the same
row (column) that can merge, the farthest (closest to an edge) pair will be
merged first (see the second example).

In this problem you are not going to solve the 2048 puzzle, but you are going to
find the final state of the board from the given one after a defined set of n
arrow key presses, assuming that no new random tiles will appear on the empty
spots.

The following example shows the next state of the board after pressing Right.

https://codesignal.s3.amazonaws.com/uploads/1664318501/ex1.png?raw=true

This example shows the next state of the board after pressing Down.

https://codesignal.s3.amazonaws.com/uploads/1664318501/ex2.png?raw=true

For more details you can visit http://gabrielecirulli.github.io/2048/ and play
online 😃

You are given a matrix 4 × 4 which corresponds to the 2048 game grid. grid[0][0]
corresponds to the upper left tile of the grid. Each element of the grid is
equal to some power of 2 if there is a tile with that value in the corresponding
position, and 0 if it corresponds to the empty spot. You are also given a
sequence of key presses as a string path. Each character of the string equals L,
R, U, or D corresponding to Left, Right, Up or Down respectively.
Please note that in some cases after pressing an arrow key nothing will be
changed.

Example

For

grid = [[0, 0, 0, 0],
        [0, 0, 2, 2],
        [0, 0, 2, 4],
        [2, 2, 4, 8]]

and path = "RR", the output should be

solution(grid, path) = [[0, 0, 0, 0],
                        [0, 0, 0, 4],
                        [0, 0, 2, 4],
                        [0, 0, 8, 8]]

Input/Output


- [input] array.array.integer grid

    A square matrix of size 4 × 4, the starting state of the board. Each value
    of the matrix is 0 a power of 2.

    Guaranteed constraints:
    grid[i][j] ∈ {0} ∪ {2i | i = 0, 1, ..., 16}.


- [input] string path

    String representing key presses. Each character of the string equals L, R,
    U, or D.

- [output] array.array.integer

    The final state of the board after the given key presses are applied.


"""

from typing import Self


class Tile:
    def __init__(self, x: int, y: int, value: int):
        self.value: int = value
        self.coord: tuple = (x, y)

    def __repr__(self):
        return str(self.value).rjust(4)


class Grid:
    grid: list[list[Tile | None]]
    rows: int
    cols: int

    def __init__(self, raw_grid: list[list[int]]):
        rows = len(raw_grid)
        cols = len(raw_grid[0])
        self.grid: list = [[None for _ in range(rows)] for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                current = raw_grid[row][col]
                if current == 0:
                    continue
                new_tile = Tile(row, col, current)
                self.grid[row][col] = new_tile

    def move_tiles(self, pressed_key: str) -> None:
        pass


def solution(raw_grid: list[list[int]], keystrokes: str):
    grid = Grid(raw_grid)
    print(*grid.grid, sep="\n")
    for pressed_key in keystrokes:
        grid.move_tiles(pressed_key)
        print("", *grid.grid, sep="\n")
        break


def main():
    grid = [
        [0, 0, 0, 0],
        [0, 0, 2, 2],
        [0, 0, 2, 4],
        [2, 2, 4, 8],
    ]
    path = "RR"
    # expected = [
    #   [0, 0, 0, 0],
    #   [0, 0, 0, 4],
    #   [0, 0, 2, 4],
    #   [0, 0, 8, 8],
    # ]
    print(solution(grid, path))


if __name__ == "__main__":
    main()
