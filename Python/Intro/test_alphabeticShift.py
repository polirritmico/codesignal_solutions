#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from alphabeticShift import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "crazy"
        expected = "dsbaz"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "fuzzy"
        expected = "gvaaz"
        output = solution(case)
        self.assertEqual(output, expected)


