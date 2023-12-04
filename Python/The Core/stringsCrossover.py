#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Define crossover operation over two equal-length strings A and B as follows:

    - The result of that operation is a string of the same length as the input
      strings.
    - result[i] is either A[i] or B[i], chosen at random.

Given array of strings inputArray and a string result, find for how many pairs
of strings from inputArray the result of the crossover operation over them may
be equal to result.

Note that (A, B) and (B, A) are the same pair. Also note that the pair cannot
include the same element of the array twice (however, if there are two equal
elements in the array, they can form a pair).

Example

For inputArray = ["abc", "aaa", "aba", "bab"] and result = "bbb", the output
should be solution(inputArray, result) = 2.
"""


def solution(arrays: list[str], result: str) -> int:
    len_arrays = len(arrays)
    len_result = len(result)
    valid_pairs = 0
    for idx_a in range(len_arrays):
        array_a = arrays[idx_a]
        for idx_b in range(idx_a + 1, len_arrays):
            array_b = arrays[idx_b]
            valid_pair = True
            for char in range(len_result):
                if array_a[char] != result[char] and array_b[char] != result[char]:
                    valid_pair = False
                    break
            if valid_pair:
                valid_pairs += 1
    return valid_pairs


def main():
    input_array = ["abc", "aaa", "aba", "bab"]
    result = "bbb"
    # expected = 2
    print(solution(input_array, result))


if __name__ == "__main__":
    main()
