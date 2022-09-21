#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from isLucky import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 1230
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = 134008
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

