#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from arrayChange import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [1, 1, 1]
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = [-1000, 0, -2, 0]
        expected = 5
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = [2, 1, 10, 1]
        expected = 12
        output = solution(case)
        self.assertEqual(output, expected)


