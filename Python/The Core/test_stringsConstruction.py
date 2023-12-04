#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from stringsConstruction import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        a = "abc"
        b = "abccba"
        expected = 2
        output = solution(a, b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        a = "ab"
        b = "abcbcb"
        expected = 1
        output = solution(a, b)
        self.assertEqual(output, expected)
