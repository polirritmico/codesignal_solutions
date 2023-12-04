#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from maximumSum import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        a = [9, 7, 2, 4, 4]
        q = [[1, 3], [1, 4], [0, 2]]
        expected = 62
        output = solution(a, q)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        a = [2, 1, 2]
        q = [[0, 1]]
        expected = 4
        output = solution(a, q)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        a = [5, 3, 2]
        q = [[0, 0], [0, 1], [1, 2], [0, 2]]
        expected = 28
        output = solution(a, q)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        a = [5, 2, 4, 1, 3]
        q = [[0, 4], [1, 2], [1, 2]]
        expected = 33
        output = solution(a, q)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        a = [4, 2, 1, 6, 5, 7, 2, 4]
        q = [
            [1, 6],
            [2, 4],
            [3, 6],
            [0, 7],
            [3, 6],
            [4, 4],
            [5, 6],
            [5, 6],
            [0, 1],
            [3, 4],
        ]
        expected = 162
        output = solution(a, q)
        self.assertEqual(output, expected)
