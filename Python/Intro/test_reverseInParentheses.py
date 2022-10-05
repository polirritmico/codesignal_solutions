#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from reverseInParentheses import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "(bar)"
        expected = "rab"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "foo(bar)baz"
        expected = "foorabbaz"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "foo(bar)baz(blim)"
        expected = "foorabbazmilb"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "foo(bar(baz))blim" # -> foo(barzab)blim
        expected = "foobazrabblim"
        output = solution(case)
        self.assertEqual(output, expected)


