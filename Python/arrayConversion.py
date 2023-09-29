#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of 2k integers (for some integer k), perform the following
operations until the array contains only one element:

    - On the 1st, 3rd, 5th, etc. iterations (1-based) replace each pair of
    consecutive elements with their sum;
    - On the 2nd, 4th, 6th, etc. iterations replace each pair of consecutive
    elements with their product.

After the algorithm has finished, there will be a single element left in the
array. Return that element.

Example:

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8], the output should be
solution(inputArray) = 186.

We have [1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186], so the
answer is 186.

"""


def solution(input_array: list[int], is_odd=True) -> int:
    if len(input_array) == 1:
        return input_array[0]
    output = []
    iterator = iter(input_array)
    if is_odd:
        for num_a, num_b in zip(iterator, iterator):
            output.append(num_a + num_b)
    else:
        for num_a, num_b in zip(iterator, iterator):
            output.append(num_a * num_b)
    return solution(output, not is_odd)


def main():
    case = [1, 2, 3, 4, 5, 6, 7, 8]
    # expected = 186
    print(solution(case))


if __name__ == "__main__":
    main()
