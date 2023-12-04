#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pairOfShoes import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [[0, 21], [1, 23], [1, 21], [0, 23]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [[0, 21], [1, 23], [1, 21], [1, 23]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [[0, 23], [1, 21], [1, 23], [0, 21], [1, 22], [0, 22]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [[0, 23], [1, 21], [1, 23], [0, 21]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [[1, 41], [1, 40], [1, 45], [0, 42], [0, 42], [0, 42]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [[1, 2], [0, 2], [1, 1], [0, 1], [1, 2], [0, 1]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = [[0, 100], [1, 1], [1, 100], [0, 1]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = [[0, 23]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = [[0, 23], [1, 23]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = [[0, 23], [1, 22]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)
