#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from stringsRearrangement import *

class Test_OneCharDiff(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        a1 = "ab"
        a2 = "ab"
        expected = False
        output = one_char_diff(a1, a2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        a1 = "ab"
        a2 = "ac"
        expected = True
        output = one_char_diff(a1, a2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        a1 = "ab"
        a2 = "ad"
        expected = True
        output = one_char_diff(a1, a2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        a1 = "ab"
        a2 = "bc"
        expected = False
        output = one_char_diff(a1, a2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        a1 = "abcdefgh"
        a2 = "abcuefgw"
        expected = False
        output = one_char_diff(a1, a2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        a1 = "a"
        a2 = "a"
        expected = False
        output = one_char_diff(a1, a2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        a1 = "a"
        a2 = "b"
        expected = True
        output = one_char_diff(a1, a2)
        self.assertEqual(output, expected)



class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = ["aba", "bbb", "bab"]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = ["ab", "bb", "aa"]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = ["q", "q"]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = ["zzzzab", "zzzzbb", "zzzzaa"]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = ["ab", "ad", "ef", "eg"]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = ["abc", "bef", "bcc", "bec", "bbc", "bdc"]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)






