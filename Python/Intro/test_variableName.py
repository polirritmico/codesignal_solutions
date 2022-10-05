#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from variableName import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "var_1__Int"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "qq-q"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "2w2"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


