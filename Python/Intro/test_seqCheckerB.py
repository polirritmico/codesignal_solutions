#d/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from seqChecker import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        array = [1, 99, 5, 6]
        expected = True
        output = solution(array)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        array = [1, 5, 4]
        expected = True
        output = solution(array)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        array = [1, 5, 4, 6]
        expected = True
        output = solution(array)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        array = [1, 5, 4, 3]
        expected = False
        output = solution(array)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        array = [1, 3, 2, 1]
        expected = False
        output = solution(array)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        array = [1, 2, 1, 2]
        expected = False
        output = solution(array)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case7(self):
        array = [3, 6, 5, 8, 10, 20, 15]
        expected = False
        output = solution(array)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case8(self):
        array = [10, 1, 2, 3, 4, 5]
        expected = True
        output = solution(array)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case9(self):
        array = [1, 2, 3, 4, 3, 6]
        expected = True
        output = solution(array)
        self.assertEqual(output, expected)

