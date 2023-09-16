#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from timedReading import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        max_length = 4
        text = "The Fox asked the stork, 'How is the soup?'"
        expected = 7
        output = solution(max_length, text)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        max_length = 1
        text = "..."
        expected = 0
        output = solution(max_length, text)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        max_length = 3
        text = "This play was good for us."
        expected = 3
        output = solution(max_length, text)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        max_length = 3
        text = "Suddenly he stopped, and glanced up at the houses"
        expected = 5
        output = solution(max_length, text)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        max_length = 6
        text = "Zebras evolved among the Old World horses within the last four million years."
        expected = 11
        output = solution(max_length, text)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        max_length = 5
        text = "Although zebra species may have overlapping ranges, they do not interbreed."
        expected = 6
        output = solution(max_length, text)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        max_length = 1
        text = "Oh!"
        expected = 0
        output = solution(max_length, text)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        max_length = 5
        text = "Now and then, however, he is horribly thoughtless, and seems to take a real delight in giving me pain."
        expected = 14
        output = solution(max_length, text)
        self.assertEqual(output, expected)
