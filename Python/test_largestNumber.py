#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from largestNumber import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 2
        expected = 99
        output = solution(case)
        self.assertEqual(output, expected)


