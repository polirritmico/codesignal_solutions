#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from willYou import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        young = True
        beautiful = True
        loved = True
        expected = False
        output = solution(young, beautiful, loved)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        young = True
        beautiful = False
        loved = True
        expected = True
        output = solution(young, beautiful, loved)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        young = False
        beautiful = False
        loved = False
        expected = False
        output = solution(young, beautiful, loved)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        young = False
        beautiful = False
        loved = True
        expected = True
        output = solution(young, beautiful, loved)
        self.assertEqual(output, expected)


