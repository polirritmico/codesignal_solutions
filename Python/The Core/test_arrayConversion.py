#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from arrayConversion import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = 186
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        expected = 64
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [3, 3, 5, 5]
        expected = 60
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [-1, 1, 2, 3, 5, 5, 3, 7]
        expected = 100
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [99]
        expected = 99
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [99, 1]
        expected = 100
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = [34, 60, -9, -67, -100, -27, 100, 21]
        expected = -22511
        output = solution(case)
        self.assertEqual(output, expected)
