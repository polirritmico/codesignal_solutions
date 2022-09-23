#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from sumUpNumbers import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "2 apples, 12 oranges"
        expected = 14
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "123450"
        expected = 123450
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "Your payment method is invalid"
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "no digits at all"
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = "there are some (12) digits 5566 in this 770 string 239"
        expected = 6587
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = "42+781"
        expected = 823
        output = solution(case)
        self.assertEqual(output, expected)


