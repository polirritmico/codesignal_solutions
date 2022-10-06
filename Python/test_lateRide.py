#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from lateRide import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 240
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = 808
        expected = 14
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = 1439
        expected = 19
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = 0
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = 23
        expected = 5
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = 8
        expected = 8
        output = solution(case)
        self.assertEqual(output, expected)


