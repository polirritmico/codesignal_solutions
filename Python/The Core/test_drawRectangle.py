#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from drawRectangle import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        canvas = [
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
        ]
        rectangle = [1, 1, 4, 3]
        expected = [
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["a", "*", "-", "-", "*", "a", "a", "a"],
            ["a", "|", "a", "a", "|", "a", "a", "a"],
            ["b", "*", "-", "-", "*", "b", "b", "b"],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
        ]
        output = solution(canvas, rectangle)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        canvas = [
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
        ]
        rectangle = [0, 0, 1, 1]
        expected = [
            ["*", "*", "a", "a", "a", "a", "a", "a"],
            ["*", "*", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
        ]
        output = solution(canvas, rectangle)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        canvas = [
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
        ]
        rectangle = [0, 2, 7, 3]
        expected = [
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a", "a"],
            ["*", "-", "-", "-", "-", "-", "-", "*"],
            ["*", "-", "-", "-", "-", "-", "-", "*"],
        ]
        output = solution(canvas, rectangle)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        canvas = [["a", "a", "a"], ["a", "a", "a"], ["a", "a", "a"], ["b", "b", "b"]]
        rectangle = [0, 0, 2, 3]
        expected = [["*", "-", "*"], ["|", "a", "|"], ["|", "a", "|"], ["*", "-", "*"]]
        output = solution(canvas, rectangle)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        canvas = [["#", "#"], ["a", "a"], ["a", "a"], ["b", "b"]]
        rectangle = [0, 1, 1, 2]
        expected = [["#", "#"], ["*", "*"], ["*", "*"], ["b", "b"]]
        output = solution(canvas, rectangle)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        canvas = [["1", "2"], ["4", "3"], ["5", "6"], ["8", "7"]]
        rectangle = [0, 0, 1, 3]
        expected = [["*", "*"], ["|", "|"], ["|", "|"], ["*", "*"]]
        output = solution(canvas, rectangle)
        self.assertEqual(output, expected)
