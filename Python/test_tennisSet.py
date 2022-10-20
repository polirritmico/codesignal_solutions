#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from tennisSet import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        score1 = 3
        score2 = 6
        expected = True
        output = solution(score1, score2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        score1 = 8
        score2 = 5
        expected = False
        output = solution(score1, score2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        score1 = 6
        score2 = 5
        expected = False
        output = solution(score1, score2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        score1 = 7
        score2 = 7
        expected = False
        output = solution(score1, score2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        score1 = 6
        score2 = 4
        expected = True
        output = solution(score1, score2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        score1 = 7
        score2 = 5
        expected = True
        output = solution(score1, score2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        score1 = 7
        score2 = 2
        expected = False
        output = solution(score1, score2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        score1 = 7
        score2 = 6
        expected = True
        output = solution(score1, score2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        score1 = 4
        score2 = 10
        expected = False
        output = solution(score1, score2)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case10(self):
        score1 = 0
        score2 = 0
        expected = False
        output = solution(score1, score2)
        self.assertEqual(output, expected)


