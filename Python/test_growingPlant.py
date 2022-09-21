#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from growingPlant import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        upSpeed = 100
        downSpeed = 10
        desiredHeight = 910
        expected = 10
        output = solution(upSpeed, downSpeed, desiredHeight)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        upSpeed = 10
        downSpeed = 9
        desiredHeight = 4
        expected = 1
        output = solution(upSpeed, downSpeed, desiredHeight)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        upSpeed = 5
        downSpeed = 2
        desiredHeight = 7
        expected = 2
        output = solution(upSpeed, downSpeed, desiredHeight)
        self.assertEqual(output, expected)


