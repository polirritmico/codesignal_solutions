#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from addBorder import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = ["abc", "ded"]
        expected = ["*****", "*abc*", "*ded*", "*****"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = ["a"]
        expected = ["***", "*a*", "***"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = ["aa", "**", "zz"]
        expected = ["****", "*aa*", "****", "*zz*", "****"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"]
        expected = [
            "*******",
            "*abcde*",
            "*fghij*",
            "*klmno*",
            "*pqrst*",
            "*uvwxy*",
            "*******",
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = ["wzy**"]
        expected = ["*******", "*wzy***", "*******"]
        output = solution(case)
        self.assertEqual(output, expected)
