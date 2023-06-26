#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from crosswordFormation import solution


class TestBase(unittest.TestCase):
    def test_minimal(self):
        case = ["abc", "dee", "abd", "cde"]
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case1(self):
        case = ["crossword", "square", "formation", "something"]
        expected = 6
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = ["anaesthetist", "thatch", "ethnics", "sabulous"]
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = ["eternal", "texas", "chainsaw", "massacre"]
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = ["africa", "america", "australia", "antarctica"]
        expected = 62
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = ["phenomenon", "remuneration", "particularly", "pronunciation"]
        expected = 62
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = ["onomatopoeia", "philosophical", "provocatively", "thesaurus"]
        expected = 20
        output = solution(case)
        self.assertEqual(output, expected)
