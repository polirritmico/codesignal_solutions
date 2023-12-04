#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from isUnstablePair import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        filename_1 = "aa"
        filename_2 = "AAB"
        expected = True
        output = solution(filename_1, filename_2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        filename_1 = "A"
        filename_2 = "z"
        expected = False
        output = solution(filename_1, filename_2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        filename_1 = "yyyyyy"
        filename_2 = "Azzzzzzzzz"
        expected = False
        output = solution(filename_1, filename_2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        filename_1 = "mehOu"
        filename_2 = "mehau"
        expected = True
        output = solution(filename_1, filename_2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        filename_1 = "aaz"
        filename_2 = "AAzz"
        expected = True
        output = solution(filename_1, filename_2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        filename_1 = "fdsAs"
        filename_2 = "dzdw"
        expected = False
        output = solution(filename_1, filename_2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        filename_1 = "aaad"
        filename_2 = "aaAdd"
        expected = True
        output = solution(filename_1, filename_2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        filename_1 = "zzzzzAa123"
        filename_2 = "zzzzza"
        expected = True
        output = solution(filename_1, filename_2)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        filename_1 = "123za"
        filename_2 = "123Z"
        expected = False
        output = solution(filename_1, filename_2)
        self.assertEqual(output, expected)
