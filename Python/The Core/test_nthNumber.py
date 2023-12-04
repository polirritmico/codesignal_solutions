#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from nthNumber import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        s = "8one 003number 201numbers li-000233le number444"
        n = 4
        expected = "233"
        output = solution(s, n)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        s = "some023020 num ber 033 02103 32 meh peh beh 4328 "
        n = 5
        expected = "4328"
        output = solution(s, n)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        s = "007 is an awesome agent"
        n = 1
        expected = "7"
        output = solution(s, n)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        s = "Everyone hates error 404"
        n = 1
        expected = "404"
        output = solution(s, n)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        s = "LaS003920tP3rEt4t04Yte0023s3t"
        n = 4
        expected = "4"
        output = solution(s, n)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        s = "=_aaYiM*}&0077|D))ztIV00012432748730156644204805614898523099655216oio0854102350044141_|YDL0584511290939644184700867021026771007612398051168360441323oIc:G*0204864749576405915~wqgN0037594999439741539584332{F&wjxiLy-mE"
        n = 4
        expected = "584511290939644184700867021026771007612398051168360441323"
        output = solution(s, n)
        self.assertEqual(output, expected)
