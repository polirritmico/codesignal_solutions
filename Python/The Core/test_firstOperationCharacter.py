#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from firstOperationCharacter import solution


# @unittest.skip
class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "(2 + 2) * 2"
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "2 + 2 * 2"
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "((2 + 2) * 2) * 3 + (2 + (2 * 2))"
        expected = 28
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "2+((22+2222)+(2222+222))"
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "2 + 3 * 45 * 56 + 198 + 10938 * 102938 + 5"
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "1022224552222222 * 3"
        expected = 17
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "4 * 3 + 2"
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)
