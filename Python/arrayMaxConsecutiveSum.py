#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_array, step):
    # Get first sum
    current_range_sum = 0
    for i in range(step):
        current_range_sum += input_array[i]
    max_range_sum = current_range_sum

    # Remove first number from the sum and add the next one
    for i in range(len(input_array) - step):
        current_range_sum -= input_array[i]
        current_range_sum += input_array[i + step]
        max_range_sum = max(current_range_sum, max_range_sum)

    return max_range_sum

def main():
    case = [2, 3, 5, 1, 6]
    k = 2
    # Expected = 8
    print(solution(case, k))

if __name__ == "__main__":
    main()

