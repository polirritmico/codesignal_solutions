#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from regularMonths import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "02-2016"
        expected = "08-2016"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "05-2027"
        expected = "11-2027"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "09-2099"
        expected = "02-2100"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "01-1970"
        expected = "06-1970"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "07-2024"
        expected = "09-2025"
        output = solution(case)
        self.assertEqual(output, expected)
