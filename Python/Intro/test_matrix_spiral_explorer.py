#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from palindrome import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_solution(self):
        case = "aba"
        expected = True
        output = solution(case)
        self.assertEqual(expected, output)

    #@unittest.skip
    def test_case1(self):
        case = "a"
        expected = True
        output = solution(case)
        self.assertEqual(expected, output)

    #@unittest.skip
    def test_case2(self):
        case = "ab"
        expected = False
        output = solution(case)
        self.assertEqual(expected, output)

    #@unittest.skip
    def test_case3(self):
        case = "abac"
        expected = False
        output = solution(case)
        self.assertEqual(expected, output)

    #@unittest.skip
    def test_case4(self):
        case = "zzzazzazz"
        expected = False
        output = solution(case)
        self.assertEqual(expected, output)

