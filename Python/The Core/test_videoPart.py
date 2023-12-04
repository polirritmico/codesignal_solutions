#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from videoPart import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        part = "02:20:00"
        total = "07:00:00"
        expected = [1, 3]
        output = solution(part, total)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        part = "25:26:20"
        total = "25:26:20"
        expected = [1, 1]
        output = solution(part, total)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        part = "00:02:20"
        total = "00:10:00"
        expected = [7, 30]
        output = solution(part, total)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        part = "08:08:08"
        total = "20:20:20"
        expected = [2, 5]
        output = solution(part, total)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        part = "00:00:07"
        total = "01:10:00"
        expected = [1, 600]
        output = solution(part, total)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        part = "07:32:29"
        total = "10:12:51"
        expected = [1597, 2163]
        output = solution(part, total)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        part = "01:41:59"
        total = "02:00:00"
        expected = [6119, 7200]
        output = solution(part, total)
        self.assertEqual(output, expected)
