#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Let's call two integers A and B friends if each integer from the array divisors
is either a divisor of both A and B or neither A nor B. If two integers are
friends, they are said to be in the same clan. How many clans are the integers
from 1 to k, inclusive, broken into?

Example

For divisors = [2, 3] and k = 6, the output should be
solution(divisors, k) = 4.

The numbers 1 and 5 are friends and form a clan, 2 and 4 are friends and form a
clan, and 3 and 6 do not have friends and each is a clan by itself. So the
numbers 1 through 6 are broken into 4 clans.
"""


def is_friendly(number: int, divisors: list[int]) -> bool:
    prev_divisible = None
    for divisor in divisors:
        is_divisible = number % divisor == 0
        prev_divisible = is_divisible if prev_divisible is None else prev_divisible
        if is_divisible != prev_divisible:
            return False
    return True


def solution(divisors: list[int], k: int) -> int:
    integers_to_check = [integer for integer in range(1, k)]
    friendly_numbers = []
    for idx_a in range(0, len(integers_to_check) - 1):
        num_a = integers_to_check[idx_a]
        if not is_friendly(num_a, divisors):
            continue
        for idx_b in range(idx_a + 1, len(integers_to_check)):
            num_b = integers_to_check[idx_b]
            if not is_friendly(num_b, divisors):
                continue
            friends = (num_a, num_b)
            friendly_numbers.append(friends)
    return friendly_numbers


def main():
    divisors = [2, 3, 4]
    k = 6
    # expected = 5
    print(solution(divisors, k))


if __name__ == "__main__":
    main()
