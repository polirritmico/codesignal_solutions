#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from uniqueDigitProducts import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [2, 8, 121, 42, 222, 23]
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [239]
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [100, 101, 111]
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [100, 23, 42, 239, 22339, 9999999, 456, 78, 228, 1488]
        expected = 10
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected = 10
        output = solution(case)
        self.assertEqual(output, expected)
