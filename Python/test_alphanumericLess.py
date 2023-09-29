#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from alphanumericLess import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        sA = "a"
        sB = "a1"
        expected = True
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        sA = "ab"
        sB = "a1"
        expected = False
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        sA = "b"
        sB = "a1"
        expected = False
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        sA = "x11y012"
        sB = "x011y13"
        expected = True
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        sA = "ab123"
        sB = "ab34z"
        expected = False
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        sA = "0000"
        sB = "000"
        expected = True
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        sA = "10"
        sB = "01"
        expected = False
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        sA = "ab000144"
        sB = "ab144"
        expected = True
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        sA = "ab"
        sB = "a"
        expected = False
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        sA = "000"
        sB = "0000"
        expected = False
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case11(self):
        sA = "abc123"
        sB = "abc123"
        expected = False
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case12(self):
        sA = "zza1233"
        sB = "zza1234"
        expected = True
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case13(self):
        sA = "zzz1"
        sB = "zzz1"
        expected = False
        output = solution(sA, sB)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case14(self):
        sA = "00"
        sB = "a2"
        expected = True
        output = solution(sA, sB)
        self.assertEqual(output, expected)
