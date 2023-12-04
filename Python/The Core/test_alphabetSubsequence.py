#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from alphabetSubsequence import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "effg"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "cdce"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "ace"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "bxz"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "cdefghijkxyzz"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "qa"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "fkyz"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "xz"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = "pfyz"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = "fz"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)
