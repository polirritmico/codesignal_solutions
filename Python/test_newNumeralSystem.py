#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from newNumeralSystem import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "G"
        expected = ["A + G", "B + F", "C + E", "D + D"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "A"
        expected = ["A + A"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "D"
        expected = ["A + D", "B + C"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "E"
        expected = ["A + E", "B + D", "C + C"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "F"
        expected = ["A + F", "B + E", "C + D"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "I"
        expected = ["A + I", "B + H", "C + G", "D + F", "E + E"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "K"
        expected = ["A + K", "B + J", "C + I", "D + H", "E + G", "F + F"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "L"
        expected = ["A + L", "B + K", "C + J", "D + I", "E + H", "F + G"]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = "O"
        expected = [
            "A + O",
            "B + N",
            "C + M",
            "D + L",
            "E + K",
            "F + J",
            "G + I",
            "H + H",
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = "P"
        expected = [
            "A + P",
            "B + O",
            "C + N",
            "D + M",
            "E + L",
            "F + K",
            "G + J",
            "H + I",
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case11(self):
        case = "S"
        expected = [
            "A + S",
            "B + R",
            "C + Q",
            "D + P",
            "E + O",
            "F + N",
            "G + M",
            "H + L",
            "I + K",
            "J + J",
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case12(self):
        case = "T"
        expected = [
            "A + T",
            "B + S",
            "C + R",
            "D + Q",
            "E + P",
            "F + O",
            "G + N",
            "H + M",
            "I + L",
            "J + K",
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case13(self):
        case = "W"
        expected = [
            "A + W",
            "B + V",
            "C + U",
            "D + T",
            "E + S",
            "F + R",
            "G + Q",
            "H + P",
            "I + O",
            "J + N",
            "K + M",
            "L + L",
        ]
        output = solution(case)
        self.assertEqual(output, expected)
