#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from curiousClock import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        some_time = "2016-08-26 22:40"
        leaving_time = "2016-08-29 10:00"
        expected = "2016-08-24 11:20"
        output = solution(some_time, leaving_time)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        some_time = "2016-08-26 22:40"
        leaving_time = "2016-08-26 22:41"
        expected = "2016-08-26 22:39"
        output = solution(some_time, leaving_time)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        some_time = "2015-01-14 09:12"
        leaving_time = "2015-11-04 17:36"
        expected = "2014-03-26 00:48"
        output = solution(some_time, leaving_time)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        some_time = "2016-02-28 12:21"
        leaving_time = "2016-03-01 22:21"
        expected = "2016-02-26 02:21"
        output = solution(some_time, leaving_time)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        some_time = "1995-05-30 13:48"
        leaving_time = "2016-04-22 05:32"
        expected = "1974-07-06 22:04"
        output = solution(some_time, leaving_time)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        some_time = "1992-09-29 00:00"
        leaving_time = "1998-12-04 23:59"
        expected = "1986-07-25 00:01"
        output = solution(some_time, leaving_time)
        self.assertEqual(output, expected)
