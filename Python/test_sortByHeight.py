#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from sortByHeight import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [-1, 150, 190, 170, -1, -1, 160, 180]
        expected = [-1, 150, 160, 170, -1, -1, 180, 190]
        output = solution(case)
        self.assertEqual(output, expected)


