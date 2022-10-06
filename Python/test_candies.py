#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from candies import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        n = 3
        m = 10
        expected = 9
        output = solution(n, m)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        n = 7
        m = 10
        expected = 7
        output = solution(n, m)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        n = 3
        m = 23
        expected = 21
        output = solution(n, m)
        self.assertEqual(output, expected)


