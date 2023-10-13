#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from isInformationConsistent import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [[0, 1, 0, 1], [-1, 1, 0, 0], [-1, 0, 0, 1]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case2(self):
        case = [[1, 0], [-1, 0], [1, 1], [1, 1]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case3(self):
        case = [[1, -1, 0, 1], [1, -1, 0, -1]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case4(self):
        case = [[0, 0, -1], [-1, 1, -1], [-1, 1, 0], [0, 1, 0]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case5(self):
        case = [[0, 0, -1, 1, 1, 0, 0, 1, -1, 0], [-1, 1, -1, 1, 0, 1, -1, 1, 1, 0]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case6(self):
        case = [[0, 0], [-1, 1]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case7(self):
        case = [[0, 0, -1, 0], [-1, 1, 1, -1], [-1, 0, 0, 0], [0, 1, 0, -1]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case8(self):
        case = [[0, 0], [0, 0]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case9(self):
        case = [[-1, -1], [-1, 1]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    def test_case10(self):
        case = [[0, 0, -1], [-1, 1, 1], [0, 1, 0], [0, 1, 0]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)
