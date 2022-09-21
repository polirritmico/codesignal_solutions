#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from knapsackLight import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        value1 = 10
        weight1 = 5
        value2 = 6
        weight2 = 4
        maxW = 8
        expected = 10
        output = solution(value1, weight1, value2, weight2, maxW)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        value1 = 10
        weight1 = 5
        value2 = 6
        weight2 = 4
        maxW = 9
        expected = 16
        output = solution(value1, weight1, value2, weight2, maxW)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        value1 = 5
        weight1 = 3
        value2 = 7
        weight2 = 4
        maxW = 6
        expected = 7
        output = solution(value1, weight1, value2, weight2, maxW)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        value1 = 10
        weight1 = 2
        value2 = 11
        weight2 = 3
        maxW = 1
        expected = 0
        output = solution(value1, weight1, value2, weight2, maxW)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        value1 = 15
        weight1 = 2
        value2 = 20
        weight2 = 3
        maxW = 2
        expected = 15
        output = solution(value1, weight1, value2, weight2, maxW)
        self.assertEqual(output, expected)

