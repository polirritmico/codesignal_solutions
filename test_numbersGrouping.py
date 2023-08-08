#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from numbersGrouping import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [20000, 239, 10001, 999999, 10000, 20566, 29999]
        expected = 11
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [
            10000,
            20000,
            30000,
            40000,
            50000,
            60000,
            10000,
            120000,
            150000,
            200000,
            300000,
            1000000,
            10000000,
            100000000,
            10000000,
        ]
        expected = 28
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [10000]
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [10000, 1]
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [
            685400881,
            696804468,
            696804942,
            803902442,
            976412678,
            976414920,
            47763597,
            803900633,
            233144924,
            47764349,
            233149077,
            214990733,
            214994039,
            280528089,
            280524347,
            685401797,
        ]
        expected = 24
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [
            598589004,
            92986320,
            520103781,
            808743817,
            635098665,
            95244159,
            808747008,
            867017063,
            635092226,
            867013865,
            92989995,
            520100093,
            95245838,
            84897101,
            598583113,
            84893918,
        ]
        expected = 24
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = [
            1000000000,
            999990000,
            999980000,
            999970000,
            999960000,
            999950000,
            999940000,
            999930000,
            999920000,
            999910000,
        ]
        expected = 20
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = [
            102382103,
            21039898,
            39823,
            433,
            30928398,
            40283209,
            23234,
            342534,
            98473483,
            498398424,
            9384984,
            9839239,
        ]
        expected = 24
        output = solution(case)
        self.assertEqual(output, expected)
