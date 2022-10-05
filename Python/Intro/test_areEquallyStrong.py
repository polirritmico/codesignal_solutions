#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from areEquallyStrong import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        yourLeft = 10
        yourRight = 15
        friendsLeft = 15
        friendsRight = 10
        expected = True
        output = solution(yourLeft, yourRight, friendsLeft, friendsRight)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        yourLeft = 15
        yourRight = 10
        friendsLeft = 15
        friendsRight = 10
        expected = True
        output = solution(yourLeft, yourRight, friendsLeft, friendsRight)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        yourLeft = 15
        yourRight = 10
        friendsLeft = 15
        friendsRight = 9
        expected = False
        output = solution(yourLeft, yourRight, friendsLeft, friendsRight)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        yourLeft = 10
        yourRight = 5
        friendsLeft = 5
        friendsRight = 10
        expected = True
        output = solution(yourLeft, yourRight, friendsLeft, friendsRight)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        yourLeft = 20
        yourRight = 15
        friendsLeft = 5
        friendsRight = 20
        expected = False
        output = solution(yourLeft, yourRight, friendsLeft, friendsRight)
        self.assertEqual(output, expected)



