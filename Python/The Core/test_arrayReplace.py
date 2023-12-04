#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from arrayReplace import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        input_array = [1, 2, 1]
        elem_to_replace = 1
        substitution_elem = 3
        expected = [3, 2, 3]
        output = solution(input_array, elem_to_replace, substitution_elem)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        input_array = [1, 2, 3, 4, 5]
        elem_to_replace = 3
        substitution_elem = 0
        expected = [1, 2, 0, 4, 5]
        output = solution(input_array, elem_to_replace, substitution_elem)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        input_array = [1, 1, 1]
        elem_to_replace = 1
        substitution_elem = 10
        expected = [10, 10, 10]
        output = solution(input_array, elem_to_replace, substitution_elem)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        input_array = [1, 2, 1, 2, 1]
        elem_to_replace = 2
        substitution_elem = 1
        expected = [1, 1, 1, 1, 1]
        output = solution(input_array, elem_to_replace, substitution_elem)
        self.assertEqual(output, expected)


