#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from swapDiagonals import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[3, 2, 1], [4, 5, 6], [9, 8, 7]]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [[239]]
        expected = [[239]]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [[1, 10], [100, 1000]]
        expected = [[10, 1], [1000, 100]]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [
            [43, 455, 32, 103],
            [102, 988, 298, 981],
            [309, 21, 53, 64],
            [2, 22, 35, 291],
        ]
        expected = [
            [103, 455, 32, 43],
            [102, 298, 988, 981],
            [309, 53, 21, 64],
            [291, 22, 35, 2],
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [
            [34, 1000, 139, 248, 972, 584],
            [98, 1, 398, 128, 762, 654],
            [33, 498, 132, 543, 764, 43],
            [329, 12, 54, 764, 666, 213],
            [928, 109, 489, 71, 837, 332],
            [93, 298, 42, 53, 76, 43],
        ]
        expected = [
            [584, 1000, 139, 248, 972, 34],
            [98, 762, 398, 128, 1, 654],
            [33, 498, 543, 132, 764, 43],
            [329, 12, 764, 54, 666, 213],
            [928, 837, 489, 71, 109, 332],
            [43, 298, 42, 53, 76, 93],
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [[1, 2], [1, 2]]
        expected = [[2, 1], [2, 1]]
        output = solution(case)
        self.assertEqual(output, expected)
