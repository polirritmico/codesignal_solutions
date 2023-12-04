#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from candles import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        candles_number = 5
        make_new = 2
        expected = 9
        output = solution(candles_number, make_new)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        candles_number = 1
        make_new = 2
        expected = 1
        output = solution(candles_number, make_new)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        candles_number = 3
        make_new = 3
        expected = 4
        output = solution(candles_number, make_new)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        candles_number = 11
        make_new = 3
        expected = 16
        output = solution(candles_number, make_new)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        candles_number = 15
        make_new = 5
        expected = 18
        output = solution(candles_number, make_new)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        candles_number = 14
        make_new = 3
        expected = 20
        output = solution(candles_number, make_new)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        candles_number = 12
        make_new = 2
        expected = 23
        output = solution(candles_number, make_new)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        candles_number = 6
        make_new = 4
        expected = 7
        output = solution(candles_number, make_new)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        candles_number = 13
        make_new = 5
        expected = 16
        output = solution(candles_number, make_new)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case10(self):
        candles_number = 2
        make_new = 3
        expected = 2
        output = solution(candles_number, make_new)
        self.assertEqual(output, expected)


