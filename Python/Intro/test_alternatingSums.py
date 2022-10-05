#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from alternatingSums import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [50, 60, 60, 45, 70]
        expected = [180, 105]
        output = solution(case)
        self.assertEqual(output, expected)


