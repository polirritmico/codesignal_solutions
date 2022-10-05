#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from bishopAndPawn import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        bishop = "a1"
        pawn = "c3"
        expected = True
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        bishop = "h1"
        pawn = "h3"
        expected = False
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        bishop = "h1"
        pawn = "h3"
        expected = False
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        bishop = "a5"
        pawn = "c3"
        expected = True
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        bishop = "e7"
        pawn = "d6"
        expected = True
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

