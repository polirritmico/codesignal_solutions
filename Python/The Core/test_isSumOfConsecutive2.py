#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from isSumOfConsecutive2 import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 9
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 8
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 15
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = 24
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = 13
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = 25
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        case = 99
        expected = 5
        output = solution(case)
        self.assertEqual(output, expected)


