#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from validTime import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "13:58"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "25:51"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "02:76"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "24:00"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "02:61"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "27:00"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "19:66"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "12:31"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = "25:73"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = "09:56"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case11(self):
        case = "03:29"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)
