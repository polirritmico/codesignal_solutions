#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from replaceAllDigitsRegExp import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "There are 12 points"
        expected = "There are ## points"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "012ss210"
        expected = "###ss###"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = " _Aas 23"
        expected = " _Aas ##"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "no digits here"
        expected = "no digits here"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = " aa_0239mehce3d"
        expected = " aa_####mehce#d"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "v z gv4zyx eu mu "
        expected = "v z gv#zyx eu mu "
        output = solution(case)
        self.assertEqual(output, expected)
