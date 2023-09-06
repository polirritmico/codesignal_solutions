#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from mostFrequentDigitSum import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = 88
        expected = 9
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = 8
        expected = 8
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = 1
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = 17
        expected = 9
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = 239
        expected = 9
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = 994
        expected = 9
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = 99999
        expected = 18
        output = solution(case)
        self.assertEqual(output, expected)
