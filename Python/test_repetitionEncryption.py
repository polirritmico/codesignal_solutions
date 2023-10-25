#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from repetitionEncryption import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "Hi, hi Jane! I'm so. So glad to to finally be able to write - WRITE!! - to you!"
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "Yo-yo, how's s it going going for ya? Ya is okay, okay'nt ya?"
        expected = 5
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "Hi Jane, how are you doing today?"
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "My friend, friend of mine, I am really-really happy for you! You are amazing, please write me back when you can."
        expected = 3
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "Everything is fine, fine perfectly here. Here I have fun (fun all the day!) days. Although I miss you, so please please, Jane, write, write me whenever you can! Can you do that? That is the only (!!ONLY!!) thing I ask from you, you sunshine."
        expected = 9
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "Do not notify me about this in the future"
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "ho-ho--he-he"
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "WeLl wElL"
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)
