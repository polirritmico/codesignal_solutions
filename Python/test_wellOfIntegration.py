#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from wellOfIntegration import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = 6
        expected = [1, 3]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = 2
        expected = [1]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = 8
        expected = [0, 2, 4]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = 4
        expected = [0, 2]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = 44
        expected = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
        output = solution(case)
        self.assertEqual(output, expected)
