#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_array, element_to_replace, substitution_element):
    for index, element in enumerate(input_array):
        if element == element_to_replace:
            input_array[index] = substitution_element
    return input_array


def main():
    case = [ 1, 2, 3 ]
    print(solution(case, 1, 3))

if __name__ == "__main__":
    main()

