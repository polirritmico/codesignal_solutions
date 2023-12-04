#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from htmlEndTagByStartTag import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "<button type='button' disabled>"
        expected = "</button>"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case2(self):
        case = "<i>"
        expected = "</i>"
        output = solution(case)
        self.assertEqual(output, expected)
