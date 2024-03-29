#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from correctNonogram import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        size = 5
        nonogram_field = [
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "2", "2", "1", "-", "1"],
            ["-", "-", "-", "2", "1", "1", "3", "3"],
            ["-", "3", "1", "#", "#", "#", ".", "#"],
            ["-", "-", "2", "#", "#", ".", ".", "."],
            ["-", "-", "2", ".", ".", ".", "#", "#"],
            ["-", "1", "2", "#", ".", ".", "#", "#"],
            ["-", "-", "5", "#", "#", "#", "#", "#"],
        ]
        expected = True
        output = solution(size, nonogram_field)
        self.assertEqual(output, expected)

    # @unittest.skip

    def test_case2(self):
        size = 5
        nonogram_field = [
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "1", "-", "-"],
            ["-", "-", "-", "3", "3", "2", "5", "5"],
            ["-", "-", "3", ".", ".", ".", "#", "#"],
            ["-", "2", "2", "#", "#", "#", "#", "#"],
            ["-", "-", "5", "#", "#", "#", "#", "#"],
            ["-", "-", "5", "#", "#", "#", "#", "#"],
            ["-", "-", "2", ".", ".", ".", "#", "#"],
        ]
        expected = False
        output = solution(size, nonogram_field)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        size = 5
        nonogram_field = [
            ["-", "-", "-", "-", "-", "1", "-", "-"],
            ["-", "-", "-", "-", "-", "1", "-", "1"],
            ["-", "-", "-", "1", "2", "1", "5", "1"],
            ["-", "-", "3", "#", "#", "#", ".", "."],
            ["-", "2", "1", ".", "#", "#", ".", "#"],
            ["-", "-", "3", ".", ".", "#", "#", "#"],
            ["-", "-", "2", ".", ".", "#", "#", "."],
            ["-", "-", "2", ".", ".", "#", "#", "."],
        ]
        expected = False
        output = solution(size, nonogram_field)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        size = 5
        nonogram_field = [
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "5", "4", "5", "4", "5"],
            ["-", "1", "3", "#", "#", "#", ".", "#"],
            ["-", "-", "5", "#", "#", "#", "#", "#"],
            ["-", "-", "5", "#", "#", "#", "#", "#"],
            ["-", "-", "5", "#", "#", "#", "#", "#"],
            ["-", "3", "1", "#", ".", "#", "#", "#"],
        ]
        expected = False
        output = solution(size, nonogram_field)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        size = 5
        nonogram_field = [
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "2"],
            ["-", "-", "-", "2", "2", "2", "4", "1"],
            ["-", "-", "-", ".", ".", ".", ".", "."],
            ["-", "-", "2", ".", ".", ".", "#", "#"],
            ["-", "-", "3", ".", ".", "#", "#", "#"],
            ["-", "-", "4", "#", "#", "#", "#", "."],
            ["-", "2", "2", ".", "#", "#", "#", "#"],
        ]
        expected = False
        output = solution(size, nonogram_field)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        size = 5
        nonogram_field = [
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "1", "-", "-", "-"],
            ["-", "-", "-", "1", "3", "1", "2", "1"],
            ["-", "-", "1", ".", "#", ".", ".", "."],
            ["-", "-", "-", ".", ".", ".", ".", "."],
            ["-", "-", "1", ".", "#", ".", ".", "."],
            ["-", "1", "2", ".", "#", ".", "#", "#"],
            ["-", "-", "4", "#", "#", "#", "#", "."],
        ]
        expected = True
        output = solution(size, nonogram_field)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        size = 9
        nonogram_field = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "4", "3", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "2", "2", "2", "1", "10", "3", "4", "2", "2"],
            ["-", "-", "-", "-", "1", ".", ".", ".", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "-", "5", ".", ".", "#", "#", "#", "#", "#", ".", "."],
            ["-", "-", "-", "-", "7", ".", "#", "#", "#", "#", "#", "#", "#", "."],
            ["-", "-", "-", "-", "9", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["1", "1", "1", "1", "1", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
            ["-", "-", "-", "-", "1", ".", ".", ".", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "-", "1", ".", ".", ".", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "1", "1", ".", ".", "#", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "-", "3", ".", ".", "#", "#", "#", ".", ".", ".", "."],
        ]
        expected = False
        output = solution(size, nonogram_field)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        size = 9
        nonogram_field = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "4", "3", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "2", "2", "2", "1", "9", "3", "4", "2", "2"],
            ["-", "-", "-", "-", "1", ".", ".", ".", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "-", "5", ".", ".", "#", "#", "#", "#", "#", ".", "."],
            ["-", "-", "-", "-", "7", ".", "#", "#", "#", "#", "#", "#", "#", "."],
            ["-", "-", "-", "-", "9", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["1", "1", "1", "1", "1", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
            ["-", "-", "-", "-", "1", ".", ".", ".", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "-", "1", ".", ".", ".", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "1", "1", ".", ".", "#", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "-", "3", ".", ".", "#", "#", "#", ".", ".", ".", "."],
        ]
        expected = True
        output = solution(size, nonogram_field)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        size = 9
        nonogram_field = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "4", "3", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "2", "2", "2", "1", "9", "3", "4", "2", "2"],
            ["-", "-", "-", "-", "1", ".", ".", ".", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "-", "5", ".", ".", "#", "#", "#", "#", "#", ".", "."],
            ["-", "-", "-", "-", "7", ".", "#", "#", "#", "#", "#", "#", "#", "."],
            ["-", "-", "-", "-", "9", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["1", "1", "1", "1", "1", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
            ["-", "-", "-", "-", "1", ".", ".", ".", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "-", "1", ".", ".", "#", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "1", "1", ".", ".", "#", ".", "#", ".", ".", ".", "."],
            ["-", "-", "-", "-", "3", ".", ".", "#", "#", "#", ".", ".", ".", "."],
        ]
        expected = False
        output = solution(size, nonogram_field)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        size = 10
        nonogram_field = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "1", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "1", "2", "1", "-", "-", "1", "1", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "4", "2", "1", "7", "1", "6", "4", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "2", "1", "4", "1", "8", "1", "1", "2", "1", "3"],
            ["-", "-", "-", "3", "3", "#", "#", "#", ".", "#", "#", "#", ".", ".", "."],
            ["-", "-", "-", "-", "1", ".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
            ["-", "-", "-", "-", "5", ".", "#", "#", "#", "#", "#", ".", ".", ".", "."],
            ["-", "-", "2", "4", "1", "#", "#", ".", "#", "#", "#", "#", ".", ".", "#"],
            ["-", "-", "-", "1", "7", "#", ".", ".", "#", "#", "#", "#", "#", "#", "#"],
            ["-", "-", "1", "5", "1", "#", ".", ".", "#", "#", "#", "#", "#", ".", "#"],
            ["-", "-", "-", "-", "7", "#", "#", "#", "#", "#", "#", "#", ".", ".", "."],
            ["-", "-", "-", "-", "5", ".", "#", "#", "#", "#", "#", ".", ".", ".", "."],
            ["-", "-", "1", "1", "1", "#", ".", "#", ".", "#", ".", ".", ".", ".", "."],
            ["-", "-", "-", "-", "7", "#", "#", "#", "#", "#", "#", "#", ".", ".", "."],
        ]
        expected = True
        output = solution(size, nonogram_field)
        self.assertEqual(output, expected)
