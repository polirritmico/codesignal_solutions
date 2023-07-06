#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from isTandemRepeat import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "tandemtandem"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case2(self):
        case = "qqq"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case3(self):
        case = "2w2ww"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case4(self):
        case = "interestinterest"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)
