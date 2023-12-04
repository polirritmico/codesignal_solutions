#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from polygonPerimeter import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [[False, True, True], [True, True, False], [True, False, False]]
        expected = 12
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [[True, True, True], [True, False, True], [True, True, True]]
        expected = 16
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [[True, True, True, True, True], [True, True, True, True, True]]
        expected = 14
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [[False, True, True], [True, True, False], [True, True, False]]
        expected = 12
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [
            [False, False, True, False],
            [False, True, True, True],
            [True, True, False, True],
            [True, False, True, True],
        ]
        expected = 22
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [
            [False, False, True, False, False],
            [False, True, True, True, True],
            [True, True, False, True, True],
            [True, False, True, True, True],
        ]
        expected = 24
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = [
            [False, False, False, False, False],
            [False, True, True, True, True],
            [True, True, False, False, True],
            [True, False, True, True, True],
        ]
        expected = 24
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = [
            [False, False, True, False, False],
            [False, True, True, True, False],
            [True, True, False, True, True],
            [False, False, True, True, False],
        ]
        expected = 22
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = [
            [False, False, True, True, True],
            [False, True, True, False, True],
            [False, True, False, True, True],
            [True, True, False, True, False],
            [True, False, True, True, False],
        ]
        expected = 32
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = [[False, False, False], [False, True, False], [False, False, False]]
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)
