#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from dayOfWeek import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "02-01-2016"
        expected = 5
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "01-01-1900"
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "02-29-2016"
        expected = 28
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "01-16-2027"
        expected = 11
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "10-12-2000"
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "02-29-2072"
        expected = 40
        output = solution(case)
        self.assertEqual(output, expected)
