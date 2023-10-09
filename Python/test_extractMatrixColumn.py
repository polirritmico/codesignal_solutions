#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from extractMatrixColumn import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        matrix = [[1, 1, 1, 2], [0, 5, 0, 4], [2, 1, 3, 6]]
        column = 2
        expected = [1, 0, 3]
        output = solution(matrix, column)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        matrix = [[1, 1, 1], [0, 5, 0], [2, 1, 3]]
        column = 2
        expected = [1, 0, 3]
        output = solution(matrix, column)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        matrix = [[1, 1], [5, 0], [2, 3]]
        column = 0
        expected = [1, 5, 2]
        output = solution(matrix, column)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        matrix = [[1, 1, 1], [0, 5, 0], [2, 1, 3], [10, 100, 300]]
        column = 1
        expected = [1, 5, 1, 100]
        output = solution(matrix, column)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        matrix = [[0, 1, 1, 5], [5, 0, 0, 0], [2, 1, 0, 10]]
        column = 3
        expected = [5, 0, 10]
        output = solution(matrix, column)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        matrix = [[0]]
        column = 0
        expected = [0]
        output = solution(matrix, column)
        self.assertEqual(output, expected)
