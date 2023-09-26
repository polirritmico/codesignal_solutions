#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from cipher26 import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "taiaiaertkixquxjnfxxdh"
        expected = "thisisencryptedmessage"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "ibttlprimfymqlpgeftwu"
        expected = "itsasecrettoeverybody"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "ftnexvoky"
        expected = "fourtytwo"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "taevzhzmashvjw"
        expected = "thereisnospoon"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "abdgkpvcktdoanbqgxpicxtqon"
        expected = "abcdefghijklmnopqrstuvwxyz"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "z"
        expected = "z"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "ta"
        expected = "th"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "tai"
        expected = "thi"
        output = solution(case)
        self.assertEqual(output, expected)
