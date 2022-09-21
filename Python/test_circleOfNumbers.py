#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from circleOfNumbers import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        n = 10
        firstNumber = 2
        expected = 7
        output = solution(n, firstNumber)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        n = 10
        firstNumber = 7
        expected = 2
        output = solution(n, firstNumber)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        n = 4
        firstNumber = 1
        expected = 3
        output = solution(n, firstNumber)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        n = 6
        firstNumber = 3
        expected = 0
        output = solution(n, firstNumber)
        self.assertEqual(output, expected)


