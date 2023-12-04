#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from arithmeticExpression import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        a = 2
        b = 3
        c = 5
        expected = True
        output = solution(a, b, c)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        a = 8
        b = 2
        c = 4
        expected = True
        output = solution(a, b, c)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        a = 8
        b = 3
        c = 2
        expected = False
        output = solution(a, b, c)
        self.assertEqual(output, expected)



    #@unittest.skip
    def test_case4(self):
        a = 6
        b = 3
        c = 3
        expected = True
        output = solution(a, b, c)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        a = 18
        b = 2
        c = 9
        expected = True
        output = solution(a, b, c)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        a = 2
        b = 3
        c = 6
        expected = True
        output = solution(a, b, c)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        a = 5
        b = 2
        c = 0
        expected = False
        output = solution(a, b, c)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        a = 10
        b = 2
        c = 2
        expected = False
        output = solution(a, b, c)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        a = 5
        b = 2
        c = 2
        expected = False
        output = solution(a, b, c)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case10(self):
        a = 1
        b = 2
        c = 1
        expected = False
        output = solution(a, b, c)
        self.assertEqual(output, expected)


