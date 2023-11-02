#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from befunge93_B import solution


# @unittest.skip
class TestExtra(unittest.TestCase):
    def test_end(self):
        # @: end program; the program output should be returned then
        case = ["@"]
        expected = ""
        output = solution(case)
        self.assertEqual(output, expected)

    def test_output_int(self):
        # .: pop value and output it as an integer followed by a space
        case = ["2.@"]
        expected = "2 "
        output = solution(case)
        self.assertEqual(output, expected)

    def test_output_int_empty(self):
        case = [".@"]
        expected = "0 "
        output = solution(case)
        self.assertEqual(output, expected)

    def test_operator_mult(self):
        # *: multiplication; pop a, pop b, then push a * b
        case = ["24*.@"]
        expected = "8 "
        output = solution(case)
        self.assertEqual(output, expected)

    def test_output_ascii_char(self):
        # ,: pop value and output it as ASCII character
        case = ["99*,@"]
        expected = "Q"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_cmd_bridge(self):
        # #: bridge; skip next cell
        case = [">77*#3,@"]
        expected = "1"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_cmd_conditional_mov_hor(self):
        # _: pop a value; move right if value = 0, left otherwise
        case = [
            "  v@   ",
            "_@_99*,",
        ]
        expected = "Q"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_cmd_conditional_mov_ver(self):
        # |: pop a value; move down if value = 0, up otherwise
        case = [
            "v @    ",
            ">0|@   ",
            "@ >77*,",
        ]
        expected = "1"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_cmd_duplicate(self):
        # :: duplicate value on top of the stack
        case = ["7:*,@"]
        expected = "1"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_cmd_duplicate_empty(self):
        # :: duplicate value on top of the stack
        case = [":.@"]
        expected = "0 "
        output = solution(case)
        self.assertEqual(output, expected)

    def test_cmd_swap_stack(self):
        # \\: swap the top stack value with the second to the top
        case = ["110\\...@"]
        expected = "1 0 1 "
        output = solution(case)
        self.assertEqual(output, expected)

    def test_cmd_pop(self):
        # $: pop value from the stack and discard it
        case = ["72$7*,@"]
        expected = "1"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_string_mode(self):
        # ": start string mode; push each character's ASCII value all the way up to the next "
        case = ['"zA",,@']
        expected = "Az"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_string_mode_with_empty_char(self):
        # (whitespace character): empty instruction; does nothing
        case = ['"zA"   ,   ,   @']
        expected = "Az"
        output = solution(case)
        self.assertEqual(output, expected)

    def test_operator_add(self):
        # +: addition; pop a, pop b, then push a + b
        case = ["52+.@"]
        expected = "7 "
        output = solution(case)
        self.assertEqual(output, expected)

    def test_operator_subtraction(self):
        # -: subtraction; pop a, pop b, then push b - a
        case = ["12-.@"]
        expected = "-1 "
        output = solution(case)
        self.assertEqual(output, expected)
        case = ["21-.@"]
        expected = "1 "
        output = solution(case)
        self.assertEqual(output, expected)

    def test_operator_div(self):
        # /: integer division; pop a, pop b, then push b / a
        case = ["84/.@"]
        expected = "2 "
        output = solution(case)
        self.assertEqual(output, expected)

    def test_operator_mod(self):
        # %: modulo operation; pop a, pop b, then push b % a
        case = ["74%.@"]
        expected = "3 "
        output = solution(case)
        self.assertEqual(output, expected)

    def test_operator_not(self):
        # !: logical NOT; pop a value, if the value = 0, push 1, otherwise push 0
        case = ["0!.@"]
        expected = "1 "
        output = solution(case)
        self.assertEqual(output, expected)

        case = ["0!.@"]
        expected = "1 "
        output = solution(case)
        self.assertEqual(output, expected)

    def test_operator_greater_than(self):
        # `: greater than; pop a and b, then push 1 if b > a, otherwise 0
        case = ["27`.@"]
        expected = "0 "
        output = solution(case)
        self.assertEqual(output, expected)
        case = ["27\\`.@"]
        expected = "1 "
        output = solution(case)
        self.assertEqual(output, expected)


# @unittest.skip
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
