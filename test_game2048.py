#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from game2048 import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        grid = [[0, 0, 0, 0], [0, 0, 2, 2], [0, 0, 2, 4], [2, 2, 4, 8]]
        path = "RR"
        expected = [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 2, 4], [0, 0, 8, 8]]
        output = solution(grid, path)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        grid = [[0, 0, 0, 2], [0, 0, 4, 2], [0, 0, 4, 2], [0, 0, 4, 2]]
        path = "D"
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 4, 4], [0, 0, 8, 4]]
        output = solution(grid, path)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        grid = [[0, 2, 2, 0], [0, 4, 2, 2], [2, 4, 4, 8], [2, 4, 0, 0]]
        path = "L"
        expected = [[4, 0, 0, 0], [4, 4, 0, 0], [2, 8, 8, 0], [2, 4, 0, 0]]
        output = solution(grid, path)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        grid = [[0, 0, 0, 2], [0, 0, 4, 2], [0, 0, 4, 2], [0, 0, 4, 2]]
        path = "DD"
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 4, 0], [0, 0, 8, 8]]
        output = solution(grid, path)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        grid = [[0, 0, 0, 2], [0, 0, 4, 2], [0, 0, 4, 2], [0, 0, 4, 2]]
        path = "DRRD"
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 8], [0, 0, 8, 4]]
        output = solution(grid, path)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        grid = [
            [2, 4, 8, 16],
            [256, 128, 64, 32],
            [512, 1024, 2048, 4096],
            [65536, 32768, 16384, 8192],
        ]
        path = "URLD"
        expected = [
            [2, 4, 8, 16],
            [256, 128, 64, 32],
            [512, 1024, 2048, 4096],
            [65536, 32768, 16384, 8192],
        ]
        output = solution(grid, path)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        grid = [[0, 2, 0, 2], [0, 4, 4, 2], [0, 0, 4, 2], [0, 0, 4, 2]]
        path = "LLU"
        expected = [[4, 4, 0, 0], [8, 2, 0, 0], [8, 0, 0, 0], [0, 0, 0, 0]]
        output = solution(grid, path)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        grid = [[0, 2, 0, 2], [0, 4, 4, 2], [0, 0, 4, 2], [0, 0, 4, 2]]
        path = "LLUR"
        expected = [[0, 0, 0, 8], [0, 0, 8, 2], [0, 0, 0, 8], [0, 0, 0, 0]]
        output = solution(grid, path)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        grid = [[0, 0, 0, 2], [0, 0, 4, 2], [0, 0, 4, 2], [0, 0, 4, 2]]
        path = "DRRL"
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [8, 0, 0, 0], [8, 4, 0, 0]]
        output = solution(grid, path)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        grid = [[0, 0, 0, 2], [0, 0, 4, 2], [0, 0, 4, 2], [0, 0, 4, 2]]
        path = "DRRLLD"
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [16, 4, 0, 0]]
        output = solution(grid, path)
        self.assertEqual(output, expected)
