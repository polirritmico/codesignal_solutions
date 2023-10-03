#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from cyclicString import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "cabca"
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "aba"
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "ccccccccccc"
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "bcaba"
        expected = 5
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "abacabaabacab"
        expected = 7
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "aab"
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "abaaba"
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "zazazaza"
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = "abbaab"
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)
