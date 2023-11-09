#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1: ║ 2: ═ 3: ╔ 4: ╗ 5: ╝ 6: ╚ 7: ╬
sources: a, b, c, etc.
targets: A, B, C, etc.

Water pours from each source in each direction that has a pipe connected to it
(thus it can even pour in all four directions). The puzzle is solved correctly
only if ALL water poured from each source eventually reaches a corresponding
sink.

Help Carlos check whether the arrangement of pipes is correct. If it is correct,
return the number of cells with pipes that will be full of water at the end of
the game. If not, return -X, where X is the number of cells with water before
the first leakage point is reached, or if the first drop of water reaches an
incorrect destination (whichever comes first). Assume that water moves from one
cell to another at the same speed.

[output] integer

If the pipe arrangement is correct, return the number of cells with pipes that
will be filled with water at the end of the game. If not, return -X, where X is
the number of cells with water before the first leakage point is reached, or if
the first drop of water reaches an incorrect destination.

"""

from typing import Optional, Self


class Pipe:
    avaliable_sockets: list[str]
    connections: dict[str, Self]
    coords: tuple[int, int]
    pipe_type: str
    water_source: Self
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
        return str(f"{self.pipe_type}: {self.coords}")

    def __init__(self, x: int, y: int, pipe_type: str):
        self.connections = {}
        self.coords = (x, y)
        self.pipe_type = pipe_type
        if pipe_type.islower() or pipe_type.isupper():
            pipe_type = "+"
        self.avaliable_sockets = self.char_to_sockets_map[pipe_type].copy()
        self.water_source = None

    def get_surroundings(self, grid: list) -> dict[str, Self | None]:
        top = grid[self.coords[0] - 1][self.coords[1]]
        btm = grid[self.coords[0] + 1][self.coords[1]]
        left = grid[self.coords[0]][self.coords[1] - 1]
        right = grid[self.coords[0]][self.coords[1] + 1]
        surroundings = {}
        if top is not None:
            surroundings["↑"] = top
        if btm is not None:
            surroundings["↓"] = btm
        if left is not None:
            surroundings["←"] = left
        if right is not None:
            surroundings["→"] = right
        return surroundings

    def connect_surroundings(self, grid: list) -> dict[str, Self]:
        target_pipe: Pipe
        for self_socket, target_pipe in self.get_surroundings(grid).items():
            if self_socket not in self.avaliable_sockets:
                continue
            if isinstance(target_pipe, list):
                target_pipe = target_pipe[0] if self_socket in "↑↓" else target_pipe[1]
            if self.pipe_type.isalpha() and target_pipe.pipe_type.isalpha():
                continue
            target_socket = self.compatible_sockets_map[self_socket]
            if target_socket not in target_pipe.avaliable_sockets:
                continue
            self.connections[self_socket] = target_pipe
            target_pipe.connections[target_socket] = self
            target_pipe.water_source = self
            self.avaliable_sockets.remove(self_socket)
            target_pipe.avaliable_sockets.remove(target_socket)

    def next_pipe(self) -> Optional[Self]:
        for pipe in self.connections.values():
            if pipe is not self.water_source:
                return pipe
        return None


class Circuit:
    counted_register: list[list[Pipe]]

    def __init__(self, source: Pipe = None, target: Pipe = None):
        self.grid: list[list[Pipe]]
        self.path_current_pipe: dict[str, Pipe] = {}
        self.path_leaking_state: dict[str, bool] = {}
        self.source: Pipe = source
        self.target: Pipe = target

    def is_leaking(self) -> bool:
        return any(leaking for leaking in self.path_leaking_state.values())

    def open_water_source(self) -> None:
        self.source.connect_surroundings(self.grid)
        for path, pipe in self.source.connections.items():
            self.path_current_pipe[path] = pipe
            self.path_leaking_state[path] = False

    def not_counted_pipe(self, coords: tuple[int, int]) -> bool:
        return not Circuit.counted_register[coords[0]][coords[1]]

    def fill_one_level(self) -> int:
        filled_pipes_in_all_circuit_paths = 0
        paths_that_reached_their_target = []
        for path, pipe in self.path_current_pipe.items():
            assert pipe is not None, "fill_one_level should have stop earlier"
            if pipe is self.target:
                paths_that_reached_their_target.append(path)
                continue
            if self.not_counted_pipe(pipe.coords):
                filled_pipes_in_all_circuit_paths += 1
                Circuit.counted_register[pipe.coords[0]][pipe.coords[1]] = True
            pipe.connect_surroundings(self.grid)
            next_pipe: Pipe = pipe.next_pipe()
            if next_pipe is None:
                self.path_leaking_state[path] = True
            else:
                next_pipe.water_source = pipe
            self.path_current_pipe[path] = next_pipe

        for path in paths_that_reached_their_target:
            del self.path_current_pipe[path]
        return filled_pipes_in_all_circuit_paths

    @classmethod
    def get_circuits(cls, raw_grid: list[str]) -> list[Self]:
        rows = len(raw_grid)
        cols = len(raw_grid[0])
        # +2 adds a frame arround the grid to avoid border checkings. +1 to coords.
        grid = [[None for _ in range(cols + 2)] for _ in range(rows + 2)]
        water_circuits: dict[str, Circuit] = {}
        for row in range(rows):
            for col in range(cols):
                current = raw_grid[row][col]
                if current == "0":
                    continue
                elif current == "7":
                    new_pipe = [
                        Pipe(row + 1, col + 1, "1"),
                        Pipe(row + 1, col + 1, "2"),
                    ]
                else:
                    new_pipe = Pipe(row + 1, col + 1, current)

                if current.islower():
                    if current in water_circuits:
                        water_circuits[current].source = new_pipe
                    else:
                        water_circuits[current] = Circuit(source=new_pipe)
                elif current.isupper():
                    current = current.lower()
                    if current in water_circuits:
                        water_circuits[current].target = new_pipe
                    else:
                        water_circuits[current] = Circuit(target=new_pipe)
                grid[row + 1][col + 1] = new_pipe

        for circuit in water_circuits.values():
            circuit.grid = grid
        Circuit.counted_register = [
            [None for _ in range(cols + 2)] for _ in range(rows + 2)
        ]
        return list(water_circuits.values())


def solution(raw_grid: list[str]) -> int:
    water_circuits: list[Circuit] = Circuit.get_circuits(raw_grid)
    circuit: Circuit
    for circuit in water_circuits:
        circuit.open_water_source()

    total_filled_pipes = 0
    leaking_circuit = False
    while not leaking_circuit and len(water_circuits) > 0:
        for circuit in water_circuits:
            total_filled_pipes += circuit.fill_one_level()
            if len(circuit.path_current_pipe) == 0:
                water_circuits.remove(circuit)
        leaking_circuit = any(circuit.is_leaking() for circuit in water_circuits)

    return total_filled_pipes * -1 if leaking_circuit else total_filled_pipes


def main():
    # 1: ║ 2: ═ 3: ╔ 4: ╗ 5: ╝ 6: ╚ 7: ╬
    case = [
        "a010",
        "C01A",
        "101b",
        "101B",
        "c250",
    ]
    # a: 0 -> no connection
    # b: 0 -> no connection
    # c: 8 -> leak
    # expected = -8
    print(solution(case))


if __name__ == "__main__":
    main()
