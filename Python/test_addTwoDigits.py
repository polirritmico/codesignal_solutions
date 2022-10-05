#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from addTwoDigits import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 29
        expected = 11
        output = solution(case)
        self.assertEqual(output, expected)


