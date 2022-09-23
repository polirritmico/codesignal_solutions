#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from longestWord import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "Ready, steady, go!"
        expected = "steady"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "Ready[[[, steady, go!"
        expected = "steady"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "ABCd"
        expected = "ABCd"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "To be or not to be"
        expected = "not"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = "You are the best!!!!!!!!!!!! CodeFighter ever!"
        expected = "CodeFighter"
        output = solution(case)
        self.assertEqual(output, expected)


