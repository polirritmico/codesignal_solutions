#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from boxesPacking import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        length = [1, 3, 2]
        width = [1, 3, 2]
        height = [1, 3, 2]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        length = [1, 1]
        width = [1, 1]
        height = [1, 1]
        expected = False
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        length = [3, 1, 2]
        width = [3, 1, 2]
        height = [3, 2, 1]
        expected = False
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        length = [2]
        width = [3]
        height = [4]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        length = [5, 7, 4, 1, 2]
        width = [4, 10, 3, 1, 4]
        height = [6, 5, 5, 1, 2]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        length = [6, 4]
        width = [5, 3]
        height = [4, 5]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        length = [6, 3]
        width = [5, 4]
        height = [4, 5]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        length = [6, 3]
        width = [5, 5]
        height = [4, 4]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        length = [883, 807]
        width = [772, 887]
        height = [950, 957]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        length = [6, 5]
        width = [5, 3]
        height = [4, 4]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case11(self):
        length = [4, 10, 3, 1, 4]
        width = [5, 7, 4, 1, 2]
        height = [6, 5, 5, 1, 2]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case12(self):
        length = [10, 8, 6, 4, 1]
        width = [7, 7, 6, 3, 2]
        height = [9, 6, 3, 2, 1]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case13(self):
        length = [9980, 9984, 9981]
        width = [9980, 9984, 9983]
        height = [9981, 9984, 9982]
        expected = True
        output = solution(length, width, height)
        self.assertEqual(output, expected)
