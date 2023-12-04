#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Volleyball Positions

You are watching a volleyball tournament, but you missed the beginning of the
very first game of your favorite team. Now you're curious about how the coach
arranged the players on the field at the start of the game.

The team you favor plays in the following formation:

0 3 0
4 0 2
0 6 0
5 0 1

where positive numbers represent positions occupied by players. After the team
gains the serve, its members rotate one position in a clockwise direction, so
the player in position 2 moves to position 1, the player in position 3 moves to
position 2, and so on, with the player in position 1 moving to position 6.

Here's how the players change their positions:

https://codesignal.s3.amazonaws.com/uploads/1664318503/example.png?raw=true

Given the current formation of the team and the number of times k it gained the
serve, find the initial position of each player in it.

Example

    For

    formation = [["empty",   "Player5", "empty"],
                 ["Player4", "empty",   "Player2"],
                 ["empty",   "Player3", "empty"],
                 ["Player6", "empty",   "Player1"]]

    and k = 2, the output should be

    solution(formation, k) = [
        ["empty",   "Player1", "empty"],
        ["Player2", "empty",   "Player3"],
        ["empty",   "Player4", "empty"],
        ["Player5", "empty",   "Player6"]
    ]

    For

    formation = [["empty", "Alice", "empty"],
                 ["Bob",   "empty", "Charlie"],
                 ["empty", "Dave",  "empty"],
                 ["Eve",   "empty", "Frank"]]

    and k = 6, the output should be

    solution(formation, k) = [
        ["empty", "Alice", "empty"],
        ["Bob",   "empty", "Charlie"],
        ["empty", "Dave",  "empty"],
        ["Eve",   "empty", "Frank"]
    ]

array.array.string formation

Array of strings representing names of the players in the positions
corresponding to those in the schema above. It is guaranteed that for each empty
position the corresponding element of formation is "empty". It is also
guaranteed that there is no player called "empty" in the team.

Guaranteed constraints:
formation.length = 4,
formation[i].length = 3.

"""


def solution(formation: list[list[str]], k: int) -> int:
    ending_positions = []
    at_up = []
    for horizontal_idx in range(3):
        up = formation[0][horizontal_idx]
        down = formation[1][horizontal_idx]
        up_in_position = up != "empty"
        at_up.append(up_in_position)
        player_in_spot = up if up_in_position else down
        ending_positions.append(player_in_spot)

    for horizontal_idx in range(2, -1, -1):
        up = formation[2][horizontal_idx]
        down = formation[3][horizontal_idx]
        up_in_position = up != "empty"
        at_up.append(up_in_position)
        player_in_spot = up if up_in_position else down
        ending_positions.append(player_in_spot)

    shifts = k % 6
    starting_positions = ending_positions[shifts:] + ending_positions[:shifts]
    starting_formation = [["empty" for _ in range(3)] for _ in range(4)]
    for position_idx in range(3):
        inner_position = 0 if at_up[position_idx] else 1
        starting_formation[inner_position][position_idx] = starting_positions.pop(0)
    for position_idx in range(2, -1, -1):
        inner_position = 2 if at_up[position_idx] else 3
        starting_formation[inner_position][position_idx] = starting_positions.pop(0)
    return starting_formation


def main():
    formation = [
        ["empty", "Player5", "empty"],
        ["Player4", "empty", "Player2"],
        ["empty", "Player3", "empty"],
        ["Player6", "empty", "Player1"],
    ]
    k = 2
    # expected = [
    #     ["empty", "Player1", "empty"],
    #     ["Player2", "empty", "Player3"],
    #     ["empty", "Player4", "empty"],
    #     ["Player5", "empty", "Player6"],
    # ]
    print(solution(formation, k))


if __name__ == "__main__":
    main()
