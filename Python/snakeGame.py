#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Snake Game

Your task is to imitate a turn-based variation of the popular "Snake" game.

https://codesignal.s3.amazonaws.com/uploads/1658518010310/solution_snake.gif

You are given the initial configuration of the board and a list of commands
which the snake follows one-by-one. The game ends if one of the following
happens:

    - the snake tries to eat its tail;
    - the snake tries to move out of the board;
    - it executes all the given commands.

Output the board configuration after the game ends.

Example

    For

gameBoard = [['.', '.', '.', '.'],
             ['.', '.', '<', '*'],
             ['.', '.', '.', '*']]

and commands = "FFFFFRFFRRLLF", the output should be

solution(gameBoard, commands) = [['.', '.', '.', '.'],
                                 ['X', 'X', 'X', '.'],
                                 ['.', '.', '.', '.']]

    For

gameBoard = [['.', '.', '^', '.', '.'],
             ['.', '.', '*', '*', '.'],
             ['.', '.', '.', '*', '*']]

and commands = "RFRF", the output should be

solution(gameBoard, commands) = [['.', '.', 'X', 'X', '.'],
                                 ['.', '.', 'X', 'X', '.'],
                                 ['.', '.', '.', 'X', '.']]

    For

gameBoard = [['.', '.', '*', '>', '.'],
             ['.', '*', '*', '.', '.'],
             ['.', '.', '.', '.', '.']]

and commands = "FRFFRFFRFLFF", the output should be

solution(gameBoard, commands) = [['.', '.', '.', '.', '.'],
                                 ['<', '*', '*', '.', '.'],
                                 ['.', '.', '*', '.', '.']]

Input/Output

[input] array.array.char gameBoard

A rectangular matrix of characters. It is guaranteed that it represents a
correct game board configuration, i.e. there is exactly one snake. Direction of
snake's head is depicted by one of the following characters ('^', '>', 'v',
'<'). All of the other snake's body parts are depicted by '*'s (note, that if
the snake has length 1 then there is no asterisks in its representation).
All cells which are not occupied by the snake are depicted by '.'s.

It is guaranteed that all snake cells are connected and no snake cell has more
than two neighbors.

[input] string commands

A list of commands, where 'F' means go one cell forward in the current
direction, 'L' and 'R' mean change current direction 90 degrees left
(counter-clockwise) or right (clockwise) correspondingly.

[output] array.array.char

Configuration of the board after the end of the game.

If the snake dies, output its state before the losing move and replace each of
the cells it occupied with Xs.


"""


class Snake:
    rotation_lockup: dict = {
        "^": {"L": "<", "R": ">"},
        ">": {"L": "^", "R": "v"},
        "v": {"L": ">", "R": "<"},
        "<": {"L": "v", "R": "^"},
    }

    def __init__(self, board: list[list[str]]) -> None:
        self.board = board
        self.has_collided = False
        self.rows = len(board)
        self.cols = len(board[0])
        for x, rows in enumerate(board):
            for y, character in enumerate(rows):
                if character in "><^v":
                    self.position = [x, y]
                    self.direction = character
                    break
        self.set_body_chain()

    def surround_filter(self, coord: list[int, int]) -> bool:
        return (
            coord is not None
            and self.board[coord[0]][coord[1]] != "."
            and coord not in self.body
        )

    def set_body_chain(self) -> None:
        current = self.position
        self.body = [current]
        while True:
            surroundings = [
                [current[0] - 1, current[1]] if current[0] - 1 >= 0 else None,
                [current[0] + 1, current[1]] if current[0] + 1 < self.rows else None,
                [current[0], current[1] - 1] if current[1] - 1 >= 0 else None,
                [current[0], current[1] + 1] if current[1] + 1 < self.cols else None,
            ]
            next_part = next(filter(self.surround_filter, surroundings), None)
            if next_part is not None:
                self.body.append(next_part)
                current = next_part
            else:
                return

    def export(self):
        if self.has_collided:
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.board[row][col] != ".":
                        self.board[row][col] = "X"
        return self.board

    def rotate_head(self, command: str) -> None:
        self.direction = self.rotation_lockup[self.direction][command]
        self.board[self.position[0]][self.position[1]] = self.direction

    def move(self) -> None:
        if self.direction == "<":
            next_position = (self.position[0], self.position[1] - 1)
        elif self.direction == ">":
            next_position = (self.position[0], self.position[1] + 1)
        elif self.direction == "v":
            next_position = (self.position[0] + 1, self.position[1])
        elif self.direction == "^":
            next_position = (self.position[0] - 1, self.position[1])

        self.has_collided = (
            next_position[0] < 0
            or next_position[0] >= self.rows
            or next_position[1] < 0
            or next_position[1] >= self.cols
            or self.board[next_position[0]][next_position[1]] == "*"
        )

        if not self.has_collided:
            if len(self.body) > 0:
                last_part = self.body.pop()
                self.board[last_part[0]][last_part[1]] = "."
            self.board[self.position[0]][self.position[1]] = "*"
            self.board[next_position[0]][next_position[1]] = self.direction
            self.body.insert(0, next_position)
            self.position = next_position


def solution(game_board: list[list[str]], commands: str) -> list[list[str]]:
    snake = Snake(game_board)
    for command in commands:
        if command == "F":
            snake.move()
            if snake.has_collided:
                break
        else:
            snake.rotate_head(command)

    return snake.export()


def main():
    game_board = [
        [".", ".", "*", ">", "."],
        [".", "*", "*", ".", "."],
        [".", ".", ".", ".", "."],
    ]
    commands = "FRFFRFFRFLFF"
    # expected = [
    #     [".", ".", ".", ".", "."],
    #     ["<", "*", "*", ".", "."],
    #     [".", ".", "*", ".", "."],
    # ]
    print(*solution(game_board, commands), sep="\n")


if __name__ == "__main__":
    main()
