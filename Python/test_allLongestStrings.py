#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from allLongestStrings import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = ["aba", "aa", "ad", "vcd", "aba"]
        expected = ["aba", "vcd", "aba"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = ["aa"]
        expected = ["aa"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = ["abc", "eeee", "abcd", "dcd"]
        expected = ["eeee", "abcd"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
        expected = ["zzzzzz", "abcdef", "aaaaaa"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = ["enyky", "benyky", "yely", "varennyky"]
        expected = ["varennyky"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = ["abacaba", "abacab", "abac", "xxxxxx"]
        expected = ["abacaba"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = [
            "young",
            "yooooooung",
            "hot",
            "or",
            "not",
            "come",
            "on",
            "fire",
            "water",
            "watermelon",
        ]
        expected = ["yooooooung", "watermelon"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = ["onsfnib", "aokbcwthc", "jrfcw"]
        expected = ["aokbcwthc"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = ["lbgwyqkry"]
        expected = ["lbgwyqkry"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = ["i"]
        expected = ["i"]
        output = solution(case)
        self.assertEqual(output, expected)
