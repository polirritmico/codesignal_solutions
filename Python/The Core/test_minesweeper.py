#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from minesweeper import solution, sum_inner_frame

# @unittest.skip


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        matrix = [[True, False, False], [False, True, False], [False, False, False]]
        expected = [[1, 2, 1], [2, 1, 1], [1, 1, 1]]
        output = solution(matrix)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        matrix = [[False, False, False], [False, False, False]]
        expected = [[0, 0, 0], [0, 0, 0]]
        output = solution(matrix)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        matrix = [
            [True, False, False, True],
            [False, False, True, False],
            [True, True, False, True],
        ]
        expected = [[0, 2, 2, 1], [3, 4, 3, 3], [1, 2, 3, 1]]
        output = solution(matrix)
        self.assertEqual(output, expected)


class TestInnerSum(unittest.TestCase):
    # @unittest.skip
    def setUp(self):
        self.matrix = [
            [True, False, False],
            [False, True, False],
            [False, False, False],
        ]

    # @unittest.skip
    def test_case1(self):
        case = (0, 0)
        expected = 1
        output = sum_inner_frame(case, self.matrix)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = (0, 1)
        expected = 2
        output = sum_inner_frame(case, self.matrix)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = (0, 2)
        expected = 1
        output = sum_inner_frame(case, self.matrix)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = (1, 0)
        expected = 2
        output = sum_inner_frame(case, self.matrix)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case_center_coord(self):
        case = (1, 1)
        expected = 1
        output = sum_inner_frame(case, self.matrix)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = (1, 2)
        expected = 1
        output = sum_inner_frame(case, self.matrix)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = (2, 0)
        expected = 1
        output = sum_inner_frame(case, self.matrix)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = (2, 1)
        expected = 1
        output = sum_inner_frame(case, self.matrix)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = (2, 2)
        expected = 1
        output = sum_inner_frame(case, self.matrix)
        self.assertEqual(output, expected)
