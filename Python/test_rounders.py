#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from rounders import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 15
        expected = 20
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 1234
        expected = 1000
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 1445
        expected = 2000
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = 14
        expected = 10
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = 10
        expected = 10
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = 7001
        expected = 7000
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        case = 99
        expected = 100
        output = solution(case)
        self.assertEqual(output, expected)


