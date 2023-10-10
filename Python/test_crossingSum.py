#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from crossingSum import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        matrix = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
        a = 1
        b = 3
        expected = 12
        output = solution(matrix, a, b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        matrix = [[1, 1], [1, 1]]
        a = 0
        b = 0
        expected = 3
        output = solution(matrix, a, b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        matrix = [[1, 1], [3, 3], [1, 1], [2, 2]]
        a = 3
        b = 0
        expected = 9
        output = solution(matrix, a, b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        matrix = [[100]]
        a = 0
        b = 0
        expected = 100
        output = solution(matrix, a, b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        matrix = [[1, 2], [3, 4]]
        a = 1
        b = 1
        expected = 9
        output = solution(matrix, a, b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        matrix = [[1, 2, 3, 4]]
        a = 0
        b = 3
        expected = 10
        output = solution(matrix, a, b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [1, 2, 2, 2, 2],
            [1, 2, 2, 2, 2],
            [1, 2, 2, 2, 2],
            [1, 2, 2, 2, 2],
            [1, 2, 2, 2, 2],
            [1, 2, 2, 2, 2],
        ]
        a = 1
        b = 1
        expected = 21
        output = solution(matrix, a, b)
        self.assertEqual(output, expected)
