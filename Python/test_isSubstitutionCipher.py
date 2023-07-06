#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from isSubstitutionCipher import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        string1 = "aacb"
        string2 = "aabc"
        expected = True
        output = solution(string1, string2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        string1 = "aa"
        string2 = "bc"
        expected = False
        output = solution(string1, string2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        string1 = "aaxxaaz"
        string2 = "aazzaay"
        expected = True
        output = solution(string1, string2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        string1 = "aaxyaa"
        string2 = "aazzaa"
        expected = False
        output = solution(string1, string2)
        self.assertEqual(output, expected)
