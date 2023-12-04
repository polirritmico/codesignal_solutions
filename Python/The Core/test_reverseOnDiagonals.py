#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from reverseOnDiagonals import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[9, 2, 7], [4, 5, 6], [3, 8, 1]]
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
        expected = [[1000, 100], [10, 1]]
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
            [291, 455, 32, 2],
            [102, 53, 21, 981],
            [309, 298, 988, 64],
            [103, 22, 35, 43],
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
            [43, 1000, 139, 248, 972, 93],
            [98, 837, 398, 128, 109, 654],
            [33, 498, 764, 54, 764, 43],
            [329, 12, 543, 132, 666, 213],
            [928, 762, 489, 71, 1, 332],
            [584, 298, 42, 53, 76, 34],
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [[1, 1], [2, 2]]
        expected = [[2, 2], [1, 1]]
        output = solution(case)
        self.assertEqual(output, expected)
