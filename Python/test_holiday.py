#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from holiday import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        x = 3
        week_day = "Wednesday"
        month = "November"
        year_number = 2016
        expected = 16
        output = solution(x, week_day, month, year_number)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        x = 5
        week_day = "Thursday"
        month = "November"
        year_number = 2016
        expected = -1
        output = solution(x, week_day, month, year_number)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        x = 1
        week_day = "Thursday"
        month = "January"
        year_number = 2015
        expected = 1
        output = solution(x, week_day, month, year_number)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        x = 2
        week_day = "Thursday"
        month = "January"
        year_number = 2015
        expected = 8
        output = solution(x, week_day, month, year_number)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        x = 3
        week_day = "Thursday"
        month = "January"
        year_number = 2015
        expected = 15
        output = solution(x, week_day, month, year_number)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        x = 3
        week_day = "Thursday"
        month = "January"
        year_number = 2101
        expected = 20
        output = solution(x, week_day, month, year_number)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        x = 3
        week_day = "Thursday"
        month = "January"
        year_number = 2401
        expected = 18
        output = solution(x, week_day, month, year_number)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        x = 2
        week_day = "Thursday"
        month = "December"
        year_number = 2500
        expected = 9
        output = solution(x, week_day, month, year_number)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        x = 5
        week_day = "Monday"
        month = "February"
        year_number = 2016
        expected = 29
        output = solution(x, week_day, month, year_number)
        self.assertEqual(output, expected)
