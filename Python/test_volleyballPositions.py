#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from volleyballPositions import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        formation = [
            ["empty", "Player5", "empty"],
            ["Player4", "empty", "Player2"],
            ["empty", "Player3", "empty"],
            ["Player6", "empty", "Player1"],
        ]
        k = 2
        expected = [
            ["empty", "Player1", "empty"],
            ["Player2", "empty", "Player3"],
            ["empty", "Player4", "empty"],
            ["Player5", "empty", "Player6"],
        ]
        output = solution(formation, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        formation = [
            ["empty", "Alice", "empty"],
            ["Bob", "empty", "Charlie"],
            ["empty", "Dave", "empty"],
            ["Eve", "empty", "Frank"],
        ]
        k = 6
        expected = [
            ["empty", "Alice", "empty"],
            ["Bob", "empty", "Charlie"],
            ["empty", "Dave", "empty"],
            ["Eve", "empty", "Frank"],
        ]
        output = solution(formation, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        formation = [
            ["empty", "player 3", "empty"],
            ["player 3", "empty", "player"],
            ["empty", "4", "empty"],
            ["5", "empty", "42"],
        ]
        k = 1000000
        expected = [
            ["empty", "5", "empty"],
            ["4", "empty", "player 3"],
            ["empty", "player", "empty"],
            ["42", "empty", "player 3"],
        ]
        output = solution(formation, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        formation = [
            ["empty", "player 3", "empty"],
            ["player 8", "empty", "player"],
            ["empty", "4", "empty"],
            ["5", "empty", "42"],
        ]
        k = 0
        expected = [
            ["empty", "player 3", "empty"],
            ["player 8", "empty", "player"],
            ["empty", "4", "empty"],
            ["5", "empty", "42"],
        ]
        output = solution(formation, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        formation = [
            ["empty", "player 3", "empty"],
            ["player 8", "empty", "player"],
            ["empty", "4", "empty"],
            ["5", "empty", "42"],
        ]
        k = 1000000000
        expected = [
            ["empty", "5", "empty"],
            ["4", "empty", "player 8"],
            ["empty", "player", "empty"],
            ["42", "empty", "player 3"],
        ]
        output = solution(formation, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        formation = [
            ["empty", "Alice", "empty"],
            ["Bob", "empty", "Charlie"],
            ["empty", "Dave", "empty"],
            ["Eve", "empty", "Frank"],
        ]
        k = 7
        expected = [
            ["empty", "Charlie", "empty"],
            ["Alice", "empty", "Frank"],
            ["empty", "Eve", "empty"],
            ["Bob", "empty", "Dave"],
        ]
        output = solution(formation, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        formation = [
            ["empty", "1", "empty"],
            ["?", "empty", "!"],
            ["empty", ".", "empty"],
            ["3", "empty", "2"],
        ]
        k = 666
        expected = [
            ["empty", "1", "empty"],
            ["?", "empty", "!"],
            ["empty", ".", "empty"],
            ["3", "empty", "2"],
        ]
        output = solution(formation, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        formation = [
            ["empty", "", "empty"],
            ["", "empty", ""],
            ["empty", "!!!", "empty"],
            ["", "empty", ""],
        ]
        k = 541
        expected = [
            ["empty", "", "empty"],
            ["", "empty", ""],
            ["empty", "", "empty"],
            ["", "empty", "!!!"],
        ]
        output = solution(formation, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        formation = [
            ["empty", "Alice", "empty"],
            ["Bob", "empty", "Charlie"],
            ["empty", "Dave", "empty"],
            ["Eve", "empty", "Frank"],
        ]
        k = 0
        expected = [
            ["empty", "Alice", "empty"],
            ["Bob", "empty", "Charlie"],
            ["empty", "Dave", "empty"],
            ["Eve", "empty", "Frank"],
        ]
        output = solution(formation, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        formation = [
            ["empty", "a", "empty"],
            ["b", "empty", "c"],
            ["empty", "d", "empty"],
            ["e", "empty", "f"],
        ]
        k = 3220832
        expected = [
            ["empty", "f", "empty"],
            ["c", "empty", "d"],
            ["empty", "b", "empty"],
            ["a", "empty", "e"],
        ]
        output = solution(formation, k)
        self.assertEqual(output, expected)
