#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from newYearCelebrations import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        take_off_time = "23:35"
        minutes = [60, 90, 140]
        expected = 3
        output = solution(take_off_time, minutes)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        take_off_time = "00:00"
        minutes = [60, 120, 180, 250]
        expected = 4
        output = solution(take_off_time, minutes)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        take_off_time = "13:36"
        minutes = [23, 33, 45, 56, 66, 88]
        expected = 1
        output = solution(take_off_time, minutes)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        take_off_time = "22:50"
        minutes = []
        expected = 1
        output = solution(take_off_time, minutes)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        take_off_time = "20:18"
        minutes = [222, 342]
        expected = 3
        output = solution(take_off_time, minutes)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        take_off_time = "12:05"
        minutes = [
            1,
            109,
            113,
            344,
            345,
            478,
            545,
            565,
            809,
            814,
            838,
            883,
            971,
            1007,
            1029,
            1053,
            1133,
            1271,
            1314,
            1500,
        ]
        expected = 1
        output = solution(take_off_time, minutes)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        take_off_time = "17:10"
        minutes = [150, 160, 293, 589, 614, 716, 760, 776, 781, 911, 1040, 1438]
        expected = 3
        output = solution(take_off_time, minutes)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        take_off_time = "18:15"
        minutes = [117, 241, 364, 375, 545, 1317]
        expected = 1
        output = solution(take_off_time, minutes)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        take_off_time = "19:44"
        minutes = [545, 1320]
        expected = 1
        output = solution(take_off_time, minutes)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        take_off_time = "21:13"
        minutes = [52, 257, 323, 515, 579, 600, 703, 707, 1127, 1298]
        expected = 3
        output = solution(take_off_time, minutes)
        self.assertEqual(output, expected)
