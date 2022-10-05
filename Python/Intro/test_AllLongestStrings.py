#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from AllLongestStrings import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_example(self):
        case = ["aba", "aa", "ad", "vcd", "aba"]
        expected = ["aba", "vcd", "aba"]
        output = solution(case)
        self.assertEqual(output, expected)

