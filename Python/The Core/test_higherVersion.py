#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from higherVersion import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        ver_a = "1.2.2"
        ver_b = "1.2.0"
        expected = True
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        ver_a = "1.0.5"
        ver_b = "1.1.0"
        expected = False
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        ver_a = "1.1.0"
        ver_b = "1.1.5"
        expected = False
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        ver_a = "10"
        ver_b = "9"
        expected = True
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        ver_a = "1.0.10"
        ver_b = "1.1.5"
        expected = False
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        ver_a = "5"
        ver_b = "1"
        expected = True
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        ver_a = "1.1.10"
        ver_b = "1.2.0"
        expected = False
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        ver_a = "1.2.2"
        ver_b = "1.2.10"
        expected = False
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        ver_a = "1.10.2"
        ver_b = "1.2.10"
        expected = True
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        ver_a = "0"
        ver_b = "0"
        expected = False
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case11(self):
        ver_a = "4.3.22.1"
        ver_b = "4.3.22.1"
        expected = False
        output = solution(ver_a, ver_b)
        self.assertEqual(output, expected)
