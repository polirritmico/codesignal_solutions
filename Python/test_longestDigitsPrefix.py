#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from longestDigitsPrefix import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "123aa1"
        expected = "123"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "0123456789"
        expected = "0123456789"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "  3) always check for whitespaces"
        expected = ""
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "12abc34"
        expected = "12"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = "the output is 42"
        expected = ""
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = "aaaaaaa"
        expected = ""
        output = solution(case)
        self.assertEqual(output, expected)


