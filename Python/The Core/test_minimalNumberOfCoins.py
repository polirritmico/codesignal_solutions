#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from minimalNumberOfCoins import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        coins = [1, 2, 10]
        price = 28
        expected = 6
        output = solution(coins, price)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        coins = [1, 5, 10, 100]
        price = 239
        expected = 10
        output = solution(coins, price)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        coins = [1]
        price = 8
        expected = 8
        output = solution(coins, price)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        coins = [1, 2, 20, 60, 120]
        price = 150
        expected = 7
        output = solution(coins, price)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        coins = [1, 3, 6, 30]
        price = 45
        expected = 4
        output = solution(coins, price)
        self.assertEqual(output, expected)
