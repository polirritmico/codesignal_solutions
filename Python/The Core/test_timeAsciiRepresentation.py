#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# from timeAsciiRepresentation import hour_and_minutes_clock_angles, solution,
import timeAsciiRepresentation as S


@unittest.skip
class TestCustom(unittest.TestCase):
    def test_clock_angles1(self):
        case_hour = 1
        case_minutes = 30
        expected_hour = 45
        expected_minutes = 270

        output = S.hour_and_minutes_clock_angles((case_hour, case_minutes))
        self.assertEqual(output[1], expected_minutes)
        self.assertEqual(output[0], expected_hour)

    def test_clock_angles2(self):
        case_hour = 12
        case_minutes = 15
        expected_hour = 83
        expected_minutes = 0

        output = S.hour_and_minutes_clock_angles((case_hour, case_minutes))
        self.assertEqual(output[1], expected_minutes)
        self.assertEqual(output[0], expected_hour)

    def test_clock_angles3(self):
        case_hour = 21
        case_minutes = 0
        expected_hour = 180
        expected_minutes = 90

        output = S.hour_and_minutes_clock_angles((case_hour, case_minutes))
        self.assertEqual(output[1], expected_minutes)
        self.assertEqual(output[0], expected_hour)


# @unittest.skip
class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        # fmt: off
        case = [
            [".", "*", "*", "*", ".", ".", "*", ".", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ":", ".", "*", "*", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", "*", "*", "*", ".", ".", "*", ".", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
        ]
        expected = [
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", "."],
            [".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", "*", "."],
            ["*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", "*", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", "*", "*"],
            [".", "*", "*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*", "*", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", "*", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", "*", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
        ]
        output = S.solution(case)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        # fmt: off
        case = [
            [".", "*", "*", "*", ".", "*", "*", "*", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ":", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", "*", "*", "*", ".", "*", "*", "*", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
        ]
        expected = [
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", "*", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", "*", ".", "."],
            [".", "*", "*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*", "*", "."],
            ["*", "*", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", "*", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*"],
            [".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
        ]
        output = S.solution(case)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        # fmt: off
        case = [
            [".", "*", "*", "*", ".", "*", "*", "*", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
            [".", ".", ".", "*", ".", ".", ".", "*", ".", ".", "*", ".", ".", ".", "*", ".", "*"],
            [".", ".", ".", "*", ".", ".", ".", "*", ".", ".", "*", ".", ".", ".", "*", ".", "*"],
            [".", ".", ".", "*", ".", ".", ".", "*", ".", ".", "*", ".", ".", ".", "*", ".", "*"],
            [".", ".", ".", "*", ".", ".", ".", "*", ".", ".", "*", ".", ".", ".", "*", ".", "*"],
            [".", ".", ".", "*", ".", ".", ".", "*", ".", ".", "*", ".", ".", ".", "*", ".", "*"],
            [".", ".", ".", "*", ".", ".", ".", "*", ".", ".", "*", ".", ".", ".", "*", ".", "*"],
            [".", ".", ".", "*", ".", ".", ".", "*", ".", ".", "*", ".", ".", ".", "*", ".", "*"],
            [".", "*", "*", "*", ".", "*", "*", "*", ":", ".", "*", "*", "*", ".", "*", "*", "*"],
            [".", "*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", "*", "*", "*", ".", "*", "*", "*", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
        ]
        expected = [
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", "*", "*", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", "*", "*", ".", ".", ".", "*", "*", ".", ".", ".", ".", "*", "*", ".", "."],
            [".", "*", "*", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", "*", "*", "."],
            ["*", "*", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", "*", "*"],
            ["*", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*"],
            [".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
        ]
        output = S.solution(case)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        # fmt: off
        case = [
            [".", ".", "*", ".", ".", "*", "*", "*", ".", ".", "*", ".", "*", ".", "*", "*", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", "*", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ":", ".", "*", "*", "*", ".", "*", "*", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", "*", ".", "*"],
            [".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", "*", ".", "*", "*", "*"],
        ]
        expected = [
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", "."],
            [".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", "."],
            ["*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*"],
            ["*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", "*", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", "*", "*", "*", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", "*", "*", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", "*", "*"],
            [".", "*", "*", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", "*", "*", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", "*", "*", ".", ".", ".", "*", "*", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", ".", "*", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
        ]
        output = S.solution(case)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        # fmt: off
        case = [
            [".", ".", "*", ".", ".", "*", "*", "*", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
            [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", "*", "*", ":", ".", "*", "*", "*", ".", "*", "*", "*"],
            [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
            [".", ".", "*", ".", ".", "*", "*", "*", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
        ]
        expected = [
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", "."],
            [".", "*", "*", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", "."],
            ["*", "*", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*"],
            ["*", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
            ["*", "*", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", "*", "*"],
            [".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", "*", "*", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", "*", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
        ]
        output = S.solution(case)
        self.assertListEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        # fmt: off
        case = [
            [".", "*", "*", "*", ".", "*", "*", "*", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ":", ".", "*", ".", "*", ".", "*", "*", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", ".", "*", ".", "*", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", "*"],
            [".", "*", "*", "*", ".", "*", "*", "*", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
        ]
        expected = [
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", "*", ".", "*", "*", "*", "*", ".", ".", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", "*", ".", "*", ".", ".", "*", "*", ".", "."],
            [".", "*", "*", ".", ".", ".", ".", ".", "*", "*", "*", ".", ".", ".", "*", "*", "."],
            ["*", "*", ".", ".", ".", ".", ".", ".", "*", "*", "*", ".", ".", ".", ".", "*", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*"],
            [".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", "."],
            [".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", "."],
            [".", ".", ".", "*", "*", ".", ".", ".", ".", ".", ".", ".", "*", "*", ".", ".", "."],
            [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
        ]
        output = S.solution(case)
        self.assertListEqual(output, expected)