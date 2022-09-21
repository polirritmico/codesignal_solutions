#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from addBorder import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = ["abc", "ded"]
        expected = ["*****", "*abc*", "*ded*", "*****"]
        output = solution(case)
        self.assertEqual(output, expected)


