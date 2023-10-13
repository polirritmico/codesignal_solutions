#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from shuffledArray import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [1, 12, 3, 6, 2]
        expected = [1, 2, 3, 6]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [1, -3, -5, 7, 2]
        expected = [-5, -3, 2, 7]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [2, -1, 2, 2, -1]
        expected = [-1, -1, 2, 2]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [-3, -3]
        expected = [-3]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [37, 11, -37, -85, -67, 32, 90, -90, 56, 80, 37]
        expected = [-90, -85, -67, -37, 11, 37, 37, 56, 80, 90]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [18, -73, -39, 65, -65, -52]
        expected = [-65, -52, -39, 18, 65]
        output = solution(case)
        self.assertEqual(output, expected)
