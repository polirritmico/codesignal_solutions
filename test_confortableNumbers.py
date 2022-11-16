#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from confortableNumbers import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        l = 10
        r = 12
        expected = 2
        output = solution(l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        l = 1
        r = 9
        expected = 20
        output = solution(l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        l = 13
        r = 13
        expected = 0
        output = solution(l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        l = 12
        r = 108
        expected = 707
        output = solution(l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        l = 239
        r = 777
        expected = 6166
        output = solution(l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        l = 1
        r = 1000
        expected = 11435
        output = solution(l, r)
        self.assertEqual(output, expected)


