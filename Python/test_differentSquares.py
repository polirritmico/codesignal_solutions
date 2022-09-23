#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from differentSquares import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [[1,2,1], 
            [2,2,2],
            [2,2,2],
            [1,2,3],
            [2,2,1]]
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = [[9,9,9,9,9], 
            [9,9,9,9,9], 
            [9,9,9,9,9], 
            [9,9,9,9,9], 
            [9,9,9,9,9], 
            [9,9,9,9,9]]
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = [[3]]
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = [[3,4,5,6,7,8,9]]
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = [[3], 
            [4], 
            [5], 
            [6], 
            [7]]
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = [[2,5,3,4,3,1,3,2], 
            [4,5,4,1,2,4,1,3], 
            [1,1,2,1,4,1,1,5], 
            [1,3,4,2,3,4,2,4], 
            [1,5,5,2,1,3,1,1], 
            [1,2,3,3,5,1,2,4], 
            [3,1,4,4,4,1,5,5], 
            [5,1,3,3,1,5,3,5], 
            [5,4,4,3,5,4,4,4]]
        expected = 54
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case7(self):
        case = [[1,1,1,1,1,1,2,2,2,3,3,3,9,9,9,2,3,9]]
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)


