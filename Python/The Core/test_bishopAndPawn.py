#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from bishopAndPawn import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        bishop = "a1"
        pawn = "c3"
        expected = True
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        bishop = "h1"
        pawn = "h3"
        expected = False
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        bishop = "a5"
        pawn = "c3"
        expected = True
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        bishop = "g1"
        pawn = "f3"
        expected = False
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        bishop = "e7"
        pawn = "d6"
        expected = True
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        bishop = "e7"
        pawn = "a3"
        expected = True
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        bishop = "e3"
        pawn = "a7"
        expected = True
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        bishop = "a1"
        pawn = "h8"
        expected = True
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        bishop = "a1"
        pawn = "h7"
        expected = False
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        bishop = "h1"
        pawn = "a8"
        expected = True
        output = solution(bishop, pawn)
        self.assertEqual(output, expected)
