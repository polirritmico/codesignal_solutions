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
    def __init__(self, face_colors) -> None:
        self.faces = [[color for _ in range(9)] for color in face_colors]

    def rotate(self, direction: str) -> None:
        print(f"Direction: {direction}")

        if direction.upper() == "U":
            sources = [(0, 0), (3, 8), (2, 4)]
            targets = [(3, 8), (2, 4), (0, 0)]
        elif direction.upper() == "U'":
            sources = [(0, 0), (3, 8), (2, 4)]
            targets = [(2, 4), (0, 0), (3, 8)]

        elif direction.upper() == "B":
            sources = [(1, 0), (2, 8), (3, 4)]
            targets = [(2, 8), (3, 4), (1, 0)]
        elif direction.upper() == "B'":
            sources = [(1, 0), (2, 8), (3, 4)]
            targets = [(3, 4), (1, 0), (2, 8)]

        elif direction.upper() == "R":
            sources = [(3, 0), (0, 8), (1, 4)]
            targets = [(0, 8), (1, 4), (3, 0)]
        elif direction.upper() == "R'":
            sources = [(3, 0), (0, 8), (1, 4)]
            targets = [(1, 4), (3, 0), (0, 8)]

        elif direction.upper() == "L":
            sources = [(2, 0), (1, 8), (0, 4)]
            targets = [(1, 8), (0, 4), (2, 0)]
        elif direction.upper() == "L'":
            sources = [(2, 0), (1, 8), (0, 4)]
            targets = [(0, 4), (2, 0), (1, 8)]

        else:
            raise ValueError()

        # -------------------------------------------

        if direction == "u":
            # fmt: off
            sources += [(0, 1), (0, 2), (0, 3), (2, 6), (2, 5), (2, 1), (3, 3), (3, 7), (3, 6)]
            targets += [(3, 3), (3, 7), (3, 6), (0, 1), (0, 2), (0, 3), (2, 6), (2, 5), (2, 1)]
        elif direction == "u'":
            # fmt: off
            sources += [(0, 1), (0, 2), (0, 3), (2, 6), (2, 5), (2, 1), (3, 3), (3, 7), (3, 6)]
            targets += [(2, 6), (2, 5), (2, 1), (3, 3), (3, 7), (3, 6), (0, 1), (0, 2), (0, 3)]
        elif direction == "b":
            # fmt: off
            sources += [(1, 1), (1, 2), (1, 3), (2, 3), (2, 7), (2, 6), (3, 6), (3, 5), (3, 1)]
            targets += [(2, 3), (2, 7), (2, 6), (3, 6), (3, 5), (3, 1), (1, 1), (1, 2), (1, 3)]
        elif direction == "b'":
            # fmt: off
            sources += [(1, 1), (1, 2), (1, 3), (2, 3), (2, 7), (2, 6), (3, 6), (3, 5), (3, 1)]
            targets += [(3, 6), (3, 5), (3, 1), (1, 1), (1, 2), (1, 3), (2, 3), (2, 7), (2, 6)]
        elif direction == "l":
            # fmt: off
            sources += [(0, 6), (0, 5), (0, 1), (2, 1), (2, 2), (2, 3), (1, 3), (1, 7), (1, 6)]
            targets += [(2, 1), (2, 2), (2, 3), (1, 3), (1, 7), (1, 6), (0, 6), (0, 5), (0, 1)]
        elif direction == "l'":
            # fmt: off
            sources += [(0, 6), (0, 5), (0, 1), (2, 1), (2, 2), (2, 3), (1, 3), (1, 7), (1, 6)]
            targets += [(1, 3), (1, 7), (1, 6), (0, 6), (0, 5), (0, 1), (2, 1), (2, 2), (2, 3)]
        elif direction == "r":
            # fmt: off
            sources += [(3, 1), (3, 2), (3, 3), (1, 6), (1, 5), (1, 4), (0, 3), (0, 7), (0, 6)]
            targets += [(0, 3), (0, 7), (0, 6), (3, 1), (3, 2), (3, 3), (1, 6), (1, 5), (1, 1)]
        elif direction == "r'":
            # fmt: off
            sources += [(3, 1), (3, 2), (3, 3), (1, 6), (1, 5), (1, 4), (0, 3), (0, 7), (0, 6)]
            targets += [(1, 6), (1, 5), (1, 1), (0, 3), (0, 7), (0, 6), (3, 1), (3, 2), (3, 3)]

        self.apply_rotation(sources, targets)

    def apply_rotation(self, sources, targets):
        source_colors = [self.faces[source[0]][source[1]] for source in sources]
        for target, source_color in zip(targets, source_colors):
            self.faces[target[0]][target[1]] = source_color

    def print(self):
        U = self.faces[0]
        B = self.faces[1]
        L = self.faces[2]
        R = self.faces[3]

        print(f"      {L[4]}               {U[0]}               {R[8]}")
        print(
            f"   {L[6]} {L[5]} {L[1]}         {U[1]} {U[2]} {U[3]}         {R[3]} {R[7]} {R[6]}"
        )
        print(
            f"{L[8]} {L[7]} {L[3]} {L[2]} {L[0]}   {U[4]} {U[5]} {U[6]} {U[7]} {U[8]}   {R[0]} {R[2]} {R[1]} {R[5]} {R[4]}"
        )
        print(f"\n                 {B[8]} {B[7]} {B[6]} {B[5]} {B[4]}")
        print(f"                    {B[3]} {B[2]} {B[1]}")
        print(f"                       {B[0]}\n")

    def invert_moves(self, moves: list[str]) -> list[str]:
        output = []
        for move in reversed(moves):
            if move.endswith("'"):
                move = move[:-1]
            else:
                move += "'"
            output.append(move)
        return output


def solution(face_colors: list[str], moves: list[str]):
    pyraminx = Pyraminx(face_colors)
    moves = pyraminx.invert_moves(moves)
    pyraminx.print()
    for move in moves:
        pyraminx.rotate(move)
        pyraminx.print()
    print("----------------------")
    return pyraminx.faces


def main():
    pyraminx = Pyraminx(["a", "b", "c", "d"])
    faces = [
        [f"U{i}" for i in range(9)],
        [f"B{i}" for i in range(9)],
        [f"L{i}" for i in range(9)],
        [f"R{i}" for i in range(9)],
    ]
    pyraminx.faces = faces

    # moves = ["l", "r'", "U'", "u", "r'", "B", "l'", "b'"]
    moves = ["L"]
    # moves = pyraminx.invert_moves(moves)
    pyraminx.print()
    for move in moves:
        pyraminx.rotate(move)
        print("--------------------------------------------------")
        pyraminx.print()
    print("==================================================")
    return pyraminx.faces

    # face_colors = ["W", "A", "S", "D"]
    # moves = ["l", "r'", "U'", "u", "r'", "B", "l'", "b'"]
    # expected = [
    #     ["W", "W", "D", "A", "W", "W", "S", "A", "A"],
    #     ["A", "D", "D", "A", "D", "D", "D", "A", "A"],
    #     ["S", "S", "S", "S", "S", "W", "A", "A", "S"],
    #     ["W", "W", "W", "D", "D", "S", "W", "S", "D"],
    # ]
    # output = solution(face_colors, moves)

    # print("--------------------")
    # print("output vs expected")
    # for out_line, exp_line in zip(output, expected):
    #     print(f"{out_line}\t\t{exp_line}")
    # print()


if __name__ == "__main__":
    main()
