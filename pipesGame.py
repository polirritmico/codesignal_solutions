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
        self.avaliable_sockets = self.char_to_sockets_map[pipe_type].copy()

    def get_surroundings(self, grid: list[list[Self]]) -> dict[str, Self | None]:
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

    def connect_surroundings(self, grid: list[list[Self]]) -> dict[str, Self]:
        target_pipe: Pipe
        for self_socket, target_pipe in self.get_surroundings(grid).items():
            if self_socket not in self.avaliable_sockets:
                continue
            target_socket = self.compatible_sockets_map[self_socket]
            if isinstance(target_pipe, list):
                target_pipe = target_pipe[0] if self_socket in "↑↓" else target_pipe[1]
            if self.pipe_type.islower() and target_pipe.pipe_type.islower():
                continue
            if target_socket not in target_pipe.avaliable_sockets:
                continue
            self.connections[self_socket] = target_pipe
            target_pipe.connections[target_socket] = self
            self.avaliable_sockets.remove(self_socket)
            target_pipe.avaliable_sockets.remove(target_socket)

    def next_pipe(self, source: Self) -> Optional[Self]:
        for pipe in self.connections.values():
            if pipe is not source:
                return pipe
        return None


class Circuit:
    counted_double_layer: list = []

    def __init__(self, source: Pipe = None, target: Pipe = None):
        self.grid: list[list[Pipe]]
        self.paths_closed: dict[str, bool] = {}
        self.size: int = 0
        self.source: Pipe = source
        self.target: Pipe = target

    def connect_circuit(self) -> None:
        for water_source_path, source_connection in self.source.connections.items():
            source_pipe: Pipe = self.source
            current_pipe: Pipe = source_connection
            next_pipe: Pipe
            while True:
                if current_pipe is None:
                    self.paths_closed[water_source_path] = False
                    break
                elif current_pipe is self.target:
                    self.paths_closed[water_source_path] = True
                    break
                current_pipe.connect_surroundings(self.grid)
                next_pipe = current_pipe.next_pipe(source_pipe)
                source_pipe = current_pipe
                current_pipe = next_pipe

    def connect_source_surroundings(self) -> None:
        self.source.connect_surroundings(self.grid)

    def is_closed(self) -> bool:
        return all(self.paths_closed.values())

    def is_double_layer_pipe(self, pipe: Pipe) -> bool:
        return isinstance(self.grid[pipe.coords[0]][pipe.coords[1]], list)

    def closed_circuit_filled_counter(self) -> int:
        count = 0
        for water_source_path, source_connection in self.source.connections.items():
            source_pipe: Pipe = self.source
            current_pipe: Pipe = source_connection
            while True:
                if current_pipe is None or current_pipe is self.target:
                    break
                if self.is_double_layer_pipe(current_pipe):
                    if current_pipe.coords not in self.counted_double_layer:
                        self.counted_double_layer.append(current_pipe.coords)
                        count += 1
                else:
                    count += 1
                next_pipe = current_pipe.next_pipe(source_pipe)
                source_pipe = current_pipe
                current_pipe = next_pipe
        return count

    def open_circuit_filled_counter(self) -> dict[str, int]:
        circuit_counts = []
        count = 0
        for water_source_path, source_connection in self.source.connections.items():
            source_pipe: Pipe = self.source
            current_pipe: Pipe = source_connection
            while True:
                if current_pipe is None or current_pipe is self.target:
                    break
                if self.is_double_layer_pipe(current_pipe):
                    if current_pipe.coords not in self.counted_double_layer:
                        self.counted_double_layer.append(current_pipe.coords)
                        count += 1
                else:
                    count += 1
                next_pipe = current_pipe.next_pipe(source_pipe)
                source_pipe = current_pipe
                current_pipe = next_pipe
            circuit_counts.append(count)
            count = 0
        return circuit_counts


def generate_circuits(raw_grid: list[str]) -> dict[str, Circuit]:
    rows = len(raw_grid)
    cols = len(raw_grid[0])
    grid = [[None for _ in range(cols + 2)] for _ in range(rows + 2)]
    water_circuits: dict[str, Circuit] = {}
    for row in range(rows):
        for col in range(cols):
            current = raw_grid[row][col]
            if current == "0":
                continue
            elif current == "7":
                new_pipe = [Pipe(row + 1, col + 1, "1"), Pipe(row + 1, col + 1, "2")]
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
    return water_circuits.values()


def solution(raw_grid: list[str]) -> int:
    water_circuits: list[Circuit] = generate_circuits(raw_grid)
    circuit: Circuit
    for circuit in water_circuits:
        circuit.connect_source_surroundings()
        circuit.connect_circuit()
    correct_solution = all([circuit.is_closed() for circuit in water_circuits])
    if correct_solution:
        return sum(map(lambda wc: wc.closed_circuit_filled_counter(), water_circuits))
    else:
        # TODO: this function should get the first leaked time, not the min
        filled = [circuit.open_circuit_filled_counter() for circuit in water_circuits]
        filled = [count for sublist in filled for count in sublist]
        print(filled)
        output = (min(filled) + 1) * len(filled)
        return -output


def main():
    # 1: ║ 2: ═ 3: ╔ 4: ╗ 5: ╝ 6: ╚ 7: ╬
    case = [
        "a22A00",
        "z2220Z",
    ]
    # a: 10, 10 leak
    # z: 10, 8, 12
    # expected = -48
    print(solution(case))


if __name__ == "__main__":
    main()
