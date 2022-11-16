#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from weakNumbers import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 9
        expected = [2, 2]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 1
        expected = [0, 1]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 2
        expected = [0, 2]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = 7
        expected = [2, 1]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = 500
        expected = [403, 1]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = 4
        expected = [0, 4]
        output = solution(case)
        self.assertEqual(output, expected)


