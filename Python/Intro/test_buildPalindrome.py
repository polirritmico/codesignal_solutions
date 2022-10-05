#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from buildPalindrome import *

class TesFunctions(unittest.TestCase):

    #@unittest.skip
    def test_is_palindrome1(self):
        case = "abacaba"
        expected = True
        output = is_palindrome(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_is_palindrome2(self):
        case = "abacab"
        expected = False
        output = is_palindrome(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_is_palindrome3(self):
        case = "anitalavalatina"
        expected = True
        output = is_palindrome(case)
        self.assertEqual(output, expected)


# @unittest.skip
class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "abcdc"
        expected = "abcdcba"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "ababab"
        expected = "abababa"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "abba"
        expected = "abba"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "abaa"
        expected = "abaaba"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = "aaaaba"
        expected = "aaaabaaaa"
        output = solution(case)
        self.assertEqual(output, expected)


