#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(array_a, array_b):
    diff_a = []
    diff_b = []
    for a, b in zip(array_a, array_b):
        if a != b:
            diff_a.append(a)
            diff_b.insert(0, b)
    length = len(diff_a)
    if length == 0:
        return True
    if length == 2 and diff_a == diff_b:
        return True
    return False


def main():
    case = 0
    solution(case)

if __name__ == "__main__":
    main()

