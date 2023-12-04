#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from leastFactorial import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 17
        expected = 24
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 5
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = 109
        expected = 120
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        case = 11
        expected = 24
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        case = 55
        expected = 120
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case10(self):
        case = 24
        expected = 24
        output = solution(case)
        self.assertEqual(output, expected)


