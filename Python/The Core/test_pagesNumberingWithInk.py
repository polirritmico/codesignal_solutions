#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pagesNumberingWithInk import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        current = 1
        number_of_digits = 5
        expected = 5
        output = solution(current, number_of_digits)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        current = 21
        number_of_digits = 5
        expected = 22
        output = solution(current, number_of_digits)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        current = 8
        number_of_digits = 4
        expected = 10
        output = solution(current, number_of_digits)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        current = 21
        number_of_digits = 6
        expected = 23
        output = solution(current, number_of_digits)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        current = 10
        number_of_digits = 3
        expected = 10
        output = solution(current, number_of_digits)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        current = 76
        number_of_digits = 250
        expected = 166
        output = solution(current, number_of_digits)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        current = 80
        number_of_digits = 1000
        expected = 419
        output = solution(current, number_of_digits)
        self.assertEqual(output, expected)


