#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from palindromeRearranging import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "aabb"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "abbcabb"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "zyyzzzzz"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = "zaa"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


