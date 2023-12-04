#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from rangeBitCount import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        a = 2
        b = 7
        expected = 11
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        a = 0
        b = 1
        expected = 1
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        a = 1
        b = 10
        expected = 17
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        a = 8
        b = 9
        expected = 3
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        a = 9
        b = 10
        expected = 4
        output = solution(a, b)
        self.assertEqual(output, expected)


