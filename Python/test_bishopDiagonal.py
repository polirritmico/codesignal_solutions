#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from bishopDiagonal import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        bishop_a = "d7"
        bishop_b = "f5"
        expected = ["c8", "h3"]
        output = solution(bishop_a, bishop_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        bishop_a = "d8"
        bishop_b = "b5"
        expected = ["b5", "d8"]
        output = solution(bishop_a, bishop_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        bishop_a = "a1"
        bishop_b = "h8"
        expected = ["a1", "h8"]
        output = solution(bishop_a, bishop_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        bishop_a = "g3"
        bishop_b = "e1"
        expected = ["e1", "h4"]
        output = solution(bishop_a, bishop_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        bishop_a = "b4"
        bishop_b = "e7"
        expected = ["a3", "f8"]
        output = solution(bishop_a, bishop_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        bishop_a = "h1"
        bishop_b = "a1"
        expected = ["a1", "h1"]
        output = solution(bishop_a, bishop_b)
        self.assertEqual(output, expected)
