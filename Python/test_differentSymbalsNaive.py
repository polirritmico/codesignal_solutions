#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from differentSymbalsNaive import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "cabca"
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "cccccccccc"
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "aba"
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

