#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from digitDifferenceSort import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [152, 23, 7, 887, 243]
        expected = [7, 887, 23, 243, 152]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = []
        expected = []
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [
            561,
            798,
            132,
            339,
            218,
            724,
            462,
            332,
            9,
            343,
            592,
            34,
            95,
            292,
            626,
            970,
        ]
        expected = [
            9,
            34,
            343,
            332,
            132,
            798,
            626,
            95,
            462,
            724,
            561,
            339,
            292,
            592,
            218,
            970,
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [
            8,
            76,
            7,
            26,
            7,
            60,
            87,
            77,
            72,
            61,
            13,
            60,
            8,
            32,
            48,
            63,
            82,
            56,
            17,
            18,
            28,
            85,
            95,
            69,
            95,
        ]
        expected = [
            8,
            77,
            7,
            7,
            8,
            56,
            32,
            87,
            76,
            13,
            69,
            85,
            63,
            95,
            95,
            48,
            26,
            61,
            72,
            28,
            17,
            82,
            60,
            60,
            18,
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [
            714,
            13,
            804,
            419,
            97,
            850,
            440,
            215,
            836,
            408,
            743,
            131,
            364,
            846,
            80,
            403,
            720,
            618,
            118,
            892,
            711,
            682,
            427,
            949,
            624,
        ]
        expected = [
            131,
            97,
            13,
            364,
            624,
            403,
            846,
            743,
            215,
            440,
            949,
            427,
            836,
            682,
            711,
            714,
            892,
            118,
            618,
            720,
            80,
            408,
            850,
            419,
            804,
        ]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [
            13098,
            1308,
            12398,
            52433,
            213,
            424,
            213,
            243,
            12213,
            54234,
            99487,
            81892,
            1,
            97897,
        ]
        expected = [
            1,
            97897,
            12213,
            243,
            213,
            424,
            213,
            54234,
            52433,
            99487,
            81892,
            12398,
            1308,
            13098,
        ]
        output = solution(case)
        self.assertEqual(output, expected)
