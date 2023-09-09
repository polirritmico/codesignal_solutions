#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from numberOfClans import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        divisors = [2, 3]
        k = 6
        expected = 4
        output = solution(divisors, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        divisors = [2, 3, 4]
        k = 6
        expected = 5
        output = solution(divisors, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        divisors = [1, 3]
        k = 10
        expected = 2
        output = solution(divisors, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        divisors = [6, 2, 2, 8, 9, 2, 2, 2, 2]
        k = 10
        expected = 5
        output = solution(divisors, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        divisors = [2, 5]
        k = 9
        expected = 3
        output = solution(divisors, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        divisors = [1, 2, 3]
        k = 8
        expected = 4
        output = solution(divisors, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        divisors = [5, 6]
        k = 5
        expected = 2
        output = solution(divisors, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        divisors = [7, 1, 3, 4, 4]
        k = 5
        expected = 3
        output = solution(divisors, k)
        self.assertEqual(output, expected)
