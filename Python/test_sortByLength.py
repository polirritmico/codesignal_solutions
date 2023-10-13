#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from sortByLength import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = ["abc", "", "aaa", "a", "zz"]
        expected = ["", "a", "zz", "abc", "aaa"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = ["zz", "", "bb", "ccc", "cc"]
        expected = ["", "zz", "bb", "cc", "ccc"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = ["abc", "e", "abcd"]
        expected = ["e", "abc", "abcd"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = ["a", "c", "a", "a"]
        expected = ["a", "c", "a", "a"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [
            "thitl",
            "",
            "sadhxirg",
            "hx",
            "ondyxds",
            "kncor",
            "sqrg",
            "hqtchyxku",
            "rl",
            "wd",
        ]
        expected = [
            "",
            "hx",
            "rl",
            "wd",
            "sqrg",
            "thitl",
            "kncor",
            "ondyxds",
            "sadhxirg",
            "hqtchyxku",
        ]
        output = solution(case)
        self.assertEqual(output, expected)
