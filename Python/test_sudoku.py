#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from sudoku import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [[1,3,2,5,4,6,9,8,7], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [9,2,1,4,3,5,8,7,6], 
 [3,5,4,7,6,8,2,1,9], 
 [6,8,7,1,9,2,5,4,3], 
 [5,7,6,9,8,1,4,3,2], 
 [2,4,3,6,5,7,1,9,8], 
 [8,1,9,3,2,4,7,6,5]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = [[8,3,6,5,3,6,7,2,9], 
 [4,2,5,8,7,9,3,8,1], 
 [7,9,1,2,1,4,6,5,4], 
 [9,2,1,4,3,5,8,7,6], 
 [3,5,4,7,6,8,2,1,9], 
 [6,8,7,1,9,2,5,4,3], 
 [5,7,6,9,8,1,4,3,2], 
 [2,4,3,6,5,7,1,9,8], 
 [8,1,9,3,2,4,7,6,5]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = [[1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = [[1,3,4,2,5,6,9,8,7], 
 [4,6,8,5,7,9,3,2,1], 
 [7,9,2,8,1,3,6,5,4], 
 [9,2,3,1,4,5,8,7,6], 
 [3,5,7,4,6,8,2,1,9], 
 [6,8,1,7,9,2,5,4,3], 
 [5,7,6,9,8,1,4,3,2], 
 [2,4,5,6,3,7,1,9,8], 
 [8,1,9,3,2,4,7,6,5]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = [[1,3,2,5,4,6,9,8,7], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [9,2,1,4,3,5,8,7,6], 
 [3,5,4,7,6,8,2,1,9], 
 [6,8,7,1,9,2,5,4,3], 
 [5,4,6,9,8,1,4,3,2], 
 [2,7,3,6,5,7,1,9,8], 
 [8,1,9,3,2,4,7,6,5]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = [[1,2,3,4,5,6,7,8,9], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [1,2,3,4,5,6,7,8,9], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [1,2,3,4,5,6,7,8,9], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


