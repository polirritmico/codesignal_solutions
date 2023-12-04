#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from isPower import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 125
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 72
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 100
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = 11
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = 324
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = 256
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        case = 119
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        case = 400
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        case = 350
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case10(self):
        case = 361
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

