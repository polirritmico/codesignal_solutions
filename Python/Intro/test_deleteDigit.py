#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from deleteDigit import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 152
        expected = 52
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = 1001
        expected = 101
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = 10
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = 222219
        expected = 22229
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = 109
        expected = 19
        output = solution(case)
        self.assertEqual(output, expected)


