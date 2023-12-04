#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from houseNumbersSum import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [5, 1, 2, 3, 0, 1, 5, 0, 2]
        expected = 11
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [4, 2, 1, 6, 0]
        expected = 13
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [4, 1, 2, 3, 0, 10, 2]
        expected = 10
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [0, 1, 2, 3, 0]
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [5, 1, 1, 3, 0, 1, 5, 0, 2]
        expected = 10
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
        expected = 90
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = [10, 10, 10, 10, 10, 10, 10, 10, 0, 10]
        expected = 80
        output = solution(case)
        self.assertEqual(output, expected)
