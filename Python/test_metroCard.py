#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from metroCard import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 30
        expected = [31]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 31
        expected = [28, 30, 31]
        output = solution(case)
        self.assertEqual(output, expected)


