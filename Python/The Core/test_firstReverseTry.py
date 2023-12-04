#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from firstReverseTry import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [1, 2, 3, 4, 5]
        expected = [5, 2, 3, 4, 1]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = []
        expected = []
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = [239]
        expected = [239]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = [23, 54, 12, 3, 4, 56, 23, 12, 5, 324]
        expected = [324, 54, 12, 3, 4, 56, 23, 12, 5, 23]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = [-1, 1]
        expected = [1, -1]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = [88, -101, -310, 818, 747, -888, -183, -687, -723, 188, -611,
                677, -597, 293, -295, -162, -265, 368, 346, 81, -831, 198, -94,
                685, -434, -241, -566, -397, 501, -183, 366, -669, 96, -592,
                358, 598, 444, -929, 769, -361, -754, 218, -464, 332, 893, 422,
                -192, -287, -850, 543]
        expected = [543, -101, -310, 818, 747, -888, -183, -687, -723, 188,
                -611, 677, -597, 293, -295, -162, -265, 368, 346, 81, -831,
                198, -94, 685, -434, -241, -566, -397, 501, -183, 366, -669,
                96, -592, 358, 598, 444, -929, 769, -361, -754, 218, -464, 332,
                893, 422, -192, -287, -850, 88]
        output = solution(case)
        self.assertEqual(output, expected)


