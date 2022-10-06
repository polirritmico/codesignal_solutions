#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from maxMultiple import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        divisor = 3
        bound = 10
        expected = 9
        output = solution(divisor, bound)
        self.assertEqual(output, expected)


