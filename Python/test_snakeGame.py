#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from snakeGame import solution


# @unittest.skip
class TestCustom(unittest.TestCase):
    # @unittest.skip
    def test_forward(self):
        game_board = [
            [".", ".", ".", "."],
            [".", ".", "<", "*"],
            [".", ".", ".", "*"],
        ]
        commands = "F"
        expected = [
            [".", ".", ".", "."],
            [".", "<", "*", "*"],
            [".", ".", ".", "."],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_forward_x2(self):
        game_board = [
            [".", ".", ".", "."],
            [".", ".", "<", "*"],
            [".", ".", ".", "*"],
        ]
        commands = "FF"
        expected = [
            [".", ".", ".", "."],
            ["<", "*", "*", "."],
            [".", ".", ".", "."],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_left(self):
        game_board = [
            [".", ".", ".", "."],
            [".", ".", "<", "*"],
            [".", ".", ".", "*"],
        ]
        commands = "L"
        expected = [
            [".", ".", ".", "."],
            [".", ".", "v", "*"],
            [".", ".", ".", "*"],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_right(self):
        game_board = [
            [".", ".", ".", "."],
            [".", ".", "<", "*"],
            [".", ".", ".", "*"],
        ]
        commands = "R"
        expected = [
            [".", ".", ".", "."],
            [".", ".", "^", "*"],
            [".", ".", ".", "*"],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_collision(self):
        game_board = [
            [".", ".", ".", "."],
            ["<", "*", "*", "."],
            [".", ".", ".", "."],
        ]
        commands = "F"
        expected = [
            [".", ".", ".", "."],
            ["X", "X", "X", "."],
            [".", ".", ".", "."],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)


# @unittest.skip
class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        game_board = [[".", ".", ".", "."], [".", ".", "<", "*"], [".", ".", ".", "*"]]
        commands = "FFFFFRFFRRLLF"
        expected = [[".", ".", ".", "."], ["X", "X", "X", "."], [".", ".", ".", "."]]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        game_board = [
            [".", ".", "^", ".", "."],
            [".", ".", "*", "*", "."],
            [".", ".", ".", "*", "*"],
        ]
        commands = "RFRF"
        expected = [
            [".", ".", "X", "X", "."],
            [".", ".", "X", "X", "."],
            [".", ".", ".", "X", "."],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        game_board = [
            [".", ".", "*", ">", "."],
            [".", "*", "*", ".", "."],
            [".", ".", ".", ".", "."],
        ]
        commands = "FRFFRFFRFLFF"
        expected = [
            [".", ".", ".", ".", "."],
            ["<", "*", "*", ".", "."],
            [".", ".", "*", ".", "."],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        game_board = [
            ["*", "*", ">"],
            ["*", ".", "."],
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."],
        ]
        commands = "RFRFFLFLFFRFRFFLFLFFRFRFFLFF"
        expected = [
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."],
            ["X", "X", "X"],
            ["X", ".", "."],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        game_board = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "<", "*", "*", "*", "*", ".", "."],
            [".", ".", ".", ".", ".", ".", "*", ".", "."],
            [".", ".", ".", ".", "*", "*", "*", ".", "."],
            [".", ".", ".", ".", "*", ".", ".", ".", "."],
            [".", ".", ".", ".", "*", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        commands = "FFFFFRFFRRLLF"
        expected = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["X", "X", "X", "X", "X", "X", "X", ".", "."],
            [".", ".", ".", ".", ".", ".", "X", ".", "."],
            [".", ".", ".", ".", "X", "X", "X", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        game_board = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "<", "*", "*", "*", "*", ".", "."],
            [".", ".", ".", ".", ".", ".", "*", ".", "."],
            [".", ".", ".", ".", "*", "*", "*", ".", "."],
            [".", ".", ".", ".", "*", ".", ".", ".", "."],
            [".", ".", ".", ".", "*", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        commands = "LFLFRFLFRFFF"
        expected = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "*", "*", "*", "*", ".", ".", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", "."],
            [".", ".", ".", ".", "*", ".", ".", ".", "."],
            [".", ".", ".", ".", "*", ".", ".", ".", "."],
            [".", ".", ".", ".", "v", ".", ".", ".", "."],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        game_board = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "<", "*", "*", "*", ".", ".", "."],
            [".", ".", ".", ".", ".", "*", ".", ".", "."],
            [".", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", ".", ".", "*", ".", "*", "*", "."],
            [".", ".", ".", ".", "*", "*", "*", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        commands = "LFLFLFFFF"
        expected = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "X", "X", "X", "X", ".", ".", "."],
            [".", ".", "X", "X", ".", "X", ".", ".", "."],
            [".", ".", ".", ".", "X", "X", ".", ".", "."],
            [".", ".", ".", ".", "X", ".", ".", ".", "."],
            [".", ".", ".", ".", "X", "X", "X", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        game_board = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "*", "*", "*", "*", ".", ".", "."],
            [".", ".", ".", ".", ".", "*", ".", ".", "."],
            [".", ".", ".", ".", ".", "v", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        commands = "LFLFFFLFFFFFFLFFFFFFLFFFFFFFFLFFFFFF"
        expected = [
            [".", ".", ".", ".", ".", ".", ".", ".", "^"],
            [".", ".", ".", ".", ".", ".", ".", ".", "*"],
            [".", ".", ".", ".", ".", ".", ".", ".", "*"],
            [".", ".", ".", ".", ".", ".", ".", ".", "*"],
            [".", ".", ".", ".", ".", ".", ".", ".", "*"],
            [".", ".", ".", ".", ".", ".", ".", ".", "*"],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        output = solution(game_board, commands)
        self.assertEqual(output, expected)
