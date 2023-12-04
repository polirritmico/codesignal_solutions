#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from magicWell import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        a = 1
        b = 2
        n = 2
        expected = 8
        output = solution(a, b, n)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        a = 1
        b = 1
        n = 1
        expected = 1
        output = solution(a, b, n)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        a = 1601
        b = 337
        n = 0
        expected = 0
        output = solution(a, b, n)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        a = 1936
        b = 1835
        n = 5
        expected = 17800540
        output = solution(a, b, n)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        a = 687
        b = 1337
        n = 0
        expected = 0
        output = solution(a, b, n)
        self.assertEqual(output, expected)


