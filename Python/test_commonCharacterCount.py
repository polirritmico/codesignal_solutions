#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from commonCharacterCount import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        s1 = "aabcc"
        s2 = "adcaa"
        expected = 3
        output = solution(s1, s2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        s1 = "zzzz"
        s2 = "zzzzzzz"
        expected = 4
        output = solution(s1, s2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        s1 = "abca"
        s2 = "xyzbac"
        expected = 3
        output = solution(s1, s2)
        self.assertEqual(output, expected)


