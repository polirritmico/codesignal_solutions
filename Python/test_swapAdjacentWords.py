#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from swapAdjacentWords import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "CodeFight On"
        expected = "On CodeFight"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "How are you today guys"
        expected = "are How today you guys"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "IAmALongStringWithNoWhiteSpaceCharacters"
        expected = "IAmALongStringWithNoWhiteSpaceCharacters"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "A b C D e F g h I j"
        expected = "b A D C F e h g j I"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = ""
        expected = ""
        output = solution(case)
        self.assertEqual(output, expected)
