#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from createArray import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 49
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        output = solution(case)
        self.assertEqual(output, expected)


