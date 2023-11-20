#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You've mastered the Rubik's Cube and got bored solving it, so now you are
looking for a new challenge. One puzzle similar to the Rubik's Cube caught your
attention. It's called a Pyraminx puzzle, and is a triangular pyramid-shaped
puzzle. The parts are arranged in a pyramidal pattern on each side, while the
layers can be rotated with respect to each vertex, and the individual tips can
be rotated as well. There are 4 faces on the Pyraminx. The puzzle should be held
so that one face faces you and one face faces down, as in the image below. The
four corners are then labeled U (for up), R (for right), L (for left), and B
(for back). The front face thus contains the U, R, and L corners.

https://codesignal.s3.amazonaws.com/uploads/1658518006608/solution_notation.gif

Let's write down all possible moves for vertex U in the following notation:

* U - 120° counterclockwise turn of topmost tip (assuming that we're looking at
  the pyraminx from the top, and vertex U is the topmost);
* U' - clockwise turn for the same tip;
* u - 120° counterclockwise turn of two upper layer;
* u' - clockwise turn for the same layers.

https://codesignal.s3.amazonaws.com/uploads/1658518006600/solution_moves.png

For other vertices the moves can be described similarly:

The first puzzle you bought wasn't assembled, so you get your professional
pyraminx solver friend to assemble it. He does, and you wrote down all his moves
notated as described above. Now the puzzle's faces have colors faceColors[0]
(front face), faceColors[1] (bottom face), faceColors[2] (left face),
faceColors[3] (right face). You want to know the initial state of the puzzle to
repeat your friend's moves and see how he solved it.

Example

For faceColors = ['R', 'G', 'Y', 'O'] and moves = ["B", "b'", "u'", "R"], the
output should be

solution(faceColors, moves) = [['Y', 'Y', 'Y', 'Y', 'R', 'R', 'R', 'R', 'G'],
                               ['G', 'R', 'O', 'O', 'O', 'G', 'G', 'G', 'G'],
                               ['Y', 'O', 'Y', 'G', 'O', 'O', 'G', 'G', 'Y'],
                               ['R', 'O', 'O', 'R', 'O', 'Y', 'Y', 'R', 'R']]

Let's repeat the friend's steps in reverse order:

Final state:

https://codesignal.s3.amazonaws.com/uploads/1658518006504/solution_end.gif?raw=true

Before the last move:

https://codesignal.s3.amazonaws.com/uploads/1658518006510/solution_move1.gif?raw=true

One more move before that:

https://codesignal.s3.amazonaws.com/uploads/1658518006549/solution_move2.gif?raw=true

And one more:

https://codesignal.s3.amazonaws.com/uploads/1658518006561/solution_move3.gif?raw=true

Finally, the initial state:

https://codesignal.s3.amazonaws.com/uploads/1658518006576/solution_move4.gif?raw=true



Input/Output

[input] array.char faceColors

A distinct array of four distinct characters, representing the front, bottom,
left and right faces, respectively.

Guaranteed constraints:
faceColors.length = 4.

[input] array.string moves

Guaranteed constraints:
1 ≤ moves.length ≤ 100,

moves[i] ∈ {"U", "U'", "u", "u'", "L", "L'", "l", "l'",
            "R", "R'", "r", "r'", "B", "B'", "b", "b'"}.

[output] array.array.char

Initial state of the puzzle. result[0] should contain 9 characters corresponding
to the front face, result[1] - to the bottom face, result[2] - to the left face
and result[3] - to the right face.

The colors for each face should be given in top-to-bottom and left-to-right
order, starting from the marked vertex (i.e. U, B, L or R), assuming that this
vertex is at the top of the puzzle.


"""


class Pyraminx:
    base_rotations_lookup = {
        # fmt: off
        "u": [(0, 0), (0, 1), (0, 2), (0, 3)] + [(3, 8), (3, 3), (3, 7), (3, 6)] + [(2, 4), (2, 6), (2, 5), (2, 1)],
        "b": [(1, 0), (1, 1), (1, 2), (1, 3)] + [(2, 8), (2, 3), (2, 7), (2, 6)] + [(3, 4), (3, 6), (3, 5), (3, 1)],
        "l": [(2, 0), (2, 1), (2, 2), (2, 3)] + [(1, 8), (1, 3), (1, 7), (1, 6)] + [(0, 4), (0, 6), (0, 5), (0, 1)],
        "r": [(3, 0), (3, 1), (3, 2), (3, 3)] + [(0, 8), (0, 3), (0, 7), (0, 6)] + [(1, 4), (1, 6), (1, 5), (1, 1)],
    }
    source_coords: dict[str, list[tuple[int, int]]]
    rotations_lookup: dict[str, list[tuple[int, int]]]

    def __init__(self, face_colors: list[str]) -> None:
        self.faces = [[color] * 9 for color in face_colors]
        self.generate_turn_coords_from_base_rotations()

    def generate_turn_coords_from_base_rotations(self) -> None:
        self.rotations_lookup = {}
        self.source_coords = {}
        for turn_dir, coords in self.base_rotations_lookup.items():
            counterclock_target_coords = coords[4:] + coords[:4]
            clockwise_target_coords = coords[-4:] + coords[:-4]
            tip_clockwise_target_coords = [coords[8], coords[0], coords[4]]
            tip_counterclock_target_coords = [coords[4], coords[8], coords[0]]

            tip_source_coords = [coords[0], coords[4], coords[8]]
            self.source_coords[turn_dir] = coords
            self.source_coords[turn_dir.upper()] = tip_source_coords

            self.rotations_lookup[turn_dir] = counterclock_target_coords
            self.rotations_lookup[turn_dir + "'"] = clockwise_target_coords
            self.rotations_lookup[turn_dir.upper()] = tip_counterclock_target_coords
            self.rotations_lookup[turn_dir.upper() + "'"] = tip_clockwise_target_coords

    def invert_moves(self, moves: list[str]) -> list[str]:
        inverted_moves = []
        for move in reversed(moves):
            if move.endswith("'"):
                move = move[:-1]
            else:
                move += "'"
            inverted_moves.append(move)
        return inverted_moves

    def rotate(self, direction: str) -> None:
        sources = self.source_coords[direction[0]]
        targets = self.rotations_lookup[direction]

        source_colors = [self.faces[coord[0]][coord[1]] for coord in sources]
        for target, source_color in zip(targets, source_colors):
            self.faces[target[0]][target[1]] = source_color

    def print(self):
        U = self.faces[0]
        B = self.faces[1]
        L = self.faces[2]
        R = self.faces[3]

        if len(U[0]) == 1:
            print(f"\n    {L[4]}           {U[0]}           {R[8]}")
            print(
                f"  {L[6]} {L[5]} {L[1]}       {U[1]} {U[2]} {U[3]}       {R[3]} {R[7]} {R[6]}"
            )
            print(
                f"{L[8]} {L[7]} {L[3]} {L[2]} {L[0]}   {U[4]} {U[5]} {U[6]} {U[7]} {U[8]}   {R[0]} {R[2]} {R[1]} {R[5]} {R[4]}"
            )
            print(f"            {B[8]} {B[7]} {B[6]} {B[5]} {B[4]}")
            print(f"              {B[3]} {B[2]} {B[1]}")
            print(f"                {B[0]}\n")
        else:
            print(f"\n      {L[4]}               {U[0]}               {R[8]}")
            print(
                f"   {L[6]} {L[5]} {L[1]}         {U[1]} {U[2]} {U[3]}         {R[3]} {R[7]} {R[6]}"
            )
            print(
                f"{L[8]} {L[7]} {L[3]} {L[2]} {L[0]}   {U[4]} {U[5]} {U[6]} {U[7]} {U[8]}   {R[0]} {R[2]} {R[1]} {R[5]} {R[4]}"
            )
            print(f"                 {B[8]} {B[7]} {B[6]} {B[5]} {B[4]}")
            print(f"                    {B[3]} {B[2]} {B[1]}")
            print(f"                       {B[0]}\n")


def solution(face_colors: list[str], moves: list[str]) -> list[list[str]]:
    pyraminx = Pyraminx(face_colors)
    for inverted_move in pyraminx.invert_moves(moves):
        pyraminx.rotate(inverted_move)
    return pyraminx.faces


def main():
    face_colors = ["W", "A", "S", "D"]
    moves = ["l", "r'", "U'", "u", "r'", "B", "l'", "b'"]
    expected = [
        ["W", "W", "D", "A", "W", "W", "S", "A", "A"],
        ["A", "D", "D", "A", "D", "D", "D", "A", "A"],
        ["S", "S", "S", "S", "S", "W", "A", "A", "S"],
        ["W", "W", "W", "D", "D", "S", "W", "S", "D"],
    ]
    output = solution(face_colors, moves)

    print("--------------------")
    print("output vs expected")
    for out_line, exp_line in zip(output, expected):
        print(f"{out_line}\t\t{exp_line}")
    print()


if __name__ == "__main__":
    main()
