#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from equalPairOfBits import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        n = 10
        m = 11
        expected = 2
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        n = 0
        m = 0
        expected = 1
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        n = 28
        m = 27
        expected = 8
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        n = 895
        m = 928
        expected = 32
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        n = 1073741824
        m = 1006895103
        expected = 262144
        output = solution(n, m)
        self.assertEqual(output, expected)


