#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from isBeautifulString import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "bbbaacdafe"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "aabbb"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "bbc"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "bbbaa"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = "abcdefghijklmnopqrstuvwxyzz"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = "abcdefghijklmnopqrstuvwxyz"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)





