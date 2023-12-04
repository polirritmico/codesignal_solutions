#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from decipher import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "10197115121"
        expected = "easy"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "98"
        expected = "b"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "122"
        expected = "z"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "1229897"
        expected = "zba"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "97989910010110210310410510610710810911011111211311411511611711811912012112297"
        expected = "abcdefghijklmnopqrstuvwxyza"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "10297115106108102108971061151041029897107106115981001029710711510010298"
        expected = "fasjlflajshfbakjsbdfaksdfb"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "11211111911310110810910097107108115111112119113101106107971101021101061021041149710511411497"
        expected = "powqelmdaklsopwqejkanfnjfhrairra"
        output = solution(case)
        self.assertEqual(output, expected)
