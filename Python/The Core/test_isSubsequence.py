#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from isSubsequence import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        t = "CodeSignal"
        s = "CoSi"
        expected = True
        output = solution(t, s)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        t = "CodeSignal"
        s = "cosi"
        expected = False
        output = solution(t, s)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        t = "somestring"
        s = ""
        expected = True
        output = solution(t, s)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        t = "penny"
        s = "longsenselessstringwithpennyinside"
        expected = False
        output = solution(t, s)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        t = "parliament"
        s = "partialmen"
        expected = False
        output = solution(t, s)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        t = ""
        s = ""
        expected = True
        output = solution(t, s)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        t = ""
        s = "hoho"
        expected = False
        output = solution(t, s)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        t = "he sd.f dsk e8.sd??l**23, 23,f.s++83+"
        s = "h  8.?*3+"
        expected = True
        output = solution(t, s)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        t = "abc"
        s = "d"
        expected = False
        output = solution(t, s)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        t = "abcd"
        s = "ad"
        expected = True
        output = solution(t, s)
        self.assertEqual(output, expected)
