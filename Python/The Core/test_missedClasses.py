#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from missedClasses import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        year = 2015
        days_of_the_week = [2, 3]
        holidays = ["11-04", "02-22", "02-23", "03-07", "03-08", "05-09"]
        expected = 3
        output = solution(year, days_of_the_week, holidays)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        year = 1900
        days_of_the_week = []
        holidays = []
        expected = 0
        output = solution(year, days_of_the_week, holidays)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        year = 2100
        days_of_the_week = [1, 4, 7]
        holidays = [
            "10-28",
            "05-03",
            "10-02",
            "05-07",
            "05-25",
            "09-04",
            "10-30",
            "03-03",
            "09-02",
            "11-08",
        ]
        expected = 4
        output = solution(year, days_of_the_week, holidays)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        year = 1956
        days_of_the_week = [1, 4, 6, 7]
        holidays = [
            "03-17",
            "04-03",
            "03-08",
            "09-18",
            "05-28",
            "02-14",
            "10-20",
            "01-02",
            "01-22",
            "10-04",
            "02-02",
            "10-07",
            "09-30",
            "05-20",
            "05-23",
            "09-22",
            "01-12",
            "05-02",
            "10-21",
            "03-20",
        ]
        expected = 13
        output = solution(year, days_of_the_week, holidays)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        year = 2067
        days_of_the_week = [1, 2, 3, 4, 5, 6, 7]
        holidays = [
            "01-20",
            "02-09",
            "01-25",
            "09-01",
            "05-30",
            "12-24",
            "09-05",
            "10-15",
            "09-25",
            "10-23",
            "10-10",
            "05-29",
            "02-05",
            "11-19",
            "04-28",
            "02-17",
            "05-04",
            "01-26",
            "05-31",
            "03-19",
            "12-31",
            "09-26",
            "05-19",
            "05-14",
            "09-03",
            "05-21",
            "02-08",
            "11-09",
            "09-09",
            "04-21",
        ]
        expected = 30
        output = solution(year, days_of_the_week, holidays)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        year = 2000
        days_of_the_week = []
        holidays = []
        expected = 0
        output = solution(year, days_of_the_week, holidays)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        year = 1995
        days_of_the_week = [1, 2, 3]
        holidays = [
            "10-28",
            "05-26",
            "09-24",
            "11-28",
            "09-17",
            "03-29",
            "09-08",
            "05-13",
            "10-23",
            "11-29",
            "04-26",
            "10-27",
            "09-26",
            "09-09",
            "12-07",
        ]
        expected = 5
        output = solution(year, days_of_the_week, holidays)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        year = 2045
        days_of_the_week = [1, 2, 3, 5]
        holidays = [
            "11-12",
            "09-10",
            "11-10",
            "05-12",
            "05-03",
            "03-04",
            "02-14",
            "12-25",
            "09-24",
            "11-17",
            "09-22",
            "09-14",
            "12-04",
            "01-24",
            "03-24",
            "05-26",
            "09-01",
            "11-20",
            "04-30",
            "03-20",
            "10-04",
            "11-21",
            "01-14",
            "05-11",
            "12-03",
            "11-01",
        ]
        expected = 15
        output = solution(year, days_of_the_week, holidays)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        year = 2014
        days_of_the_week = [2, 3]
        holidays = ["11-04", "02-22", "02-23", "03-07", "03-08", "05-09"]
        expected = 1
        output = solution(year, days_of_the_week, holidays)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        year = 2100
        days_of_the_week = []
        holidays = []
        expected = 0
        output = solution(year, days_of_the_week, holidays)
        self.assertEqual(output, expected)
