#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from constructSquare import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "ab"
        expected = 81
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "zzz"
        expected = -1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "aba"
        expected = 900
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "abcbbb"
        expected = 810000
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "abc"
        expected = 961
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "aaaabbcde"
        expected = 999950884
        output = solution(case)
        self.assertEqual(output, expected)
