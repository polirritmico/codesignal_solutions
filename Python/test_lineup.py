#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from lineup import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "LLARL"
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = "RLR"
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = ""
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = "L"
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = "0"
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = "AAAAAAAAAAAAAAA"
        expected = 15
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        case = "RRRRRRRRRRLLLLLLLLLRRRRLLLLLLLLLL"
        expected = 16
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        case = "AALAAALARAR"
        expected = 5
        output = solution(case)
        self.assertEqual(output, expected)


