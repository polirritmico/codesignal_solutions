#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from isInfiniteProcess import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        a = 2
        b = 6
        expected = False
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        a = 2
        b = 3
        expected = True
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        a = 2
        b = 10
        expected = False
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        a = 0
        b = 1
        expected = True
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        a = 3
        b = 1
        expected = True
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        a = 10
        b = 10
        expected = False
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        a = 5
        b = 10
        expected = True
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        a = 6
        b = 10
        expected = False
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        a = 10
        b = 0
        expected = True
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case10(self):
        a = 5
        b = 5
        expected = False
        output = solution(a, b)
        self.assertEqual(output, expected)


