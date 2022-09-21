#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from arrayMaximalAdjacentDifference import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [2, 4, 1, 0]
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = [1, 1, 1, 1]
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = [-1, 4, 10, 3, -2]
        expected = 7
        output = solution(case)
        self.assertEqual(output, expected)


