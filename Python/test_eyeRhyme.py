#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from eyeRhyme import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "cough\tbough"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "CodeFig!ht\tWith all your might"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "quod erat demonstrandum\tand that, ladies and gentlemen, is the end of my memorandum"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "yup\tyes"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "hey\they"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "E = MC<sup>2</sup>\twhich in turn equals sup"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "Isn't it correct?!\tIt definitely is! Does it mean that we've just obtained a full set?!"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "Nothing can go wrong here :)\tHehehehe:)"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = "!1?/\tsldkjfl3 sldjf 1?/"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = "simple\tpimple"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)
