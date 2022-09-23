#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from chessKnight import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "a1"
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "c2"
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "c4"
        expected = 8
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "g6"
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = "a3"
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = "b7"
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

