#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from bugAndBugfixes import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "Roll d6-3 and 4d4+3 to pick a weapon, and finish the boss with 3d7!"
        expected = 43
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "d6-almost 01d4+2 12d01-3 5d5-00 a valid formula"
        expected = 46
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "meh4d2-3D3"
        expected = 5
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "ad3+4, 44b-6, 5daa"
        expected = 7
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "4d6-L1d20-10 did4n't expect that"
        expected = 38
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "nothing here"
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)
