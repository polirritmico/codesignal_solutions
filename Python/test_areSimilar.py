#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from areSimilar import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        expected = True
        output = solution(a, b)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        a = [1, 2, 3]
        b = [2, 1, 3]
        expected = True
        output = solution(a, b)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        a = [1, 2, 2]
        b = [2, 1, 1]
        expected = False
        output = solution(a, b)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        a = [1, 2, 1, 2]
        b = [2, 2, 1, 1]
        expected = True
        output = solution(a, b)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        a = [2, 3, 1]
        b = [1, 3, 2]
        expected = True
        output = solution(a, b)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
        b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
        expected = False
        output = solution(a, b)
        self.assertEqual(output, expected)

