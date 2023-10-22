#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from chessBishopDream import solution


# @unittest.skip
class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        board_size = [3, 7]
        init_position = [1, 2]
        init_direction = [-1, 1]
        k = 13
        expected = [0, 1]
        output = solution(board_size, init_position, init_direction, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        board_size = [1, 2]
        init_position = [0, 0]
        init_direction = [1, 1]
        k = 6
        expected = [0, 1]
        output = solution(board_size, init_position, init_direction, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        board_size = [2, 2]
        init_position = [1, 0]
        init_direction = [1, 1]
        k = 12
        expected = [1, 0]
        output = solution(board_size, init_position, init_direction, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        board_size = [1, 1]
        init_position = [0, 0]
        init_direction = [1, -1]
        k = 1000000000
        expected = [0, 0]
        output = solution(board_size, init_position, init_direction, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        board_size = [2, 3]
        init_position = [1, 2]
        init_direction = [-1, -1]
        k = 41
        expected = [0, 2]
        output = solution(board_size, init_position, init_direction, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        board_size = [17, 19]
        init_position = [14, 8]
        init_direction = [1, -1]
        k = 239239
        expected = [4, 17]
        output = solution(board_size, init_position, init_direction, k)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        board_size = [17, 19]
        init_position = [16, 18]
        init_direction = [1, 1]
        k = 239239239
        expected = [10, 2]
        output = solution(board_size, init_position, init_direction, k)
        self.assertEqual(output, expected)
