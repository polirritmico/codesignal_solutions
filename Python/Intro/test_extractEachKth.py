#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from extractEachKth import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [2, 4, 6, 8, 10]
        k = 2
        expected = [2, 6, 10]
        output = solution(case, k)
        self.assertEqual(output, expected)


