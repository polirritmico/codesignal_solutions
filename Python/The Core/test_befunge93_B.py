#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from befunge93 import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = [
            "               v",
            'v  ,,,,,"Hello"<',
            ">48*,          v",
            '"!dlroW",,,,,,v>',
            "25*,@         > ",
        ]
        expected = "Hello World!\n"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = [
            '>25*"!dlrow ,olleH":v ',
            "                 v:,_@",
            "                 >  ^ ",
        ]
        expected = "Hello, world!\n"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = ["1+:::*.9`#@_"]
        expected = "1 4 9 16 25 36 49 64 81 100 "
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = [
            '"^a&EPm=kY}t/qYC+i9wHye$m N@~x+"v',
            '"|DsY<"-"z6n<[Yo2x|UP5VD:">:#v_@>',
            '-:19+/"0"+,19+%"0"+,      ^  >39*',
        ]
        expected = "3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip

    def test_case5(self):
        case = ["@"]
        expected = ""
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = [">!|", " @<", "  .", "  /", "  1", "  .", "  `"]
        expected = "0 0 "
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = [
            '">:#,_66*2-,@This prints itself out backwards......  but it has to be 80x1 cell'
        ]
        expected = 'llec 1x08 eb ot sah ti tub  ......sdrawkcab tuo flesti stnirp sihT@,-2*66_,#:>"'
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = ["v>v>", "v^v^", "v^v^", "v^v^", ">^>^"]
        expected = ""
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = ["94/.@"]
        expected = "2 "
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = [
            "92+9*                           :. v  <      ",
            '>v"bottles of beer on the wall"+910<         ',
            ",:                                           ",
            "^_ $                             :.v         ",
            '            >v"bottles of beer"+910<         ',
            "            ,:                               ",
            "            ^_ $                     v       ",
            '>v"Take one down, pass it around"+910<       ',
            ",:                                           ",
            "^_ $                           1-v           ",
            "                                 :           ",
            '        >v"bottles of beer"+910.:_          v',
            "        ,:                                   ",
            "        ^_ $                          ^      ",
            '                    >v" no more beer..."+910<',
            "                    ,:                       ",
            "                    ^_ $$ @                  ",
        ]
        expected = "99 bottles of beer on the wall\n99 bottles of beer\nTake one down, pass it around\n98 bottles of beer\nb"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case11(self):
        case = [
            "<>: #+1 #:+ 3 : *6+ $#2 9v#",
            "v 7 :   +   8 \\ + + 5   <  ",
            '>-  :2  -:  " " 1 + \\ v ^< ',
            "2 + :   7   + : 7 + v > :  ",
            ":1- :3- >   :#, _ @ >:3 5*-",
        ]
        expected = "BEFUNGE!EGNUFEB"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case12(self):
        case = [
            '25*3*4+>:."=",:,"   "v',
            "       |-*2*88:+1,,, <",
            "       @              ",
        ]
        expected = "34 =\"   35 =#   36 =$   37 =%   38 =&   39 ='   40 =(   41 =)   42 =*   43 =+   44 =,   45 =-   46 ="
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case13(self):
        case = ["vv    <>v *<", "9>:1-:|$>\\:|", ">^    >^@.$<"]
        expected = "362880 "
        output = solution(case)
        self.assertEqual(output, expected)
