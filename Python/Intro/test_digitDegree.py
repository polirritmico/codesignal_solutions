#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from digitDegree import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 5
        expected = 0
        output = solution(case)
        print("Case: {}".format(case))
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = 100
        expected = 1
        output = solution(case)
        print("Case: {}".format(case))
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = 91
        expected = 2
        output = solution(case)
        print("Case: {}".format(case))
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = 99
        expected = 2
        output = solution(case)
        print("Case: {}".format(case))
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = 1000000000
        expected = 1
        output = solution(case)
        print("Case: {}".format(case))
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = 9
        expected = 0
        output = solution(case)
        print("Case: {}".format(case))
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case8(self):
        case = 877
        expected = 2
        output = solution(case)
        print("Case: {}".format(case))
        self.assertEqual(output, expected)

