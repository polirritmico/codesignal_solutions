#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from rowsRearranging import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [[2, 7, 1], [0, 2, 0], [1, 3, 1]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [[6, 4], [2, 2], [4, 3]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = [[0, 1], [1, 2], [2, 3], [-1, 4]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [[2, 2, 2], [1, 1, 1]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = [[1, 3, 1], [0, 2, 0], [1, 7, 2]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [[3, 34, 2, 5, 2], [2, 34, 5, 2, 1]]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = [[0], [1], [2], [-1]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = [
            [293, -294, -108, 284, -127, 133, 93],
            [-247, -45, 33, -51, 12, -85, -295],
            [-272, 275, 285, 157, 175, 261, 163],
            [74, -89, -67, 106, -207, 47, 147],
            [-5, -56, -248, 166, -55, 166, 212],
            [-50, -63, 155, -217, 230, -298, -61],
            [-66, 181, 233, -175, 64, -69, -76],
        ]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = [
            [-186, 169, 47, 28, 275, 67, -118, -9, 162],
            [-296, 269, -261, 54, 253, 213, 300, -52, -124],
            [175, -205, -217, -114, -170, 266, 230, -38, -138],
            [-298, 295, 124, -277, -279, -243, -218, -206, 148],
            [12, 8, -221, -190, -175, -299, 244, -169, -66],
            [36, 294, 229, -144, 218, 19, -166, 169, 264],
        ]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = [[22, 149, -107, 159, -158, 295]]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)
