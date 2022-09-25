#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from fileNaming import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = ["doc", 
                "doc", 
                "image", 
                "doc(1)", 
                "doc"]     
        expected = ["doc", 
                    "doc(1)", 
                    "image", 
                    "doc(1)(1)", 
                    "doc(2)"]
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = ["a(1)", "a(6)", "a", "a", "a", "a",
                "a", "a", "a", "a", "a", "a"]    
        expected = ["a(1)", "a(6)", "a", "a(2)", "a(3)", "a(4)", "a(5)", 
                    "a(7)", "a(8)", "a(9)", "a(10)", "a(11)"]
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", 
                "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]   
        expected = ["dd", "dd(1)", "dd(2)", "dd(3)", "dd(1)(1)", 
                    "dd(1)(2)", "dd(1)(1)(1)", "dd(4)", "dd(1)(3)"]
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = ["a", "b", "cd", "b ", "a(3)"] 
        expected = ["a", "b", "cd", "b ", "a(3)"]
        output = solution(case)
        self.assertEqual(output, expected)


