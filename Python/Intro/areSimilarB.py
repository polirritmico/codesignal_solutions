#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(array_a, array_b):
    a_dict = dict()
    b_dict = dict()
    diff_counter = 0
    for a, b in zip(array_a, array_b):
        if a != b:
            a_dict[a] = a_dict.get(a, 0) + 1
            b_dict[b] = b_dict.get(b, 0) + 1
            diff_counter += 1
            if diff_counter > 2:
                return False
    if len(a_dict) == 0:
        return True
    for a in a_dict:
        if a not in b_dict or a_dict[a] - b_dict[a] != 0:
            return False
    return True


def main():
    case = 0
    solution(case)

if __name__ == "__main__":
    main()

