#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from squareDigitsSequence import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 16
        expected = 9
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 103
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 1
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = 13
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = 89
        expected = 9
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = 612
        expected = 16
        output = solution(case)
        self.assertEqual(output, expected)


