#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from killKthBit import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        n = 37
        k = 3
        expected = 33
        output = solution(n, k)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        n = 37
        k = 4
        expected = 37
        output = solution(n, k)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        n = 37
        k = 2
        expected = 37
        output = solution(n, k)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        n = 0
        k = 4
        expected = 0
        output = solution(n, k)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        n = 2147483647
        k = 16
        expected = 2147450879
        output = solution(n, k)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        n = 374823748
        k = 13
        expected = 374819652
        output = solution(n, k)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        n = 2734827
        k = 4
        expected = 2734819
        output = solution(n, k)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        n = 1084197039
        k = 15
        expected = 1084197039
        output = solution(n, k)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        n = 1160825071
        k = 3
        expected = 1160825067
        output = solution(n, k)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case10(self):
        n = 2039063284
        k = 4
        expected = 2039063284
        output = solution(n, k)
        self.assertEqual(output, expected)


