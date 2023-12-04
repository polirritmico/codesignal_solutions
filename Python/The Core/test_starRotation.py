#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from starRotation import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        matrix = [
            [1, 0, 0, 2, 0, 0, 3],
            [0, 1, 0, 2, 0, 3, 0],
            [0, 0, 1, 2, 3, 0, 0],
            [8, 8, 8, 9, 4, 4, 4],
            [0, 0, 7, 6, 5, 0, 0],
            [0, 7, 0, 6, 0, 5, 0],
            [7, 0, 0, 6, 0, 0, 5],
        ]
        width = 7
        center = [3, 3]
        t = 1
        expected = [
            [8, 0, 0, 1, 0, 0, 2],
            [0, 8, 0, 1, 0, 2, 0],
            [0, 0, 8, 1, 2, 0, 0],
            [7, 7, 7, 9, 3, 3, 3],
            [0, 0, 6, 5, 4, 0, 0],
            [0, 6, 0, 5, 0, 4, 0],
            [6, 0, 0, 5, 0, 0, 4],
        ]
        output = solution(matrix, width, center, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        matrix = [
            [1, 0, 0, 2, 0, 0, 3],
            [0, 1, 0, 2, 0, 3, 0],
            [0, 0, 1, 2, 3, 0, 0],
            [8, 8, 8, 9, 4, 4, 4],
            [0, 0, 7, 6, 5, 0, 0],
        ]
        width = 3
        center = [1, 5]
        t = 81
        expected = [
            [1, 0, 0, 2, 0, 0, 0],
            [0, 1, 0, 2, 3, 3, 3],
            [0, 0, 1, 2, 0, 0, 0],
            [8, 8, 8, 9, 4, 4, 4],
            [0, 0, 7, 6, 5, 0, 0],
        ]
        output = solution(matrix, width, center, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        matrix = [
            [1, 0, 0, 2, 0, 0, 3],
            [0, 1, 0, 2, 0, 3, 0],
            [0, 0, 1, 2, 3, 0, 0],
            [8, 8, 8, 9, 4, 4, 4],
            [0, 0, 7, 6, 5, 0, 0],
            [0, 7, 0, 6, 0, 5, 0],
            [7, 0, 0, 6, 0, 0, 5],
        ]
        width = 3
        center = [3, 3]
        t = 15
        expected = [
            [1, 0, 0, 2, 0, 0, 3],
            [0, 1, 0, 2, 0, 3, 0],
            [0, 0, 2, 3, 4, 0, 0],
            [8, 8, 1, 9, 5, 4, 4],
            [0, 0, 8, 7, 6, 0, 0],
            [0, 7, 0, 6, 0, 5, 0],
            [7, 0, 0, 6, 0, 0, 5],
        ]
        output = solution(matrix, width, center, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        matrix = [[1, 0, 3], [3, 4, 5], [8, 99, 0]]
        width = 3
        center = [1, 1]
        t = 4
        expected = [[0, 99, 8], [5, 4, 3], [3, 0, 1]]
        output = solution(matrix, width, center, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        matrix = [[8, 16, 32], [1, 0, 3], [3, 4, 5], [8, 99, 0], [42, 56, 64]]
        width = 3
        center = [2, 1]
        t = 12
        expected = [[8, 16, 32], [0, 99, 8], [5, 4, 3], [3, 0, 1], [42, 56, 64]]
        output = solution(matrix, width, center, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        matrix = [
            [1, 0, 0, 2, 0, 7, 3, 1, 24, 0, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 0, 7, 3, 1, 25, 0, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 0, 99, 3, 1, 0, 0, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 0, 8, 3, 1, 0, 54, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 0, 7, 3, 1, 0, 88, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 0, 88, 3, 1, 0, 0, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 0, 99, 3, 1, 0, 0, 2, 0, 0, 3, 4],
        ]
        width = 5
        center = [3, 4]
        t = 1
        expected = [
            [1, 0, 0, 2, 0, 7, 3, 1, 24, 0, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 0, 7, 0, 1, 25, 0, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 2, 0, 3, 1, 0, 0, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 0, 99, 3, 1, 0, 54, 2, 0, 0, 3, 4],
            [1, 0, 0, 0, 7, 8, 3, 1, 0, 88, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 3, 88, 3, 1, 0, 0, 2, 0, 0, 3, 4],
            [1, 0, 0, 2, 0, 99, 3, 1, 0, 0, 2, 0, 0, 3, 4],
        ]
        output = solution(matrix, width, center, t)
        self.assertEqual(output, expected)
