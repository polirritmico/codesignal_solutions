#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from rectangleRotation import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        a = 6
        b = 4
        expected = 23
        output = solution(a, b)
        self.assertEqual(output, expected)

    def test_case2(self):
        a = 30
        b = 2
        expected = 65
        output = solution(a, b)
        self.assertEqual(output, expected)

    def test_case3(self):
        a = 8
        b = 6
        expected = 49
        output = solution(a, b)
        self.assertEqual(output, expected)

    def test_case4(self):
        a = 16
        b = 20
        expected = 333
        output = solution(a, b)
        self.assertEqual(output, expected)

    def test_case5(self):
        a = 20
        b = 32
        expected = 653
        output = solution(a, b)
        self.assertEqual(output, expected)

    def test_case6(self):
        a = 30
        b = 26
        expected = 795
        output = solution(a, b)
        self.assertEqual(output, expected)

    def test_case7(self):
        a = 50
        b = 4
        expected = 177
        output = solution(a, b)
        self.assertEqual(output, expected)

    def test_case8(self):
        a = 2
        b = 2
        expected = 5
        output = solution(a, b)
        self.assertEqual(output, expected)

    def test_case9(self):
        a = 50
        b = 50
        expected = 2521
        output = solution(a, b)
        self.assertEqual(output, expected)

    def test_case10(self):
        a = 38
        b = 42
        expected = 1563
        output = solution(a, b)
        self.assertEqual(output, expected)

