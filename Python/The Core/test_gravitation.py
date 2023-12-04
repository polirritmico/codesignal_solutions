#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from gravitation import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = ["#..##", ".##.#", ".#.##", "....."]
        expected = [1, 4]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = ["#..##", ".##.#", ".#.##", "..##."]
        expected = [1, 2, 3, 4]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = ["##", "..", "..", ".."]
        expected = [0, 1]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = ["#..#.", ".##..", ".#...", ".#..."]
        expected = [1, 4]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = ["#....", ".#..#", "..#..", "...#."]
        expected = [3]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = ["#.#..", ".####", "#.#..", "....."]
        expected = [2]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = ["######", "......", "......", ".....#"]
        expected = [5]
        output = solution(case)
        self.assertEqual(output, expected)
