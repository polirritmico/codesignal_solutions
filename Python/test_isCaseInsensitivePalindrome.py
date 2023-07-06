#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from isCaseInsensitivePalindrome import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "AaBaa"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case2(self):
        case = "AaBaaa"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)
