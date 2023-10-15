#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given an array of integers a. A range sum query is defined by a pair of
non-negative integers l and r (l <= r). The output to a range sum query on the
given array a is the sum of all the elements of a that have indices from l to r,
inclusive.

You have the array a and a list of range sum queries q. Find an algorithm that
can rearrange the array a in such a way that the total sum of all of the query
outputs is maximized, and return this total sum.

Example

For a = [9, 7, 2, 4, 4] and q = [[1, 3], [1, 4], [0, 2]], the output should be
solution(a, q) = 62.

You can get this sum if the array a is rearranged to be [2, 9, 7, 4, 4]. In that
case, the first range sum query [1, 3] returns the sum 9 + 7 + 4 = 20, the
second query [1, 4] returns the sum 9 + 7 + 4 + 4 = 24, and the third query [0,
2] returns the sum 2 + 9 + 7 = 18. The total sum will be 20 + 24 + 18 = 62.

"""


def solution(array: list[int], queries: list[list[int]]) -> int:
    matches_of_num_per_query = [0 for _ in array]
    for index_range in queries:
        for number_index in range(index_range[0], index_range[1] + 1):
            matches_of_num_per_query[number_index] += 1
    array.sort()
    matches_of_num_per_query.sort()
    return sum(num * matches for num, matches in zip(array, matches_of_num_per_query))


def main():
    a = [9, 7, 2, 4, 4]
    q = [[1, 3], [1, 4], [0, 2]]
    # expected = 62
    print(solution(a, q))


if __name__ == "__main__":
    main()
