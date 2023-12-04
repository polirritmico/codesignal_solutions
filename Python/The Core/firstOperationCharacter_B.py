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

from typing import Self


class BracketsGroup:
    def __init__(self, level: int = 0, open_idx: int = 0, parent_group: Self = None):
        self.level: int = level
        self.open: int = open_idx
        self.close: int = 0
        self.parent_group: Self = parent_group
        self.subgroups: list[Self] = []
        self.expression: str = ""

    def extract_expression(self, expression: str = "") -> str:
        self.expression = expression[self.open + 1 : self.close]
        return self.expression


def parse_brackets(expression: str) -> list[str]:
    current_group: BracketsGroup = None
    current_level = 0
    brackets_groups: list[BracketsGroup] = []
    for i in range(len(expression)):
        current = expression[i]
        if current == "(":
            if current_group is None:
                new_group = BracketsGroup(current_level, i)
                brackets_groups.append(new_group)
            else:
                new_group = BracketsGroup(current_level, i, current_group)
                current_group.subgroups.append(new_group)
            current_group = new_group
            current_level += 1
        elif current == ")":
            current_group.close = i
            current_group.extract_expression(expression)
            current_group = current_group.parent_group
            current_level -= 1
    return brackets_groups


def first_computed_search_index(expression) -> int:
    index = expression.find("*")
    if index != -1:
        return index
    return expression.find("+")


def get_lower_level(brackets: BracketsGroup) -> BracketsGroup:
    lower_level_groups: list[BracketsGroup] = [brackets[0]]
    current_level = 0
    for level in brackets:
        for group in level.subgroups:
            if current_level < group.level:
                current_level = group.level
                lower_level_groups = [group]
            elif current_level == group.level:
                lower_level_groups.append(group)

    if len(lower_level_groups) == 1:
        return lower_level_groups[0]

    for group in lower_level_groups:
        if "*" in group.expression:
            return group
    return lower_level_groups[0]


def solution(expression: str) -> int:
    brackets = parse_brackets(expression)
    if len(brackets) == 0:
        return first_computed_search_index(expression)
    group = get_lower_level(brackets)
    index = first_computed_search_index(group.expression)
    return group.open + index + 1


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
