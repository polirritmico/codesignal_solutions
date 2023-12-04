#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from countElements import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "[[0, 20], [33, 99]]"
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = '[ "one", 2, "three" ]'
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "true"
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "[[1, 2, [3]], 4]"
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = '["oh, no! kind, of, tricky", "test, case"]'
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = '"try this!, [1, 2, 3, 32], false"'
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = '"a,,,,,,,,,,,,,,asdf"'
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "1023456789"
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = '["ZZZ]zero"]'
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = '[true,"false", true, [2], false, false]'
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case11(self):
        case = "[]"
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case12(self):
        case = '["[   -45,   95]   ", [ 87,  -655]]'
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case13(self):
        case = "111"
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)
