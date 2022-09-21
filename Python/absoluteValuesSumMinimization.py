#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(array):
    diffs_sum = []
    for current_number in array:
        current_diff = 0
        for compare_to in array:
            current_diff += abs(compare_to - current_number)
        diffs_sum.append(current_diff)

    values_collection = {}
    for current_number, value in zip(array, diffs_sum):
        values_collection[current_number] = value
    return min(values_collection, key=values_collection.get)


def main():
    case = [2, 4, 7]
    # expected 4
    print(solution(case))

if __name__ == "__main__":
    main()

