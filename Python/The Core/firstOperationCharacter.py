#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string which represents a valid arithmetic expression, find the index of
the character in the given expression corresponding to the arithmetic operation
which needs to be computed first.

Note that several operations of the same type with equal priority are computed
from left to right.

See the explanation of the third example for more details about the operations
priority in this problem.

Example

For expr = "(2 + 2) * 2", the output should be solution(expr) = 3.

There are two operations in the expression: + and *. The result of + should be
computed first, since it is enclosed in parentheses. Thus, the output is the
index of the '+' sign, which is 3.

For expr = "2 + 2 * 2", the output should be solution(expr) = 6.

There are two operations in the given expression: + and *. Since there are no
parentheses, * should be computed first as it has higher priority. The answer is
the position of '*', which is 6.

For expr = "((2 + 2) * 2) * 3 + (2 + (2 * 2))", the output should be
solution(expr) = 28.

There are two operations which are enclosed in two parentheses: + at the
position 4, and * at the position 28. Since * has higher priority than +, the
answer is 28.

"""


def solution(expression: str) -> int:
    inner_bracket_level = 0
    innermost_bracket_group = 0
    for char in expression:
        if char == "(":
            inner_bracket_level += 1
        elif char == ")":
            inner_bracket_level -= 1
        innermost_bracket_group = max(innermost_bracket_group, inner_bracket_level)

    operations = ("*", "+")
    for operator in operations:
        for index, char in enumerate(expression):
            if char == "(":
                inner_bracket_level += 1
            elif char == ")":
                inner_bracket_level -= 1
            if char == operator and inner_bracket_level == innermost_bracket_group:
                return index


def main():
    case = "((2 + 2) * 2) * 3 + (2 + (2 * 2))"
    # expected = 28

    # case = "2 + 2 * 2"
    # expected = 6
    # case = "(2 + 2) * 2"
    # expected = 3
    print(solution(case))


if __name__ == "__main__":
    main()
