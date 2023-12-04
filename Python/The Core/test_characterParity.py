#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from characterParity import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "5"
        expected = "odd"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "8"
        expected = "even"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "q"
        expected = "not a digit"
        output = solution(case)
        self.assertEqual(output, expected)
