#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from programTranslation import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        code = "function add($n, m) {\t  return n + $m;\t}"
        args = ["n", "m"]
        expected = "function add($n, $m) {\t  return $n + $m;\t}"
        output = solution(code, args)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        code = "function findSum(a, $cnt) {\t  var a0 = $a;\t  for (var _cnt = 0, _cnt < cnt; _cnt++)\t    a0 += _cnt;\t  return a0;\t}"
        args = ["a", "cnt"]
        expected = "function findSum($a, $cnt) {\t  var a0 = $a;\t  for (var _cnt = 0, _cnt < $cnt; _cnt++)\t    a0 += _cnt;\t  return a0;\t}"
        output = solution(code, args)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        code = "function doNothing($uselessVar) {\t  return $uselessVar;\t}"
        args = ["uselessVar"]
        expected = "function doNothing($uselessVar) {\t  return $uselessVar;\t}"
        output = solution(code, args)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        code = "function addToVariable(variable) {\t  variable_which_should_be_increased = 14;\t  variable_which_should_be_increased += variable;\t  return variable_which_should_be_increased;\t}"
        args = ["variable"]
        expected = "function addToVariable($variable) {\t  variable_which_should_be_increased = 14;\t  variable_which_should_be_increased += $variable;\t  return variable_which_should_be_increased;\t}"
        output = solution(code, args)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        code = "function replaceThemAll(rep, laceT, hemAll, ornot) {\t  var tmp = rep;\t  rep = laceT;\t  laceT = hemAll;\t  hemAll = tmp;\t  return [rep, laceT, hemAll]\t}"
        args = ["rep", "laceT", "hemAll"]
        expected = "function replaceThemAll($rep, $laceT, $hemAll, ornot) {\t  var tmp = $rep;\t  $rep = $laceT;\t  $laceT = $hemAll;\t  $hemAll = tmp;\t  return [$rep, $laceT, $hemAll]\t}"
        output = solution(code, args)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        code = "function returnSecond(fu_,_re5,NOO) {\t  return _re5;\t}"
        args = ["fu_", "_re5", "NOO"]
        expected = "function returnSecond($fu_,$_re5,$NOO) {\t  return $_re5;\t}"
        output = solution(code, args)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        code = "function getLength(k, m) {\t  return m.length;\t}"
        args = ["m"]
        expected = "function getLength(k, $m) {\t  return $m.length;\t}"
        output = solution(code, args)
        self.assertEqual(output, expected)
