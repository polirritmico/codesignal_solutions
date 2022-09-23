#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from lineEncoding import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "aabbbc"
        expected = "2a3bc"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "abbcabb"
        expected = "a2bca2b"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "abcd"
        expected = "abcd"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "zzzz"
        expected = "4z"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = "wwwwwwwawwwwwww"
        expected = "7wa7w"
        output = solution(case)
        self.assertEqual(output, expected)


