#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from stolenLunch import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "you'll n4v4r 6u4ss 8t: cdja"
        expected = "you'll never guess it: 2390"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = ""
        expected = ""
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "0123456789"
        expected = "abcdefghij"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "jihgfedcba"
        expected = "9876543210"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "you won't know!!"
        expected = "you won't know!!"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "just 63jd73 some random note jkhdf83 ds823 that you, dfj238 dsf38 little one?, will abjk38 s83    skdu3 29never get!"
        expected = "9ust gd93hd som4 r0n3om not4 9k735id 3sicd t70t you, 359cdi 3s5di l8ttl4 on4?, w8ll 019kdi sid    sk3ud cjn4v4r 64t!"
        output = solution(case)
        self.assertEqual(output, expected)
