#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from boxBlur import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [[1, 1, 1], [1, 7, 1], [1, 1, 1]]
        expected = [[1]]
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case2(self):
        case = [[0, 18, 9], [27, 9, 0], [81, 63, 45]]
        expected = [[28]]
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case3(self):
        case = [[36, 0, 18, 9], [27, 54, 9, 0], [81, 63, 72, 45]]
        expected = [[40, 30]]
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case4(self):
        case = [[7, 4, 0, 1], [5, 6, 2, 2], [6, 10, 7, 8], [1, 4, 2, 0]]
        expected = [[5, 4], [4, 4]]
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case5(self):
        case = [
            [36, 0, 18, 9, 9, 45, 27],
            [27, 0, 54, 9, 0, 63, 90],
            [81, 63, 72, 45, 18, 27, 0],
            [0, 0, 9, 81, 27, 18, 45],
            [45, 45, 27, 27, 90, 81, 72],
            [45, 18, 9, 0, 9, 18, 45],
            [27, 81, 36, 63, 63, 72, 81],
        ]
        expected = [
            [39, 30, 26, 25, 31],
            [34, 37, 35, 32, 32],
            [38, 41, 44, 46, 42],
            [22, 24, 31, 39, 45],
            [37, 34, 36, 47, 59],
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case6(self):
        case = [
            [36, 0, 18, 9, 9, 45, 27],
            [27, 0, 254, 9, 0, 63, 90],
            [81, 255, 72, 45, 18, 27, 0],
            [0, 0, 9, 81, 27, 18, 45],
            [45, 45, 227, 227, 90, 81, 72],
            [45, 18, 9, 255, 9, 18, 45],
            [27, 81, 36, 127, 255, 72, 81],
        ]
        expected = [
            [82, 73, 48, 25, 31],
            [77, 80, 57, 32, 32],
            [81, 106, 88, 68, 42],
            [44, 96, 103, 89, 45],
            [59, 113, 137, 126, 80],
        ]
        output = solution(case)
        self.assertEqual(output, expected)
