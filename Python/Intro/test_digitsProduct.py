#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from digitsProduct import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 12
        expected = 26
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = 19
        expected = -1
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = 450
        expected = 2559
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = 0
        expected = 10
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = 13
        expected = -1
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = 1
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case7(self):
        case = 243
        expected = 399
        output = solution(case)
        self.assertEqual(output, expected)


