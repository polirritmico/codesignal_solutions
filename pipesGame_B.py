#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Carlos always loved playing video games, especially the well-known computer game
"Pipes". Today he finally decided to write his own version of the legendary game
from scratch.

In this game the player has to place the pipes on a rectangular field to make
water pour from each source to a respective sink. He has already come up with
the entire program, but one question still bugs him: how can he best check that
the arrangement of pipes is correct?

It's your job to help him figure out exactly that.

Carlos has 7 types of pipes in his game, with numbers corresponding to each
type:

1 - vertical pipe
2 - horizontal pipe
3-6 - corner pipes: ╭, ╮, ╯, ╰
7 - two pipes crossed in the same cell (note that these pipes are not connected)

Here they are, pipes 1 to 7, respectively:

1: ║ 2: ═ 3: ╔ 4: ╗ 5: ╝ 6: ╚ 7: ╬

https://codesignal.s3.amazonaws.com/uploads/1664318504/pipe_types.png?raw=true

Water pours from each source in each direction that has a pipe connected to it
(thus it can even pour in all four directions). The puzzle is solved correctly
only if all water poured from each source eventually reaches a corresponding
sink.

Help Carlos check whether the arrangement of pipes is correct. If it is correct,
return the number of cells with pipes that will be full of water at the end of
the game. If not, return -X, where X is the number of cells with water before
the first leakage point is reached, or if the first drop of water reaches an
incorrect destination (whichever comes first). Assume that water moves from one
cell to another at the same speed.

Example

For

state = ["a224C22300000",
         "0001643722B00",
         "0b27275100000",
         "00c7256500000",
         "0006A45000000"]

the output should be solution(state) = 19.

Here is how the game will end:

https://codesignal.s3.amazonaws.com/uploads/1664318504/example.png?raw=true


Input/Output

[input] array.string state

Array of strings of an equal length representing some state of the game. The
pipes are represented by the numbers '1' to '7', the sources are given as
lowercase English letters, and the corresponding sinks are marked by uppercase
letters. Empty cells are marked with '0'.

It is guaranteed that each letter from the English alphabet either is not
present in state, or appears there twice (in uppercase and lowercase).

Guaranteed constraints:
1 ≤ state.length ≤ 100,
1 ≤ state[i].length ≤ 100,
state[i][j] ∈ {0-7, a-z, A-Z}.

[output] integer

If the pipe arrangement is correct, return the number of cells with pipes that
will be filled with water at the end of the game. If not, return -X, where X is
the number of cells with water before the first leakage point is reached, or if
the first drop of water reaches an incorrect destination.

"""
from typing import Optional, Self


class Pipe:
    avaliable_connections: list[str]
    connections: dict[str, Optional[Self]]
    coords: tuple[int]
    filled: bool
    pipe_type: str
    char_to_sockets_map: dict[str, list[str]] = {
        "1": ["↑", "↓"],  # ║
        "2": ["←", "→"],  # ═
        "3": ["→", "↓"],  # ╔
        "4": ["←", "↓"],  # ╗
        "5": ["↑", "←"],  # ╝
        "6": ["↑", "→"],  # ╚
        "+": ["↑", "→", "↓", "←"],  # ╬
    }
    compatible_sockets_map: dict[str, str] = {
        "→": "←",
        "←": "→",
        "↑": "↓",
        "↓": "↑",
    }

    def __str__(self):
        return str(f"{self.coords}: {self.pipe_type}")

    def __repr__(self):
        return str(f"{self.pipe_type}: {self.coords}")

    def __init__(self, x: int, y: int, pipe_type: str):
        self.connections = {}
        self.coords = (x, y)
        self.filled = False
        self.pipe_type = pipe_type
        if pipe_type.islower() or pipe_type.isupper():
            pipe_type = "+"
        elif pipe_type not in self.char_to_sockets_map:
            raise ValueError()
        self.avaliable_connections = self.char_to_sockets_map[pipe_type].copy()

    def set_connections(self, surroundings: dict[str, Self]) -> None:
        neighbor: Pipe
        for position, neighbor in surroundings.items():
            if position not in self.avaliable_connections:
                continue
            if isinstance(neighbor, list):
                neighbor = neighbor[0] if position in "↑↓" else neighbor[1]
            neighbor_connection = self.compatible_sockets_map[position]
            if neighbor_connection not in neighbor.avaliable_connections:
                continue
            self.connections[position] = neighbor
            self.avaliable_connections.remove(position)
            neighbor.connections[neighbor_connection] = self
            neighbor.avaliable_connections.remove(neighbor_connection)
        print(f"pipe_type: {self.pipe_type} connections: {self.connections}")

    def get_surroundings(self, grid: list[list[Self]]) -> dict[str, Self]:
        top = grid[self.coords[0] - 1][self.coords[1]]
        btm = grid[self.coords[0] + 1][self.coords[1]]
        right = grid[self.coords[0]][self.coords[1] + 1]
        left = grid[self.coords[0]][self.coords[1] - 1]
        surroundings = {}
        if top is not None:
            surroundings["↑"] = top
        if btm is not None:
            surroundings["↓"] = btm
        if right is not None:
            surroundings["→"] = right
        if left is not None:
            surroundings["←"] = left

        return surroundings

    def follow_connections(self, from_pipe: Self) -> Self:
        neighbor: Pipe
        for neighbor in self.connections:
            if neighbor is from_pipe:
                continue
            print(self.coords)
            yield (neighbor.follow_connections(self))


class Circuit:
    def __init__(self, source: Pipe = None, target: Pipe = None):
        self.is_closed: bool = False
        self.source: Pipe = source
        self.size: int = 0
        self.target: Pipe = target

    def connect_circuit(self, grid: list[list[Self]]) -> None:
        self.source.set_connections(self.source.get_surroundings(grid))
        print(self.source.connections)
        neighborn: Pipe
        # TODO: Recursive function to connect all the circuit
        for neighborn in self.source.connections.values():
            neighborn.follow_connections(self.source)


def construct_grid(grid_str: list[str], circuits: dict[Circuit]) -> list[list[Pipe]]:
    rows = len(grid_str)
    cols = len(grid_str[0])
    grid = [[None for _ in range(cols + 2)] for _ in range(rows + 2)]
    for row in range(rows):
        for col in range(cols):
            current = grid_str[row][col]
            if current == "0":
                continue
            elif current == "7":
                new_pipe = [Pipe(row + 1, col + 1, "1"), Pipe(row + 1, col + 1, "2")]
            else:
                new_pipe = Pipe(row + 1, col + 1, current)
            if current.islower():
                if current in circuits:
                    circuits[current].source = new_pipe
                else:
                    circuits[current] = Circuit(source=new_pipe)
            elif current.isupper():
                current = current.lower()
                if current in circuits:
                    circuits[current].target = new_pipe
                else:
                    circuits[current] = Circuit(target=new_pipe)
            grid[row + 1][col + 1] = new_pipe
    return grid


def solution(state: list[str]) -> int:
    water_circuits: dict[Circuit] = {}
    grid: list[list[Pipe]] = construct_grid(state, water_circuits)
    print(*grid, sep="\n")
    print()
    circuit: Circuit
    for circuit in water_circuits.values():
        circuit.connect_circuit(grid)


def main():
    case = [
        "a222A",
    ]
    # case = [
    #     "a224C22300000",
    #     "0001643722B00",
    #     "0b27275100000",
    #     "00c7256500000",
    #     "0006A45000000",
    # ]
    # expected = 19
    print(solution(case))


if __name__ == "__main__":
    main()
