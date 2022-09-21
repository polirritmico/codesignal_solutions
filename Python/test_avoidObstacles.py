#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from avoidObstacles import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case0(self):
        case = [2, 4]
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case1(self):
        case = [5, 3, 6, 7, 9]
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = [2, 3]
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = [1, 4, 10, 6, 2]
        expected = 7
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = [1000,999]
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

