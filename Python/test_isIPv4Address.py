#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from isIPv4Address import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = "172.16.254.1"
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = "172.316.254.1"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = ".254.255.0"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = "1.1.1.1a"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = "64.233.161.00"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = "01.233.161.131"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case7(self):
        case = "192.168.0.-1"
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)

