#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Let's remember the '90s and play an old-school Lines game with the following
rules.

The game starts with a 9 × 9 field with several colored balls placed on its
cells (there are 7 possible colors but not all colors have to be present
initially). The player can move one ball per turn, and they may only move a ball
if there is a clear path between the current position of the chosen ball and the
desired destination. Clear paths are formed by neighboring empty cells. Two
cells are neighboring if they have a common side. The goal is to remove balls by
forming lines (horizontal, vertical or diagonal) of at least five balls of the
same color. If the player manages to form one or more such lines, the move is
called successful, and the balls in those lines disappear. Otherwise, the move
is called unsuccessful, and three more balls appear on the field.

You are given the game logs, and your task is to calculate the player's final
score. Here's the information you have:

- The field state at the initial moment;
- The clicks the user has made. Note that a click does not necessarily result in
  a move:
    - If the user clicks a ball and then another, the first click is ignored;
    - If two consecutive clicks result in an incorrect move, they are ignored;
- After each unsuccessful move three more balls appear:
    - newBalls contains the balls' colors;
    - newBallsCoordinates contains their coordinates;
    - Note that after the balls appear, new lines may form;
- Whenever new lines appear, they are removed and the player receives A + B - 1
  points, where:
    - A is the number of lines of at least five balls;
    - B is the total number of balls in those lines;
- Possible ball colors are red, blue, orange, violet, green, yellow and cyan,
  which are represented in logs by "R", "B", "O", "V", "G", "Y" and "C"
  respectively.

Example

For

field = [['.', 'G', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', 'V', '.'],
         ['.', 'O', '.', '.', 'O', '.', '.', '.', '.'],
         ['.', '.', '.', '.', 'O', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', 'O'],
         ['.', '.', '.', '.', 'O', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['R', '.', '.', '.', '.', '.', '.', 'B', 'R'],
         ['.', '.', 'C', '.', '.', '.', '.', 'Y', 'O']]

clicks = [[4, 8], [2, 1], [4, 4], [6, 4], [4, 8], [1, 2], [1, 4], [4, 8], [6, 4]],
newBalls = ['R', 'V', 'C', 'G', 'Y', 'O'], and
newBallsCoordinates = [[1, 2], [8, 5], [8, 6], [1, 1], [1, 8], [7, 4]],

the output should be:
    solution(field, clicks, newBalls, newBallsCoordinates) = 6.

The only correct moves were:
    Orange ball moved from [2, 1] to [4, 4];
    Red ball moved from [1, 2] to [1, 4];
    Orange ball moved from [4, 8] to [6, 4]

After the third move a vertical line with 6 orange balls appears, so it is
removed and the player receives 1 + 6 - 1 = 6 points.

https://codesignal.s3.amazonaws.com/uploads/1664394256/example1.jpg?raw=true

For

field = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', 'O', '.', 'O', '.', 'O', '.', '.'],
         ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', 'O'],
         ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
         ['.', '.', 'O', '.', 'O', '.', 'O', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

clicks = [[4, 8], [4, 4]],
newBalls = [], and
newBallsCoordinates = [], the output should be
solution(field, clicks, newBalls, newBallsCoordinates) = 17.

After the move there will be three lines with exactly 5 balls of the same color,
so the answer is 3 + (5 + 5 + 5) - 1 = 17.

https://codesignal.s3.amazonaws.com/uploads/1664394256/example2.jpg?raw=true

Input/Output

[input] array.array.char field

A rectangular matrix, where each element represents either a ball of some color
(see above), or an empty cell ('.'). It is guaranteed that initially there are
no lines of five or more balls of the same color.

Guaranteed constraints:
field.length = 9,
field[i].length = 9.

[input] array.array.integer clicks

Each element of clicks consists of two integers and represents some cell from
fields that was clicked.

Guaranteed constraints:
2 ≤ clicks.length ≤ 40,
0 ≤ clicks[i][j] ≤ 8.

[input] array.char newBalls

It is guaranteed that there are enough elements in the array to add balls after
each unsuccessful move.

Guaranteed constraints:
0 ≤ newBalls.length ≤ 60.

[input] array.array.integer newBallsCoordinates

The ith element represents the coordinates of the ith appeared ball.
It is guaranteed that balls are added only to the empty cells.

Guaranteed constraints:
newBallsCoordinates.length = newBalls.length,
newBallsCoordinates[i].length = 2,
0 ≤ newBallsCoordinates[i][j] ≤ 8.

[output] integer

The player's final score.


"""


class Ball:
    @classmethod
    def ball_generator(
        self, new_balls_colors: list[str], new_balls_coords: list[list[int, int]]
    ):
        for color, coord in zip(new_balls_colors, new_balls_coords):
            yield Ball(color, coord[0], coord[1])

    def __init__(self, color: str, row: int, col: int):
        self.color = color
        self.row = row
        self.col = col

    def __str__(self) -> str:
        return f"{self.color} ({self.row}, {self.col})"

    def __repr__(self) -> str:
        return self.color.rjust(4)


class LineGame:
    ball_generator: iter
    score: int
    height: int
    width: int
    min_line_size: int = 5
    field: list[list[Ball | None]]
    selected: Ball | None

    def __init__(self, field_raw: list[list[str]]) -> None:
        self.height = len(field_raw)
        self.height = len(field_raw[0])
        self.score = 0
        self.selected: Ball | None = None
        self.field = []
        for x, row in enumerate(field_raw):
            new_row = []
            for y, tile in enumerate(row):
                new_row.append(None if tile == "." else Ball(tile, x, y))
            self.field.append(new_row)

    def set_ball_generator(
        self, new_balls: list[str], new_balls_coords: list[list[int, int]]
    ) -> None:
        self.ball_generator = Ball.ball_generator(new_balls, new_balls_coords)

    def add_new_balls(self, balls_to_add: int) -> None:
        for _ in range(balls_to_add):
            new_ball: Ball = next(self.ball_generator)
            self.field[new_ball.row][new_ball.col] = new_ball

    def are_connected(self, target_coord: list[int, int]) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        checked_tiles = [
            [False for _ in range(self.height)] for _ in range(self.height)
        ]
        tiles_to_explore = [(self.selected.row, self.selected.col)]

        while len(tiles_to_explore) > 0:
            current = tiles_to_explore.pop(0)
            checked_tiles[current[0]][current[1]] = True

            if current[0] == target_coord[0] and current[1] == target_coord[1]:
                return True

            for direction in directions:
                row = current[0] + direction[0]
                col = current[1] + direction[1]

                if row < 0 or row >= self.height or col < 0 or col >= self.height:
                    continue
                if not checked_tiles[row][col] and self.field[row][col] is None:
                    tiles_to_explore.append((row, col))
        return False

    def move_ball(self, origin: Ball, target: list[int, int]) -> None:
        self.field[target[0]][target[1]] = origin
        self.field[origin.row][origin.col] = None

    def count_points(self, balls_lines: list[list[Ball]]) -> int:
        lines = len(balls_lines)
        if lines == 0:
            return 0
        balls = sum(len(line) for line in balls_lines)
        return lines + balls - 1

    def get_all_diagonals(self) -> list[list[Ball | None]]:
        diagonals = []
        size = self.height
        for col in range(size):
            ranges = range(size - col)
            left_diagonal = [self.field[col + i][i] for i in ranges]
            right_diagonal = [self.field[col + i][size - 1 - i] for i in ranges]
            diagonals.append(left_diagonal)
            diagonals.append(right_diagonal)

        for col in range(1, size):
            ranges = range(size - col)
            left_diagonal = [self.field[i][col + i] for i in ranges]
            right_diagonal = [self.field[i][size - col - i - 1] for i in ranges]
            diagonals.append(left_diagonal)
            diagonals.append(right_diagonal)

        return diagonals

    def completed_lines_balls(self) -> list[list[Ball]]:
        full_rows = [row for row in self.field]
        full_columns = [[row[col] for row in self.field] for col in range(self.height)]
        full_diagonals = self.get_all_diagonals()
        rows = self.filter_completed_lines(full_rows)
        columns = self.filter_completed_lines(full_columns)
        diagonals = self.filter_completed_lines(full_diagonals)

        return rows + columns + diagonals

    def filter_completed_lines(self, full_lines: list[list[Ball]]) -> list[list[Ball]]:
        filtered_lines = []
        for raw_line in full_lines:
            line = []
            line_color = ""
            for i in range(len(raw_line)):
                current = raw_line[i]
                if len(line) == 0:
                    if isinstance(current, Ball):
                        line_color = current.color
                        line.append(current)
                else:
                    if isinstance(current, Ball):
                        if line_color == current.color:
                            line.append(current)
                            continue
                        elif len(line) >= self.min_line_size:
                            filtered_lines.append(line)
                        line = [current]
                        line_color = current.color
                    else:
                        if len(line) >= self.min_line_size:
                            filtered_lines.append(line)
                        line = []
                        line_color = ""
            if len(line) >= self.min_line_size:
                filtered_lines.append(line)

        return filtered_lines

    def remove_balls(self, balls_lines: list[list[Ball]]) -> None:
        for line in balls_lines:
            for ball in line:
                self.field[ball.row][ball.col] = None
                del ball

    def click(self, coord: list) -> None:
        current = self.field[coord[0]][coord[1]]
        if self.selected:
            if current is None:
                if self.are_connected(coord):
                    self.move_ball(self.selected, coord)
                    balls_lines = self.completed_lines_balls()
                    if len(balls_lines) == 0:
                        self.add_new_balls(3)
                    else:
                        self.score += self.count_points(balls_lines)
                        self.remove_balls(balls_lines)
                self.selected = None
            else:
                self.selected = current
        elif isinstance(current, Ball):
            self.selected = current


def solution(
    field: list[list[str]],
    clicks: list[list[int, int]],
    new_balls: list[str],
    new_balls_coords: list[list[int, int]],
) -> int:
    game = LineGame(field)
    game.set_ball_generator(new_balls, new_balls_coords)

    for coord in clicks:
        game.click(coord)

    return game.score


def main():
    field = [
        ["V", ".", ".", ".", "O", ".", ".", ".", "O"],
        ["V", "O", ".", ".", "O", ".", ".", "O", "V"],
        ["V", ".", "O", ".", "O", ".", "O", ".", "."],
        ["V", ".", ".", "O", "O", "O", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "O"],
        ["V", ".", ".", "O", "O", "O", ".", ".", "."],
        ["V", ".", "O", ".", "O", ".", "O", ".", "."],
        ["V", "O", ".", ".", "O", ".", ".", "O", "."],
        ["V", ".", ".", ".", "O", ".", ".", ".", "O"],
    ]
    clicks = [[4, 8], [4, 4], [1, 8], [4, 0]]
    new_balls = []
    new_balls_coords = []
    # expected = 36
    print(solution(field, clicks, new_balls, new_balls_coords))


if __name__ == "__main__":
    main()
