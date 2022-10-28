#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from arrayPacking import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [24, 85, 0]
        expected = 21784
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = [187, 99, 42, 43]
        expected = 724198331
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = [5]
        expected = 5
        output = solution(case)
        self.assertEqual(output, expected)


