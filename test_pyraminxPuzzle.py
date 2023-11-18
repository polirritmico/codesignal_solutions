#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# from pyraminxPuzzle import Pyraminx, solution
from pyraminxPuzzle import solution


@unittest.skip
class TestCustom(unittest.TestCase):
    # def setUp(self):
    #     self.pyraminx = Pyraminx(["R", "G", "Y", "O"])

    # @unittest.skip
    def test_coords(self):
        move = "U"
        faces = [
            [f"U{i}" for i in range(9)],
            [f"B{i}" for i in range(9)],
            [f"L{i}" for i in range(9)],
            [f"R{i}" for i in range(9)],
        ]

    # @unittest.skip
    def test_example_move_U(self):
        move = "U"
        expected = [
            ["Y", "R", "R", "R", "R", "R", "R", "R", "R"],
            ["G", "G", "G", "G", "G", "G", "G", "G", "G"],
            ["Y", "Y", "Y", "Y", "O", "Y", "Y", "Y", "Y"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "R"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_example_move_U_delta(self):
        move = "U'"
        expected = [
            ["O", "R", "R", "R", "R", "R", "R", "R", "R"],
            ["G", "G", "G", "G", "G", "G", "G", "G", "G"],
            ["Y", "Y", "Y", "Y", "R", "Y", "Y", "Y", "Y"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "Y"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_example_move_B(self):
        move = "B"
        expected = [
            ["R", "R", "R", "R", "R", "R", "R", "R", "R"],
            ["O", "G", "G", "G", "G", "G", "G", "G", "G"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "G"],
            ["O", "O", "O", "O", "Y", "O", "O", "O", "O"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_example_move_B_delta(self):
        move = "B'"
        expected = [
            ["R", "R", "R", "R", "R", "R", "R", "R", "R"],
            ["Y", "G", "G", "G", "G", "G", "G", "G", "G"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "O"],
            ["O", "O", "O", "O", "G", "O", "O", "O", "O"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_example_move_R(self):
        move = "R"
        expected = [
            ["R", "R", "R", "R", "R", "R", "R", "R", "O"],
            ["G", "G", "G", "G", "R", "G", "G", "G", "G"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["G", "O", "O", "O", "O", "O", "O", "O", "O"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_example_move_R_delta(self):
        move = "R'"
        expected = [
            ["R", "R", "R", "R", "R", "R", "R", "R", "G"],
            ["G", "G", "G", "G", "O", "G", "G", "G", "G"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["R", "O", "O", "O", "O", "O", "O", "O", "O"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_example_move_L(self):
        move = "L"
        expected = [
            ["R", "R", "R", "R", "G", "R", "R", "R", "R"],
            ["G", "G", "G", "G", "G", "G", "G", "G", "Y"],
            ["R", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_example_move_L_delta(self):
        move = "L'"
        expected = [
            ["R", "R", "R", "R", "Y", "R", "R", "R", "R"],
            ["G", "G", "G", "G", "G", "G", "G", "G", "R"],
            ["G", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_example_move_u(self):
        move = "u"
        expected = [
            ["Y", "Y", "Y", "Y", "R", "R", "R", "R", "R"],
            ["G", "G", "G", "G", "G", "G", "G", "G", "G"],
            ["Y", "O", "Y", "Y", "O", "O", "O", "Y", "Y"],
            ["O", "O", "O", "R", "O", "O", "R", "R", "R"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_example_move_u_delta(self):
        move = "u'"
        expected = [
            ["O", "O", "O", "O", "R", "R", "R", "R", "R"],
            ["G", "G", "G", "G", "G", "G", "G", "G", "G"],
            ["Y", "R", "Y", "Y", "R", "R", "R", "Y", "Y"],
            ["O", "O", "O", "Y", "O", "O", "Y", "Y", "Y"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.assertListEqual(output, expected)
        # expected = [
        #     ["R", "R", "R", "R", "R", "R", "R", "R", "R"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G"],
        #     ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
        #     ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
        # ]

    # @unittest.skip
    def test_example_move_l(self):
        move = "l"
        expected = [
            ["R", "G", "R", "R", "G", "G", "G", "R", "R"],
            ["G", "G", "G", "Y", "G", "G", "Y", "Y", "Y"],
            ["R", "R", "R", "R", "Y", "Y", "Y", "Y", "Y"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.pyraminx.print()
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_example_move_l_delta(self):
        move = "l'"
        expected = [
            ["R", "Y", "R", "R", "Y", "Y", "Y", "R", "R"],
            ["G", "G", "G", "R", "G", "G", "R", "R", "R"],
            ["G", "G", "G", "G", "Y", "Y", "Y", "Y", "Y"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ]
        self.pyraminx.rotate(move)
        output = self.pyraminx.faces
        self.pyraminx.print()
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_invert_moves(self):
        moves = ["B", "b'", "u'", "R"]
        expected = ["R'", "u", "b", "B'"]

        output = self.pyraminx.invert_moves(moves)
        self.assertEqual(output, expected)


# @unittest.skip
class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        face_colors = ["R", "G", "Y", "O"]
        moves = ["B", "b'", "u'", "R"]
        expected = [
            ["Y", "Y", "Y", "Y", "R", "R", "R", "R", "G"],
            ["G", "R", "O", "O", "O", "G", "G", "G", "G"],
            ["Y", "O", "Y", "G", "O", "O", "G", "G", "Y"],
            ["R", "O", "O", "R", "O", "Y", "Y", "R", "R"],
        ]
        output = solution(face_colors, moves)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        face_colors = ["R", "G", "Y", "O"]
        moves = ["l", "l'"]
        expected = [
            ["R", "R", "R", "R", "R", "R", "R", "R", "R"],
            ["G", "G", "G", "G", "G", "G", "G", "G", "G"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ]
        output = solution(face_colors, moves)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        face_colors = ["R", "G", "Y", "O"]
        moves = ["l", "l'", "u", "R", "U'", "L", "R'", "u'", "l'", "L'", "r"]
        expected = [
            ["Y", "O", "R", "G", "G", "G", "G", "G", "G"],
            ["G", "O", "G", "Y", "O", "O", "Y", "Y", "Y"],
            ["R", "G", "R", "R", "O", "Y", "Y", "Y", "Y"],
            ["R", "R", "R", "R", "O", "O", "O", "O", "R"],
        ]
        output = solution(face_colors, moves)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        face_colors = ["R", "G", "Y", "O"]
        moves = ["r"]
        expected = [
            ["R", "R", "R", "G", "R", "R", "G", "G", "G"],
            ["G", "O", "G", "G", "O", "O", "O", "G", "G"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
            ["R", "R", "R", "R", "O", "O", "O", "O", "O"],
        ]
        output = solution(face_colors, moves)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        face_colors = ["A", "B", "C", "D"]
        moves = [
            "l",
            "l'",
            "r'",
            "r",
            "u",
            "U",
            "u'",
            "R'",
            "L",
            "R",
            "L'",
            "B'",
            "U'",
            "b",
            "B",
            "b'",
        ]
        expected = [
            ["A", "A", "A", "A", "A", "A", "A", "A", "A"],
            ["B", "B", "B", "B", "B", "B", "B", "B", "B"],
            ["C", "C", "C", "C", "C", "C", "C", "C", "C"],
            ["D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ]
        output = solution(face_colors, moves)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        face_colors = ["R", "G", "Y", "E"]
        moves = ["b", "l", "r", "u"]
        expected = [
            ["E", "Y", "E", "G", "Y", "Y", "R", "G", "G"],
            ["Y", "E", "Y", "R", "E", "E", "E", "R", "R"],
            ["G", "G", "G", "Y", "R", "R", "E", "E", "E"],
            ["R", "G", "R", "R", "G", "G", "Y", "Y", "Y"],
        ]
        output = solution(face_colors, moves)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        face_colors = ["R", "U", "L", "E"]
        moves = ["U", "B", "R", "L"]
        expected = [
            ["E", "R", "R", "R", "L", "R", "R", "R", "U"],
            ["L", "U", "U", "U", "E", "U", "U", "U", "R"],
            ["U", "L", "L", "L", "R", "L", "L", "L", "E"],
            ["R", "E", "E", "E", "U", "E", "E", "E", "L"],
        ]
        output = solution(face_colors, moves)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        face_colors = ["W", "A", "S", "D"]
        moves = ["l", "r'", "U'", "u", "r'", "B", "l'", "b'"]
        expected = [
            ["W", "W", "D", "A", "W", "W", "S", "A", "A"],
            ["A", "D", "D", "A", "D", "D", "D", "A", "A"],
            ["S", "S", "S", "S", "S", "W", "A", "A", "S"],
            ["W", "W", "W", "D", "D", "S", "W", "S", "D"],
        ]
        output = solution(face_colors, moves)
        self.assertListEqual(output, expected)

    @unittest.skip
    def test_case9(self):
        face_colors = ["W", "A", "S", "D"]
        moves = [
            "B'",
            "R'",
            "L",
            "U'",
            "B",
            "r'",
            "l",
            "B'",
            "L'",
            "r'",
            "L",
            "U",
            "u'",
            "U",
            "B'",
            "r",
            "L'",
            "R",
            "B",
            "r",
            "R'",
            "R",
            "U'",
            "U",
            "L",
            "r",
            "L",
            "B'",
            "U",
            "B",
            "R",
            "R'",
            "R",
            "u'",
            "l",
            "R'",
            "R",
            "B",
            "R'",
            "U",
            "u",
            "U",
            "u'",
            "B'",
            "r",
            "L'",
            "B'",
            "R'",
            "B'",
            "r",
            "R'",
            "r",
            "L",
            "R'",
            "B",
            "u",
            "B'",
            "B",
            "L",
            "U",
            "B",
            "B",
            "L",
            "R",
            "B",
            "R",
            "u'",
            "R'",
            "B",
            "u",
            "u'",
            "L'",
            "B",
            "R'",
            "l'",
            "U",
            "U'",
            "B",
            "r",
            "L'",
            "B",
            "r'",
            "U",
            "R",
            "R'",
            "u'",
            "r",
            "R'",
            "u'",
            "r'",
            "L'",
            "R'",
            "r'",
            "U",
            "u'",
            "B'",
            "U",
            "L'",
            "L'",
            "B",
        ]
        expected = [
            ["W", "S", "D", "S", "W", "S", "S", "W", "A"],
            ["D", "W", "A", "A", "D", "A", "D", "W", "A"],
            ["S", "A", "A", "D", "S", "W", "W", "S", "A"],
            ["W", "D", "D", "W", "S", "D", "A", "S", "D"],
        ]
        output = solution(face_colors, moves)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        face_colors = ["W", "A", "S", "D"]
        moves = [
            "L",
            "L",
            "L",
            "r'",
            "r'",
            "r'",
            "U",
            "U'",
            "U",
            "U'",
            "b",
            "b'",
            "b'",
            "b",
        ]
        expected = [
            ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["A", "A", "A", "A", "A", "A", "A", "A", "A"],
            ["S", "S", "S", "S", "S", "S", "S", "S", "S"],
            ["D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ]
        output = solution(face_colors, moves)
        self.assertListEqual(output, expected)
