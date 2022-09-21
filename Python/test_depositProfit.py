#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from depositProfit import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        deposit = 100
        rate = 20
        threshold = 170
        expected = 3
        output = solution(deposit, rate, threshold)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        deposit = 100
        rate = 1
        threshold = 101
        expected = 1
        output = solution(deposit, rate, threshold)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        deposit = 1
        rate = 100
        threshold = 64
        expected = 6
        output = solution(deposit, rate, threshold)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        deposit = 20
        rate = 20
        threshold = 50
        expected = 6
        output = solution(deposit, rate, threshold)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        deposit = 50
        rate = 25
        threshold = 100
        expected = 4
        output = solution(deposit, rate, threshold)
        self.assertEqual(output, expected)


