#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from stringsCrossover import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        input_array = ["abc", "aaa", "aba", "bab"]
        result = "bbb"
        expected = 2
        output = solution(input_array, result)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        input_array = ["aacccc", "bbcccc"]
        result = "abdddd"
        expected = 0
        output = solution(input_array, result)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        input_array = ["a", "b", "c", "d", "e"]
        result = "c"
        expected = 4
        output = solution(input_array, result)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        input_array = ["aa", "ab", "ba"]
        result = "bb"
        expected = 1
        output = solution(input_array, result)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        input_array = ["a", "b", "c", "d", "e"]
        result = "f"
        expected = 0
        output = solution(input_array, result)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        input_array = ["aaa", "aaa"]
        result = "aaa"
        expected = 1
        output = solution(input_array, result)
        self.assertEqual(output, expected)
