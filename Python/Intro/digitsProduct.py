#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_product(number):
    product = 1
    while number != 0:
        remainder = number % 10
        product *= remainder
        number = number // 10
    return product


def solution(expected_product):
    output = 0
    count = 1
    for _ in range(10000):
        output = get_product(count)
        if output == expected_product:
            return count
        count += 1
    return -1



def main():
    case = 12
    # Expected 26 (2 * 6 = 12)
    print(solution(case))

if __name__ == "__main__":
    main()

