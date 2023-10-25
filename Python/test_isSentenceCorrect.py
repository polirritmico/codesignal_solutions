#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from isSentenceCorrect import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "This is an example of *correct* sentence."
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "!this sentence is TOTALLY incorrecT"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "Almost correct sentence"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "Something is !wrong! here."
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "Time to roll!!!"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "This one is okay though, isn't it?"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "this sentence, I'm afraid, is a bit incorrect."
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "I'm glad this sentence is correct, my friends."
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = "CodeSignal is lame!!!"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = "No way, CodeSignal is awesome!"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)
