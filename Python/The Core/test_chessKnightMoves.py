#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from chessKnightMoves import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "a1"
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "c2"
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "h8"
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "d5"
        expected = 8
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "a2"
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "h7"
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "h6"
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "b2"
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = "f4"
        expected = 8
        output = solution(case)
        self.assertEqual(output, expected)
