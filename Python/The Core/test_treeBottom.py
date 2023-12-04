#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from treeBottom import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))"
        expected = [5, 11, 4]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "(1 () ())"
        expected = [1]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "(1000 () ())"
        expected = [1000]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "(413 (683 () ()) (355 (913 (985 () ()) ()) ()))"
        expected = [985]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "(65 (88 (45 (4 () ()) ()) ()) (1000000000 () ()))"
        expected = [4]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "(1 (2 (4 (8 () ()) (9 () ())) (5 (10 () ()) (11 () ()))) (3 (6 (12 () ()) (13 () ())) (7 (14 () ()) (15 () ()))))"
        expected = [8, 9, 10, 11, 12, 13, 14, 15]
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "(1 () (2 () (3 () (5 () (8 () (13 () (21 () (34 () ()))))))))"
        expected = [34]
        output = solution(case)
        self.assertEqual(output, expected)
