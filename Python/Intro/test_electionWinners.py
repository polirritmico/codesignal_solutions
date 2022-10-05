#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from electionWinners import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        votes = [2, 3, 5, 2]
        k = 3
        expected = 2
        output = solution(votes, k)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        votes = [1, 3, 3, 1, 1]
        k = 0
        expected = 0
        output = solution(votes, k)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        votes = [5, 1, 3, 4, 1]
        k = 0
        expected = 1
        output = solution(votes, k)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        votes = [1, 1, 1, 1]
        k = 1
        expected = 4
        output = solution(votes, k)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        votes = [1, 1, 1, 1]
        k = 0
        expected = 0
        output = solution(votes, k)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        votes = [3, 1, 1, 3, 1]
        k = 2
        expected = 2
        output = solution(votes, k)
        self.assertEqual(output, expected)


