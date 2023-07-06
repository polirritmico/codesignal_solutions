#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from findEmailDomain import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "prettyandsimple@example.com"
        expected = "example.com"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case2(self):
        case = '" "@space.com'
        expected = "space.com"
        output = solution(case)
        self.assertEqual(output, expected)
