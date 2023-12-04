#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from makeArrayConsecutive2 import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [6, 2, 3, 8]
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = [0, 3]
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = [5, 4, 6]
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = [6, 3]
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = [1]
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)


