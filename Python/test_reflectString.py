#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from reflectString import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "name"
        expected = "mznv"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "abyz"
        expected = "zyba"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "nnnnn"
        expected = "mmmmm"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "pqr"
        expected = "kji"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "codesignal"
        expected = "xlwvhrtmzo"
        output = solution(case)
        self.assertEqual(output, expected)
