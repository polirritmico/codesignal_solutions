#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_array, replace, substitution):
    return [substitution if n == replace else n for n in input_array]


def main():
    input_array = [1, 2, 1]
    elem_to_replace = 1
    substitution_elem = 3
    print(solution(input_array, elem_to_replace, substitution_elem))

if __name__ == "__main__":
    main()

