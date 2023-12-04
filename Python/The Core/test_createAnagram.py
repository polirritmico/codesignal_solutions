#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from createAnagram import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        s = "AABAA"
        t = "BBAAA"
        expected = 1
        output = solution(s, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        s = "OBGHK"
        t = "RPGUC"
        expected = 4
        output = solution(s, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB"
        t = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC"
        expected = 1
        output = solution(s, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        s = "HDFFVR"
        t = "FEDDEE"
        expected = 4
        output = solution(s, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        s = "AABCDS"
        t = "BASEAE"
        expected = 2
        output = solution(s, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        s = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZY"
        t = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYZ"
        expected = 31
        output = solution(s, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        t = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        expected = 0
        output = solution(s, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        s = "AAAAAA"
        t = "AAAAAA"
        expected = 0
        output = solution(s, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        s = "KJDMDLEEKALIJB"
        t = "AFDJGDCGHMIGHB"
        expected = 7
        output = solution(s, t)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        s = "BBAAABCBCAABB"
        t = "BBBCCCBABBACA"
        expected = 2
        output = solution(s, t)
        self.assertEqual(output, expected)
