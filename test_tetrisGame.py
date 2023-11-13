#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from tetrisGame import Piece, Tetris, solution


class TestCustom(unittest.TestCase):
    # @unittest.skip
    def test_rotate1(self):
        case = [["#"], ["#"], ["#"], ["#"]]
        expected = [["#", "#", "#", "#"]]
        piece = Piece(case)
        piece.rotate_clockwise()
        output = piece.shape
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_rotate2(self):
        case = [["#", "#"], ["#", "#"]]
        expected = [["#", "#"], ["#", "#"]]
        piece = Piece(case)
        piece.rotate_clockwise()
        output = piece.shape
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_rotate3(self):
        case = [
            [".", "#", "."],
            ["#", "#", "#"],
        ]
        expected = [
            ["#", "."],
            ["#", "#"],
            ["#", "."],
        ]
        piece = Piece(case)
        piece.rotate_clockwise()
        output = piece.shape
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_rotate3x2(self):
        case = [
            [".", "#", "."],
            ["#", "#", "#"],
        ]
        expected = [
            ["#", "#", "#"],
            [".", "#", "."],
        ]
        piece = Piece(case)
        piece.rotate_clockwise()
        piece.rotate_clockwise()
        self.assertListEqual(piece.shape, expected)

        expected = [
            ["#", "#", "#"],
            [".", "#", "."],
        ]
        output = piece.shape
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_remove_line(self):
        field = [
            ["0", ".", ".", "."],
            ["1", ".", "#", "#"],
            ["2", "#", "#", "#"],
            ["3", ".", "#", "#"],
        ]
        expected = [
            [".", ".", ".", "."],
            ["0", ".", ".", "."],
            ["1", ".", "#", "#"],
            ["3", ".", "#", "#"],
        ]
        tetris = Tetris(4, 4)
        tetris.field = field
        tetris.remove_line(2)

        self.assertListEqual(tetris.field, expected)

    # @unittest.skip
    def test_filled_lines_counter(self):
        case = [
            [".", ".", ".", "."],
            ["#", "#", "#", "#"],
            ["#", ".", ".", "."],
            [".", "#", ".", "."],
            ["#", "#", "#", "#"],
            ["#", "#", "#", "."],
        ]
        tetris = Tetris(6, 4)
        tetris.field = case
        expected = [1, 4]

        output = tetris.get_filled_lines()
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_drop_piece(self):
        piece_shape = [
            ["#", "#", "#"],
            [".", "#", "."],
        ]
        field = [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", "#", ".", "."],
        ]
        expected = [
            [".", ".", ".", "."],
            ["#", "#", "#", "."],
            [".", "#", ".", "."],
            [".", "#", ".", "."],
        ]
        piece = Piece(piece_shape)
        tetris = Tetris(4, 4)
        tetris.field = field
        tetris.drop_piece(piece)
        self.assertListEqual(tetris.field, expected)

    # @unittest.skip
    def test_drop_piece2(self):
        piece_shape = [
            ["#", "#", "#"],
            [".", "#", "."],
        ]
        field = [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", "#", ".", "."],
        ]
        expected = [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", "#", "#", "#"],
            [".", "#", "#", "."],
        ]
        piece = Piece(piece_shape)
        piece.coord[1] = 1
        tetris = Tetris(4, 4)
        tetris.field = field
        tetris.drop_piece(piece)
        self.assertListEqual(tetris.field, expected)

    # @unittest.skip
    def test_drop_piece_with_obstacle(self):
        piece_shape = [
            ["#", "#", "#"],
            [".", "#", "."],
        ]
        field = [
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."],
            [".", "#", "#", ".", "."],
            ["#", "#", ".", ".", "."],
        ]
        expected = [
            [".", ".", ".", ".", "."],
            [".", ".", "#", "#", "#"],
            [".", "#", "#", "#", "."],
            ["#", "#", ".", ".", "."],
        ]
        piece = Piece(piece_shape)
        piece.coord[1] = 2
        tetris = Tetris(4, 5)
        tetris.field = field
        tetris.drop_piece(piece)
        self.assertListEqual(tetris.field, expected)


# @unittest.skip
class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", ".", "."], ["#", "#", "#"]],
            [["#", "#", "."], [".", "#", "#"]],
            [["#", "#", "#", "#"]],
            [["#", "#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
        ]
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
        ]
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [
            [["#", "#", "#", "#"]],
            [["#", "#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
        ]
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [
            [[".", "#", "#"], ["#", "#", "."]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#", "."], [".", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#", "#", "#"]],
            [["#", ".", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#"], [".", ".", "#"]],
            [[".", "#", "#"], ["#", "#", "."]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#", "."], [".", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#", "#", "#"]],
            [["#", ".", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#"], [".", ".", "#"]],
        ]
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [
            [[".", "#", "."], ["#", "#", "#"]],
            [[".", ".", "#"], ["#", "#", "#"]],
            [["#", "#", "."], [".", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [[".", ".", "#"], ["#", "#", "#"]],
            [["#", "#", "."], [".", "#", "#"]],
        ]
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [
            [[".", "#", "#"], ["#", "#", "."]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#", "."], [".", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#", "#", "#"]],
            [["#", ".", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#"], [".", ".", "#"]],
        ]
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = [
            [["#", "#", "#"], [".", "#", "."]],
            [[".", "#", "."], ["#", "#", "#"]],
            [[".", "#", "#"], ["#", "#", "."]],
            [["#", ".", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [[".", ".", "#"], ["#", "#", "#"]],
            [["#", "#", "#", "#"]],
            [["#", "#", "#"], [".", "#", "."]],
            [["#", "#", "."], [".", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#", "#"], [".", ".", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#", "#"]],
            [[".", ".", "#"], ["#", "#", "#"]],
            [["#", "#", "."], [".", "#", "#"]],
            [["#", "#", "#"], [".", ".", "#"]],
        ]
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = [
            [["#", "#", "#"], [".", "#", "."]],
            [["#", ".", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [[".", "#", "#"], ["#", "#", "."]],
            [["#", "#", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#", "#", "#"]],
            [["#", "#", "#"], ["#", ".", "."]],
            [["#", "#", "."], [".", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [[".", ".", "#"], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [[".", "#", "#"], ["#", "#", "."]],
            [["#", "#", "."], [".", "#", "#"]],
            [["#", "#", "#", "#"]],
            [["#", "#", "#"], [".", ".", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#", "."], [".", "#", "#"]],
            [[".", ".", "#"], ["#", "#", "#"]],
            [["#", "#", "#", "#"]],
            [["#", ".", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#"], [".", ".", "#"]],
        ]
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    @unittest.skip
    def test_case9(self):
        case = [
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#"], ["#", "#"]],
            [["#", "#", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
        ]
        expected = 11
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = [
            [[".", "#", "."], [".", "#", "#"]],
            [[".", ".", "#"], ["#", "#", "#"]],
            [["#", "#", "."], [".", "#", "#"]],
            [[".", "#", "."], ["#", "#", "#"]],
            [[".", ".", "#"], ["#", "#", "#"]],
            [["#", "#", "."], [".", "#", "#"]],
        ]
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)
