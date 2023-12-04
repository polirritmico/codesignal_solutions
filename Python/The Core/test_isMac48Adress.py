#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from isMac48Adress import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "00-1B-63-84-45-E6"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case2(self):
        case = "Z1-1B-63-84-45-E6"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case3(self):
        case = "not a MAC-48 address"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)
