#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from mirrorBits import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 97
        expected = 67
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 8
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 123
        expected = 111
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = 86782
        expected = 65173
        output = solution(case)
        self.assertEqual(output, expected)


