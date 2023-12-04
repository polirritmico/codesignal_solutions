#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from contoursShifting import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
        ]
        expected = [
            [5, 1, 2, 3],
            [9, 7, 11, 4],
            [13, 6, 15, 8],
            [17, 10, 14, 12],
            [18, 19, 20, 16],
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [[238, 239, 240, 241, 242, 243, 244, 245]]
        expected = [[245, 238, 239, 240, 241, 242, 243, 244]]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [[238], [239], [240], [241], [242], [243], [244], [245]]
        expected = [[245], [238], [239], [240], [241], [242], [243], [244]]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        expected = [[4, 1, 2], [7, 8, 3], [10, 5, 6], [11, 12, 9]]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ]
        expected = [
            [6, 1, 2, 3, 4],
            [11, 8, 9, 14, 5],
            [16, 7, 12, 13, 10],
            [17, 18, 19, 20, 15],
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
        ]
        expected = [
            [6, 1, 2, 3, 4],
            [11, 8, 9, 7, 5],
            [12, 13, 14, 15, 10],
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = [
            [1, 2, 3],
            [6, 7, 8],
            [11, 12, 13],
            [16, 17, 18],
            [21, 22, 23],
            [24, 25, 26],
        ]
        expected = [
            [6, 1, 2],
            [11, 12, 3],
            [16, 17, 8],
            [21, 22, 13],
            [24, 7, 18],
            [25, 26, 23],
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = [[239]]
        expected = [[239]]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = [[1, 4], [3, 5], [55, 55], [23, 56]]
        expected = [[3, 1], [55, 4], [23, 5], [56, 55]]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_custom1(self):
        case = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        expected = [[6, 1, 2, 3, 4], [7, 8, 9, 10, 5]]
        output = solution(case)
        self.assertEqual(output, expected)
