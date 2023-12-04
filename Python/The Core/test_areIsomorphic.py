#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from areIsomorphic import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        array_a = [[1, 1, 1], [0, 0]]
        array_b = [[2, 1, 1], [2, 1]]
        expected = True
        output = solution(array_a, array_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        array_a = [[2], []]
        array_b = [[2]]
        expected = False
        output = solution(array_a, array_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        array_a = [[2], [1], [3, 5]]
        array_b = [[], [1], [1, 6]]
        expected = False
        output = solution(array_a, array_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        array_a = [[1, 1, 1], [0, 0]]
        array_b = [[2, 1, 3], [2, 0], []]
        expected = False
        output = solution(array_a, array_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        array_a = [[], [1]]
        array_b = [[], [6, 2, 5]]
        expected = False
        output = solution(array_a, array_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        array_a = [[1, 3, 4], []]
        array_b = [[2, 1, 2], []]
        expected = True
        output = solution(array_a, array_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        array_a = [[]]
        array_b = [[]]
        expected = True
        output = solution(array_a, array_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        array_a = [[2], [1], [3, 50, 33]]
        array_b = [[], [1], [1, 6, 32]]
        expected = False
        output = solution(array_a, array_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        array_a = [[6], [3, 5, 2, 4]]
        array_b = [[34], [6, 2, 5]]
        expected = False
        output = solution(array_a, array_b)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        array_a = [[6], [3, 5, 2, 4]]
        array_b = [[34], [6, 2, 5, 4], [1, 2, 3]]
        expected = False
        output = solution(array_a, array_b)
        self.assertEqual(output, expected)
