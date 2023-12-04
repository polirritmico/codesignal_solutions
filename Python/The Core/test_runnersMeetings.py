#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from runnersMeetings import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        position = [1, 4, 2]
        speed = [27, 18, 24]
        expected = 3
        output = solution(position, speed)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        position = [1, 4, 2]
        speed = [5, 6, 2]
        expected = 2
        output = solution(position, speed)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        position = [1, 2, 3]
        speed = [1, 1, 1]
        expected = -1
        output = solution(position, speed)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        position = [1, 1000]
        speed = [23, 22]
        expected = 2
        output = solution(position, speed)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        position = [-2, 0, 2, 4]
        speed = [6, 5, 4, 3]
        expected = 4
        output = solution(position, speed)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        position = [-2, 0, 2, 4]
        speed = [6, 5, 4, 2]
        expected = 3
        output = solution(position, speed)
        self.assertEqual(output, expected)
