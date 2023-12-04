#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from whoseTurn import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "b1;g1;b8;g8"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "c3;g1;b8;g8"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "g1;g2;g3;g4"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "f8;h1;f3;c2"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "a5;d3;c4;h3"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "f8;g1;h2;h5"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "a6;g1;a5;a4"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "g5;h1;a2;h5"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = "e1;f7;f8;b4"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = "g2;d7;h5;h1"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)
