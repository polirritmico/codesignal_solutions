#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from properNounCorrection import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "pARis"
        expected = "Paris"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case2(self):
        case = "this is a test"
        expected = "This is a test"
        output = solution(case)
        self.assertEqual(output, expected)
