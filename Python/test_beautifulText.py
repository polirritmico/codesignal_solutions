#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from beautifulText import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        string = "Look at this example of a correct text"
        lf = 5
        r = 15
        expected = True
        output = solution(string, lf, r)
        self.assertEqual(output, expected)

    def test_case2(self):
        string = "abc def ghi"
        lf = 4
        r = 10
        expected = False
        output = solution(string, lf, r)
        self.assertEqual(output, expected)

    def test_case3(self):
        string = "a a a a a a a a"
        lf = 1
        r = 10
        expected = True
        output = solution(string, lf, r)
        self.assertEqual(output, expected)

    def test_case4(self):
        string = "ab cd fg xyz"
        lf = 1
        r = 5
        expected = False
        output = solution(string, lf, r)
        self.assertEqual(output, expected)

    def test_case5(self):
        string = "aa aa aaaaa aaaaa aaaaa"
        lf = 6
        r = 11
        expected = True
        output = solution(string, lf, r)
        self.assertEqual(output, expected)

    def test_case6(self):
        string = "aa aa aaaaa aaaaa aaaaa"
        lf = 5
        r = 10
        expected = True
        output = solution(string, lf, r)
        self.assertEqual(output, expected)

    def test_case7(self):
        string = "aa aa aaaaa aaaaa aaaaa"
        lf = 6
        r = 10
        expected = False
        output = solution(string, lf, r)
        self.assertEqual(output, expected)

    def test_case8(self):
        string = "aaa aaaaaaa"
        lf = 3
        r = 10
        expected = False
        output = solution(string, lf, r)
        self.assertEqual(output, expected)

    def test_case9(self):
        string = "dht skq dkg"
        lf = 4
        r = 10
        expected = False
        output = solution(string, lf, r)
        self.assertEqual(output, expected)

    def test_case10(self):
        string = "skspv iakqh ygzwz ntkmi xqhpj"
        lf = 3
        r = 7
        expected = True
        output = solution(string, lf, r)
        self.assertEqual(output, expected)

    def test_case11(self):
        string = "skspv iakqh ygzwz ntkmi xqhpj"
        lf = 8
        r = 9
        expected = False
        output = solution(string, lf, r)
        self.assertEqual(output, expected)
