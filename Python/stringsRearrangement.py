#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools


def one_char_diff(string1, string2):
    diff_flag = False
    for char1, char2 in zip(string1, string2):
        if diff_flag and char1 != char2:
            return False
        if char1 != char2:
            diff_flag = True
    if diff_flag:
        return True
    return False

def valid_permutation(string_list):
    for i in range(1, len(string_list)):
        previous = string_list[i - 1]
        current = string_list[i]
        if not one_char_diff(previous, current):
            return False
    return True

def solution(input_array):
    permutations = itertools.permutations(input_array, len(input_array))
    for permutation in permutations:
        if valid_permutation(permutation):
            return True
    return False

def main():
    # Expected false
    #case = ["aba", "bbb", "bab"]
    # Expected true → aa, ab, bb || bb, ab, aa
    case = ["ab", "bb", "aa"]
    print(solution(case))

if __name__ == "__main__":
    main()

