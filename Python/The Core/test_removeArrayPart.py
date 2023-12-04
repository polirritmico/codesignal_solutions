#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from removeArrayPart import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [2, 3, 2, 3, 4, 5]
        l = 2
        r = 4
        expected = [2, 3, 5]
        output = solution(case, l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = [0, -2, 5, 6]
        l = 3
        r = 3
        expected = [0, -2, 5]
        output = solution(case, l, r)
        self.assertEqual(output, expected)


