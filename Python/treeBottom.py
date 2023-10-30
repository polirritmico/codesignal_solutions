#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tree Bottom

You are given a recursive notation of a binary tree: each node of a tree is
represented as a set of three elements:

    - value of the node;
    - left subtree;
    - right subtree.

So, a tree can be written as (value left_subtree right_subtree). It is
guaranteed that 1 ≤ value ≤ 109. If a node doesn't exist then it is represented
as an empty set: (). For example, here is a representation of a tree in the
given picture:

    (2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))

https://codesignal.s3.amazonaws.com/uploads/1664318506/tree.png?raw=true

Your task is to obtain a list of nodes, that are the most distant from the tree
root, in the order from left to right.

In the notation of a node its value and subtrees are separated by exactly one
space character.

Example

For

tree = "(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))"

the output should be solution(tree) = [5, 11, 4].

"""


def solution(tree: str) -> list[int]:
    current_level = 0
    innermost_level = 0
    for char in tree:
        if char == "(":
            current_level += 1
        if char == ")":
            current_level -= 1
        innermost_level = max(innermost_level, current_level)

    innermost_nodes = []
    reading_number = False
    current_number = ""

    for target_level in range(innermost_level, -1, -1):
        for index, char in enumerate(tree):
            if char == "(":
                current_level += 1
                if current_level == target_level:
                    reading_number = True
            elif char == ")":
                if reading_number:
                    reading_number = False
                    if current_number != "":
                        innermost_nodes.append(int(current_number))
                        current_number = ""
                current_level -= 1
            elif reading_number and current_level == target_level:
                current_number += char
        if len(innermost_nodes) != 0:
            return innermost_nodes


def main():
    case = "(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))"
    # expected = [5, 11, 4]
    print(solution(case))


if __name__ == "__main__":
    main()
