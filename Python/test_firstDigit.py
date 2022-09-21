#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from firstDigit import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "var_1_Int"
        expected = "1"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "q2q-q"
        expected = "2"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "0ss"
        expected = "0"
        output = solution(case)
        self.assertEqual(output, expected)


