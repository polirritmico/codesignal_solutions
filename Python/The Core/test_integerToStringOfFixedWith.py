#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from integerToStringOfFixedWith import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        number = 1234
        width = 2
        expected = "34"
        output = solution(number, width)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        number = 1234
        width = 4
        expected = "1234"
        output = solution(number, width)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        number = 1234
        width = 5
        expected = "01234"
        output = solution(number, width)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        number = 0
        width = 1
        expected = "0"
        output = solution(number, width)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        number = 89
        width = 4
        expected = "0089"
        output = solution(number, width)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        number = 23456
        width = 4
        expected = "3456"
        output = solution(number, width)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        number = 899
        width = 3
        expected = "899"
        output = solution(number, width)
        self.assertEqual(output, expected)
