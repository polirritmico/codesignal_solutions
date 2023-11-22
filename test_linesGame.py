#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from linesGame import Ball, LineGame, solution


class TestCustom(unittest.TestCase):
    def test_filtered_line_last_other_color(self):
        field = [
            ["O", "O", "O", "O", "O", "X", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        case = [
            Ball("O", 0, 0),
            Ball("O", 0, 1),
            Ball("O", 0, 2),
            Ball("O", 0, 3),
            Ball("O", 0, 4),
            Ball("X", 0, 5),
            None,
            None,
            None,
        ]
        expected = [
            [
                case[0],
                case[1],
                case[2],
                case[3],
                case[4],
            ]
        ]

        game = LineGame(field)
        output = game.filter_completed_lines([case.copy()])
        self.assertListEqual(output, expected)

    def test_get_all_diagonals(self):
        field = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        expected = [
            [1, 6, 11, 16],
            [5, 10, 15],
            [9, 14],
            [13],
            [2, 7, 12],
            [3, 8],
            [4],
            # reverse diagonal
            [4, 7, 10, 13],
            [8, 11, 14],
            [12, 15],
            [16],
            [3, 6, 9],
            [2, 5],
            [1],
        ]

        game = LineGame(field)
        game.field = field
        game.min_line_size = 1
        output: list[list[int]] = game.get_all_diagonals()

        assert len(output) == len(expected)

        output.sort()
        expected.sort()
        for output_diagonal, expected_diagonal in zip(output, expected):
            output_diagonal.sort()
            expected_diagonal.sort()
            assert output_diagonal == expected_diagonal


# @unittest.skip
class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        field = [
            [".", "G", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "V", "."],
            [".", "O", ".", ".", "O", ".", ".", ".", "."],
            [".", ".", ".", ".", "O", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "O"],
            [".", ".", ".", ".", "O", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["R", ".", ".", ".", ".", ".", ".", "B", "R"],
            [".", ".", "C", ".", ".", ".", ".", "Y", "O"],
        ]
        clicks = [
            [4, 8],
            [2, 1],
            [4, 4],
            [6, 4],
            [4, 8],
            [1, 2],
            [1, 4],
            [4, 8],
            [6, 4],
        ]
        new_balls = ["R", "V", "C", "G", "Y", "O"]
        new_balls_coords = [[1, 2], [8, 5], [8, 6], [1, 1], [1, 8], [7, 4]]
        expected = 6
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        field = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "O", ".", "O", ".", "O", ".", "."],
            [".", ".", ".", "O", "O", "O", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "O"],
            [".", ".", ".", "O", "O", "O", ".", ".", "."],
            [".", ".", "O", ".", "O", ".", "O", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        clicks = [[4, 8], [4, 4]]
        new_balls = []
        new_balls_coords = []
        expected = 17
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        field = [
            ["O", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "O", "."],
            [".", ".", ".", ".", ".", ".", "O", ".", "."],
            [".", ".", ".", ".", ".", "O", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "O", ".", ".", ".", ".", "."],
            [".", ".", "O", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        clicks = [[0, 0], [4, 4]]
        new_balls = []
        new_balls_coords = []
        expected = 6
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
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
        expected = 36
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        field = [
            ["V", ".", ".", ".", ".", ".", ".", ".", "."],
            ["V", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", "O", ".", "O", ".", "O", ".", "."],
            ["V", ".", ".", "O", "O", "O", ".", ".", "."],
            [".", "V", "V", "V", ".", ".", ".", ".", "O"],
            ["V", ".", ".", "O", "O", "O", ".", ".", "."],
            ["V", ".", "O", ".", "O", ".", "O", ".", "."],
            ["V", ".", ".", ".", ".", ".", ".", ".", "."],
            ["V", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        clicks = [[4, 8], [4, 4], [1, 8], [4, 0]]
        new_balls = []
        new_balls_coords = []
        expected = 17
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        field = [
            [".", ".", ".", "G", "G", ".", ".", "G", "."],
            ["G", ".", ".", ".", ".", ".", ".", "G", "."],
            [".", "G", ".", ".", ".", ".", ".", "G", "."],
            [".", ".", "G", ".", ".", ".", ".", "G", "G"],
            ["G", "G", "G", ".", "G", "G", ".", ".", "."],
            [".", ".", ".", ".", "G", ".", "G", "G", "."],
            [".", ".", ".", ".", ".", "G", ".", ".", "."],
            [".", ".", ".", ".", "G", ".", ".", ".", "."],
            [".", ".", ".", "G", ".", ".", ".", ".", "."],
        ]
        clicks = [[0, 3], [4, 7], [0, 4], [4, 3]]
        new_balls = []
        new_balls_coords = []
        expected = 25
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        field = [
            [".", "R", "R", "R", ".", "R", ".", "G", "."],
            ["G", ".", ".", ".", ".", ".", ".", "G", "."],
            [".", "G", ".", ".", ".", ".", ".", "G", "."],
            [".", ".", "G", ".", ".", ".", ".", "G", "G"],
            ["G", "G", "G", ".", "G", "G", ".", ".", "."],
            [".", ".", ".", ".", "G", ".", "G", "G", "."],
            [".", ".", ".", ".", ".", "G", ".", ".", "."],
            [".", ".", ".", ".", "G", ".", ".", ".", "."],
            [".", ".", ".", "G", ".", ".", ".", ".", "."],
        ]
        clicks = [[0, 5], [0, 4]]
        new_balls = ["G", "G", "R"]
        new_balls_coords = [[4, 3], [4, 7], [0, 0]]
        expected = 33
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        field = [
            ["R", "R", "R", "R", ".", "R", ".", "G", "."],
            ["G", ".", ".", ".", ".", ".", ".", "G", "."],
            [".", "G", ".", ".", ".", ".", ".", "G", "."],
            [".", ".", "G", ".", ".", ".", ".", "G", "G"],
            ["G", "G", "G", ".", "G", "G", ".", ".", "."],
            [".", ".", ".", ".", "G", ".", "G", "G", "."],
            [".", ".", ".", ".", ".", "G", ".", ".", "."],
            [".", ".", ".", ".", "G", ".", ".", ".", "."],
            [".", ".", ".", "G", ".", ".", ".", ".", "."],
        ]
        clicks = [[0, 5], [0, 4]]
        new_balls = ["G", "G", "R"]
        new_balls_coords = [[4, 3], [4, 7], [0, 0]]
        expected = 5
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        field = [
            ["R", "R", "R", "R", ".", "R", ".", "G", "."],
            ["G", ".", ".", ".", ".", ".", ".", "G", "."],
            [".", "G", ".", ".", ".", ".", ".", "G", "."],
            [".", ".", "G", ".", ".", ".", ".", "G", "G"],
            ["G", "G", "G", ".", "G", "G", ".", ".", "."],
            [".", ".", ".", ".", "G", ".", "G", "G", "."],
            [".", ".", ".", ".", ".", "G", ".", ".", "."],
            [".", ".", ".", ".", "G", ".", ".", "G", "."],
            [".", ".", ".", "G", ".", ".", ".", "G", "."],
        ]
        clicks = [[0, 5], [0, 4], [0, 7], [6, 7]]
        new_balls = ["G", "G", "R"]
        new_balls_coords = [[4, 3], [4, 7], [0, 0]]
        expected = 34
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        field = [
            ["Y", ".", ".", ".", ".", ".", ".", ".", "Y"],
            [".", "Y", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "Y", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "Y", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "Y", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "Y", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "Y", "."],
            [".", ".", ".", ".", "Y", "Y", "Y", "Y", "."],
        ]
        clicks = [[0, 8], [8, 8], [0, 0], [8, 8]]
        new_balls = ["G", "Y", "Y"]
        new_balls_coords = [[0, 1], [4, 4], [0, 0]]
        expected = 14
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case11(self):
        field = [
            ["R", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        clicks = [
            [0, 0],
            [0, 1],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 1],
            [0, 0],
        ]
        new_balls = [
            "G",
            "G",
            "G",
            "G",
            "R",
            "R",
            "R",
            "R",
            "Y",
            "G",
            "G",
            "G",
            "G",
            "R",
            "R",
            "R",
            "R",
            "Y",
            "G",
            "G",
            "G",
            "G",
            "R",
            "R",
            "R",
            "R",
            "Y",
            "G",
            "G",
            "G",
            "G",
            "R",
            "R",
            "R",
            "R",
            "Y",
            "O",
            "V",
            "O",
            "V",
            "O",
            "V",
            "O",
            "V",
            "C",
            "O",
            "V",
            "O",
            "V",
            "O",
            "V",
            "O",
            "V",
            "Y",
            "O",
            "V",
            "O",
            "R",
            "Y",
            "C",
        ]
        new_balls_coords = [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [3, 0],
            [3, 1],
            [3, 2],
            [3, 3],
            [3, 4],
            [3, 5],
            [3, 6],
            [3, 7],
            [3, 8],
            [4, 0],
            [4, 1],
            [4, 2],
            [4, 3],
            [4, 4],
            [4, 5],
            [4, 6],
            [4, 7],
            [4, 8],
            [5, 0],
            [5, 1],
            [5, 2],
            [5, 3],
            [5, 4],
            [5, 5],
            [5, 6],
            [5, 7],
            [5, 8],
            [6, 0],
            [6, 1],
            [6, 2],
            [6, 3],
            [6, 4],
            [6, 5],
            [6, 6],
            [6, 7],
            [6, 8],
            [7, 0],
            [7, 1],
            [7, 2],
            [7, 3],
            [7, 4],
            [7, 5],
        ]
        expected = 0
        output = solution(field, clicks, new_balls, new_balls_coords)
        self.assertEqual(output, expected)
