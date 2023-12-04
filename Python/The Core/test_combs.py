#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from combs import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        comb_a = "*..*"
        comb_b = "*.*"
        expected = 5
        output = solution(comb_a, comb_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        comb_a = "*...*"
        comb_b = "*.*"
        expected = 5
        output = solution(comb_a, comb_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        comb_a = "*..*.*"
        comb_b = "*.***"
        expected = 9
        output = solution(comb_a, comb_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        comb_a = "*.*"
        comb_b = "*.*"
        expected = 4
        output = solution(comb_a, comb_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        comb_a = "*.**"
        comb_b = "*.*"
        expected = 5
        output = solution(comb_a, comb_b)
        self.assertEqual(output, expected)
