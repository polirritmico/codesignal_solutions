#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pawnRace import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        white = "e2"
        black = "e7"
        to_move = "w"
        expected = "draw"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        white = "e3"
        black = "d7"
        to_move = "b"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        white = "a7"
        black = "h2"
        to_move = "w"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        white = "c5"
        black = "b7"
        to_move = "w"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        white = "g2"
        black = "a3"
        to_move = "b"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        white = "h4"
        black = "g7"
        to_move = "w"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        white = "f2"
        black = "h6"
        to_move = "w"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        white = "d3"
        black = "h2"
        to_move = "b"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        white = "a3"
        black = "d5"
        to_move = "w"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        white = "c3"
        black = "e7"
        to_move = "b"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case11(self):
        white = "g4"
        black = "e4"
        to_move = "w"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case12(self):
        white = "f4"
        black = "h6"
        to_move = "b"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case13(self):
        white = "b5"
        black = "f3"
        to_move = "w"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case14(self):
        white = "c5"
        black = "e5"
        to_move = "b"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case15(self):
        white = "c6"
        black = "e2"
        to_move = "w"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case16(self):
        white = "f6"
        black = "h4"
        to_move = "b"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case17(self):
        white = "e3"
        black = "f4"
        to_move = "w"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case18(self):
        white = "a6"
        black = "f7"
        to_move = "w"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case19(self):
        white = "e7"
        black = "h3"
        to_move = "b"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case20(self):
        white = "c7"
        black = "e6"
        to_move = "w"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case21(self):
        white = "g2"
        black = "f2"
        to_move = "b"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case22(self):
        white = "f2"
        black = "e5"
        to_move = "w"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case23(self):
        white = "c2"
        black = "d7"
        to_move = "b"
        expected = "white"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case24(self):
        white = "d4"
        black = "e3"
        to_move = "w"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case25(self):
        white = "h3"
        black = "g6"
        to_move = "b"
        expected = "black"
        output = solution(white, black, to_move)
        self.assertEqual(output, expected)
