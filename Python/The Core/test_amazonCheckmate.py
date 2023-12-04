#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from amazonCheckmate import solution


# @unittest.skip
class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        king = "d3"
        amazon = "e4"
        expected = [5, 21, 0, 29]
        output = solution(king, amazon)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        king = "a1"
        amazon = "g5"
        expected = [0, 29, 1, 29]
        output = solution(king, amazon)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        king = "a3"
        amazon = "e4"
        expected = [1, 32, 1, 23]
        output = solution(king, amazon)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        king = "f3"
        amazon = "f2"
        expected = [6, 11, 0, 38]
        output = solution(king, amazon)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        king = "b7"
        amazon = "a8"
        expected = [0, 10, 0, 45]
        output = solution(king, amazon)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        king = "f7"
        amazon = "d3"
        expected = [4, 28, 1, 21]
        output = solution(king, amazon)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        king = "g2"
        amazon = "c3"
        expected = [9, 21, 0, 24]
        output = solution(king, amazon)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        king = "f3"
        amazon = "c1"
        expected = [4, 18, 0, 32]
        output = solution(king, amazon)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        king = "d4"
        amazon = "h8"
        expected = [0, 18, 0, 36]
        output = solution(king, amazon)
        self.assertEqual(output, expected)
