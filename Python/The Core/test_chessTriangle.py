#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from chessTriangle import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        n = 2
        m = 3
        expected = 8
        output = solution(n, m)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        n = 1
        m = 30
        expected = 0
        output = solution(n, m)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        n = 3
        m = 3
        expected = 48
        output = solution(n, m)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        n = 2
        m = 2
        expected = 0
        output = solution(n, m)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        n = 5
        m = 2
        expected = 40
        output = solution(n, m)
        self.assertEqual(output, expected)
