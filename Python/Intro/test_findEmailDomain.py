#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from findEmailDomain import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "prettyandsimple@example.com"
        expected = "example.com"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "fully-qualified-domain@codesignal.com"
        expected = "codesignal.com"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = "\" \"@space.com"
        expected = "space.com"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "someaddress@yandex.ru"
        expected = "yandex.ru"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = "\" \"@xample.org"
        expected = "xample.org"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case7(self):
        case = "\"very.unusual.@.unusual.com\"@usual.com"
        expected = "usual.com"
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case9(self):
        case = "example-indeed@strange-example.com"
        expected = "strange-example.com"
        output = solution(case)
        self.assertEqual(output, expected)



