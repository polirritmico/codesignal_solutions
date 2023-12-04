#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from additionWithoutCarrying import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        param1 = 456
        param2 = 1734
        expected = 1180
        output = solution(param1, param2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        param1 = 99999
        param2 = 0
        expected = 99999
        output = solution(param1, param2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        param1 = 999
        param2 = 999
        expected = 888
        output = solution(param1, param2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        param1 = 0
        param2 = 0
        expected = 0
        output = solution(param1, param2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        param1 = 54321
        param2 = 54321
        expected = 8642
        output = solution(param1, param2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        param1 = 54321
        param2 = 56789
        expected = 0
        output = solution(param1, param2)
        self.assertEqual(output, expected)


