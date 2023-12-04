#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from arrayPreviousLess import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [3, 5, 2, 4, 5]
        expected = [-1, 3, -1, 2, 4]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [2, 2, 1, 3, 4, 5, 5, 3]
        expected = [-1, -1, -1, 1, 3, 4, 4, 1]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [3, 2, 1]
        expected = [-1, -1, -1]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [100, 101, 102]
        expected = [-1, 100, 101]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [7, 7, 8, 3, 4, 4, 2, 5, 6, 7, 7]
        expected = [-1, -1, 7, -1, 3, 3, -1, 2, 5, 6, 6]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [68, 135, 101, 170, 125]
        expected = [-1, 68, 68, 101, 101]
        output = solution(case)
        self.assertEqual(output, expected)
