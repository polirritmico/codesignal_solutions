#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n):
    last_sum = n
    found_elements = []
    while not last_sum in found_elements:
        found_elements.append(last_sum)
        digits = [int(char) for char in str(last_sum)]
        last_sum = 0
        for digit in digits:
            last_sum += digit ** 2
    return len(found_elements) + 1


def main():
    case = 16
    #expected = 9
    print(solution(case))


if __name__ == "__main__":
    main()

