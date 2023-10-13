#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from sortByHeight import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [-1, 150, 190, 170, -1, -1, 160, 180]
        expected = [-1, 150, 160, 170, -1, -1, 180, 190]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [-1, -1, -1, -1, -1]
        expected = [-1, -1, -1, -1, -1]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [-1]
        expected = [-1]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [4, 2, 9, 11, 2, 16]
        expected = [2, 2, 4, 9, 11, 16]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
        expected = [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
        expected = [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]
        output = solution(case)
        self.assertEqual(output, expected)
