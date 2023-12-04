#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from encloseInBrackets import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "abcdef"
        expected = "(abcdef)"
        output = solution(case)
        self.assertEqual(output, expected)
